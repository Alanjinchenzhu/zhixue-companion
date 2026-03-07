# 📚 智学伴侣 - 错题管理 AI 助手

> 拍照上传错题 → AI 分析知识点 → 生成相似题 → 智能复习计划

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![UniApp](https://img.shields.io/badge/UniApp-1.0-green.svg)](https://uniapp.dcloud.net.cn/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)

---

## 🎯 项目简介

智学伴侣是一款基于 AI 的错题管理工具，帮助学生高效整理错题、精准复习、提升学习成绩。

### 核心功能

1. **📸 拍照搜题** - 上传错题照片，AI 自动识别题目内容
2. **🤖 AI 分析** - 智能分析知识点、解题思路、易错点
3. **📝 错题本** - 自动归类整理，支持标签和笔记
4. **🔄 相似题推荐** - 根据错题生成相似练习题
5. **📊 学习统计** - 可视化学习数据和进步轨迹
6. **⏰ 智能提醒** - 基于遗忘曲线的复习提醒

---

## 🚀 快速开始

### 前端（UniApp）

```bash
# 进入前端目录
cd frontend

# 安装依赖
npm install

# 运行项目
npm run dev:h5  # H5 开发
npm run dev:mp-weixin  # 微信小程序
```

### 后端（Python FastAPI）

```bash
# 进入后端目录
cd backend

# 创建虚拟环境
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 启动服务
python app.py
```

### Docker 部署

```bash
# 构建并启动
docker-compose up -d --build

# 查看日志
docker-compose logs -f

# 停止服务
docker-compose down
```

访问地址：`http://localhost:8000`

---

## 📁 项目结构

```
智学伴侣/
├── frontend/                 # UniApp 前端
│   ├── pages/               # 页面
│   │   ├── index/          # 首页
│   │   ├── camera/         # 拍题页
│   │   ├── question/       # 题目详情
│   │   ├── stats/          # 统计页
│   │   └── user/           # 个人中心
│   ├── components/          # 组件
│   ├── static/             # 静态资源
│   ├── App.vue
│   ├── main.js
│   ├── manifest.json
│   └── pages.json
├── backend/                # Python 后端
│   ├── app.py             # 主应用
│   ├── config.py          # 配置
│   ├── models/            # 数据模型
│   ├── routes/            # 路由
│   ├── services/          # 业务逻辑
│   └── requirements.txt   # 依赖
├── docker-compose.yml      # Docker 编排
├── Dockerfile             # Docker 镜像
├── README.md
└── .gitignore
```

---

## 🛠️ 技术栈

### 前端
- **框架**：UniApp 3.x
- **语言**：Vue 3 + TypeScript
- **UI 组件**：uView UI
- **状态管理**：Pinia
- **构建工具**：Vite

### 后端
- **框架**：FastAPI
- **语言**：Python 3.8+
- **数据库**：SQLite / MySQL
- **ORM**：SQLAlchemy
- **认证**：JWT

### AI 服务
- **大模型**：DeepSeek API（环境变量配置）
- **图像识别**：OCR 文字识别
- **知识点分析**：AI 智能分析

---

## 📱 功能演示

### 核心功能清单

- [x] 用户注册/登录
- [x] 拍照上传题目
- [x] AI 题目识别
- [x] 知识点分析
- [x] 错题本管理
- [x] 相似题推荐
- [x] 学习统计
- [x] 复习提醒
- [x] 数据同步

---

## 🎨 UI 设计

本项目 UI 设计遵循 **UI/UX Pro Max** 技能规范：

- **配色**：智慧蓝为主色调，清新专业
- **字体**：系统字体，保证可读性
- **间距**：8px 基准系统
- **圆角**：8-12px 现代化圆角
- **阴影**：多层次阴影系统

详细设计规范见：[UI 设计方案](../智学伴侣-UI 设计方案.md)

---

## 💰 变现路径

### 免费版
- 每日拍题 10 次
- 基础错题管理
- 简单统计

### 会员版（9.9 元/月）
- 无限拍题
- AI 深度分析
- 相似题推荐
- 学习报告
- 云同步

### 其他变现
- 课程推荐分成
- VIP 题库访问
- 一对一辅导对接

---

## 📄 开源协议

MIT License

---

## 👥 开发团队

**开发者**：龙虾工程师  
**设计理念**：让学习更高效，让进步看得见

---

## 📞 联系方式

- GitHub: [@Alanjinchenzhu](https://github.com/Alanjinchenzhu/file-downloader)
- 问题反馈：[Issues](https://github.com/Alanjinchenzhu/file-downloader/issues)

---

*最后更新：2026-03-08*
