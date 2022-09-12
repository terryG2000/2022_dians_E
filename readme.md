# 麦克风格式
```
pi123456@raspberrypi:/proc/asound/card1 $ cat stream0 
Yundea Technology Yundea 8MICA at usb-0000:01:00.0-1.4, full speed : USB Audio

Capture:
  Status: Stop
  Interface 2
    Altset 1
    Format: S16_LE  //小端有符号字
    Channels: 8
    Endpoint: 0x83 (3 IN) (ASYNC)
    Rates: 48000
    Bits: 16
    Channel map: FL FR FC LFE SL SR FLC FRC
```
# 文件夹
## __pycache__
pyqt python 编译后的二进制文件
## .vscode
vscode 配置文件
## pyqt
pyqt 的ui文件
* __init__.py: 方便import
* test_main.py:主窗口
* Ui_untitled.py:pyqt ui文件
* Ui_untitled.ui :未编译前的ui文件
## /


