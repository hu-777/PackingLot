#!/usr/bin/env python
# coding: utf-8

# In[3]:


# coding=utf-8
# 使用百度API，ocr识别图片中的文字，参考网页https://ai.baidu.com/ai-doc/OCR/dk3iqnq51
import sys
import json
import base64
import os
import time
# 保证兼容python2以及python3
IS_PY3 = sys.version_info.major == 3
if IS_PY3:
    from urllib.request import urlopen #打开网址
    from urllib.request import Request  #网页请求
    from urllib.error import URLError   #网址错误
    from urllib.parse import urlencode  #网址编码
    from urllib.parse import quote_plus #屏蔽特殊字符


# 防止https证书校验不正确
import ssl #套接字编程安全性和身份验证
ssl._create_default_https_context = ssl._create_unverified_context

API_KEY = 'I0Du0ipYBloybRNMubWe7E1C' #这里用你自己申请的资源API_KEY替换

SECRET_KEY = 'iPsKzr3W1JQiEwXnL7qTf49winAZ9WYF' #这里用你自己申请的资源SECRET_KEY替换


OCR_URL = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"


"""  TOKEN start """
TOKEN_URL = 'https://aip.baidubce.com/oauth/2.0/token'


"""
    获取token
"""
def fetch_token():
    params = {'grant_type': 'client_credentials',
              'client_id': API_KEY,
              'client_secret': SECRET_KEY}
    post_data = urlencode(params) 
    if (IS_PY3):
        post_data = post_data.encode('utf-8')
    req = Request(TOKEN_URL, post_data)  #向TOKEN_URL发送请求，参数在post_data
    try:
        f = urlopen(req, timeout=5)  #根据请求获得反馈的内容
        result_str = f.read()        #读取内容
    except URLError as err:
        print(err)
    if (IS_PY3):
        result_str = result_str.decode()  #解码


    result = json.loads(result_str)  #json是一种便于人读写的对象格式

    if ('access_token' in result.keys() and 'scope' in result.keys()):
        if not 'brain_all_scope' in result['scope'].split(' '):  
            print ('please ensure has check the  ability')
            exit()
        return result['access_token']
    else:
        print ('please overwrite the correct API_KEY and SECRET_KEY')
        exit()

"""
    读取文件
"""
def read_file(image_path):
    f = None
    try:
        f = open(image_path, 'rb')
        return f.read()
    except:
        print('read image file fail')
        return None
    finally:
        if f:
            f.close()


"""
    调用远程服务
"""
def request(url, data):
    req = Request(url, data.encode('utf-8'))
    has_error = False
    try:
        f = urlopen(req)
        result_str = f.read()
        if (IS_PY3):
            result_str = result_str.decode()
        return result_str
    except  URLError as err:
        print(err)


def tupianshibie():
    if __name__ == '__main__':

        # 获取access token
        token = fetch_token()

        # 拼接通用文字识别高精度url
        image_url = OCR_URL + "?access_token=" + token

        

        # 读取书籍页面图片
        #file_content = read_file('./text.jpg')
        directory = './' #选择图片路径
        for filename in os.listdir(directory):     #依次读取路径下的每一个文件   
            fn = directory + filename              #fn是包含路径的文件
            print(fn)
            text = ""
            if os.path.isfile(fn) and fn.endswith(('.jpg','.jfif','jpeg','bmp','png')):     #确定是图片文件               
                file_content = read_file(fn)      #读取fn文件数据
                # 调用文字识别服务
                result = request(image_url, urlencode({'image': base64.b64encode(file_content)})) 
                
                # 解析返回结果
                result_json = json.loads(result)
                for words_result in result_json["words_result"]:
                    text = text + words_result["words"]
                # 打印文字
                print(text)
                time.sleep(2)
                # 将识别的文字保存到文本文件中
                output_file_path = '车牌识别\chepaihao.txt'
                with open(output_file_path, 'a', encoding='utf-8') as f:
                    f.write(text)
                    f.write("\n")
                #print("识别的文字已保存到文件:", output_file_path)


"""
    找到并提取'D:\\桌面\\New project\output_text.txt'中的车牌号码
"""
def find_car_number():
    with open('车牌识别\chepaihao.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        # 找到车牌号码
        car_number = ''
        for i in range(len(text)):
            if (text[i]==('京','津','黑','吉','辽','冀','豫','鲁','晋','陕','蒙','宁','甘','新','青',
                          '藏','鄂','皖','苏','沪','浙','闵','湘','赣','川','渝','贵','云','粤','桂',
                            '琼','港','澳','台')) and (text[i+1].isdigit() or text[i+1]=='A' or text[i+1]=='B' 
                                                   or text[i+1]=='C' or text[i+1]=='D' or text[i+1]=='E' 
                                                   or text[i+1]=='F' or text[i+1]=='G' or text[i+1]=='H' 
                                                   or text[i+1]=='I' or text[i+1]=='J' or text[i+1]=='K' 
                                                   or text[i+1]=='L' or text[i+1]=='M' or text[i+1]=='N' 
                                                   or text[i+1]=='O' or text[i+1]=='P' or text[i+1]=='Q' 
                                                   or text[i+1]=='R' or text[i+1]=='S' or text[i+1]=='T' 
                                                   or text[i+1]=='U' or text[i+1]=='V' or text[i+1]=='W' 
                                                   or text[i+1]=='X' or text[i+1]=='Y' or text[i+1]=='Z'):
                car_number = car_number + text[i]
                if ((text[i].isdigit()) or (text[i]=='A' or text[i]=='B' 
                                            or text[i]=='C' or text[i]=='D' or text[i]=='E' 
                                            or text[i]=='F' or text[i]=='G' or text[i]=='H' 
                                            or text[i]=='I' or text[i]=='J' or text[i]=='K' 
                                            or text[i]=='L' or text[i]=='M' or text[i]=='N' 
                                            or text[i]=='O' or text[i]=='P' or text[i]=='Q' 
                                            or text[i]=='R' or text[i]=='S' or text[i]=='T' 
                                            or text[i]=='U' or text[i]=='V' or text[i]=='W' 
                                            or text[i]=='X' or text[i]=='Y' or text[i]=='Z')):
                    car_number = car_number + text[i]
            output_file_path = 'chepaihao.txt'
            with open(output_file_path, 'a', encoding='utf-8') as f:
                f.write(car_number)
                f.write("\n")
                print("识别的文字已保存到文件:", output_file_path)
            break

        
        # 打印车牌号码


def main():
    tupianshibie()
    find_car_number()
main()
