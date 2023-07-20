import deepdanbooru as dd
import os
def get_mark(img_path,model,tags,yz,remove):
    """
    对一个图片评估标签
    Args:
        image_path:图片路径
        model:忘记了就去看deepdanbooru的源代码
        tags:使用函数处理过的标签
        yz:阈值
        remove:评估完是否删除图片
    """
    markdict = {}
    for tag,mark in dd.commands.evaluate_image(img_path, model, tags, yz):
        markdict[tag] = str(mark)
        #print(f"{tag}:{mark}")
    if remove:
        os.remove(img_path)
    return markdict
def get_files_in_folder(folder_path):
    """
    获取文件夹包含子目录中所有文件
    """
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(file_path)
    return file_list