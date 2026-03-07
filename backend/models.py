#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数据模型 - SQLAlchemy ORM
"""

from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
    """用户模型"""
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    email = Column(String(100), unique=True)
    created_at = Column(DateTime, default=datetime.now)
    is_vip = Column(Integer, default=0)  # 0: 普通用户，1: VIP
    vip_expire_at = Column(DateTime, nullable=True)
    
    questions = relationship('Question', back_populates='user')

class Question(Base):
    """题目模型"""
    __tablename__ = 'questions'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    content = Column(Text, nullable=False)  # 题目内容
    subject = Column(String(50), nullable=False)  # 科目
    knowledge_point = Column(String(200))  # 知识点
    difficulty = Column(String(20), default='medium')  # easy/medium/hard
    image_url = Column(String(500))  # 题目图片 URL
    analysis = Column(Text)  # AI 分析结果
    solution = Column(Text)  # 解题思路
    common_mistakes = Column(Text)  # 易错点
    mastery = Column(String(20), default='unlearned')  # unlearned/partial/mastered
    review_count = Column(Integer, default=0)  # 复习次数
    last_review_at = Column(DateTime, nullable=True)  # 最后复习时间
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    user = relationship('User', back_populates='questions')
    similar_questions = relationship('SimilarQuestion', back_populates='question')

class SimilarQuestion(Base):
    """相似题模型"""
    __tablename__ = 'similar_questions'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    question_id = Column(Integer, ForeignKey('questions.id'), nullable=False)
    content = Column(Text, nullable=False)
    similarity = Column(Float, default=0.0)  # 相似度 0-1
    source = Column(String(100))  # 来源
    
    question = relationship('Question', back_populates='similar_questions')

class LearningStats(Base):
    """学习统计模型"""
    __tablename__ = 'learning_stats'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    date = Column(DateTime, nullable=False)  # 统计日期
    total_questions = Column(Integer, default=0)  # 总题数
    mastered_questions = Column(Integer, default=0)  # 已掌握
    learning_time = Column(Integer, default=0)  # 学习时长（分钟）
    accuracy_rate = Column(Float, default=0.0)  # 正确率
    created_at = Column(DateTime, default=datetime.now)

# 数据库配置
DATABASE_URL = "sqlite:///./zhixue.db"

def init_db():
    """初始化数据库"""
    engine = create_engine(DATABASE_URL, echo=False)
    Base.metadata.create_all(engine)
    return engine

def get_session(engine):
    """获取数据库会话"""
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal()

if __name__ == "__main__":
    # 初始化数据库
    engine = init_db()
    print("✅ 数据库初始化成功")
    print(f"📁 数据库文件：zhixue.db")
