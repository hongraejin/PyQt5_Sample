import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtGui

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        btn = QPushButton("button", self)
        # btn 의 글씨 크기에 맞추어서 버튼 크기 구성
        btn.move(50,50)

        # app instance 호출하여 종료함
        btn.clicked.connect(QCoreApplication.instance().quit)


        self.resize(500,500)
        self.setWindowTitle('첫 번쨰 학습시간')
        self.show()

    # app 자체를 X로 종료했을 때 실행되는 함수임.
    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:

        ans = QMessageBox.question(self, "종료확인", "종룍하시겠습니까?",
                             QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)
        if ans == QMessageBox.Yes:
            a0.accept()
        else:
            a0.ignore()

app = QApplication(sys.argv)
w = Exam()
app.exec_()

