import numpy as np
import read_from_wave_class as readwave
import matplotlib.pyplot as plt

re_wave=readwave.read_frome_wave();
print(re_wave.file_params());
wave_data=re_wave.read_frames(4,1920);

plt.figure(1);
plt.subplot(2,1,1);
plt.plot(wave_data[0,:]);
plt.subplot(2,1,2);
plt.plot(wave_data[1,:]);

correlation_res=np.correlate(wave_data[0,:],wave_data[1,:],'same');
plt.figure(2);
plt.plot(correlation_res);


res_list=np.zeros((3,200));
for i in range(200):
    wave_data=re_wave.read_frames(4,1920);
    res_list[0][i]=np.argmax(np.correlate(wave_data[0,:],wave_data[1,:],'same'));
    res_list[1][i]=np.argmax(np.correlate(wave_data[1,:],wave_data[2,:],'same'));
    res_list[2][i]=np.argmax(np.correlate(wave_data[2,:],wave_data[3,:],'same'));
plt.figure(3);
plt.subplot(3,1,1);
plt.plot(res_list[0,:]);
plt.subplot(3,1,2);
plt.plot(res_list[1,:]);
plt.subplot(3,1,3);
plt.plot(res_list[2,:]);



plt.show();