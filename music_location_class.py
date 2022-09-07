# from dis import dis
# from platform import freedesktop_os_release
# import wave
# from cgitb import reset
from signal import signal
import numpy as np
import matplotlib.pyplot as plt
import time


class music_location():
    
    # distance_mic=0.25;  #阵元间距  小于波长的一半
    # wavespeed=340;      #波速
    # miccount=4;         #阵元数量
    # fs=16000;           #采样频率
    # freq=672;           #信号频率
    # sp=1000;            #采样点数
    def __init__(self,distance_mic_,wavespeed_,miccount_,fs_,freq_,sp_,angle_range):
        self.distance_mic=distance_mic_;    #阵元间距  小于波长的一半
        self.wavespeed=wavespeed_;          #波速
        self.miccount=miccount_;            #阵元数量
        self.fs=fs_;                        #采样频率q
        self.ts=1/self.fs;                  #时域采样周期
        self.freq=freq_;                    #信号频率
        self.sp=sp_;                        #采样点数
        self.freq_res=self.fs/self.sp;      #fft 频率分辨率
        self.angle_range=angle_range;
        self.dtorad=np.pi/180;                   #degrad 转 rad 

    def location(self,data):
        self.fft_res=np.zeros([self.miccount,self.sp],dtype=np.complex);
        for cnt in np.arange(self.miccount):
            self.fft_res[cnt,:]=np.fft.fft(data[cnt,:]);
        
        freq_counter=int(self.freq/self.freq_res);
        print("freq_counter    =",freq_counter)
        freq_range_start=freq_counter-0
        freq_range_end=freq_counter+1

        rxx=np.zeros((7,self.miccount,self.miccount),dtype=np.complex);
        eigvetor=np.zeros((7,self.miccount,self.miccount),dtype=np.complex);
        noise_eigvetor=np.zeros((7,self.miccount,self.miccount-1),dtype=np.complex);

        rxx_cnt=0;
        for i in np.arange(freq_range_start,freq_range_end,1):  
            temp=np.zeros((self.miccount,1),dtype=np.complex);
            temp[0,0]=self.fft_res[0,i];
            temp[1,0]=self.fft_res[1,i];
            temp[2,0]=self.fft_res[2,i];
            temp[3,0]=self.fft_res[3,i];
            rxx[rxx_cnt,:,:]=np.dot(temp,temp.T.conjugate());  #计算每个频率下各个阵元的协方差矩阵
            # rxx[rxx_cnt,:,:]=np.dot(self.fft_res[:,i],self.fft_res[:,i].T.conjugate());  #计算每个频率下各个阵元的协方差矩阵
            eigvetor[rxx_cnt,:,:],eigval,_ = np.linalg.svd(rxx[rxx_cnt,:,:])                                                                                                                                                                                                                                                                
            noise_eigvetor[rxx_cnt,:,:]=eigvetor[rxx_cnt,:,1:]
            rxx_cnt+=1;
        
        # angle_1=np.arctan(self.fft_res[0][80].imag/self.fft_res[0][80].real);
        # angle_2=np.arctan(self.fft_res[1][80].imag/self.fft_res[1][80].real);
        # angle_3=np.arctan(self.fft_res[2][80].imag/self.fft_res[2][80].real);
        # angle_4=np.arctan(self.fft_res[3][80].imag/self.fft_res[3][80].real);
        
        # print("angle between 1 and 2:",angle_1-angle_2);
        # print("angle between 2 and 3:",angle_2-angle_3);
        # print("angle between 3 and 4:",angle_3-angle_4);

        res=np.zeros(int((self.angle_range[1]-self.angle_range[0])/0.1));
        print("renge angle :",int((self.angle_range[1]-self.angle_range[0])/0.1))
        cnt=0;
        for deg in np.arange(self.angle_range[0],self.angle_range[1],0.1):
            rxx_cnt=0;
            for i in np.arange(freq_range_start,freq_range_end,1):  
                n_freq=i*self.freq_res;  #频率
                n_time=1/n_freq; #周期
                dir_vetor=np.zeros([1,self.miccount],dtype=np.complex);
                tim_dif=self.distance_mic*np.sin(deg*self.dtorad)/self.wavespeed;
                dir_vetor[0,:]=np.exp(-1j*2*np.pi*np.linspace(0,self.miccount-1,self.miccount)*(tim_dif/n_time)); #1 * 4 矩阵
                dir_vetort=dir_vetor.T;
                res[cnt] += abs(np.dot(np.dot(np.dot(dir_vetort.T.conjugate(),noise_eigvetor[rxx_cnt,:,:]),noise_eigvetor[rxx_cnt,:,:].T.conjugate()),dir_vetort));
                rxx_cnt +=1;
                
            res[cnt]=1/(res[cnt]/(100));
            cnt +=1;

        maxindex=np.argmax(res);
        # print("max index :",maxindex)
        resangle=self.angle_range[0]+maxindex*0.1;
        print("angle:  ",resangle);
        # print("max val              :",res[maxindex])
        
        # plt.figure(3);
        # plt.plot(np.arange(-30,30,0.1),res); 
        return res,resangle;



