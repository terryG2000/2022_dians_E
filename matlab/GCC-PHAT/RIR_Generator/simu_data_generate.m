% 设置一个[5 4 6]的房间，仿真的参考麦克风放置在[2.5 0.5 1],源分别放置在[0.5 3.5 2]和[4.5 3.5 2] 
clc
clear;

%% 设置位置参数，产生相应的冲击响应
c = 340; 
fs = 8000; 
N = 36;
d = 0.04;
L = [5 4 6];                % 房间尺寸
s = [2.6 1.9 5];          % 两个声源位置
for i=1:N
    r(i,:)=[(2.5+d*(mod(i-1,6))) (2-d*(floor((i-1)/6))) 1]; %zhenyuan 
end
% scatter(r(:,1),r(:,2))
beta1 = 0.2;                 % Reverberation time (s)
beta2 = 0.25; 
beta3 = 0.3;
beta4 = 0.35;
beta5 = 0.4;
beta6 = 0.45;
n = 4096;                   % Number of samples

%% 产生通道
for i=1:N
      h200(:,i)=rir_generator(c, fs, r(i,:), s, L, beta1, n);
      h250(:,i)=rir_generator(c, fs, r(i,:), s, L, beta2, n);
      h300(:,i)=rir_generator(c, fs, r(i,:), s, L, beta3, n);
      h350(:,i)=rir_generator(c, fs, r(i,:), s, L, beta4, n);
      h400(:,i)=rir_generator(c, fs, r(i,:), s, L, beta5, n);
      h450(:,i)=rir_generator(c, fs, r(i,:), s, L, beta6, n);
end
save('D:\software\work_relative\matlab\matlab\beamforming\4_18enhancetext\data_of_simulation\channel\h200.mat','h200');
save('D:\software\work_relative\matlab\matlab\beamforming\4_18enhancetext\data_of_simulation\channel\h250.mat','h250');
save('D:\software\work_relative\matlab\matlab\beamforming\4_18enhancetext\data_of_simulation\channel\h300.mat','h300');
save('D:\software\work_relative\matlab\matlab\beamforming\4_18enhancetext\data_of_simulation\channel\h350.mat','h350');
save('D:\software\work_relative\matlab\matlab\beamforming\4_18enhancetext\data_of_simulation\channel\h400.mat','h400');
save('D:\software\work_relative\matlab\matlab\beamforming\4_18enhancetext\data_of_simulation\channel\h450.mat','h450');

%% 绘制房间、阵元、声源
% scatter3(r(:,1),r(:,2),r(:,3))
% hold on
% scatter3(s(1),s(2),s(3))
% o=[0,0,0];
% L1=L(1);W=L(2);H=L(3);
% x=[o(1),o(1)+L1,o(1)+L1,o(1),  o(1);o(1),  o(1)+L1,o(1)+L1,o(1),  o(1)];
% y=[o(2),o(2),   o(2)+W, o(2)+W,o(2);o(2),  o(2),   o(2)+W, o(2)+W,o(2)];
% z=[o(3),o(3),   o(3),   o(3),  o(3);o(3)+H,o(3)+H, o(3)+H, o(3)+H,o(3)+H];
% hold on
% mesh(x,y,z)
% hidden off


