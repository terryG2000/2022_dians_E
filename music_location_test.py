# from dis import dis
# from platform import freedesktop_os_release
# import wave
# from cgitb import reset
from signal import signal
import numpy as np
import matplotlib.pyplot as plt
import time

distance_mic=0.25;  #阵元间距  小于波长的一半
wavespeed=340;      #波速
miccount=4;         #阵元数量
fs=16000;           #采样频率
ts=1/fs;            #时域采样周期
freq=672;           #信号频率
freq2=480; #     
sp=1000;            #采样点数
freq_res=fs/sp;     #fft 频率分辨率
signal_num=1;       #信源数量
dc_va=500;          #信源直流分量

noise_exp=0;        #噪声期望
noise_var=5;        #噪声标准差

wave_arived_angle=-0.7;        #信源角度
wave_arived_angle2=10;
dtorad=np.pi/180;               #degrad 转 rad 

x=np.linspace(0,1000/fs,1000);      
m1=np.zeros(1000);
m2=np.zeros(1000);
m3=np.zeros(1000);
m4=np.zeros(1000);
# print(np.random.normal(noise_exp,noise_var,1000))
m1=100*np.sin((freq*2*np.pi)*(x-(0*distance_mic*np.sin(wave_arived_angle*dtorad)/wavespeed)))+dc_va+np.random.normal(noise_exp,noise_var,1000);
m2=100*np.sin((freq*2*np.pi)*(x-(1*distance_mic*np.sin(wave_arived_angle*dtorad)/wavespeed)))+dc_va+np.random.normal(noise_exp,noise_var,1000);
m3=100*np.sin((freq*2*np.pi)*(x-(2*distance_mic*np.sin(wave_arived_angle*dtorad)/wavespeed)))+dc_va+np.random.normal(noise_exp,noise_var,1000);
m4=100*np.sin((freq*2*np.pi)*(x-(3*distance_mic*np.sin(wave_arived_angle*dtorad)/wavespeed)))+dc_va+np.random.normal(noise_exp,noise_var,1000);


# m1 +=200*np.sin((freq2*2*np.pi)*(x-(0*distance_mic*np.sin(wave_arived_angle2*dtorad)/wavespeed)))+dc_va+np.random.normal(noise_exp,noise_var,1000);
# m2 +=200*np.sin((freq2*2*np.pi)*(x-(1*distance_mic*np.sin(wave_arived_angle2*dtorad)/wavespeed)))+dc_va+np.random.normal(noise_exp,noise_var,1000);
# m3 +=200*np.sin((freq2*2*np.pi)*(x-(2*distance_mic*np.sin(wave_arived_angle2*dtorad)/wavespeed)))+dc_va+np.random.normal(noise_exp,noise_var,1000);
# m4 +=200*np.sin((freq2*2*np.pi)*(x-(3*distance_mic*np.sin(wave_arived_angle2*dtorad)/wavespeed)))+dc_va+np.random.normal(noise_exp,noise_var,1000);

# m1 +=200*np.sin((freq2*2*np.pi)*(x-(0*distance_mic*np.sin(wave_arived_angle2*dtorad)/wavespeed)));
# m2 +=200*np.sin((freq2*2*np.pi)*(x-(1*distance_mic*np.sin(wave_arived_angle2*dtorad)/wavespeed)));
# m3 +=200*np.sin((freq2*2*np.pi)*(x-(2*distance_mic*np.sin(wave_arived_angle2*dtorad)/wavespeed)));
# m4 +=200*np.sin((freq2*2*np.pi)*(x-(3*distance_mic*np.sin(wave_arived_angle2*dtorad)/wavespeed)));

#信号源数量估计   窄带信号的协方差矩阵分解  特征值估计法 
signal_num_est=np.zeros([4,1000],dtype=np.complex);
signal_num_est[0][:]=m1;
signal_num_est[1][:]=m2;
signal_num_est[2][:]=m3;
signal_num_est[3][:]=m4;

estimate_cov=np.dot(signal_num_est,signal_num_est.T.conjugate());
est_eigvector,est_eigval,_=np.linalg.svd(estimate_cov);


