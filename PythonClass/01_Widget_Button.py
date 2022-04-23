import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        btn = QPushButton("button", self)
        # btn 의 글씨 크기에 맞추어서 버튼 크기 구성
        btn.resize(btn.sizeHint())
        btn.setToolTip("tool tip ")
        btn.move(20,30)

        self.setGeometry(300,300,400,500)
        self.setWindowTitle('첫 번쨰 학습시간')

        self.show()


app = QApplication(sys.argv)
w = Exam()
app.exec_()