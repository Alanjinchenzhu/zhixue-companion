#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
智学伴侣 - 后端服务
错题管理 AI 助手
"""

import os
import time
from datetime import datetime, timedelta
from typing import List, Optional
from fastapi import FastAPI, HTTPException, Depends, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import uvicorn

# 导入配置和模型
from config import settings
from models import init_db, get_session, Question as QuestionModel, LearningStats

# 初始化数据库
engine = init_db()

app = FastAPI(
    title="智学伴侣 API",
    description="错题管理 AI 助手 - 后端服务",
    version="1.0.0"
)

# CORS 配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==================== 数据模型 ====================

class Question(BaseModel):
    """题目模型"""
    id: Optional[int] = None
    content: str = Field(..., description="题目内容")
    subject: str = Field(..., description="科目：数学/英语/物理等")
    knowledge_point: str = Field(..., description="知识点")
    difficulty: str = Field(default="medium", description="难度：easy/medium/hard")
    created_at: datetime = Field(default_factory=datetime.now)
    mastery: str = Field(default="unlearned", description="掌握程度：unlearned/partial/mastered")
    
class QuestionAnalysis(BaseModel):
    """题目分析结果"""
    knowledge_point: str
    solution_idea: str
    common_mistakes: str
    similar_questions: List[str]

class UserStats(BaseModel):
    """用户统计"""
    total_questions: int
    mastered_questions: int
    learning_days: int
    accuracy_rate: float

# ==================== 内存数据库（MVP 版本） ====================

questions_db = []
stats = {
    "total": 0,
    "mastered": 0,
    "days": 7,
    "accuracy": 0.85
}

# ==================== API 路由 ====================

@app.get("/")
async def root():
    """根路径"""
    return {
        "name": "智学伴侣 API",
        "version": "1.0.0",
        "status": "running"
    }

@app.get("/health")
async def health_check():
    """健康检查"""
    return {"status": "healthy", "timestamp": datetime.now()}

@app.get("/api/stats", response_model=UserStats)
async def get_stats():
    """获取学习统计"""
    return UserStats(
        total_questions=stats["total"],
        mastered_questions=stats["mastered"],
        learning_days=stats["days"],
        accuracy_rate=stats["accuracy"]
    )

@app.post("/api/questions")
async def create_question(question: Question):
    """添加错题"""
    question.id = len(questions_db) + 1
    questions_db.append(question.dict())
    stats["total"] += 1
    return {"success": True, "question_id": question.id}

@app.get("/api/questions", response_model=List[Question])
async def get_questions(subject: Optional[str] = None, limit: int = 20):
    """获取错题列表"""
    if subject:
        filtered = [q for q in questions_db if q["subject"] == subject]
        return filtered[:limit]
    return questions_db[:limit]

@app.get("/api/questions/{question_id}", response_model=Question)
async def get_question(question_id: int):
    """获取题目详情"""
    for q in questions_db:
        if q["id"] == question_id:
            return q
    raise HTTPException(status_code=404, detail="题目不存在")

@app.post("/api/questions/{question_id}/analyze")
async def analyze_question(question_id: int):
    """AI 分析题目（调用 DeepSeek API）"""
    # MVP 版本：返回模拟数据
    # 实际应调用 DeepSeek API 进行分析
    return QuestionAnalysis(
        knowledge_point="二次函数最值问题",
        solution_idea="使用配方法或求导法找到函数最值",
        common_mistakes="符号处理错误、配方不完整",
        similar_questions=[
            "已知 f(x) = x² - 4x + 3，求最小值",
            "求函数 y = -x² + 2x + 1 的最大值"
        ]
    )

@app.put("/api/questions/{question_id}/mastery")
async def update_mastery(question_id: int, mastery: str):
    """更新掌握程度"""
    for q in questions_db:
        if q["id"] == question_id:
            q["mastery"] = mastery
            if mastery == "mastered":
                stats["mastered"] += 1
            return {"success": True}
    raise HTTPException(status_code=404, detail="题目不存在")

@app.post("/api/upload")
async def upload_question(file: UploadFile = File(...)):
    """上传题目图片（OCR 识别）"""
    # MVP 版本：返回模拟数据
    # 实际应调用 OCR API 识别图片文字
    return {
        "success": True,
        "message": "图片上传成功，正在识别...",
        "filename": file.filename
    }

@app.get("/api/recommend")
async def recommend_questions(question_id: int, limit: int = 5):
    """推荐相似题目"""
    # MVP 版本：返回模拟数据
    return [
        {"id": i, "content": f"相似题 {i}", "similarity": 0.9 - i*0.1}
        for i in range(1, limit + 1)
    ]

# ==================== 主程序 ====================

if __name__ == "__main__":
    print("=" * 50)
    print("📚 智学伴侣 - 后端服务")
    print("=" * 50)
    print(f"🚀 启动地址：http://localhost:8000")
    print(f"📊 API 文档：http://localhost:8000/docs")
    print(f"💾 数据库：{DATABASE_URL}")
    print("=" * 50)
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="info"
    )
