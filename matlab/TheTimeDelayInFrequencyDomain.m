close all;clear;clc;


%一度 时间差 2.6e-6
%采样时间  2.0e-5
%当角度小于30度  td=7.4e-5 距离差小于2.5 时 该方法误差在1度以内1.6525e-06
FS=48000;
TS=1/FS;
n=2000*4;
fft_freq_div=FS/n;
freq_dis=50;
time_shifft=1e-6;
time=0+time_shifft:TS:TS*(n-1)+time_shifft;
td=-2.6*30e-6;

%构造原始信号和 延时信号

f=800:freq_dis:1200;
i=1;
x=zeros(1,length(time));
xd=zeros(1,length(time));
while i<length(f)
    x=x+sin(2*pi*f(1,i)*time);
    xd=xd+sin(2*pi*f(1,i)*(time-td));
    i=i+1;
end

% freq_range=[36 51] % n=2048
freq_range_temp=zeros(1,100);
freq_range_dis=zeros(1,100);
cnt=0;
for i=135:1:220
    temp=(fft_freq_div*i)-f;
    [M,I]=min(abs(temp));
    if abs(M)<6
      cnt=cnt+1;
      freq_range_temp(cnt)=i;
      freq_range_dis(cnt)=fft_freq_div*i;
      if cnt>=2 && freq_range_temp(cnt)==freq_range_temp(cnt-1)
          freq_range_temp(cnt)=0;
          cnt=cnt-1;
      end
    end
end
freq_range=freq_range_temp(1:cnt)

% figure(11);
% plot(x);
% time_shifft=1000e-6;
% time=0+time_shifft:TS:TS*(n-1)+time_shifft;
% f=800:freq_dis:1200;
% i=1;
% x=zeros(1,length(time));
% xd=zeros(1,length(time));
% while i<length(f)
%     x=x+sin(2*pi*f(1,i)*time);
%     xd=xd+sin(2*pi*f(1,i)*(time-td));
%     i=i+1;
% end
% hold on;
% plot(x);
% hold off;


%添加直流分量
% x=x+1;
% xd=xd+1;
%绘制原始信号
figure(1);
plot(x);

%绘制原始型号的频谱
figure(2);
x_fft=fftshift(fft(x)); %shift 将频谱向中心开始两边对称 中间是低频两边是高频
subplot(3,1,1);
plot(0:fft_freq_div:(fft_freq_div)*(n/2-1),abs(x_fft((n/2)+1:end)));
subplot(3,1,2);
plot(x);
subplot(3,1,3);
plot(angle(x_fft((n/2)+1:end)));

%绘制延时信号的频谱
figure(3);
xd_fft=fftshift(fft(xd));
subplot(3,1,1);
plot(0:fft_freq_div:(fft_freq_div)*(n/2-1),abs(xd_fft((n/2)+1:end)));
subplot(3,1,2);
plot(xd);
subplot(3,1,3);
plot(angle(xd_fft((n/2)+1:end)));


%绘制频域互功率谱
figure(4);
diff=x_fft.*conj(xd_fft);% 共轭
subplot(4,1,1);
plot(0:fft_freq_div:(fft_freq_div)*(300-1),abs(diff((n/2)+1:(n/2)+300)),'*');
subplot(4,1,2);
plot(0:fft_freq_div:(fft_freq_div)*(300-1),angle(diff((n/2)+1:(n/2)+300)),'*');


subplot(4,1,4);
plot(abs(diff((n/2)+1:(n/2)+300)),'*');

%绘制频域互功率相位谱
subplot(4,1,3);
plot(angle(diff((n/2)+1:(n/2)+300)),'*');


%拟合频段直线
% lsm_X=(freq_range(1)-1)*fft_freq_div:fft_freq_div:(fft_freq_div)*(freq_range(2)-1)
lsm_X=(freq_range.*fft_freq_div)
lsm_one=ones(length(lsm_X),1);

lsm_A=[lsm_X' lsm_one];
% lsm_Y=(angle(diff((n/2)+1+freq_range(1)-1:(n/2)+1+freq_range(2)-1)))';
lsm_Y=zeros(1,length(freq_range));
cnt=0;
while cnt<length(lsm_Y)
    cnt=cnt+1;
    lsm_Y(cnt)=angle(diff((n/2)+1+freq_range(cnt)));
end
lsm_Y=lsm_Y';

%最小二乘求解参数
R=lsm_A'*lsm_A;
res=inv(R)*lsm_A'*lsm_Y;

hold on;
plot([0 300],[res(2) res'*[(300-1)*(fft_freq_div); 1;]]);

disp(1/FS);
time_diff=res(1)/(2*pi);
disp(time_diff)
time_error=td-time_diff;
disp(time_error);
disp(time_error*340*1000)


% figure();
% plot(angle(diff));









