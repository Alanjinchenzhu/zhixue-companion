#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数据库初始化脚本
"""

from models import init_db, get_session, User, Question, LearningStats
from datetime import datetime, timedelta

def init_database():
    """初始化数据库并添加测试数据"""
    print("🔧 初始化数据库...")
    
    # 创建数据库表
    engine = init_db()
    session = get_session(engine)
    
    # 创建测试用户
    test_user = User(
        username="testuser",
        password_hash="hashed_password",
        email="test@example.com",
        is_vip=0
    )
    session.add(test_user)
    session.commit()
    print(f"✅ 创建测试用户：{test_user.username}")
    
    # 创建测试题目
    test_questions = [
        Question(
            user_id=test_user.id,
            content="已知函数 f(x) = x² + 2x + 1，求函数的最小值",
            subject="math",
            knowledge_point="二次函数最值",
            difficulty="medium",
            mastery="unlearned"
        ),
        Question(
            user_id=test_user.id,
            content="英语时态练习：I ___ to school yesterday.",
            subject="english",
            knowledge_point="一般过去时",
            difficulty="easy",
            mastery="partial"
        ),
        Question(
            user_id=test_user.id,
            content="物理：一个物体从静止开始做匀加速直线运动...",
            subject="physics",
            knowledge_point="匀加速直线运动",
            difficulty="hard",
            mastery="unlearned"
        )
    ]
    
    for q in test_questions:
        session.add(q)
    
    session.commit()
    print(f"✅ 创建 {len(test_questions)} 道测试题目")
    
    # 创建学习统计
    stats = LearningStats(
        user_id=test_user.id,
        date=datetime.now(),
        total_questions=len(test_questions),
        mastered_questions=0,
        learning_time=30,
        accuracy_rate=0.75
    )
    session.add(stats)
    session.commit()
    print("✅ 创建学习统计数据")
    
    session.close()
    print("\n🎉 数据库初始化完成！")
    print(f"📁 数据库文件：zhixue.db")
    print(f"👤 测试用户：testuser")
    print(f"📝 测试题目：{len(test_questions)} 道")

if __name__ == "__main__":
    init_database()
