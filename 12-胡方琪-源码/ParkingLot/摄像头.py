# -*- coding: utf-8 -*-
#代码功能：生成窗口和按钮，点击按钮，打开摄像头并显示

import sys
import cv2
import time
import datetime
import pytz
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt, QTimer

#设置时区
timezone = pytz.timezone('Asia/Shanghai')



# 创建一个名为CameraApp的类，继承自QMainWindow


class CameraApp(QMainWindow):
    # 初始化方法
    def __init__(self):
        super().__init__()

        # 设置窗口的标题和大小
        self.setWindowTitle("摄像头显示")
        self.setGeometry(100, 100, 800, 600)

        # 创建一个标签用于显示摄像头捕获的图像
        self.label = QLabel(self)
        self.label.setGeometry(50, 50, 640, 480)

        # 创建一个按钮用于打开摄像头
        self.button = QPushButton('打开摄像头', self)
        self.button.setGeometry(50, 550, 100, 30)
        self.button.clicked.connect(self.open_camera)  # 点击按钮时连接到open_camera方法

        # 创建一个按钮用于拍摄并保存某一帧
        self.button1 = QPushButton('拍摄并保存', self)
        self.button1.setGeometry(350, 550, 100, 30)
        self.button1.clicked.connect(self.capture_frame)  # 点击按钮时连接到capture_frame方法

        # 创建一个按钮用于关闭摄像头
        self.button2 = QPushButton('关闭摄像头', self)
        self.button2.setGeometry(650, 550, 100, 30)
        self.button2.clicked.connect(self.closeEvent)  # 点击按钮时连接到closeEvent方法

        # 创建一个定时器用于定时更新摄像头捕获的图像
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_camera)  # 定时器超时时连接到show_camera方法

        # 打开摄像头，创建一个VideoCapture对象
        self.cap = cv2.VideoCapture(0)

    # 打开摄像头的方法
    def open_camera(self):
        self.timer.start(30)  # 启动定时器，每30毫秒更新一次图像

    # 显示摄像头捕获的图像的方法
    def show_camera(self):
        ret, frame = self.cap.read()  # 从摄像头中读取一帧图像
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # 将图像颜色通道从BGR转换为RGB
            image = QImage(
                frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
            # 创建一个QImage对象。frame：这是一个NumPy数组，代表了图像的像素数据。frame.shape[1]：这是图像的宽度，即图像的列数。
            #frame.shape[0]：这是图像的高度，即图像的行数。frame.strides[0]：这是数组中相邻行之间的字节数。
            #这个参数通常用于处理图像数据的布局和内存布局。QImage.Format_RGB888：这是一个枚举值，代表了图像的格式。
            pixmap = QPixmap.fromImage(image)  # 从QImage对象创建一个QPixmap对象
            self.label.setPixmap(pixmap)  # 在标签上显示图像
            # 显示当前帧
            cv2.imshow('Frame', frame)


    #拍摄并保存某一帧的方法
    def capture_frame(self):
        # 读取摄像头视频流中的一帧
        ret, frame = self.cap.read()

        # 显示当前帧
        cv2.imshow('Frame', frame)

        # 设置图像文件名
        now = datetime.datetime.now()
        nowtime = now.astimezone(timezone)
        image_name = "{}.png".format(nowtime.strftime("%Y-%m-%d %H-%M-%S"))
        # 保存当前帧为图像文件
        cv2.imwrite(image_name, frame)
        print("{} 已保存".format(image_name))
        # 更新图像计数器

    def closeEvent(self,event):
        self.cap.release()
        event.accept()


# 主函数

def main():
    app = QApplication(sys.argv)  # 创建一个应用程序对象
    camera_app = CameraApp()  # 创建一个CameraApp对象
    camera_app.show()  # 显示窗口
    sys.exit(app.exec_())  # 运行应用程序的事件循环


main()  # 调用主函数
