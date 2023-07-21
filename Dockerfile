FROM python:3.10 
#使用python3.10作为基础镜像
WORKDIR /DD-webui
COPY ./DD-webui /DD-webui

# 暴露端口
#flask程序端口
EXPOSE 5000
#uWSGI统计信息端口
EXPOSE 9191
# 安装依赖项
RUN pip install --no-cache-dir -r requirements.txt
RUN python setup.py install --no-cache-dir
RUN python -c "import deepdanbooru; print('deepdanbooru 包导入成功')"
RUN rm -rf ./deepdanbooru
# 删除 setup.py 文件
RUN rm ./setup.py
# 删除 setup.cfg 文件
RUN rm ./setup.cfg
ENV FLASK_APP=app.py
CMD ["uwsgi","--socket","127.0.0.1:5000","--wsgi-file","app.py","--callable","app","--processes","4","--threads","2","--stats","127.0.0.1:9191"]