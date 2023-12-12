import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QHBoxLayout
from PyQt5.QtGui import QPainter, QFont, QPen, QBrush, QPixmap, QColor, QFontDatabase
from PyQt5.QtCore import Qt, QRect, QPointF
import cv2
import torch
from pathlib import Path
from PIL import Image
from PyQt5.QtWidgets import QFormLayout
import os

#os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = r'C:\Users\경운대학교 소프트웨어학부\AppData\Local\Programs\Python\Python39\Lib\site-packages\PyQt5\Qt5\plugins\platforms'

# YOLO 모델 로드
model_path = 'best.pt'
model = torch.hub.load('ultralytics/yolov5:master', 'custom', path=model_path)

class CustomWidget(QWidget):
    FONT_FAMILY = ""

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), Qt.white)
        color = QColor("#abffb9")
        painter.setPen(QPen(color, 1))
        painter.setBrush(QBrush(color))
        rect = QRect(70, 80, 640, 300)
        painter.drawRoundedRect(rect, 10, 10)

        pixmap = QPixmap("AD.png")
        painter.drawPixmap(rect, pixmap)

        painter.setPen(QColor(0, 0, 0))
        painter.setFont(QFont(CustomWidget.FONT_FAMILY, 40))
        text = "무인 공병 회수기"
        painter.drawText(195, 55, text)

class TopBarWidget(QWidget):
    def __init__(self, main_window, n1, n2, parent=None):
        super(TopBarWidget, self).__init__(parent)
        self.main_window = main_window
        self.n1 = n1  # 총 100원 개수 변수
        self.n2 = n2  # 총 130원 개수 변수
        self.n3 = 0   # 현재 100원 개수 변수
        self.n4 = 0   # 현재 130원 개수 변수
        self.layout = QVBoxLayout(self)
        self.initUI()

    def initUI(self):
        self.back_button = QPushButton('돌아가기', self)
        self.back_button.setGeometry(10, 10, 80, 40)
        self.back_button.setStyleSheet("""
            QPushButton {
                background-color: #abffb9;
                border: 3px solid #57b367;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #9af9a0;
            }
        """)
        self.back_button.clicked.connect(self.main_window.showScreen1)

        self.new_button = QPushButton('촬영하기', self)
        self.new_button.setGeometry(530, 80, 230, 300)
        self.new_button.clicked.connect(self.captureImage)
        self.new_button.setStyleSheet("""
            QPushButton {
                background-color: #abffb9;
                border-radius: 10px;
                border: 7px solid #9af9a0;
            }
            QPushButton:hover {
                background-color: #9af9a0;
            }
        """)

        self.label_current_100won = QLabel(f'현재 100원 개수: {self.n3}', self)
        self.label_current_130won = QLabel(f'현재 130원 개수: {self.n4}', self)
        self.label_total_100won = QLabel('총 100원 개수: ' + str(self.n1), self)
        self.label_total_130won = QLabel('총 130원 개수: ' + str(self.n2), self)

        self.label_current_100won.setGeometry(300, 100, 200, 20)
        self.label_current_130won.setGeometry(300, 130, 200, 20)
        self.label_total_100won.setGeometry(300, 160, 200, 20)
        self.label_total_130won.setGeometry(300, 190, 200, 20)

    def resetCounts(self):
        self.n3 = 0
        self.n4 = 0

    def updateCounts(self, count_100, count_130):
        self.resetCounts()

        self.n3 += count_100
        self.n4 += count_130

        self.label_current_100won.setText(f'현재 100원 개수: {self.n3}')
        self.label_current_130won.setText(f'현재 130원 개수: {self.n4}')

        self.n1 += count_100
        self.n2 += count_130
        self.label_total_100won.setText(f'총 100원 개수: {self.n1}')
        self.label_total_130won.setText(f'총 130원 개수: {self.n2}')

    def captureImage(self):
        num_frames_to_capture = 5
        count_100, count_130 = 0, 0

        cap = cv2.VideoCapture(0)

        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        for _ in range(num_frames_to_capture):
            ret, frame = cap.read()
            if not ret:
                print("Error: Unable to capture frame.")
                cap.release()
                return
        if ret:
            cv2.imwrite("save.jpg", frame)

            img_path = "save.jpg"
            img = Image.open(img_path)
            results = model(img)

            for det in results.xyxy[0]:
                class_index = int(det[5])
                class_name = model.names[class_index]

                if class_name == '100':
                    count_100 += 1
                elif class_name == '130':
                    count_130 += 1

            self.updateCounts(count_100, count_130)
            self.update()

        cap.release()

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)

        graph_x = 50
        graph_y = 100
        graph_width = 220
        graph_height = 250

        y_labels = [5, 10, 15, 20, 25, 30]
        y_step = graph_height / max(y_labels)

        for label in y_labels:
            y = graph_y + graph_height - (label * y_step)
            painter.setPen(QPen(Qt.black, 1, Qt.DotLine))
            painter.drawLine(QPointF(graph_x, y), QPointF(graph_x + graph_width, y))
            painter.setPen(QPen(Qt.black))
            x = graph_x - 50
            text_position = QPointF(x, y)
            painter.drawText(text_position, str(label))

        x_labels = ['총 100원 갯수', '총 130원 갯수']
        x_step = graph_width / (len(x_labels) * 2)

        num_100_won = self.n1
        num_130_won = self.n2

        for i, label in enumerate(x_labels):
            x = graph_x + (i * 2 + 1) * x_step
            painter.setPen(QPen(Qt.black))
            text_position = QPointF(x - 50, graph_y + graph_height + 20)
            painter.drawText(text_position, label)

            if label == '총 100원 갯수':
                bar_height = y_step * num_100_won
            elif label == '총 130원 갯수':
                bar_height = y_step * num_130_won

            bar_color = QColor("#0d7414")
            painter.setBrush(QBrush(bar_color))
            bar_width = 25
            painter.drawRect(QRect(int(x - bar_width / 2), int(graph_y + graph_height - bar_height), int(bar_width), int(bar_height)))

        total_amount = (num_100_won * 100) + (num_130_won * 130)
        painter.setPen(QPen(Qt.black))
        painter.setFont(QFont(CustomWidget.FONT_FAMILY, 16))
        painter.drawText(QPointF(graph_x + graph_width / 2 - 100, graph_y + graph_height + 70), f'총 액수: {total_amount}원')

