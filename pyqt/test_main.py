
import sys
from turtle import pencolor
from PyQt5.QtWidgets import QApplication, QDialog,QMainWindow,QWidget
import numpy as np
import Ui_untitled
# from pyqt.Ui_untitled import Ui_MainWindow
from PyQt5.QtCore import QTimer,QDateTime


class mywindows():
    def __init__(self):
        self.mymain=QMainWindow()
        self.ui=Ui_untitled.Ui_MainWindow();
        self.ui.setupUi(self.mymain);
        
        self.ui.graphicsView.setBackground('w')
        # self.ui.graphicsView.setYRange(-1, 1)   
        self.plot_data=self.ui.graphicsView.plot(pen='b');
        self.plot_data_p2=self.ui.graphicsView.plot(pen='g');
        
        
        self.ui.graphicsView_2.setBackground('w')
        self.ui.graphicsView_2.setYRange(0, 40000)   
        self.ui.graphicsView_2.setXRange(0, 3000)   
        self.plot_data_2=self.ui.graphicsView_2.plot(pen='b');
        self.plot_data_2_p2=self.ui.graphicsView_2.plot(pen='g');
        
        self.ui.graphicsView_3.setBackground('w')
        self.plot_data_3=self.ui.graphicsView_3.plot(pen='b');
        
        
        self.mymain.show()
        self.ui.pushButton.clicked.connect(lambda: self.butten_print());
        self.ui.pushButton_2.clicked.connect(lambda: self.butten_2());
        
    def butten_print(self):
        print("butten clicked ");
        self.ui.textBrowser.setText("sdff");
        
        

    def butten_2(self):
        self.plot_data.setData(np.arange(100,150),np.random.rand(50));
        self.plot_data_2.setData(np.arange(100,150),np.random.rand(50));



def test_setdata():
    mywindows.plot_data.setData(np.arange(100,150),np.random.rand(50));
    mywindows.plot_data_2.setData(np.arange(100,150),np.random.rand(50));
    print("refresh")
    
if  __name__ == "__main__":
    print("test \r\n");
    print(sys.path);
    app = QApplication(sys.argv)
    
    mywindows=mywindows()
    time1=QTimer();
    time1.timeout.connect(test_setdata);
    time1.start(1000);
    
    sys.exit(app.exec_())


# class mywindows(QDialog):
#     def __init__(self):
#         super(QDialog, self).__init__();
#         self.ui=Ui_untitled.Ui_MainWindow();
#         self.ui.setupUi(self);
#     def butten_print(self):
#         print("butten clicked ");
#         self.ui.textBrowser.setText("sdff");
#         self.plot_data=ui.graphicsView.plot([1,2,3,4,5], pen='r', symbol = 'o');

    
    
    
# if  __name__ == "__main__":
#     app = QApplication(sys.argv)
#     MainWindow = QMainWindow()
#     ui = Ui_untitled.Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     ui.pushButton.clicked.connect(lambda: mywindows.butten_print());
#     # ui.graphicsView.add
#     MainWindow.show()
#     sys.exit(app.exec_())