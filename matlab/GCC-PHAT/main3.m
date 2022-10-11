%Զ��ģ��,����˷�
clc
clear all
close all

sita = 60;
load('num.mat');
%����������Ӧ
c = 340;  % ����
fs = 8e3; % ������
room_size = [5 4 6]; % ����ߴ�[x y z] (m)
d0 = 0.2; % ��˷���
mic_num = 2; %��˷����
C = nchoosek(1:mic_num,2); %���п��ܵ����
xm = 0:d0:(mic_num-1)*d0;
delte_m = 0.5*room_size(1) - 0.5*(mic_num-1)*d0;
xm = xm' + delte_m; %ÿ����˷��x����
ym = 1.5.*ones(mic_num,1); %��˷��y����
zm = 2.*ones(mic_num,1);
mic_location = [xm,ym,zm];    %��˷�λ�� [x y z] (m)
clear xm ym zm delte_m

r = 2; %�뾶
reverberation_time = 0.5;   % ����ʱ��(s)
n = 2048;                   % �弤��Ӧ����
audio_length = fs*1;
s = wgn(audio_length,1,0); %��˹������
% [s,fs0] = audioread('BAC009S0002W0122.wav');
% s = s(1:fs0);
% s = resample(s,fs,fs0);
% plot(s);

ys = r*cos(sita*(pi/180)) + mean(mic_location(:,2));
xs = r*sin(sita*(pi/180)) + mean(mic_location(:,1));
zs = mean(mic_location(:,3));
source_location = [xs ys zs];     % ��Դλ��[x y z] (m)
h = rir_generator(c, fs, mic_location, source_location, room_size, reverberation_time, n); %ÿһ�ж�Ӧһ���弤��Ӧ

%����ÿ����˷���յ����ź�
for j = 1:mic_num
    x(:,j) = filter(h(j,:),1,s);
end

for j = 1: length(C(:,1))
    x1 = x(:,C(j,1)); %��һ����˷�
    x2 = x(:,C(j,2)); %�ڶ�����˷�
    d = norm(mic_location(C(j,1),:)-mic_location(C(j,2),:)); %������˷�ľ���
    P = (fft(x1).*conj(fft(x2))); %x1��x2�Ļ�������
    A = 1./abs(P);
    R_est1 = fftshift(ifft(A.*P));
    plot(R_est1);
    [~,tau] = max(R_est1); %Ѱ��������ĵ�
    tau = tau - 0.5*fs - 1;
    t = tau*(1/fs);
    sita_re = asin((t*c)/d)*(180/pi);
    C(j,3) = real(sita_re);
end
% end

% disp(['��������:',num2str(sita),'��']);
% disp(['���Ʒ���:',num2str(sita_re),'��']);

% hold on
% plot(SITA(:,1),SITA(:,1));
% plot(SITA(:,1),SITA(:,2));
% hold off




