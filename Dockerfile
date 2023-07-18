FROM python:3.10 
#使用python3.10作为基础镜像
WORKDIR /DD-webui
COPY ./DD-webui /DD-webui
# 安装依赖项
RUN pip install --no-cache-dir -r requirements.txt
CMD ['python','setup.py','install']
# 暴露端口
EXPOSE 5000