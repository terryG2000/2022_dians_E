clc;
clear all;
close all;
derad=pi/180;
radeg=180/pi;
twpi=2*pi;
kelm=4;
dd=0.1;
d=0:dd:(kelm-1)*dd;
iwave=2;
theta=[10.3 -10.3];
snr=3;
n=1000;
A=exp(-j*twpi*d.'*sin(theta*derad));
%A=exp(-j*twpi*d.'*0);
sinwavel =linspace(0,2*pi,n);
%sinwave=10*sin(30000*sinwavel)+1*sin(30000*sinwavel)+14*cos(30000*sinwavel);
sinwave=200+sin(200*pi*sinwavel)+10*sin(300*sinwavel);

figure(4)
plot(sinwavel,sinwave);

%S=randn(iwave,n);
%S=[sinwave; sinwave; sinwave;];
S=[sinwave;sinwave];
% SA=A*S;
S=awgn(S,snr,'measured')+105;
X=A*S;
% XT=X';
X1=X;
% X1=awgn(X,snr,'measured');

figure(1)
plot(sinwavel,X1(1,:));
Rxx=X1*X1'/n;
InvS=inv(Rxx);
[EV,D]=eig(Rxx);

ee=eig(Rxx);

EVA=diag(D');
[EVA,I]=sort(EVA); %排序 升序
EVA=fliplr(EVA);
EV=fliplr(EV(:,I));

iang=1:300
angle(iang)=-30.2+0.2*iang;
for iiang=iang%=1:301
%    angle(iang)=(iang-181)/2;
   
   phim=derad*angle(iiang);
   a=exp(-j*twpi*d*sin(phim)).';
   L=iwave;
   En=EV(:,L+1:kelm);
%    SP(iiang)=(a'*a)/(a'*En*En'*a);

   SP(iiang)=1/(a'*En*En'*a);
   
end

figure(2)
SP=abs(SP);
% SPmax=max(SP);
% SP=10*log10(SP/SPmax);
plot(angle,SP);

% h=plot(angle,SP);
% set(h,'Linewidth',2)
% xlabel('angle(degree)')
% ylabel('magnitude(dB)')
% axis([-90 90 -60 60])
% set(gca,'XTick',[-90:30:90])
% grid on