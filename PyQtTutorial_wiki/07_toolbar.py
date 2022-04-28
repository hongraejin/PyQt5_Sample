import sys

from PyQt5.QtWidgets import QApplication, QMainWindow , QAction, qApp
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 지정된 위치 자동 반복 자르기
        # action_01 = QAction(,"Exit",self)

        # wafer roation 하면서 자르기

        # wafer edge를 이어서 붙이기



        print()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())