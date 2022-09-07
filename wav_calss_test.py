import wave
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
import pyqtgraph as pg
import time
import queue

f1=wave.open(r"D:\工程文件\电赛\声源定位\音轨.wav","rb");
f2=wave.open(r"D:\工程文件\电赛\声源定位\音轨-2.wav","rb");
f3=wave.open(r"D:\工程文件\电赛\声源定位\音轨-3.wav","rb");
f4=wave.open(r"D:\工程文件\电赛\声源定位\音轨-4.wav","rb");
f5=wave.open(r"D:\工程文件\电赛\声源定位\音轨-5.wav","rb");
f6=wave.open(r"D:\工程文件\电赛\声源定位\音轨-6.wav","rb");
f7=wave.open(r"D:\工程文件\电赛\声源定位\音轨-7.wav","rb");
f8=wave.open(r"D:\工程文件\电赛\声源定位\音轨-8.wav","rb");

params =f1.getparams();
print(params);


nchannels,sampwith,framesrate,nframes=params[:4];

fs=framesrate;
sp=1920
print(nchannels,sampwith,framesrate,nframes);


def print_phase(f1,f2,f3,f4):
    f1_data_fft_orginal=np.fft.fft(f1);
    f1_data_fft=abs(f1_data_fft_orginal);
    plt.plot((fs/sp)*np.linspace(0,(sp/2)-1,sp//2),f1_data_fft[:sp//2]);
    # print(np.argmax(f1_data_fft));
    # print("f1 phase :",np.arctan(f1_data_fft_orginal[80].imag/f1_data_fft_orginal[80].real))
    f1_angle=np.arctan(f1_data_fft_orginal[80].imag/f1_data_fft_orginal[80].real)

    f2_data_fft_orginal=np.fft.fft(f2);
    f2_data_fft=abs(f2_data_fft_orginal);
    plt.plot((fs/sp)*np.linspace(0,(sp/2)-1,sp//2),f2_data_fft[:sp//2]);
    # print(np.argmax(f2_data_fft));
    # print("f2 phase :",np.arctan(f2_data_fft_orginal[80].imag/f2_data_fft_orginal[80].real))
    f2_angle=np.arctan(f2_data_fft_orginal[80].imag/f2_data_fft_orginal[80].real)

    f3_data_fft_orginal=np.fft.fft(f3);
    f3_data_fft=abs(f3_data_fft_orginal);
    plt.plot((fs/sp)*np.linspace(0,(sp/2)-1,sp//2),f3_data_fft[:sp//2]);
    # print(np.argmax(f3_data_fft));
    # print("f3 phase :",np.arctan(f3_data_fft_orginal[80].imag/f3_data_fft_orginal[80].real))
    f3_angle=np.arctan(f3_data_fft_orginal[80].imag/f3_data_fft_orginal[80].real)

    f4_data_fft_orginal=np.fft.fft(f4);
    f4_data_fft=abs(f4_data_fft_orginal);
    plt.plot((fs/sp)*np.linspace(0,(sp/2)-1,sp//2),f4_data_fft[:sp//2]);
    # print(np.argmax(f4_data_fft));
    # print("f4 phase :",np.arctan(f4_data_fft_orginal[80].imag/f4_data_fft_orginal[80].real))
    f4_angle=np.arctan(f4_data_fft_orginal[80].imag/f4_data_fft_orginal[80].real)
    
    return f1_angle,f2_angle,f3_angle,f4_angle;
    
    
    
f1_f2_angle=np.zeros(409);
f2_f3_angle=np.zeros(409);
f3_f4_angle=np.zeros(409);


f1_angle=np.zeros(409);
f2_angle=np.zeros(409);
f3_angle=np.zeros(409);
f4_angle=np.zeros(409);


cnt=0;

win = pg.GraphicsWindow(title="在同一个窗口，不同的图标中绘制双曲线");
plot1 = win.addPlot();
plot1.plot(f1_f2_angle);
plot2 = win.addPlot(title='b 窗口绘制图形');
plot2.plot(f2_f3_angle);
plot2 = win.addPlot(title='b 窗口绘制图形');
plot2.plot(f3_f4_angle);
for cnt in range(409):
    f1_data=f1.readframes(sp);
    f1_data = np.frombuffer(f1_data,dtype=np.short);
    
    f2_data=f2.readframes(sp);
    f2_data = np.frombuffer(f2_data,dtype=np.short);

    f3_data=f3.readframes(sp);
    f3_data = np.frombuffer(f3_data,dtype=np.short);

    f4_data=f4.readframes(sp);
    f4_data = np.frombuffer(f4_data,dtype=np.short);
    f1_angle[cnt],f2_angle[cnt],f3_angle[cnt],f4_angle[cnt]=print_phase(f1_data,f2_data,f3_data,f4_data);
    
    f1_f2_angle[cnt]=f1_angle[cnt] - f2_angle[cnt];
    f2_f3_angle[cnt]=f2_angle[cnt] - f3_angle[cnt];
    f3_f4_angle[cnt]=f3_angle[cnt] - f4_angle[cnt];


pg.QtGui.QApplication.exec_();

for cnt in range(409):
    f1_data=f1.readframes(sp);
    f1_data = np.frombuffer(f1_data,dtype=np.short);
    
    f2_data=f2.readframes(sp);
    f2_data = np.frombuffer(f2_data,dtype=np.short);

    f3_data=f3.readframes(sp);
    f3_data = np.frombuffer(f3_data,dtype=np.short);

    f4_data=f4.readframes(sp);
    f4_data = np.frombuffer(f4_data,dtype=np.short);
    f1_angle[cnt],f2_angle[cnt],f3_angle[cnt],f4_angle[cnt]=print_phase(f1_data,f2_data,f3_data,f4_data);
    
    f1_f2_angle[cnt]=f1_angle[cnt] - f2_angle[cnt];
    f2_f3_angle[cnt]=f2_angle[cnt] - f3_angle[cnt];
    f3_f4_angle[cnt]=f3_angle[cnt] - f4_angle[cnt];
    
    
# win = pg.GraphicsWindow(title="在同一个窗口，不同的图标中绘制双曲线");
# plot1 = win.addPlot();
# plot1.plot(f1_f2_angle);
# plot2 = win.addPlot(title='b 窗口绘制图形');
# plot2.plot(f2_f3_angle);
# plot2 = win.addPlot(title='b 窗口绘制图形');
# plot2.plot(f3_f4_angle);
# pg.QtGui.QApplication.exec_();

plt.figure();
plt.subplot(3,1,1);
plt.plot(f1_f2_angle);

plt.subplot(3,1,2);
plt.plot(f2_f3_angle);

plt.subplot(3,1,3);
plt.plot(f3_f4_angle);

plt.figure();
plt.subplot(4,1,1);
plt.plot(f1_angle);

plt.subplot(4,1,2);
plt.plot(f2_angle);

plt.subplot(4,1,3);
plt.plot(f3_angle);

plt.subplot(4,1,4);
plt.plot(f4_angle);

plt.show();


    
    
    
plt.figure();
plt.subplot(4,1,1)
f1_data=f1.readframes(1920);
f1_data = np.frombuffer(f1_data,dtype=np.short);
plt.plot(f1_data);




plt.subplot(4,1,2)
f2_data=f2.readframes(sp);
f2_data = np.frombuffer(f2_data,dtype=np.short);
plt.plot(f2_data);

plt.subplot(4,1,3)
f3_data=f3.readframes(sp);
f3_data = np.frombuffer(f3_data,dtype=np.short);
plt.plot(f3_data);

plt.subplot(4,1,4)
f4_data=f4.readframes(sp);
f4_data = np.frombuffer(f4_data,dtype=np.short);
plt.plot(f4_data);


plt.figure();
plt.subplot(4,1,1);
f1_data_fft=abs(np.fft.fft(f1_data))
plt.plot((fs/sp)*np.linspace(0,(sp/2)-1,sp//2),f1_data_fft[:sp//2]);

print(np.argmax(f1_data_fft));

plt.subplot(4,1,2);
f2_data_fft=abs(np.fft.fft(f2_data))
plt.plot((fs/sp)*np.linspace(0,(sp/2)-1,sp//2),f2_data_fft[:sp//2]);

print(np.argmax(f2_data_fft));

plt.subplot(4,1,3);
f3_data_fft=abs(np.fft.fft(f3_data))
plt.plot((fs/sp)*np.linspace(0,(sp/2)-1,sp//2),f3_data_fft[:sp//2]);

print(np.argmax(f3_data_fft));

plt.subplot(4,1,4);
f4_data_fft=abs(np.fft.fft(f4_data))
plt.plot((fs/sp)*np.linspace(0,(sp/2)-1,sp//2),f4_data_fft[:sp//2]);

print(np.argmax(f4_data_fft));





f1_data=f1_data.reshape(1,-1);
f2_data=f2_data.reshape(1,-1);
f3_data=f3_data.reshape(1,-1);
f4_data=f4_data.reshape(1,-1);


min_max_scaler=preprocessing.MinMaxScaler();
f1_data_scaler=min_max_scaler.fit_transform(f1_data.T);
f2_data_scaler=min_max_scaler.fit_transform(f2_data.T);
f3_data_scaler=min_max_scaler.fit_transform(f3_data.T);
f4_data_scaler=min_max_scaler.fit_transform(f4_data.T);



plt.figure();
plt.subplot(4,1,1);
f1_data_fft_orginal=np.fft.fft(f1_data_scaler.T[0,:]);
f1_data_fft=abs(f1_data_fft_orginal);
plt.plot((fs/sp)*np.linspace(0,(sp/2)-1,sp//2),f1_data_fft[:sp//2]);
print(np.argmax(f1_data_fft));
print("f1 phase :",np.arctan(f1_data_fft_orginal[80].imag/f1_data_fft_orginal[80].real))

plt.subplot(4,1,2);
f2_data_fft_orginal=np.fft.fft(f2_data_scaler.T[0,:]);
f2_data_fft=abs(f2_data_fft_orginal);
plt.plot((fs/sp)*np.linspace(0,(sp/2)-1,sp//2),f2_data_fft[:sp//2]);
print(np.argmax(f2_data_fft));
print("f2 phase :",np.arctan(f2_data_fft_orginal[80].imag/f2_data_fft_orginal[80].real))

plt.subplot(4,1,3);
f3_data_fft_orginal=np.fft.fft(f3_data_scaler.T[0,:]);
f3_data_fft=abs(f3_data_fft_orginal);
plt.plot((fs/sp)*np.linspace(0,(sp/2)-1,sp//2),f3_data_fft[:sp//2]);
print(np.argmax(f3_data_fft));
print("f3 phase :",np.arctan(f3_data_fft_orginal[80].imag/f3_data_fft_orginal[80].real))

plt.subplot(4,1,4);
f4_data_fft_orginal=np.fft.fft(f4_data_scaler.T[0,:]);
f4_data_fft=abs(f4_data_fft_orginal);
plt.plot((fs/sp)*np.linspace(0,(sp/2)-1,sp//2),f4_data_fft[:sp//2]);
print(np.argmax(f4_data_fft));
print("f4 phase :",np.arctan(f4_data_fft_orginal[80].imag/f4_data_fft_orginal[80].real))



plt.figure(10);

plt.subplot(3,1,1)
plt.plot(f1_data_scaler,'b');
plt.plot(f2_data_scaler,'r');

plt.subplot(3,1,2)
plt.plot(f1_data_scaler,'b');
plt.plot(f3_data_scaler,'r');

plt.subplot(3,1,3)
plt.plot(f1_data_scaler,'b');
plt.plot(f4_data_scaler,'r');


plt.show();



