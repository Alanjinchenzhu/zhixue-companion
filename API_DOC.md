# 📡 智学伴侣 - API 文档

**版本**: 1.0.0  
**基础 URL**: `http://localhost:8000`

---

## 认证接口

### 1. 用户注册

```http
POST /api/auth/register
Content-Type: application/json

{
  "username": "testuser",
  "password": "password123",
  "email": "test@example.com"
}
```

**响应**:
```json
{
  "success": true,
  "user_id": 1,
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

### 2. 用户登录

```http
POST /api/auth/login
Content-Type: application/json

{
  "username": "testuser",
  "password": "password123"
}
```

---

## 题目接口

### 1. 获取题目列表

```http
GET /api/questions?subject=math&limit=20
Authorization: Bearer {token}
```

**响应**:
```json
[
  {
    "id": 1,
    "content": "已知函数 f(x) = x² + 2x + 1...",
    "subject": "math",
    "knowledge_point": "二次函数",
    "difficulty": "medium",
    "mastery": "unlearned",
    "created_at": "2026-03-08T01:00:00"
  }
]
```

### 2. 获取题目详情

```http
GET /api/questions/{id}
Authorization: Bearer {token}
```

### 3. 添加题目

```http
POST /api/questions
Authorization: Bearer {token}
Content-Type: application/json

{
  "content": "题目内容",
  "subject": "math",
  "knowledge_point": "二次函数",
  "difficulty": "medium"
}
```

### 4. 更新掌握程度

```http
PUT /api/questions/{id}/mastery
Authorization: Bearer {token}
Content-Type: application/json

{
  "mastery": "mastered"
}
```

### 5. AI 分析题目

```http
POST /api/questions/{id}/analyze
Authorization: Bearer {token}
```

**响应**:
```json
{
  "knowledge_point": "二次函数最值问题",
  "solution_idea": "使用配方法或求导法",
  "common_mistakes": "符号处理错误",
  "similar_questions": [
    "类似题 1",
    "类似题 2"
  ]
}
```

---

## 上传接口

### 1. 上传图片

```http
POST /api/upload
Authorization: Bearer {token}
Content-Type: multipart/form-data

file: [图片文件]
```

**响应**:
```json
{
  "success": true,
  "message": "上传成功",
  "filename": "question_123.jpg",
  "ocr_result": "识别的题目文本..."
}
```

---

## 统计接口

### 1. 获取学习统计

```http
GET /api/stats
Authorization: Bearer {token}
```

**响应**:
```json
{
  "total_questions": 23,
  "mastered_questions": 15,
  "learning_days": 7,
  "accuracy_rate": 0.85
}
```

### 2. 获取知识点分布

```http
GET /api/stats/knowledge
Authorization: Bearer {token}
```

---

## 推荐接口

### 1. 获取相似题

```http
GET /api/recommend?question_id=1&limit=5
Authorization: Bearer {token}
```

**响应**:
```json
[
  {
    "id": 2,
    "content": "相似题内容",
    "similarity": 0.85
  }
]
```

---

## 错误响应

### 通用错误格式

```json
{
  "detail": "错误信息描述"
}
```

### 常见错误码

| 状态码 | 说明 |
|--------|------|
| 200 | 成功 |
| 400 | 请求参数错误 |
| 401 | 未授权（Token 无效） |
| 403 | 禁止访问（权限不足） |
| 404 | 资源不存在 |
| 500 | 服务器内部错误 |

---

## 限流说明

### 免费用户
- 每日拍题：10 次
- API 调用：100 次/小时

### VIP 用户
- 无限拍题
- API 调用：1000 次/小时

---

*最后更新：2026-03-08*
