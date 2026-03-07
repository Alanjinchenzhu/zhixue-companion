#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
API 测试脚本
"""

import requests
import json

BASE_URL = "http://localhost:8000"

def test_health():
    """测试健康检查"""
    print("\n🔍 测试健康检查...")
    response = requests.get(f"{BASE_URL}/health")
    print(f"状态码：{response.status_code}")
    print(f"响应：{response.json()}")
    assert response.status_code == 200
    print("✅ 健康检查通过")

def test_root():
    """测试根路径"""
    print("\n🔍 测试根路径...")
    response = requests.get(f"{BASE_URL}/")
    print(f"状态码：{response.status_code}")
    print(f"响应：{response.json()}")
    assert response.status_code == 200
    print("✅ 根路径测试通过")

def test_stats():
    """测试统计接口"""
    print("\n🔍 测试统计接口...")
    response = requests.get(f"{BASE_URL}/api/stats")
    print(f"状态码：{response.status_code}")
    print(f"响应：{response.json()}")
    assert response.status_code == 200
    print("✅ 统计接口测试通过")

def test_questions():
    """测试题目接口"""
    print("\n🔍 测试题目列表接口...")
    response = requests.get(f"{BASE_URL}/api/questions")
    print(f"状态码：{response.status_code}")
    print(f"响应：{response.json()}")
    assert response.status_code == 200
    print("✅ 题目列表接口测试通过")

def test_create_question():
    """测试创建题目"""
    print("\n🔍 测试创建题目...")
    data = {
        "content": "测试题目：已知函数 f(x) = x² + 2x + 1，求最小值",
        "subject": "math",
        "knowledge_point": "二次函数",
        "difficulty": "medium"
    }
    response = requests.post(f"{BASE_URL}/api/questions", json=data)
    print(f"状态码：{response.status_code}")
    print(f"响应：{response.json()}")
    assert response.status_code == 200
    print("✅ 创建题目测试通过")

def run_all_tests():
    """运行所有测试"""
    print("=" * 50)
    print("🧪 开始运行 API 测试")
    print("=" * 50)
    
    tests = [
        test_health,
        test_root,
        test_stats,
        test_questions,
        test_create_question
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            print(f"❌ 测试失败：{e}")
            failed += 1
    
    print("\n" + "=" * 50)
    print(f"✅ 通过：{passed}")
    print(f"❌ 失败：{failed}")
    print("=" * 50)

if __name__ == "__main__":
    run_all_tests()
