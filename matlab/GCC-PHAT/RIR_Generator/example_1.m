c = 340;       % Sound velocity (m/s)
fs = 8000;     % Sample frequency (samples/s)
N = 8;
d = 0.03;
r = [ones(N,1)+d*((1:N)'-1)  1*ones(N,1)  1.5*ones(N,1)];   % Receiver position [x y z] (m)
s = [1 3 1.5 ; 2.7321 2 1.5];              % Source position [x y z] (m)
L = [4.45 3.35 2.5];                % Room dimensions [x y z] (m)
R60 = 0.4;                 % Reverberation time (s)
refl = 1 - exp ( -0.161*( L(1)*L(2)*L(3) ) / ( R60 * 2 * (L(1)*L(2)+L(2)*L(3)+L(1)*L(3)) ) );
beta = ones(1,6) * (1- sqrt(refl) );
n = 4000;                   % Number of samples

h_s = rir_generator(c, fs, r, s(1,:), L, R60, n);
h_n = rir_generator(c, fs, r, s(2,:), L, R60, n);

save('D:\matlab\bin\beamforming\CHiME5\noise_reduction\simulate_data\h_s.mat','h_s');
save('D:\matlab\bin\beamforming\CHiME5\noise_reduction\simulate_data\h_n.mat','h_n');


% Para.Array_Config.Mic_Pos=r;
% Para.Array_Config.N=M;
% Para.Fs=fs;
% Para.Sound_Speed=c;
% Para.SRP.Frame_Len=512;
% Para.SRP.Overlap=256;
% Para.Scan_Pitch=(1:180);
% Para.Scan_Azimuth=1:360;
% Est_DOA_SRP=SRP_PATH(xt,Para);