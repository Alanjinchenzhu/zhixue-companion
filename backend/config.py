#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
配置文件
从环境变量读取敏感信息
"""

import os
from typing import Optional

class Settings:
    """应用配置"""
    
    # 应用配置
    APP_NAME: str = "智学伴侣"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False
    
    # 数据库配置
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./zhixue.db")
    
    # API 密钥（从环境变量读取）
    DEEPSEEK_KEY: Optional[str] = os.getenv("DEEPSEEK_KEY")
    OCR_API_KEY: Optional[str] = os.getenv("OCR_API_KEY")
    
    # JWT 配置
    JWT_SECRET: str = os.getenv("JWT_SECRET", "your-secret-key-change-in-production")
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 天
    
    # 服务器配置
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))
    
    # CORS 配置
    CORS_ORIGINS: list = [
        "http://localhost:3000",
        "http://localhost:8080",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:8080",
    ]
    
    # 文件上传配置
    MAX_FILE_SIZE: int = 10 * 1024 * 1024  # 10MB
    UPLOAD_DIR: str = "uploads"
    
    # 会员配置
    VIP_PRICE: float = 9.9  # 月费
    FREE_DAILY_LIMIT: int = 10  # 免费用户每日限制
    
    def check_api_keys(self) -> dict:
        """检查 API 密钥配置"""
        status = {}
        
        if self.DEEPSEEK_KEY:
            status['deepseek'] = '✅ 已配置'
        else:
            status['deepseek'] = '⚠️ 未配置（将使用模拟数据）'
        
        if self.OCR_API_KEY:
            status['ocr'] = '✅ 已配置'
        else:
            status['ocr'] = '⚠️ 未配置（将使用模拟数据）'
        
        return status

# 全局配置实例
settings = Settings()

if __name__ == "__main__":
    print("=" * 50)
    print(f"📚 {settings.APP_NAME} v{settings.APP_VERSION}")
    print("=" * 50)
    print(f"🌍 服务地址：http://{settings.HOST}:{settings.PORT}")
    print(f"💾 数据库：{settings.DATABASE_URL}")
    print("\n🔑 API 密钥状态:")
    for key, value in settings.check_api_keys().items():
        print(f"  - {key}: {value}")
    print("=" * 50)
