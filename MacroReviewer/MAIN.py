import sys
import pathlib

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Reviewer(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,500,300)

        # toolbar를 포함한 기본화면 구성
        self.initToolbar()



        self.setWindowTitle('MACRO Reviwer By Ray Beta Ver')
        self.show()

    def initToolbar(self):
        # toolbar1 이미지 필터
        self.make_toolbar1()

        # toolbar2 Edge Macro 이미지 자르기
        self.make_toolbar2()

        # toolbar3 Edge Macro 이미지 붙이기
        self.make_toolbar3()

        # toolbar4 고정된 좌표 분석학.
        self.make_toolbar4()


    def make_toolbar1(self):
        icon_path = pathlib.Path().joinpath('icon','filter.png')
        filterAction = QAction(QIcon(str(icon_path)),"Filter", self)
        filterAction.setShortcut("Ctrl+L")
        filterAction.setStatusTip('Macro Image Filter')
        filterAction.triggered.connect(self.toolbar1Clicked)
        self.toolbar = self.addToolBar("Filter")
        self.toolbar.addAction(filterAction)

    def toolbar1Clicked(self):
        print("Toolbar1 정상작동합니다.")

        # Central Widget 이미 있는 경우 종료

        # 버튼 생성(버튼 이름은 정리할 폴더 설정)
            # 버튼 클릭시 파일 경로 받아서 특정 Size 이하의 Macro 이미지 제거


    def make_toolbar2(self):
        icon_path = pathlib.Path().joinpath('icon','scissors.png')
        edgecutAction = QAction(QIcon(str(icon_path)),"EdgeCut", self)
        edgecutAction.setShortcut("Ctrl+U")
        edgecutAction.setStatusTip('Macro Image Cutter')
        edgecutAction.triggered.connect(self.toolbar2Clicked)
        self.toolbar = self.addToolBar("Cutter")
        self.toolbar.addAction(edgecutAction)

    def toolbar2Clicked(self):
        print("Toolbar2 정상작동합니다.")

        # Centeral Widget 이미 있는 경우 종료

        # 버튼 생성 (버튼 이름은 EDGE MACRO 처리할 폴더 설정
            # 버튼 클릭시 D Drive 로 대상 이미지 이동

            # 나중에, 각도 설정할 수 있는 부분 추가

            # LOT, WF 별 폴더생성하여 작업 시작


    def make_toolbar3(self):
        icon_path = pathlib.Path().joinpath('icon','caterpillar.png')
        edgetapeAction = QAction(QIcon(str(icon_path)),"EdgeTape", self)
        edgetapeAction.setShortcut("Ctrl+T")
        edgetapeAction.setStatusTip('Macro Image Tape')
        self.toolbar = self.addToolBar("Tape")
        self.toolbar.addAction(edgetapeAction)

    def make_toolbar4(self):
        icon_path = pathlib.Path().joinpath('icon','coordinate.png')
        postraceAction = QAction(QIcon(str(icon_path)),"PosTrace", self)
        postraceAction.setShortcut("Ctrl+P")
        postraceAction.setStatusTip('Macro Image PositionTrace')
        self.toolbar = self.addToolBar("PosTrace")
        self.toolbar.addAction(postraceAction)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Reviewer()
    sys.exit(app.exec_())