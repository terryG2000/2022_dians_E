import numpy as np
import matplotlib.pyplot as plt
import time as systime

class FrequencyDelayEstimator():
    def __init__(self,_fs,_n,_freq):
        self.fs=_fs;
        self.n=_n;
        self.freq=_freq;
        self.fft_freq_div=self.fs/self.n;

    def estimate_delay(self,data):
        cnt=0;
        freq_range_temp=np.zeros((1,100));
        for i in range(300):
            temp=(self.fft_freq_div*i)-self.freq;
            min_val=min(abs(temp));
            min_index=np.argmin(abs(temp));
            if min_val<self.fft_freq_div:
                freq_range_temp[0][cnt]=i;
                if cnt>=1 and freq_range_temp[0][cnt]==freq_range_temp[0][cnt-1]:
                    freq_range_temp[0][cnt]=0;
                    cnt=cnt-1;
                cnt=cnt+1;
        freq_range=freq_range_temp[0,:cnt];
        
        fft_res=np.fft.fft(data);
        fft_dis=fft_res[0,:].flatten()*fft_res[1,:].flatten().conjugate();
        plt.figure();
        plt.subplot(2,1,1);
        plt.plot(abs(fft_res[0,0:300]),'o');
        plt.subplot(2,1,2);
        plt.plot(np.angle(fft_dis[0:300]),'o');
        
        lsm_x=freq_range.flatten()*self.fft_freq_div;
        lsm_a=np.zeros((len(lsm_x),2));
        lsm_a[:,[0]]=lsm_x.reshape(-1,1);
        lsm_a[:,[1]]=np.ones((len(lsm_x),1));
        lsm_y=np.zeros((len(freq_range),1));
        
        for i in range(0,len(lsm_y)):
            lsm_y[i]=np.angle(fft_dis[ int(freq_range[i]) ]);
            
        res=np.dot(
                np.dot(
                    np.linalg.inv(
                        np.dot(lsm_a.T,lsm_a)
                        ),
                    lsm_a.T),
                lsm_y);
        print(res[0]/(2*np.pi));
        print("error{}".format(abs(td)-abs(res[0]/(2*np.pi))))
        return res;
        
        



if __name__ == '__main__':
    FS=48000;
    TS=1/FS;
    n=2000*4;
    fft_freq_div=FS/n;
    freq_dis=50;
    time_shifft=1e-6;
    time=np.arange(0+time_shifft,TS*(n-1)+time_shifft,TS);
    td=2.6e-6;
    

    # %构造原始信号和 延时信号

    f=np.arange(800,1200+1,freq_dis);
    
    
    estimate=FrequencyDelayEstimator(FS,n,f);
    
    i=1;
    x=np.zeros((1,len(time)));
    xd=np.zeros((1,len(time)));
    i=0;
    while i<len(f):
        x=x+np.sin(2*np.pi*f[i]*time);
        xd=xd+np.sin(2*np.pi*f[i]*(time-td));
        i=i+1;
        
        
    data=np.vstack((x.flatten(),xd.flatten()));
    
    start_time=systime.time();
    estimate.estimate_delay(data);
    print("time cost :{}".format(systime.time()-start_time))
    
    
    
    
    
    # fft_res=np.fft.fft(data);
    # fft_dis=fft_res[0,:].flatten()*fft_res[1,:].flatten().conjugate();
    
    # plt.figure();
    # plt.subplot(4,1,1);
    # plt.plot(data[0,:]);
    
    # plt.subplot(4,1,2);
    # plt.plot(abs(np.fft.fft(x[0,:])),'o');
    
    # plt.subplot(4,1,3);
    # plt.plot(abs(fft_res[0,:]),'o');
    
    # plt.subplot(4,1,4);
    # plt.plot(np.angle(fft_dis[:]),'o');
    
    
    
    plt.show();
            
        
        

                    