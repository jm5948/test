import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
import opensfm_run_all


class main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('OpenSfM')
        self.setGeometry(800, 200, 500, 500)

        # menu list
        menu = self.menuBar()
        menu.setNativeMenuBar(False)
        menu_file = menu.addMenu('File')
        menu_test = menu.addMenu('Test')
        menu_test2 = menu.addMenu('Test2')

        # menu actions
        file_exit = QAction('Exit', self)
        file_exit.triggered.connect(QCoreApplication.instance().quit)
        menu_file.addAction(file_exit)

        wg = camera_button()
        self.setCentralWidget(wg)
        self.show()



class camera_button(QWidget):
    def __init__(self):
        super().__init__()
        self.init_CTUI()

    def init_CTUI(self):

        self.set_directory = False
        self.error_message = 'Directory is not set'

        # btn list
        btn1 = QPushButton('Start Webcam', self)
        btn1.clicked.connect(self.webcam_btn)

        btn2 = QPushButton('Set Directory', self)
        btn2.clicked.connect(self.directory_btn)

        btn3 = QPushButton('Run All Process')
        btn3.clicked.connect(self.run_all_process)

        # get directory
        self.get_directory = QFileDialog(self)

        # error message
        self.error_mg = QErrorMessage(self)

        # layout
        layout = QVBoxLayout()
        layout.addWidget(btn2)
        layout.addWidget(btn1)
        layout.addWidget(btn3)

        self.setLayout(layout)
        self.show()


    def webcam_btn(self):
        if self.set_directory == False:
            self.error_mg.showMessage(self.error_message)
        else:
            self.run = opensfm_run_all.sfm_subprocesses(self.fname)
            self.run.start_webcam()

    def directory_btn(self):
        self.fname = self.get_directory.getExistingDirectory(self)
        self.set_directory = True

    def run_all_process(self):
        if self.set_directory == 0:
            self.error_mg.showMessage(self.error_message)
        else:
            run2 = opensfm_run_all.sfm_subprocesses(self.fname)
            run2.run_all()

app = QApplication(sys.argv)
main = main_window()
sys.exit(app.exec_())


