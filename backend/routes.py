#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
API 路由模块
"""

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from typing import List

from models import get_session, init_db, User, Question, LearningStats
from auth import (
    authenticate_user,
    create_access_token,
    get_password_hash,
    get_current_user,
    Token,
    UserCreate,
    UserLogin
)
from config import settings
from services import deepseek_service, ocr_service

router = APIRouter()

# ==================== 认证路由 ====================

@router.post("/auth/register", response_model=dict)
async def register(user_data: UserCreate):
    """用户注册"""
    engine = init_db()
    session = get_session(engine)
    
    # 检查用户名是否存在
    existing_user = session.query(User).filter(User.username == user_data.username).first()
    if existing_user:
        session.close()
        raise HTTPException(status_code=400, detail="用户名已存在")
    
    # 创建新用户
    new_user = User(
        username=user_data.username,
        password_hash=get_password_hash(user_data.password),
        email=user_data.email,
        is_vip=0
    )
    session.add(new_user)
    session.commit()
    session.close()
    
    # 生成 Token
    access_token = create_access_token(
        data={"sub": new_user.username},
        expires_delta=timedelta(minutes=settings.JWT_EXPIRE_MINUTES)
    )
    
    return {
        "success": True,
        "user_id": new_user.id,
        "token": access_token
    }

@router.post("/auth/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """用户登录"""
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=timedelta(minutes=settings.JWT_EXPIRE_MINUTES)
    )
    
    return Token(access_token=access_token)

@router.get("/auth/me")
async def get_me(current_user: User = Depends(get_current_user)):
    """获取当前用户信息"""
    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email,
        "is_vip": bool(current_user.is_vip),
        "created_at": current_user.created_at
    }

# ==================== 题目路由 ====================

@router.get("/questions", response_model=List[dict])
async def get_questions(
    skip: int = 0,
    limit: int = 20,
    subject: str = None,
    current_user: User = Depends(get_current_user)
):
    """获取题目列表"""
    engine = init_db()
    session = get_session(engine)
    
    query = session.query(Question).filter(Question.user_id == current_user.id)
    
    if subject:
        query = query.filter(Question.subject == subject)
    
    questions = query.offset(skip).limit(limit).all()
    session.close()
    
    return [
        {
            "id": q.id,
            "content": q.content,
            "subject": q.subject,
            "knowledge_point": q.knowledge_point,
            "difficulty": q.difficulty,
            "mastery": q.mastery,
            "created_at": q.created_at
        }
        for q in questions
    ]

@router.post("/questions", response_model=dict)
async def create_question(
    question_data: dict,
    current_user: User = Depends(get_current_user)
):
    """创建题目"""
    engine = init_db()
    session = get_session(engine)
    
    new_question = Question(
        user_id=current_user.id,
        content=question_data.get("content"),
        subject=question_data.get("subject", "unknown"),
        knowledge_point=question_data.get("knowledge_point"),
        difficulty=question_data.get("difficulty", "medium")
    )
    session.add(new_question)
    session.commit()
    session.close()
    
    return {
        "success": True,
        "question_id": new_question.id
    }

@router.get("/questions/{question_id}")
async def get_question(
    question_id: int,
    current_user: User = Depends(get_current_user)
):
    """获取题目详情"""
    engine = init_db()
    session = get_session(engine)
    
    question = session.query(Question).filter(
        Question.id == question_id,
        Question.user_id == current_user.id
    ).first()
    session.close()
    
    if not question:
        raise HTTPException(status_code=404, detail="题目不存在")
    
    return {
        "id": question.id,
        "content": question.content,
        "subject": question.subject,
        "knowledge_point": question.knowledge_point,
        "difficulty": question.difficulty,
        "mastery": question.mastery,
        "analysis": question.analysis,
        "solution": question.solution,
        "created_at": question.created_at
    }

@router.put("/questions/{question_id}/mastery")
async def update_mastery(
    question_id: int,
    mastery: str,
    current_user: User = Depends(get_current_user)
):
    """更新掌握程度"""
    engine = init_db()
    session = get_session(engine)
    
    question = session.query(Question).filter(
        Question.id == question_id,
        Question.user_id == current_user.id
    ).first()
    
    if not question:
        session.close()
        raise HTTPException(status_code=404, detail="题目不存在")
    
    question.mastery = mastery
    session.commit()
    session.close()
    
    return {"success": True}

@router.post("/questions/{question_id}/analyze")
async def analyze_question(
    question_id: int,
    current_user: User = Depends(get_current_user)
):
    """AI 分析题目"""
    engine = init_db()
    session = get_session(engine)
    
    question = session.query(Question).filter(
        Question.id == question_id,
        Question.user_id == current_user.id
    ).first()
    session.close()
    
    if not question:
        raise HTTPException(status_code=404, detail="题目不存在")
    
    # 调用 AI 分析
    analysis = await deepseek_service.analyze_question(question.content)
    similar = await deepseek_service.generate_similar_questions(question.content, 3)
    
    return {
        **analysis,
        "similar_questions": similar
    }

# ==================== 统计路由 ====================

@router.get("/stats")
async def get_stats(current_user: User = Depends(get_current_user)):
    """获取学习统计"""
    engine = init_db()
    session = get_session(engine)
    
    # 查询题目统计
    total = session.query(Question).filter(Question.user_id == current_user.id).count()
    mastered = session.query(Question).filter(
        Question.user_id == current_user.id,
        Question.mastery == "mastered"
    ).count()
    
    session.close()
    
    return {
        "total_questions": total,
        "mastered_questions": mastered,
        "learning_days": 7,  # TODO: 实际计算
        "accuracy_rate": 0.85  # TODO: 实际计算
    }

# ==================== 上传路由 ====================

@router.post("/upload")
async def upload_file(
    file: bytes,
    current_user: User = Depends(get_current_user)
):
    """上传文件（OCR 识别）"""
    text = await ocr_service.recognize_text(file)
    
    return {
        "success": True,
        "ocr_result": text
    }
