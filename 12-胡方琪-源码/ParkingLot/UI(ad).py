import sys
import cv2
import time
import os
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QLabel,QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap,QImage
from PyQt5.QtCore import Qt,QTimer
import numpy as np

class CameraApp(QMainWindow):
    #初始化
    def __init__(self):
        super().__init__()

        self.setWindowTitle('显示摄像头')
        self.setGeometry(100,100,800,600)

        self.label = QLabel(self)
        self.label.setGeometry(50,50,640,480)

        self.button1= QPushButton('打开摄像头',self)
        self.button1.setGeometry(50,550,100,30)
        self.button1.clicked.connect(self.open_camera)

          # 创建一个按钮用于拍摄并保存某一帧
        self.button2 = QPushButton('拍摄并保存', self)
        self.button2.setGeometry(350, 550, 100, 30)
        self.button2.clicked.connect(self.capture_frame)

        self.button3=QPushButton('关闭摄像头',self)
        self.button3.setGeometry(500,550,100,30)
        self.button3.clicked.connect(self.close_camera)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_camera)    

    def open_camera(self):
        self.timer.start(30)

    def close_camera(self):
        self.cap.release()

    def show_camera(self):
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():  
            print("无法打开摄像头")  
            exit()
        ret, frame = self.cap.read()  
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
            image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)  
            pixmap = QPixmap.fromImage(image) 
            self.label.setPixmap(pixmap)  # 在标签上显示图像

            # 生成时间戳命名的文件名  
            timestamp = time.strftime("%Y%m%D-%H%M%S") 
            save_dir = 'chepai'#保存路径
            filename = f"{timestamp}.jpg"  
            save_path = os.path.join(save_dir, filename) 
  
             # 保存图片  
            try:  
                cv2.imwrite(save_path, cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))  
                print(f"图片已保存为: {save_path}")  
            except Exception as e:  
                print(f"保存图片时发生错误: {e}")   
        else:
            print("无法从摄像头获取图像")
            self.cap.release()
            exit()
   
        
    def closeEvent(self,event):
        self.cap.release()
        event.accept()


#UI主界面
def main():
    app = QApplication([])
    camera_app = CameraApp()
    camera_app.show()
    sys.exit(app.exec_())

main()