plt.figure(1);
plt.subplot(4,1,1);
plt.plot(x,m1);

plt.subplot(4,1,2);
plt.plot(x,m2);

plt.subplot(4,1,3);
plt.plot(x,m3);

plt.subplot(4,1,4);
plt.plot(x,m4);


# plt.show();

st=time.time();
freq_line=(fs/sp)*np.linspace(0,(sp/2)-1,sp//2);
# asdf=np.linspace(0,(sp/2)-1,sp//2);

# m1_fft=2*np.fft.fft(m1)/sp;
# m2_fft=2*np.fft.fft(m2)/sp;
# m3_fft=2*np.fft.fft(m3)/sp;
# m4_fft=2*np.fft.fft(m4)/sp;


m1_fft=np.fft.fft(m1);
m2_fft=np.fft.fft(m2);
m3_fft=np.fft.fft(m3);
m4_fft=np.fft.fft(m4);

plt.figure(2);
plt.subplot(4,1,1);
plt.plot(freq_line,np.abs(m1_fft[:sp//2]));

plt.subplot(4,1,2);
plt.plot(freq_line,np.abs(m2_fft[:sp//2]));

plt.subplot(4,1,3);
plt.plot(freq_line,np.abs(m3_fft[:sp//2]));

plt.subplot(4,1,4);
plt.plot(freq_line,np.abs(m4_fft[:sp//2]));  #fft 结果需要全部除点数   出来直流分量其他乘以2

zzz=np.zeros([4,1],dtype=np.complex);
zt=zzz.T.conjugate();

rxx=np.zeros((43,4,4),dtype=np.complex);
eigvetor=np.zeros((43,4,4),dtype=np.complex);
noise_eigvetor=np.zeros((43,4,4-signal_num),dtype=np.complex);
for i in range(1,43):  # 1开始 43个
    mic_r=np.zeros([4,1],dtype=np.complex);
    # mic_r=([m1_fft[i]],[m2_fft[i]],[m3_fft[i]],[m4_fft[i]]);
    mic_r[0][0]=m1_fft[i];
    mic_r[1][0]=m2_fft[i];
    mic_r[2][0]=m3_fft[i];
    mic_r[3][0]=m4_fft[i];
    print("fdasf")
    print(mic_r)
    print(mic_r.T.conjugate())
    rxx[i,:,:]=np.dot(mic_r,mic_r.T.conjugate());  #计算每个频率下各个阵元的协方差矩阵
    eigvetor[i,:,:],eigval,_ = np.linalg.svd(rxx[i,:,:])                                                                                                                                                                                                                                                                
    noise_eigvetor[i,:,:]=eigvetor[i,:,signal_num:]
    # print(eigvetor[i,:,:]);
    # print(noise_eigvetor[i,:,:]);
    
    # print(np.dot(mic_r,mic_r.T.conjugate()));
    # print(i);
    # print(rxx[i,:,:]);
    # print(i);
    


res=np.zeros(600);
cnt=0;
for deg in np.arange(-30,30,0.1):
    for i in range(1,43):  #42个
        if  (i>=40 and i<=42) :#or (i>=29 and i<=31)  :
            n_freq=i*freq_res;  #频率
            n_time=1/n_freq; #周期
            dir_vetor=np.zeros([1,4],dtype=np.complex);
            tim_dif=distance_mic*np.sin(deg*dtorad)/wavespeed;
            dir_vetor[0,:]=np.exp(-1j*2*np.pi*np.linspace(0,miccount-1,miccount)*(tim_dif/n_time)); #1 * 4 矩阵
            dir_vetort=dir_vetor.T;
            res[cnt] += abs(np.dot(np.dot(np.dot(dir_vetort.T.conjugate(),noise_eigvetor[i,:,:]),noise_eigvetor[i,:,:].T.conjugate()),dir_vetort));
    res[cnt]=1/(res[cnt]/(100));
    cnt +=1;

print( "时间",time.time()-st);
plt.figure(3);
plt.plot(np.arange(-30,30,0.1),res); 
maxindex=np.argmax(res);
resangle=-30+maxindex*0.1;
print(resangle);

asdf=1;

plt.show();