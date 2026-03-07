#!/bin/bash
# 智学伴侣 - 停止服务脚本

echo "🛑 正在停止智学伴侣服务..."

# 停止后端
echo "停止后端服务..."
pkill -f "python3 app.py"

# 停止前端
echo "停止前端服务..."
pkill -f "npm run dev:h5"

# 停止 Docker 容器（如果有）
docker-compose down 2>/dev/null

sleep 2

# 检查是否还有进程
if pgrep -f "智学伴侣" > /dev/null; then
    echo "⚠️  仍有进程在运行，强制停止..."
    pkill -9 -f "智学伴侣"
fi

echo "✅ 所有服务已停止"
