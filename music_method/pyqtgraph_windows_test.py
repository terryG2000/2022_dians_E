from webbrowser import BackgroundBrowser
import pyqtgraph as pg
import numpy as np

a = np.random.random(100)
b = np.random.random(50)

def pg_windows_addplot():
    win = pg.GraphicsWindow(title="在同一个窗口，不同的图标中绘制双曲线");
    plot1 = win.addPlot();
    plot1.plot(a);
    plot2 = win.addPlot(title='b 窗口绘制图形');
    plot2.plot(b);
    pg.QtGui.QApplication.exec_();
    
pg_windows_addplot();