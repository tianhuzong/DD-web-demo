from flask import Flask,render_template,request
import DD_tools
import deepdanbooru as dd
import json
import base64
import random
app = Flask(__name__)
model = dd.project.load_model_from_project("./model")
tags = dd.data.load_tags("./model/tags.txt")
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/upload",methods=["POST"])
def upload():
        # 检查是否有文件被上传
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']
    yz : int =0.5 #生成的标签可信度阈值
    random.seed()
    rand = random.randint(7,27053667326596)
    imagepath = "./photo/" + rand
    file.save(imagepath)
    
    markdict : dict = DD_tools.get_mark(imagepath,model,tags,yz,True)
    return json.dumps(markdict)
@app.route("/api/upload",methods=["GET","POST"])
def api_upload():
    if request.method == "GET":
        pic_b64 = request.args.get("pic")
        geshi = request.args.get("kuozhanming")
    elif request.method == "POST":
        pic_b64 = request.form.get("pic")
        geshi = request.form.get("kuozhanming")
    if geshi not in ["png","jpg"]:
        return json.dumps({"msg":"error"})
    pic_bytes = base64.b64encode(pic_b64)
    random.seed()
    rand = random.randint(7,27053667326596)
    imagepath = "./apiphoto/" + str(rand) + geshi
    with open(imagepath,mode="wb") as f:
        f.write(pic_bytes)
    yz : int = 0.5 #生成的标签可信度阈值
    markdict : dict = DD_tools.get_mark(imagepath,model,tags,yz,True)
    return json.dumps(markdict)
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)