class ResultWidget(QWidget):
    def __init__(self, main_window, total_amount, n1, n2, parent=None):
        super(ResultWidget, self).__init__(parent)
        self.main_window = main_window
        self.total_amount = (n1*100)+(n2*130)
        self.count_100 = n1
        self.count_130 = n2


        # 100원과 130원을 각각 표시하는 QLabel 추가
        self.label_100won = QLabel(f'100원 개수: {self.count_100}', self)
        self.label_130won = QLabel(f'130원 개수: {self.count_130}', self)
        self.label_result = QLabel(f'총 액수: {self.total_amount}원', self)
        # QLabel에 해당하는 글자크기 조정 

        font = QFont()
        font.setPointSize(17)  # 원하는 크기로 설정
        self.label_100won.setFont(font)
        self.label_130won.setFont(font)
        self.label_result.setFont(font)


        # 수직 레이아웃
        self.layout = QVBoxLayout(self)

        self.label_100won.setAlignment(Qt.AlignCenter)
        self.label_130won.setAlignment(Qt.AlignCenter)
        self.label_result.setAlignment(Qt.AlignCenter)
        # 수평 레이아웃 상단
        self.h_layout_top = QHBoxLayout()
        self.h_layout_top.addWidget(self.label_100won, alignment=Qt.AlignTop)
        self.h_layout_top.addSpacing(50)  # 간격 추가
        self.h_layout_top.addWidget(self.label_130won, alignment=Qt.AlignTop)
        self.h_layout_top.addSpacing(50)  # 간격 추가
        self.h_layout_top.addWidget(self.label_result, alignment=Qt.AlignTop)
        self.h_layout_top.addStretch(1)
        
        label_width = 200  # 원하는 크기로 조절
        label_height = 40  # 원하는 크기로 조절

        self.label_100won.setFixedSize(label_width, label_height)
        self.label_130won.setFixedSize(label_width, label_height)
        self.label_result.setFixedSize(label_width, label_height)
        
        self.layout.addLayout(self.h_layout_top)

        # 이미지 추가
        pixmap1 = QPixmap('100won.png')  # 100원 이미지의 경로를 지정
        image_label1 = QLabel(self)
        image_label1.setPixmap(pixmap1.scaledToHeight(250).scaled(150, 250))  # 높이를 40으로 설정, 가로는 200으로 조절
        image_label1.setGeometry(30, 70, 150, 250)  # 이미지 레이블 위치 및 크기 설정

        pixmap2 = QPixmap('130won.png')  # 130원 이미지의 경로를 지정
        image_label2 = QLabel(self)
        image_label2.setPixmap(pixmap2.scaledToHeight(250).scaled(150, 250))  # 높이를 40으로 설정, 가로는 200으로 조절
        image_label2.setGeometry(290, 70, 150, 250)  # 이미지 레이블 위치 및 크기 설정
        
        pixmap3 = QPixmap('re.png')  # 리사이클 이미지의 경로를 지정
        image_label3 = QLabel(self)
        image_label3.setPixmap(pixmap3.scaledToHeight(250).scaled(250, 250))  # 높이를 40으로 설정, 가로는 200으로 조절
        image_label3.setGeometry(495, 70, 250, 250)  # 이미지 레이블 위치 및 크기 설정



        # 환급하기버튼
        self.refund_button = QPushButton('환급하기', self)
        self.refund_button.clicked.connect(self.refund)
        self.refund_button.setGeometry(300, 400, 200, 50)
        self.refund_button.setStyleSheet("""
            QPushButton {
                background-color: #abffb9;
                border: 2px solid #57b367;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #9af9a0;
            }
        """)

    def refund(self):
        self.main_window.re_showScreen1()




