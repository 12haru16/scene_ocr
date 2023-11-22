import os
import easyocr
from PIL import Image
import PIL.ExifTags as ExifTags
import datetime

def scene_text():
    reader = easyocr.Reader(['ch_sim','en']) #ocrの読み込み（一回でOK)
    start_dir='test_img/'#画像を移動
    for p in os.listdir(start_dir):
        file=""
        file+= start_dir + p
        result = reader.readtext(file)
        #print(result)

        mozi=""
        for i in result:
            n=i[1]
            print(n)
            mozi+=n

        print(mozi)
        im = Image.open(file)
        exif_dict = {
        ExifTags.TAGS[k]: v
        for k, v in im._getexif().items()
            if k in ExifTags.TAGS
        }
        if "DateTimeOriginal" in exif_dict:
            #撮影日時に基づく新規ファイル名を準備
            file_dateTime = datetime.datetime.strptime(exif_dict["DateTimeOriginal"], "%Y:%m:%d %H:%M:%S")
            file_dateTime = file_dateTime.strftime("%Y-%m-%d_%H-%M-%S")
            print(file_dateTime)
        
        im.close()
        
        os.rename(file,start_dir + mozi + "_" + file_dateTime + ".jpg")
        
scene_text()
