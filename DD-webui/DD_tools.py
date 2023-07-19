import deepdanbooru as dd
import requests
from bs4 import BeautifulSoup
import os
def get_mark(img_path,model,tags):
    markdict = {}
    for tag,mark in dd.commands.evaluate_image(img_path, model, tags, 0.5):
        markdict[tag] = str(mark)
        #print(f"{tag}:{mark}")
    return markdict
def get_files_in_folder(folder_path):
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(file_path)
    return file_list