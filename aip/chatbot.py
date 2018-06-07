# -*- coding: utf-8 -*-
'''
Transfer the voice to string
'''
import wave
from aip import AipSpeech
import numpy as np
import requests, json

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

# def record_wave():
#     p = pyaudio.PyAudio()
#     stream = p.open(format = FORMAT,
#                     channels = CHANNELS,
#                     rate = RATE,
#                     input = True,
#                     frames_per_buffer=CHUNK)
#     # print "* recording"
#     frames = []
#     for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#         data = stream.read(CHUNK)
#         frames.append(data)
#
#     # print "* done recording"
#
#     stream.stop_stream()
#     stream.close()
#     p.terminate()
#
#     wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
#     wf.setnchannels(CHANNELS)
#     wf.setsampwidth(p.get_sample_size(FORMAT))
#     wf.setframerate(RATE)
#     wf.writeframes(b''.join(frames))
#     wf.close()
#
#
#
# def identify():
#     res = aipSpeech.asr(get_file_content(WAVE_OUTPUT_FILENAME), 'pcm', 16000, {'lan': 'zh',})
#     # print res["err_msg"]
#     if res["err_msg"] == "success.":
#         print(res["result"][0])
#         cont = requests.get('http://www.tuling123.com/openapi/api?key=不能告诉你&info=%s&userid=111' % (res["result"][0], )).content
#         m = json.loads(cont)
#         print (m['text'])
#
# def Monitor():
#     p = pyaudio.PyAudio()
#     stream = p.open(format=FORMAT,
#                     channels=CHANNELS,
#                     rate=RATE,
#                     input=True,
#                     frames_per_buffer=CHUNK)
#     # print("开始缓存录音")
#     frames = []
#     rec = []
#     flag = False
#     while (True):
#         # print 'begin '
#         data = stream.read(CHUNK)
#         if flag == True:
#             rec.append(data)
#         frames.append(data)
#         audio_data = np.fromstring(data, dtype=np.short)
#         large_sample_count = np.sum( audio_data > 2000 )
#         temp = np.max(audio_data)
#
#         # print temp
#
#         if temp > 2000:
#             flag = True
#             # print "检测到信号"
#             # print '当前阈值：',temp
#
#         if temp <= 2000:
#             # record_wave()
#             if flag == True:
#                 flag = False
#                 wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
#                 wf.setnchannels(CHANNELS)
#                 wf.setsampwidth(p.get_sample_size(FORMAT))
#                 wf.setframerate(RATE)
#                 wf.writeframes(b''.join(rec))
#                 wf.close()
#                 rec = []
#                 identify()
#
#     stream.stop_stream()
#     stream.close()
#     p.terminate()

# Monitor()