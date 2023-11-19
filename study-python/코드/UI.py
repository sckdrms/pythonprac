import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor, QFont, QFontDatabase, QPixmap
from PyQt5.QtCore import QRect, Qt

class CustomWidget(QWidget):
    FONT_FAMILY = ""  # 클래스 변수로 폰트 패밀리 정의

    def paintEvent(self, event):
        painter = QPainter(self)
        color = QColor("#abffb9")
        painter.setPen(QPen(color, 1))
        painter.setBrush(QBrush(color))
        rect = QRect(110, 80, 570, 300)
        painter.drawRoundedRect(rect, 10, 10)

        # 이미지 불러오기 및 그리기
        pixmap = QPixmap("AD.png")
        painter.drawPixmap(rect, pixmap)

        # 텍스트 그리기
        painter.setPen(QColor(0, 0, 0))
        painter.setFont(QFont(CustomWidget.FONT_FAMILY, 40))
        text = "무인 공병 회수기"
        painter.drawText(155, 55, text)  # 텍스트 위치 조정

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.resize(800, 480)

    def initUI(self):
        self.setGeometry(0, 0, 800, 480)
        self.setWindowTitle('PyQt Multi-Screen Example')

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.main_layout = QVBoxLayout(self.main_widget)

        self.screen1 = CustomWidget(self)
        self.screen1.setStyleSheet("background-color: white;")
        
        # 시작하기 버튼
        self.btn_to_screen2 = QPushButton('시작하기', self.screen1)
        self.btn_to_screen2.setFont(QFont(CustomWidget.FONT_FAMILY, 16))
        self.btn_to_screen2.setFixedSize(150, 100)
        self.btn_to_screen2.setStyleSheet("border-radius: 10px;")

        # 버튼을 가운데에 배치하기 위한 수평 레이아웃
        self.button_layout = QHBoxLayout()
        self.button_layout.addStretch()
        self.button_layout.addWidget(self.btn_to_screen2)
        self.button_layout.addStretch()

        self.screen1_layout = QVBoxLayout(self.screen1)
        self.screen1_layout.addLayout(self.button_layout)  # 버튼 레이아웃 추가

        self.main_layout.addWidget(self.screen1)

        self.btn_to_screen2.move((800 - 150) / 2, 320)  # 버튼 위치 조정
        self.btn_to_screen2.clicked.connect(self.showScreen2)

        self.screen2 = QWidget(self)
        self.screen2.setStyleSheet("background-color: white;")
        self.btn_to_screen3 = QPushButton('Go to Screen 3', self.screen2)
        self.btn_to_screen3.clicked.connect(self.showScreen3)
        self.main_layout.addWidget(self.screen2)
        self.screen2_layout = QVBoxLayout(self.screen2)
        self.screen2_layout.addWidget(self.btn_to_screen3)

        self.screen3 = QWidget(self)
        self.screen3.setStyleSheet("background-color: white;")
        self.btn_to_screen1 = QPushButton('Go to Screen 1', self.screen3)
        self.btn_to_screen1.clicked.connect(self.showScreen1)
        self.main_layout.addWidget(self.screen3)
        self.screen3_layout = QVBoxLayout(self.screen3)
        self.screen3_layout.addWidget(self.btn_to_screen1)

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

    # 폰트 불러오기
    font_id = QFontDatabase.addApplicationFont("Gwangyang.ttf")
    if font_id != -1:  # 폰트가 성공적으로 불러와졌는지 확인
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        CustomWidget.FONT_FAMILY = font_family
    else:
        print("Failed to load font")

    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
