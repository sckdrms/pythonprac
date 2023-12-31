import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PyQt5.QtGui import QPainter, QFont, QFontDatabase, QPen, QBrush, QPixmap, QColor
from PyQt5.QtCore import Qt, QRect
import cv2

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
        painter.drawText(155, 55, text)

class TopBarWidget(QWidget):
    def __init__(self, main_window, n1, n2, parent=None):
        super(TopBarWidget, self).__init__(parent)
        self.main_window = main_window
        self.n1 = n1
        self.n2 = n2
        self.n3 = 0  # 현재 100원 개수를 저장하는 변수
        self.n4 = 0  # 현재 130원 개수를 저장하는 변수
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

    def captureImage(self):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        if ret:
            cv2.imwrite("save.png", frame)
            # 이미지를 캡처할 때 n3와 n4를 업데이트합니다.
            self.n3 += 1  # 100원 개수 업데이트
            self.n4 += 1  # 130원 개수 업데이트
            self.label_current_100won.setText(f'현재 100원 개수: {self.n3}')
            self.label_current_130won.setText(f'현재 130원 개수: {self.n4}')
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
            painter.drawLine(graph_x, y, graph_x + graph_width, y)
            painter.setPen(QPen(Qt.black))
            painter.drawText(graph_x - 30, y, str(label))

        x_labels = ['100원 공병', '130원 공병']
        x_step = graph_width / (len(x_labels) * 2)

        num_100_won = self.n1
        num_130_won = self.n2

        for i, label in enumerate(x_labels):
            x = graph_x + (i * 2 + 1) * x_step
            painter.setPen(QPen(Qt.black))
            painter.drawText(x - 50, graph_y + graph_height + 20, label)

            if label == '100원 공병':
                bar_height = y_step * num_100_won
            elif label == '130원 공병':
                bar_height = y_step * num_130_won

            bar_color = QColor("#0d7414")
            painter.setBrush(QBrush(bar_color))
            bar_width = 25
            painter.drawRect(x - bar_width / 2, graph_y + graph_height - bar_height, bar_width, bar_height)

        # 그래프 아래에 총 액수 텍스트 추가
        total_amount = (num_100_won * 100) + (num_130_won * 130)
        painter.setPen(QPen(Qt.black))
        painter.setFont(QFont(CustomWidget.FONT_FAMILY, 16))
        painter.drawText(graph_x + graph_width / 2 - 100, graph_y + graph_height + 70, f'총 액수: {total_amount}원')

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

        self.screen3 = QWidget(self)
        self.screen3.setStyleSheet("background-color: white;")
        self.btn_to_screen1 = QPushButton('돌아가기', self.screen3)
        self.btn_to_screen1.clicked.connect(self.showScreen1)
        self.screen3_layout = QVBoxLayout(self.screen3)
        self.screen3_layout.addWidget(self.btn_to_screen1)
        self.main_layout.addWidget(self.screen3)

        self.screen1.show()
        self.screen2.hide()
        self.screen3.hide()

    def showScreen2(self):
        self.screen1.hide()
        self.screen2.show()
        self.screen3.hide()

    def showScreen3(self):
        self.screen1.hide()
        self.screen2.hide()
        self.screen3.show()

    def showScreen1(self):
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

    n1 = 15  # 예시: 총 100원 개수
    n2 = 5   # 예시: 총 130원 개수
    ex = MainWindow(n1, n2)
    ex.show()
    sys.exit(app.exec_())
