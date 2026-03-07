# 后端服务镜像
FROM python:3.9-slim

WORKDIR /app

# 安装依赖
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 复制代码
COPY backend/ .

# 暴露端口
EXPOSE 8000

# 启动命令
CMD ["python", "app.py"]
