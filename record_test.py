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
RECORD_DEVICE_NAME = "Yundea 8MICA: USB Audio"
RECORD_RATE = 48000
RECORD_CHANNELS = 8
RECORD_WIDTH = 2
CHUNK = 1024



p = pyaudio.PyAudio();
for index in range(0,p.get_device_count()):
    info=p.get_device_info_by_index(index);
    device_name = info.get("name");
    print("device index:",index,"device name:",device_name);
    if device_name.find(RECORD_DEVICE_NAME) != -1 :
        print("record device name:",device_name,"record index :" ,index);
        record_device_index=index;
        break;

stream = p.open(
            rate=RECORD_RATE, #采样率
            format=p.get_format_from_width(RECORD_WIDTH), #抽样大小和格式 2字节
            channels=RECORD_CHANNELS, #通道数量
            input=True, #是不是输入流
            input_device_index = record_device_index,#输入设备索引
            start=False, #是否立即开启
            frames_per_buffer=CHUNK);#指定每个缓冲区大小
stream.start_stream();

print(device_name,":stream start");

def sound_record(q):
    while(1):
        data = stream.read(CHUNK,exception_on_overflow = False);
        data = np.frombuffer(data,dtype=np.short);
        data=data.reshape(CHUNK,RECORD_CHANNELS);
        data=data.T;
        q.put(data);
        time.sleep(0.1);
        print("record finish");



plt.figure("sound wave");
plt.ion();
print("figure created");
def data_process(q):
    while(1):
        data=q.get();
        plt.clf();  # 清除之前画的图
        plt.subplot(4,1,1);
        plt.plot(np.linspace(0,1,1024),data[0,:]);  # 画出当前x列表和y列表中的值的图形
        plt.ylim(-300,300);
        plt.subplot(4,1,2);
        plt.plot(np.linspace(0,1,1024),data[1,:]);  # 画出当前x列表和y列表中的值的图形
        plt.ylim(-300,300);
        plt.subplot(4,1,3);
        plt.plot(np.linspace(0,1,1024),data[2,:]);  # 画出当前x列表和y列表中的值的图形
        plt.ylim(-300,300);
        plt.subplot(4,1,4);
        plt.plot(np.linspace(0,1,1024),data[3,:]);  # 画出当前x列表和y列表中的值的图形
        plt.ylim(-300,300);
        plt.pause(0.01);  # 暂停一段时间，不然画的太快会卡住显示不出来
        plt.ioff();  # 关闭画图窗口
        print("plt finish");


def process_test():
    while(1):
        start_time=time.time();
        data = stream.read(CHUNK,exception_on_overflow = False);
        data = np.frombuffer(data,dtype=np.short);
        data=data.reshape(CHUNK,RECORD_CHANNELS);
        data=data.T;
        print("date pre :",time.time()-start_time);
        plt.clf();  # 清除之前画的图
        plt.subplot(4,1,1);
        plt.plot(np.linspace(0,1,1024),data[0,:]);  # 画出当前x列表和y列表中的值的图形
        plt.ylim(-300,300);
        plt.subplot(4,1,2);
        plt.plot(np.linspace(0,1,1024),data[1,:]);  # 画出当前x列表和y列表中的值的图形
        plt.ylim(-300,300);
        plt.subplot(4,1,3);
        plt.plot(np.linspace(0,1,1024),data[2,:]);  # 画出当前x列表和y列表中的值的图形
        plt.ylim(-300,300);
        plt.subplot(4,1,4);
        plt.plot(np.linspace(0,1,1024),data[3,:]);  # 画出当前x列表和y列表中的值的图形
        plt.ylim(-300,300);
        plt.pause(0.01);  # 暂停一段时间，不然画的太快会卡住显示不出来
        plt.ioff();  # 关闭画图窗口
        print(time.time()-start_time);




def gp_data_process():
    start_time=time.time();
    data = stream.read(CHUNK,exception_on_overflow = False);
    data = np.frombuffer(data,dtype=np.short);
    data=data.reshape(CHUNK,RECORD_CHANNELS);
    data=data.T;
    print("date pre :",time.time()-start_time);
    pw.setData(data[7,:]);
    print(time.time()-start_time);
    

def gp_init():
    win = pg.GraphicsWindow(title="在同一个窗口，不同的图标中绘制双曲线");
    plot1 = win.addPlot();
    pw=plot1.plot();

    timer = pg.QtCore.QTimer()
    timer.timeout.connect(gp_data_process) # 定时刷新数据显示
    timer.start(20) # 多少ms调用一次

    pg.QtGui.QApplication.exec_();

def test1():
    while(1) :
        print("test1");

    
def test2():
    while(1):
        print("test2");



if __name__ == "__main__":
    # q=Queue(maxsize=1);
    # p1 = Process(target=sound_record,args=(q,));
    # p2 = Process(target=data_process,args=(q,));
    # p2.start();
    # p1.start();
    # p2.join();
    # p1.join();
    win = pg.GraphicsWindow(title="在同一个窗口，不同的图标中绘制双曲线");
    plot1 = win.addPlot();
    pw=plot1.plot();

    timer = pg.QtCore.QTimer()
    timer.timeout.connect(gp_data_process) # 定时刷新数据显示
    timer.start(50) # 多少ms调用一次

    pg.QtGui.QApplication.exec_();