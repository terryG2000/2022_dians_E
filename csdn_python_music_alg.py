nmicro=16
layers = 2
micros_every_layer = nmicro//layers
R = [0.082, 0.103]
theta_micro = np.zeros(nmicro)#所有麦克风阵元的角度
for layer in range(layers):
    theta_micro[micros_every_layer*layer:micros_every_layer*(layer+1)] = \
        2*np.pi/micros_every_layer*(np.arange(micros_every_layer)+0.5*layer)
#所有麦克风阵元的坐标
pos = np.concatenate((np.stack([R[0] * np.cos(theta_micro[:8]), R[0] * np.sin(theta_micro[:8]), np.zeros(8)],axis = 1), \
    np.stack([R[1] * np.cos(theta_micro[8:]), R[1] * np.sin(theta_micro[8:]), np.zeros(8)],axis = 1)), axis=0)
#PyAudio的信号采集参数
CHUNK = 1600
FORMAT = pyaudio.paInt16
CHANNELS = 18
RATE = 16000
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
#最后求得的声源位置
xr = 0
yr = 0
#遍历的x和y，假设z为固定深度1m
X_STEP = 20
Y_STEP = 20
x = np.linspace(-0.4, 0.4, X_STEP)
y = np.linspace(-0.4, 0.4, Y_STEP)
z = 1
def beamforming():
    global xr, yr, ifplot, x, y
    while True:
        data = stream.read(1600)
        data = np.frombuffer(data, dtype=np.short)
        data = data.reshape(1600,18)[:,:16].T

        data_n = np.fft.fft(data)/data.shape[1]# [16,1600]
        data_n = data_n[:, :data_n.shape[1]//2]
        data_n[:, 1:] *= 2

        r = np.zeros((50, nmicro, nmicro-1), dtype=np.complex)
        for fi in range(1,51):
            rr = np.dot(data_n[:, fi*10-10:fi*10+10], data_n[:, fi*10-10:fi*10+10].T.conjugate())/nmicro
            feavec,_,_ = np.linalg.svd(rr)
            r[fi-1,...] = feavec[:, 1:]
            
        p = np.zeros((x.shape[0], y.shape[0]))
        for i in range(x.shape[0]):
            for j in range(y.shape[0]):
                dm = np.sqrt(x[i]**2+y[j]**2+z**2)
                delta_dn = pos[:,0]*x[i]/dm + pos[:,1]*y[j]/dm
                for fi in range(1,51):
                    a = np.exp(-1j*2*np.pi*fi*100*delta_dn/340)
                    p[i,j] = p[i,j] + 1/np.abs(np.dot(np.dot(np.dot(a.conjugate(), r[fi-1]), r[fi-1].T.conjugate()), a))

        #n = np.argmin(np
        xr = np.argmax(p)//Y_STEP
        yr = np.argmax(p)%Y_STEP
        print(x[xr],y[yr])

        p /= np.max(p)
        x1, y1 = np.meshgrid(x,y)
        ax = plt.axes(projection='3d')
        ax.plot_surface(x1,y1,np.abs(p.T))
        plt.pause(0.01)
