%远场模型,多麦克风
clc
clear all
close all

sita = 60;
load('num.mat');
%产生脉冲响应
c = 340;  % 声速
fs = 8e3; % 采样率
room_size = [5 4 6]; % 房间尺寸[x y z] (m)
d0 = 0.2; % 麦克风间距
mic_num = 2; %麦克风个数
C = nchoosek(1:mic_num,2); %所有可能的组合
xm = 0:d0:(mic_num-1)*d0;
delte_m = 0.5*room_size(1) - 0.5*(mic_num-1)*d0;
xm = xm' + delte_m; %每个麦克风的x坐标
ym = 1.5.*ones(mic_num,1); %麦克风的y坐标
zm = 2.*ones(mic_num,1);
mic_location = [xm,ym,zm];    %麦克风位置 [x y z] (m)
clear xm ym zm delte_m

r = 2; %半径
reverberation_time = 0.5;   % 混响时间(s)
n = 2048;                   % 冲激响应长度
audio_length = fs*1;
s = wgn(audio_length,1,0); %高斯白噪声
% [s,fs0] = audioread('BAC009S0002W0122.wav');
% s = s(1:fs0);
% s = resample(s,fs,fs0);
% plot(s);

ys = r*cos(sita*(pi/180)) + mean(mic_location(:,2));
xs = r*sin(sita*(pi/180)) + mean(mic_location(:,1));
zs = mean(mic_location(:,3));
source_location = [xs ys zs];     % 声源位置[x y z] (m)
h = rir_generator(c, fs, mic_location, source_location, room_size, reverberation_time, n); %每一行对应一个冲激响应

%产生每个麦克风接收到的信号
for j = 1:mic_num
    x(:,j) = filter(h(j,:),1,s);
end

for j = 1: length(C(:,1))
    x1 = x(:,C(j,1)); %第一个麦克风
    x2 = x(:,C(j,2)); %第二个麦克风
    d = norm(mic_location(C(j,1),:)-mic_location(C(j,2),:)); %两个麦克风的距离
    P = (fft(x1).*conj(fft(x2))); %x1、x2的互功率谱
    A = 1./abs(P);
    R_est1 = fftshift(ifft(A.*P));
    plot(R_est1);
    [~,tau] = max(R_est1); %寻找相关最大的点
    tau = tau - 0.5*fs - 1;
    t = tau*(1/fs);
    sita_re = asin((t*c)/d)*(180/pi);
    C(j,3) = real(sita_re);
end
% end

% disp(['来波方向:',num2str(sita),'度']);
% disp(['估计方向:',num2str(sita_re),'度']);

% hold on
% plot(SITA(:,1),SITA(:,1));
% plot(SITA(:,1),SITA(:,2));
% hold off




