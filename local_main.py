import numpy as np
import pyqtgraph as pg
import time
import threading
from PyQt5.QtCore import QTimer,QDateTime

import music_location_class as mlc
import mic_record_class as mr
import pyqt.test_main as tmain


RECORD_DEVICE_NAME = "Yundea 8MICA: USB Audio"
RECORD_RATE = 48000
RECORD_CHANNELS = 8
RECORD_WIDTH = 2 #字节数
CHUNK = 2000
record1=mr.mic_record(RECORD_DEVICE_NAME,RECORD_RATE,RECORD_CHANNELS,RECORD_WIDTH,CHUNK);

distance_mic=0.05;  #阵元间距  小于波长的一半
wavespeed=347;      #波速
miccount=4;         #阵元数量
fs=RECORD_RATE;           #采样频率
ts=1/fs;            #时域采样周期
freq=2000;          #信号频率
sp=CHUNK;            #采样点数


locas=mlc.music_location(distance_mic_=distance_mic,
                            wavespeed_=wavespeed,
                            miccount_=miccount,
                            fs_=fs,
                            freq_=freq,
                            sp_=sp);

app = tmain.QApplication(tmain.sys.argv)
    
mywindows=tmain.mywindows()
    

def get_angle():
    # data=record1.read_record_buffer();
    data=mlc.sim_data(freq=freq,
                        sp=CHUNK,
                        angle=0.1);
    res=locas.location(data[:4,:])
    mywindows.plot_data.setData(data[3,:]);
    fft_res=abs(np.fft.fft(data[3,:]))
    mywindows.plot_data_2.setData((fs/sp)*np.linspace(0,(sp/2)-1,sp//2),fft_res[:sp//2]);
    mywindows.plot_data_3.setData(range(0,600,1),res);
    print("refreash")
    
    # timer=threading.Timer(1,get_angle);
    # timer.start();

timer=QTimer();
timer.timeout.connect(get_angle);

timer.start(3000);

tmain.sys.exit(app.exec_())


# timer = pg.QtCore.QTimer()
# timer.timeout.connect(lambda : get_angle(record1)) # 定时刷新数据显示
# timer.start(2000) # 多少ms调用一次