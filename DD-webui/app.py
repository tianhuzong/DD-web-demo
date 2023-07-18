from flask import Flask,render_template,request
import DD_tools
import deepdanbooru as dd
import json
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("./index/index.html")
@app.route("/uploda",methods=["POST"])
def upload():
        # 检查是否有文件被上传
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']
    imagepath = "./photo/" + file.filename
    file.save(imagepath)
    model = dd.project.load_model_from_project("./model")
    tags = dd.data.load_tags("./model/tags.txt")
    markdict : dict = DD_tools.get_mark(imagepath,model,tags)
    return json.dumps(markdict)
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)