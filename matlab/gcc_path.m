clc
clear 
close all

%����һ��������matlab�Դ���������
load gong;
%����Ƶ��
Fs = 8192;  
%��������
dt=1/Fs;
%music_srcΪ��Դ
music_src=y;    
figure();
plot(y);

%����������˷�����
mic_d=1;
mic_x=[-mic_d mic_d];
mic_y=[0 0];
plot(mic_x,mic_y,'x');
axis([-5 5 -5 5])
hold on;
quiver(-5,0,10,0,1,'color','black');
quiver(0,-5,0,10,1,'color','black');

%��Դλ��
s_x=-20;
s_y=10;
plot(s_x,s_y,'o');
quiver(s_x,s_y,-s_x-mic_d,-s_y,1);
quiver(s_x,s_y,-s_x+mic_d,-s_y,1);

%�������
dis_s1=sqrt((mic_x(1)-s_x).^2+(mic_y(1)-s_y).^2);
dis_s2=sqrt((mic_x(2)-s_x).^2+(mic_y(2)-s_y).^2);
c=340;
delay=abs((dis_s1-dis_s2)./340);
delay=-1e-5;

%������ʱ
music_delay = delayseq(music_src,delay,Fs);
figure(2);
subplot(211);
plot(music_src);
axis([0 length(music_src) -2 2]);
subplot(212);
plot(music_delay);
axis([0 length(music_delay) -2 2]);

figure(10);
plot(abs(fft(music_delay)));

%gccphat�㷨,matlab�Դ�
[tau,R,lag] = gccphat(music_delay,music_src,Fs);
disp(tau);
figure(3);
t=1:length(tau);
plot(lag,real(R(:,1)));

%cc�㷨
[rcc,lag]=xcorr(music_delay,music_src);
figure('NumberTitle','off','Name','CC');
plot(lag/Fs,rcc);
[M,I] = max(abs(rcc));
lagDiff = lag(I);
timeDiff = lagDiff/Fs;
disp(timeDiff);

%gcc+phat�㷨�����ݹ�ʽд
RGCC=fft(rcc);
rgcc=ifft(RGCC*1./abs(RGCC));
figure('NumberTitle','off','Name','GCC');
plot(lag/Fs,rgcc);
[M,I] = max(abs(rgcc));
lagDiff = lag(I);
timeDiff = lagDiff/Fs;
disp(timeDiff);


%my gcc+phat�㷨�����ݹ�ʽд
src_fft=fft(music_src);
src_delay_fft=fft(music_delay);
Gfft=src_fft.*conj(src_delay_fft);
inv_Gfft_non=ifft(Gfft);
inv_Gfft=ifft(Gfft./abs(Gfft));
figure();
subplot(2,1,1);
plot(angle(Gfft));
subplot(2,1,2);
plot(abs(inv_Gfft));

[M,I] = max(abs(inv_Gfft));
lagDiff = lag(I);
timeDiff = lagDiff/Fs;
disp(timeDiff);


%����Ƕ�,�������Ϊƽ�沨
dis_r=tau*c;
angel=acos(tau*c./(mic_d*2))*180/pi;
if dis_s1<dis_s2
    angel=180-angel;
end
