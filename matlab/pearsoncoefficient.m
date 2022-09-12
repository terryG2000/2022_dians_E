



Fs=1000;
T=1:1:Fs;
W=2*pi*1/500;
X=sin(W*T);
Y=sin(W*T+pi/8)+normrnd(1,0.3,[1,1000])+2;

figure(1);
subplot(2,2,1);
plot(T,X);

subplot(2,2,2);
plot(T,Y);


person=(mean(X.*Y)-mean(X)*mean(Y))/(std(X)*std(Y));

subplot(2,2,3);
plot(1,person);


