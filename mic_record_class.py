import pyaudio
import matplotlib.pyplot as plt
import numpy as np
import threading
from multiprocessing import Process, Queue
import time

from pyqtgraph.Qt import QtGui,QtCore
import pyqtgraph as pg
import wave
import json
import signal
import sys
import os


# https://people.csail.mit.edu/hubert/pyaudio/docs/
#pyaudio documentation
# https://github.com/jim2meng/dueros/blob/master/example/record.py
#淘宝客服参考代码连接


class mic_record():
    def __init__(self,RECORD_DEVICE_NAME,RECORD_RATE,RECORD_CHANNELS,RECORD_WIDTH,CHUNK):
        self.p = pyaudio.PyAudio();
        self.chunk=CHUNK
        self.record_channels=RECORD_CHANNELS
        for self.index in range(0,self.p.get_device_count()):
            self.info=self.p.get_device_info_by_index(self.index);
            self.device_name = self.info.get("name");
            print("device index:",self.index,"device name:",self.device_name);
            if self.device_name.find(RECORD_DEVICE_NAME) != -1 :
                print("record device name:",self.device_name,"record index :" ,self.index);
                self.record_device_index=self.index;
                break;

        self.stream = self.p.open(
                    rate=RECORD_RATE, #采样率
                    format=self.p.get_format_from_width(RECORD_WIDTH), #抽样大小和格式 2字节
                    channels=RECORD_CHANNELS, #通道数量
                    input=True, #是不是输入流
                    input_device_index = self.record_device_index,#输入设备索引
                    start=False, #是否立即开启
                    frames_per_buffer=CHUNK);#指定每个缓冲区大小
        self.stream.start_stream();
        print(self.device_name,":stream start");
    
    def read_record_buffer(self):
        self.data = self.stream.read(self.chunk,exception_on_overflow = False);
        self.data = np.frombuffer(self.data,dtype=np.short);
        self.data=self.data.reshape(self.chunk, self.record_channels);
        self.data=self.data.T;
        return self.data;









def gp_data_process(n):
    start_time=time.time();
    data=n.read_record_buffer();
    print("date pre :",time.time()-start_time);
    pw.setData(data[7,:]);
    print(time.time()-start_time);
    





if __name__ == "__main__":
    
    win = pg.GraphicsWindow(title="在同一个窗口，不同的图标中绘制双曲线");
    plot1 = win.addPlot();
    pw=plot1.plot();
    RECORD_DEVICE_NAME = "Yundea 8MICA: USB Audio"
    RECORD_RATE = 48000
    RECORD_CHANNELS = 8
    RECORD_WIDTH = 2 #字节数
    CHUNK = 1024
    record1=mic_record(RECORD_DEVICE_NAME,RECORD_RATE,RECORD_CHANNELS,RECORD_WIDTH,CHUNK);

    timer = pg.QtCore.QTimer()
    timer.timeout.connect(lambda : gp_data_process(record1)) # 定时刷新数据显示
    timer.start(100) # 多少ms调用一次

    pg.QtGui.QApplication.exec_();