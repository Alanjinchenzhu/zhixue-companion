#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
业务逻辑服务层
"""

import httpx
from typing import Optional, List, Dict
from config import settings

class DeepSeekService:
    """DeepSeek AI 服务"""
    
    def __init__(self):
        self.api_key = settings.DEEPSEEK_KEY
        self.base_url = "https://api.deepseek.com/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    async def analyze_question(self, question_content: str) -> Dict:
        """分析题目"""
        if not self.api_key:
            return self._mock_analysis(question_content)
        
        prompt = f"""
请分析这道题目：
{question_content}

请返回以下格式：
{{
  "knowledge_point": "知识点",
  "solution_idea": "解题思路",
  "common_mistakes": "易错点",
  "difficulty": "难度（easy/medium/hard）"
}}
"""
        
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{self.base_url}/chat/completions",
                    headers=self.headers,
                    json={
                        "model": "deepseek-chat",
                        "messages": [{"role": "user", "content": prompt}],
                        "temperature": 0.7
                    },
                    timeout=30.0
                )
                response.raise_for_status()
                result = response.json()
                content = result["choices"][0]["message"]["content"]
                # 解析返回的 JSON
                import json
                return json.loads(content)
        except Exception as e:
            print(f"DeepSeek API 调用失败：{e}")
            return self._mock_analysis(question_content)
    
    def _mock_analysis(self, question_content: str) -> Dict:
        """模拟分析结果（无 API 时使用）"""
        return {
            "knowledge_point": "通用知识点",
            "solution_idea": "分析题目条件，运用相关知识求解",
            "common_mistakes": "注意审题，避免计算错误",
            "difficulty": "medium"
        }
    
    async def generate_similar_questions(self, question: str, count: int = 3) -> List[str]:
        """生成相似题"""
        if not self.api_key:
            return self._mock_similar_questions(count)
        
        prompt = f"""
基于这道题目，生成{count}道相似的练习题：
{question}

请直接返回题目列表，每道题一行。
"""
        
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{self.base_url}/chat/completions",
                    headers=self.headers,
                    json={
                        "model": "deepseek-chat",
                        "messages": [{"role": "user", "content": prompt}],
                        "temperature": 0.8
                    },
                    timeout=30.0
                )
                response.raise_for_status()
                result = response.json()
                content = result["choices"][0]["message"]["content"]
                # 按行分割
                questions = [q.strip() for q in content.split('\n') if q.strip()]
                return questions[:count]
        except Exception as e:
            print(f"生成相似题失败：{e}")
            return self._mock_similar_questions(count)
    
    def _mock_similar_questions(self, count: int) -> List[str]:
        """模拟相似题"""
        return [f"相似练习题 {i+1}" for i in range(count)]


class OCRService:
    """OCR 识别服务"""
    
    def __init__(self):
        self.api_key = settings.OCR_API_KEY
    
    async def recognize_text(self, image_data: bytes) -> str:
        """识别图片文字"""
        if not self.api_key:
            return self._mock_ocr(image_data)
        
        # 这里可以集成百度 OCR、腾讯 OCR 等
        # 示例代码：
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    "https://api.example.com/ocr",
                    headers={"Authorization": f"Bearer {self.api_key}"},
                    files={"image": image_data},
                    timeout=30.0
                )
                response.raise_for_status()
                result = response.json()
                return result.get("text", "")
        except Exception as e:
            print(f"OCR 识别失败：{e}")
            return self._mock_ocr(image_data)
    
    def _mock_ocr(self, image_data: bytes) -> str:
        """模拟 OCR 结果"""
        return "这是一道测试题目，具体内容需要根据实际图片识别..."


# 全局服务实例
deepseek_service = DeepSeekService()
ocr_service = OCRService()

if __name__ == "__main__":
    import asyncio
    
    async def test():
        print("测试 DeepSeek 服务...")
        result = await deepseek_service.analyze_question("已知函数 f(x) = x² + 2x + 1，求最小值")
        print(f"分析结果：{result}")
        
        print("\n测试生成相似题...")
        questions = await deepseek_service.generate_similar_questions("二次函数题目", 3)
        print(f"相似题：{questions}")
    
    asyncio.run(test())
