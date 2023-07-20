<p align="center">
  <h1 style="text-align: center;">DD-web-demo</h1>
</p>
作者：仙

email：tianhuzong@qq.com
QQ：[1485319167](http://wpa.qq.com/msgrd?v=3&uin=1485319167&site=qq&menu=yes)

## DD-webui:Deepdanbooru网页封装版

DD-webui是一个基于[Deepdanbooru](https://github.com/KichangKim/DeepDanbooru)（以下简称DD）封装的工具，采用Flask框架编写而成，根据DD的作者文档中的内容，需要python3.7+才能运行。由于DD的作者制作的在线工具服务器在国外，访问的速度较慢，所以DD-web-demo就此诞生了。
DD-webui有以下优势：
* **操作简易**：克隆仓库后可直接使用，无需过多设置，全程无坑
* **支持本地化部署**：不需要将图片上传到别人的服务器，本地直接加载与训练模型，节省上传到云端的时间，可以免由于网络不稳定引起的错误
* **支持docker部署**：docker采用沙箱环境隔离机制，将容器与服务器隔离起来，较有效地避免服务器直接受到恶意代码攻击
* **占用空间低**：源代码只有几MB，与训练模型只有500MB，部署docker镜像也就需要4GB左右，不需要GPU也能快速反应

**在运行这个程序时提前加载了与训练模型，节省了生成tag的时间本地部署响应速度会远远高于访问DD作者制作的demo**

## 许可证

本软件基于MIT开源协议进行授权和分发。

版权所有 (c) 2023 仙

本软件采用MIT许可证进行授权，允许被授权人有权使用、复制、修改、合并、发布、分发、再许可及/或销售本软件。

虽然本协议并未规定必须在衍生程序中标注原作者的名字，也没有规定衍生的程序必须开源，但还是鼓励大家标注原作者的名字，并且在非商用的情况下开源衍生程序

免责声明：本软件按"原样"提供，作者不承担任何明示或暗示的保证或责任。在任何情况下，作者对由使用本软件引起的任何损害或其他责任概不负责。

## 使用方法

### 环境安装
克隆本仓库：
```bash
git clone git@github.com:tianhuzong/DD-web-demo.git
```
或
```bash
git clone https://github.com/tianhuzong/DD-web-demo.git
```
国内可能由于github的DNS污染无法克隆，可以使用国内镜像仓库：
```bash
git clone git@gitee.com:thzsen/DD-web-demo.git
```
或
```bash
git clone https://gitee.com/thzsen/DD-web-demo.git
```

## 预训练模型下载
可以在[DD作者的发行版](https://kgithub.com/KichangKim/DeepDanbooru/releases/tag/v3-20211112-sgd-e28)下载，然后把解压后的文件夹里的文件覆盖DD-web-demo/DD-webui/model内的文件。

## 运行程序
### 方法一：使用docker（推荐）：
克隆仓库，下载预训练模型后，打开docker终端，进入DD-web-demo目录，可以看到该目录下有个Dockerfile，不懂怎么修改请按照作者的原配置即可，懂的话可以适当自己修改
#### 构建镜像
**Tip：由于在Windows系统中，docker默认缓存目录是在C盘，我在github代码空间构建镜像时大约是3.5-4GB，缓存也是写在C盘的，如果C盘空间不够，你可以修改docker的配置文件**
运行命令：
```bash
docker build -t <镜像名称>. //例如docker build -t ddwebui .
```
最后面的``.``千万别忘记
由于镜像较大，构建过程需要点时间，趁着构建镜像的时间去刷个视频或吃点东西吧。

#### 运行镜像
只要你前面没有出错，那么恭喜你，你的镜像构建成功啦！
接下来你只需要运行镜像：
```bash
docker run -p 5000:5000 ddwebui 
```
运行完出现提示了就访问http://127.0.0.1:5000即可
**5000:5000第一个5000是在你的服务器或电脑上的端口，第二个5000是你在dockerfile中暴露的端口，如果你要修改docker暴露的端口记得要修改app.py的port哦！**

为了要节省生成tag的时间，我在源代码一开始运行的时候就加载了一遍与训练模型，大约要花7-8秒，不然的话每反推一次tag就得等8秒
**如果你使用的是github codespace，一般情况下有自动端口转发，然后就会给你弹出一个消息框让你在浏览器打开，但是请你先别急，在终端还没有弹出提示时，你直接打开会502**
你不想使用了可以直接按<kbd>Ctrl+C</kbd>退出，但是docker容器也会跟着关闭，如果你不想让终端一直挂着，但是想要继续运行容器，那就先<kbd>Ctrl+C</kbd>,然后运行``docker ps -a``找到你原来的那个容器的ID，运行``docker start <容器ID>``，反过来，如果你想要停止了就运行``docker stop <容器ID>``。

## 方法二：直接运行
直接运行适用于测试环境或开发环境，因为直接运行少了docker沙箱机制的保护，可能会受到恶意代码的攻击，请不要用这个办法部署生成环境。

克隆仓库，下载与训练模型后直接进入DD-web-demo/DD-webui

### 创建虚拟环境
```bash
python -m venv venv
```
### 进入虚拟环境
```bash
Windows:
cd venv
Scripts\activate.bat
如果你使用的是PowerShell
那就使用
Scripts\Activate.ps1
Linux/Mac OS:
source venv/bin/activate
```
### 安装依赖
```bash
pip install -r requirements.txt
pip install .
```
运行完可以删除deepdanbooru文件夹和setup.py的文件
### 运行主程序
```bash 
python app.py
```
或者设置环境变量``FLASK_APP=app.py``，然后运行
```bash
flask run
//有写电脑/服务器可能会报错，推荐使用
python -m flask run
```
然后访问http://127.0.0.1:5000
，但是我不建议部署在github codespace，因为我在github codespace部署时一直得不到返回值，我看下是因为上传文件的问题，使用codespace部署可能会导致无法上传文件
