# 🚀 智学伴侣 - 快速开始指南

## 方式一：一键启动（推荐）

```bash
# 赋予执行权限
chmod +x start.sh

# 启动服务
./start.sh
```

访问：
- 前端：http://localhost:8080
- 后端：http://localhost:8000
- API 文档：http://localhost:8000/docs

---

## 方式二：手动启动

### 1. 启动后端

```bash
cd backend

# 安装依赖
pip3 install -r requirements.txt

# 启动服务
python3 app.py
```

### 2. 启动前端

```bash
cd frontend

# 安装依赖
npm install

# 启动开发服务器
npm run dev:h5
```

---

## 方式三：Docker 部署

```bash
# 构建并启动
docker-compose up -d --build

# 查看日志
docker-compose logs -f

# 停止服务
docker-compose down
```

---

## 测试 API

```bash
# 健康检查
curl http://localhost:8000/health

# 运行测试脚本
cd backend
python3 test_api.py
```

---

## 常见问题

### 1. 端口被占用

```bash
# 查看占用端口的进程
lsof -i :8000
lsof -i :8080

# 杀死进程
kill -9 <PID>
```

### 2. 依赖安装失败

```bash
# 使用国内镜像
pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
npm install --registry=https://registry.npmmirror.com
```

### 3. 权限问题

```bash
# 赋予执行权限
chmod +x start.sh
chmod +x stop.sh
```

---

## 项目结构

```
智学伴侣/
├── start.sh              # 启动脚本
├── stop.sh               # 停止脚本
├── backend/              # 后端服务
│   ├── app.py           # FastAPI 应用
│   ├── models.py        # 数据模型
│   ├── config.py        # 配置文件
│   └── test_api.py      # API 测试
├── frontend/             # 前端应用
│   ├── pages/           # 页面组件
│   ├── App.vue          # 应用入口
│   └── package.json     # 依赖配置
└── docs/                # 文档
    ├── README.md        # 项目说明
    ├── API_DOC.md       # API 文档
    └── DEPLOYMENT.md    # 部署指南
```

---

## 下一步

1. ✅ 启动服务
2. ✅ 访问前端页面
3. ✅ 测试 API 接口
4. ⏳ 配置环境变量（可选）
5. ⏳ 部署到生产环境

---

*最后更新：2026-03-08*
