c = 340;                    % Sound velocity (m/s) 声速
fs = 16000;                 % Sample frequency (samples/s) 采样率
r = [2 1.5 2];              % Receiver position [x y z] (m) 接收点坐标
s = [2 3.5 2];              % Source position [x y z] (m) 声源位置坐标
L = [5 4 6];                % Room dimensions [x y z] (m) 房间尺寸
beta = 0.4;                 % Reflections Coefficients  反射系数
n = 2048;                   % Number of samples  冲激响应阶数
mtype = 'omnidirectional';  % Type of microphone 麦克风类型：全指向性
order = 2;                  % Reflection order 
dim = 3;                    % Room dimension
orientation = 0;            % Microphone orientation (rad)麦克风朝向
hp_filter = 1;              % Enable high-pass filter 高通滤波器

h = rir_generator(c, fs, r, s, L, beta, n, mtype, order, dim, orientation, hp_filter);










