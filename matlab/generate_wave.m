FS=48000;
TS=1/FS;
n=2000*4;
fft_freq_div=FS/n;
freq_dis=50;
time=0:TS:60;

%构造原始信号和 延时信号

f=800:freq_dis:1200;
i=1;
x=zeros(1,length(time));
while i<length(f)
    x=x+sin(2*pi*f(1,i)*time);
    i=i+1;
end
fname = 'Asin3.wav';        % 设定文件名称 注意格式
audiowrite(fname,x,FS);     % 输出文件

figure();
plot(x(1:1:48000));