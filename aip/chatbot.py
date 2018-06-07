# -*- coding: utf-8 -*-
'''
Transfer the voice to string
'''
import wave
from aip import AipSpeech
import numpy as np
import requests, json

# Baidu info
APP_ID = '11353809'
API_KEY = 'ZTF8Ngw4GRsu4Q5My15xRBl1'
SECRET_KEY = 'e3c6b2983cfa7747d403703b28d6587e'

aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


CHUNK = 1024
# FORMAT = pyaudio.paInt16
RATE = 16000
CHANNELS = 1
RECORD_SECONDS = 2
WAVE_OUTPUT_FILENAME = r"D:\Chatbot\voise\16k.pcm"


def get_file_content(file_path):
    with open(file_path, 'rb') as fp:
        return fp.read()


res = aipSpeech.asr(get_file_content(WAVE_OUTPUT_FILENAME), 'pcm', 16000, {'lan': 'zh',})

print(res["err_msg"])
if res["err_msg"] == "success.":
    print(res["result"][0])
    cont = requests.get(
        'http://www.tuling123.com/openapi/api?key=e388af15069f4eddac400c6147a705db&info=%s&userid=274715' % (res["result"][0],)).content
    m = json.loads(cont)
    print (m['text'])