def sim_data(freq,sp,angle,noise_exp,noise_var):
    distance_mic=0.05;  #阵元间距  小于波长的一半
    wavespeed=340;      #波速
    miccount=4;         #阵元数量
    fs=48000;           #采样频率
    ts=1/fs;            #时域采样周期
    # freq=2000;          #信号频率
    noise_freq=30;     #噪音频率     
    # sp=2000;            #采样点数

    freq_res=fs/sp;     #fft 频率分辨率
    signal_num=1;       #信源数量
    dc_va=0;            #信源直流分量

    # noise_exp=10;       #噪声期望
    # noise_var=5;        #噪声标准差

    wave_arived_angle=angle;        #信源角度
    dtorad=np.pi/180;               #degrad 转 rad 

    x=np.linspace(0,sp/fs,sp);      
    m1=np.zeros(sp);
    m2=np.zeros(sp);
    m3=np.zeros(sp);
    m4=np.zeros(sp);
    # print(np.random.normal(noise_exp,noise_var,1000))
    # print(type(m1[0]))
    
    m1=2*np.sin((freq*2*np.pi)*(x-(0*distance_mic*np.sin(wave_arived_angle*dtorad)/wavespeed)))+dc_va+np.random.normal(noise_exp,noise_var,sp);
    m2=2*np.sin((freq*2*np.pi)*(x-(1*distance_mic*np.sin(wave_arived_angle*dtorad)/wavespeed)))+dc_va+np.random.normal(noise_exp,noise_var,sp);
    m3=2*np.sin((freq*2*np.pi)*(x-(2*distance_mic*np.sin(wave_arived_angle*dtorad)/wavespeed)))+dc_va+np.random.normal(noise_exp,noise_var,sp);
    m4=2*np.sin((freq*2*np.pi)*(x-(3*distance_mic*np.sin(wave_arived_angle*dtorad)/wavespeed)))+dc_va+np.random.normal(noise_exp,noise_var,sp);

    m1+=20*np.sin((noise_freq*2*np.pi)*(x-(0*distance_mic*np.sin(wave_arived_angle*dtorad)/wavespeed)));
    m2+=20*np.sin((noise_freq*2*np.pi)*(x-(1*distance_mic*np.sin(wave_arived_angle*dtorad)/wavespeed)));
    m3+=20*np.sin((noise_freq*2*np.pi)*(x-(2*distance_mic*np.sin(wave_arived_angle*dtorad)/wavespeed)));
    m4+=20*np.sin((noise_freq*2*np.pi)*(x-(3*distance_mic*np.sin(wave_arived_angle*dtorad)/wavespeed)));


    

    #信号源数量估计   窄带信号的协方差矩阵分解  特征值估计法 
    signal_num_est=np.zeros([4,sp]);
    signal_num_est[0][:]=m1;
    signal_num_est[1][:]=m2;
    signal_num_est[2][:]=m3;
    signal_num_est[3][:]=m4;
    return signal_num_est;

        
if __name__ == "__main__":

    distance_mic=0.05;  #阵元间距  小于波长的一半
    wavespeed=340;      #波速
    miccount=4;         #阵元数量
    fs=48000;           #采样频率
    ts=1/fs;            #时域采样周期
    freq=2000;          #信号频率
    freq2=480; #     
    sp=1000;            #采样点数


    loca=music_location(distance_mic_=distance_mic,
                            wavespeed_=wavespeed,
                            miccount_=miccount,
                            fs_=fs,
                            freq_=freq,
                            sp_=sp,
                            angle_range=[-60,60]);

    freq_res=fs/sp;     #fft 频率分辨率
    signal_num=1;       #信源数量
    dc_va=500;          #信源直流分量

    noise_exp=100;        #噪声期望
    noise_var=4;        #噪声标准差

    wave_arived_angle=58;        #信源角度
    wave_arived_angle2=10;
    dtorad=np.pi/180;               #degrad 转 rad 

    x=np.linspace(0,1000/fs,1000);      
    m1=np.zeros(1000);
    m2=np.zeros(1000);
    m3=np.zeros(1000);
    m4=np.zeros(1000);
    # print(np.random.normal(noise_exp,noise_var,1000))
    
    while True:
        m1=20*np.sin((freq*2*np.pi)*(x-(0*distance_mic*np.sin(wave_arived_angle*dtorad)/wavespeed)))+dc_va+np.random.normal(noise_exp,noise_var,1000);
        m2=20*np.sin((freq*2*np.pi)*(x-(1*distance_mic*np.sin(wave_arived_angle*dtorad)/wavespeed)))+dc_va+np.random.normal(noise_exp,noise_var,1000);
        m3=20*np.sin((freq*2*np.pi)*(x-(2*distance_mic*np.sin(wave_arived_angle*dtorad)/wavespeed)))+dc_va+np.random.normal(noise_exp,noise_var,1000);
        m4=20*np.sin((freq*2*np.pi)*(x-(3*distance_mic*np.sin(wave_arived_angle*dtorad)/wavespeed)))+dc_va+np.random.normal(noise_exp,noise_var,1000);



        

        #信号源数量估计   窄带信号的协方差矩阵分解  特征值估计法 
        signal_num_est=np.zeros([4,1000]);
        signal_num_est[0][:]=m1;
        signal_num_est[1][:]=m2;
        signal_num_est[2][:]=m3;
        signal_num_est[3][:]=m4;
        start_time=time.time();
        loca.location(signal_num_est);
        # print("time cost :",start_time-time.time());
    plt.show();
    print("end")
    