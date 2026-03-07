#!/bin/bash
# 智学伴侣 - 快速启动脚本

echo "📚 智学伴侣 - 快速启动"
echo "================================"

# 检查 Python
if ! command -v python3 &> /dev/null; then
    echo "❌ 未检测到 Python3，请先安装"
    exit 1
fi

# 检查 Node.js
if ! command -v node &> /dev/null; then
    echo "❌ 未检测到 Node.js，请先安装"
    exit 1
fi

# 启动后端
echo "🚀 启动后端服务..."
cd backend
pip3 install -r requirements.txt -q
python3 app.py &
BACKEND_PID=$!
cd ..

sleep 3

# 检查后端是否启动成功
if kill -0 $BACKEND_PID 2>/dev/null; then
    echo "✅ 后端服务已启动 (PID: $BACKEND_PID)"
else
    echo "❌ 后端服务启动失败"
    exit 1
fi

# 启动前端
echo "🚀 启动前端服务..."
cd frontend
if [ ! -d "node_modules" ]; then
    echo "📦 安装前端依赖..."
    npm install
fi
npm run dev:h5 &
FRONTEND_PID=$!
cd ..

sleep 3

# 检查前端是否启动成功
if kill -0 $FRONTEND_PID 2>/dev/null; then
    echo "✅ 前端服务已启动 (PID: $FRONTEND_PID)"
else
    echo "❌ 前端服务启动失败"
    exit 1
fi

echo ""
echo "================================"
echo "🎉 服务启动成功！"
echo ""
echo "📱 前端地址：http://localhost:8080"
echo "🔧 后端地址：http://localhost:8000"
echo "📡 API 文档：http://localhost:8000/docs"
echo ""
echo "按 Ctrl+C 停止所有服务"
echo "================================"

# 等待用户中断
wait
