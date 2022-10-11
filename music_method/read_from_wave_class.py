import wave
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
import pyqtgraph as pg
import time
import queue
import music_location_class as mlc
print("this read from wave class file\r\n")


class read_frome_wave():
    def __init__(self):
        # f1=wave.open(r"D:\工程文件\电赛\声源定位\音频\音轨.wav","rb");
        # f2=wave.open(r"D:\工程文件\电赛\声源定位\音频\音轨-2.wav","rb");
        # f3=wave.open(r"D:\工程文件\电赛\声源定位\音频\音轨-3.wav","rb");
        # f4=wave.open(r"D:\工程文件\电赛\声源定位\音频\音轨-4.wav","rb");
        # f5=wave.open(r"D:\工程文件\电赛\声源定位\音频\音轨-5.wav","rb");
        # f6=wave.open(r"D:\工程文件\电赛\声源定位\音频\音轨-6.wav","rb");
        # f7=wave.open(r"D:\工程文件\电赛\声源定位\音频\音轨-7.wav","rb");
        # f8=wave.open(r"D:\工程文件\电赛\声源定位\音频\音轨-8.wav","rb");
        
        
        f1=wave.open(r"D:\工程文件\电赛\声源定位\音频\pcb阵列\音轨.wav","rb");
        f2=wave.open(r"D:\工程文件\电赛\声源定位\音频\pcb阵列\音轨-2.wav","rb");
        f3=wave.open(r"D:\工程文件\电赛\声源定位\音频\pcb阵列\音轨-3.wav","rb");
        f4=wave.open(r"D:\工程文件\电赛\声源定位\音频\pcb阵列\音轨-4.wav","rb");
        f5=wave.open(r"D:\工程文件\电赛\声源定位\音频\pcb阵列\音轨-5.wav","rb");
        f6=wave.open(r"D:\工程文件\电赛\声源定位\音频\pcb阵列\音轨-6.wav","rb");
        f7=wave.open(r"D:\工程文件\电赛\声源定位\音频\pcb阵列\音轨-7.wav","rb");
        f8=wave.open(r"D:\工程文件\电赛\声源定位\音频\pcb阵列\音轨-8.wav","rb");
        self.file_list=[f1,f2,f3,f4,f5,f6,f7,f8];
    
    def file_params(self):
        params =self.file_list[0].getparams();
        print(params);
        nchannels,sampwith,framesrate,nframes=params[:4];
        print(nchannels,sampwith,framesrate,nframes);
        return nchannels,sampwith,framesrate,nframes;

    def read_frames(self,chanle_num,lenth):
        try:
            data=np.zeros([chanle_num,lenth]);
            for i in range(chanle_num):
                data[i,:]=np.frombuffer(self.file_list[i].readframes(lenth),dtype=np.short);
            return data;
        except Exception as e:
            print("read wave error\r\n");
            print(e);
            return data;
    def get_nframe(self):
        return self.file_list[0].getnframes();
    
    
    
if __name__ == "__main__":
    re_wave=read_frome_wave();
    print(re_wave.file_params());
    f1_data=re_wave.read_frames(4,1920);
    print("get n frames :", re_wave.get_nframe());
    # freq=2000;          #信号频率
    # CHUNK=1920;
    # f1_data=mlc.sim_data(freq=freq,
    #                     sp=CHUNK,
    #                     angle=10,
    #                     noise_exp=0,
    #                     noise_var=0);
    
    plt.figure();
    plt.subplot(4,1,1);
    plt.plot(f1_data[0,:]);
    
    plt.subplot(4,1,2);
    plt.plot(f1_data[1,:]);
    
    plt.subplot(4,1,3);
    plt.plot(f1_data[2,:]);
    
    plt.subplot(4,1,4);
    plt.plot(f1_data[3,:]);
    plt.show();