class MainWindow(QMainWindow):
    def __init__(self, n1, n2):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.resize(800, 480)

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.main_layout = QVBoxLayout(self.main_widget)

        self.screen1 = CustomWidget(self)
        self.screen1.setStyleSheet("background-color: white;")
        self.main_layout.addWidget(self.screen1)

        self.btn_to_screen2 = QPushButton('시작하기', self.screen1)
        self.btn_to_screen2.setFont(QFont(CustomWidget.FONT_FAMILY, 16))
        self.btn_to_screen2.setGeometry(325, 390, 160, 70)
        self.btn_to_screen2.setStyleSheet("""
            QPushButton {
                background-color: #abffb9;
                border-radius: 10px;
                border: 7px solid #abffb9;
            }
            QPushButton:hover {
                background-color: #80e68a;
            }
        """)
        self.btn_to_screen2.clicked.connect(self.showScreen2)

        self.screen2 = TopBarWidget(self, n1, n2)
        self.screen2.setStyleSheet("background-color: white;")
        self.main_layout.addWidget(self.screen2)

        self.btn_to_screen3 = QPushButton('완료', self.screen2)
        self.btn_to_screen3.setGeometry(680, 400, 90, 50)
        self.btn_to_screen3.setStyleSheet("""
            QPushButton {
                background-color: #abffb9;
                border: 2px solid #57b367;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #9af9a0;
            }
        """)
        self.btn_to_screen3.clicked.connect(self.showScreen3)

        self.screen3 = ResultWidget(self, 0, 0, 0)
        self.screen3.setStyleSheet("background-color: white;")
        self.main_layout.addWidget(self.screen3)

        self.screen1.show()
        self.screen2.hide()
        self.screen3.hide()

    def showScreen2(self):
        self.screen1.hide()
        self.screen2.show()
        self.screen3.hide()

    def showScreen3(self):
        total_amount = (self.screen2.n1 * 100) + (self.screen2.n2 * 130)
        self.screen3.total_amount = total_amount
        self.screen3.count_100 = self.screen2.n1
        self.screen3.count_130 = self.screen2.n2
        self.screen3.label_100won.setText(f'100원 개수: {self.screen2.n1}')
        self.screen3.label_130won.setText(f'130원 개수: {self.screen2.n2}')
        self.screen3.label_result.setText(f'총 액수: {total_amount}원')
        self.screen1.hide()
        self.screen2.hide()
        self.screen3.show()

    def showScreen1(self):
        self.screen2.hide()
        self.screen3.hide()
        self.screen1.show()

    def re_showScreen1(self):
        self.screen2.n1 = 0
        self.screen2.n2 = 0
        self.screen2.label_current_100won.setText(f'현재 100원 개수: {0}')
        self.screen2.label_current_130won.setText(f'현재 100원 개수: {0}')
        self.screen2.label_total_100won.setText(f'총 100원 개수: {0}')
        self.screen2.label_total_130won.setText(f'총 100원 개수: {0}')
        self.screen2.hide()
        self.screen3.hide()
        self.screen1.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    font_id = QFontDatabase.addApplicationFont("Gwangyang.ttf")
    if font_id != -1:
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        CustomWidget.FONT_FAMILY = font_family
    else:
        print("Failed to load font")

    n1 = 0
    n2 = 0

    ex = MainWindow(n1, n2)
    ex.show()
    sys.exit(app.exec_())
