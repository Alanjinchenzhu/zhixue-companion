#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
用户认证模块
"""

from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from config import settings
from models import get_session, init_db, User

# 密码加密
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 配置
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/login")

class Token(BaseModel):
    """Token 响应"""
    access_token: str
    token_type: str = "bearer"

class UserCreate(BaseModel):
    """用户创建"""
    username: str
    password: str
    email: Optional[str] = None

class UserLogin(BaseModel):
    """用户登录"""
    username: str
    password: str

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """验证密码"""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """生成密码哈希"""
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """创建访问令牌"""
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=settings.JWT_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
    return encoded_jwt

def authenticate_user(username: str, password: str) -> Optional[User]:
    """认证用户"""
    engine = init_db()
    session = get_session(engine)
    user = session.query(User).filter(User.username == username).first()
    session.close()
    
    if not user:
        return None
    if not verify_password(password, user.password_hash):
        return None
    return user

async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    """获取当前用户"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="无法验证身份",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    engine = init_db()
    session = get_session(engine)
    user = session.query(User).filter(User.username == username).first()
    session.close()
    
    if user is None:
        raise credentials_exception
    return user

if __name__ == "__main__":
    # 测试密码加密
    password = "test123"
    hashed = get_password_hash(password)
    print(f"原始密码：{password}")
    print(f"哈希密码：{hashed}")
    print(f"验证结果：{verify_password(password, hashed)}")
