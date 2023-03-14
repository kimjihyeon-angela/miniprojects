# 스레드 사용 앱
import sys 
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import time

class BackgrounWorker(QThread): # PyQt5 스레드를 위한 클래스 존재
    procChanged = pyqtSignal(int)

    def __init__(self, count=0, parent=None) -> None:
        super().__init__()
        self.main = parent
        self.working = True # 스레드 동작여부
        self.count = count
        time.sleep(0.0001)

    def run(self):
        # self.parent.pgbTask.setRange(0,100)
        # for i in range(0, 101):
        #     print(f'스레드 출력 > {i}')
        #     self.parent.pgbTask.setValue(i)
        #     self.parent.txbLog.append(f'스레드 출력 > {i}')
        while self.working:
            self.procChanged.emit(self.count) # 시그널을 내보냄
            self.count += 1 # 값 증가만 처리함

class qtApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./studyThread/threadApp.ui', self)
        self.setWindowTitle('스레드 사용 앱 v0.4')
        self.pgbTask.setValue(0)

        self.btnStart.clicked.connect(self.btnStartClicked)
        # 스레드 초기화
        self.worker = BackgrounWorker(parent=self, count=0)
        # 백그라운드 워커에 있는 시그널 접근, 처리하기 위한 슬롯 함수
        self.worker.procChanged.connect(self.procUpdated)
        self.pgbTask.setRange(0,1000000)

    @pyqtSlot(int)
    def procUpdated(self, count):
        self.txbLog.append(f'스레드 출력 > {count}')
        self.pgbTask.setValue(count)
        print(f'스레드 출력 > {count}')

    @pyqtSlot()
    def btnStartClicked(self):
        self.worker.start()
        self.worker.working = True



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())