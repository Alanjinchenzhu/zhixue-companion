# 🚀 智学伴侣 - 部署指南

## 本地开发

### 1. 环境准备

```bash
# Python 3.8+
python3 --version

# Node.js 16+
node --version

# Git
git --version
```

### 2. 克隆项目

```bash
git clone https://github.com/Alanjinchenzhu/zhixue-companion.git
cd zhixue-companion
```

### 3. 后端启动

```bash
cd backend

# 安装依赖
pip3 install -r requirements.txt

# 启动服务
python3 app.py
```

访问：http://localhost:8000
API 文档：http://localhost:8000/docs

### 4. 前端启动

```bash
cd frontend

# 安装依赖
npm install

# H5 开发
npm run dev:h5

# 微信小程序
npm run dev:mp-weixin
```

---

## Docker 部署

### 1. 构建镜像

```bash
docker-compose build
```

### 2. 启动服务

```bash
docker-compose up -d
```

### 3. 查看状态

```bash
docker-compose ps
docker-compose logs -f
```

### 4. 停止服务

```bash
docker-compose down
```

---

## 生产环境

### 环境变量配置

```bash
# .env 文件
DATABASE_URL=mysql://user:pass@localhost:3306/zhixue
DEEPSEEK_KEY=your_deepseek_key
OCR_API_KEY=your_ocr_key
JWT_SECRET=your_jwt_secret
```

### Nginx 配置

```nginx
server {
    listen 80;
    server_name your-domain.com;
    
    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### HTTPS 配置

```bash
# 使用 Let's Encrypt
certbot --nginx -d your-domain.com
```

---

## 监控与日志

### 健康检查

```bash
curl http://localhost:8000/health
```

### 日志查看

```bash
# 应用日志
tail -f logs/app.log

# Docker 日志
docker-compose logs -f backend
```

---

## 常见问题

### 1. 端口被占用

```bash
# 查看占用端口的进程
lsof -i :8000

# 杀死进程
kill -9 <PID>
```

### 2. 数据库连接失败

```bash
# 检查数据库文件
ls -la zhixue.db

# 重新初始化
python3 models.py
```

### 3. 依赖安装失败

```bash
# 使用国内镜像
pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

---

*最后更新：2026-03-08*
