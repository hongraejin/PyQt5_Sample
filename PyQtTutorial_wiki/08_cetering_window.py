import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Centering')
        self.resize(500,350)
        self.center()
        self.show()

    def center(self):
        # 창의 위치와 크기 정보를 가져옴
        qr = self.frameGeometry()

        # 사용하는 모니터의 화면 가운데으 위치를 파악함
        cp = QDesktopWidget().availableGeometry().center()

        # 창의 위치와 크기 정보를 수정함
        qr.moveCenter(cp)

        # 현재 창을 화면의 중심으로 이동했던 직각사각형의 왼쪽 위로 위치하게 함.
        self.move(qr.topLeft())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    myapp = MyApp()
    sys.exit(app.exec_())