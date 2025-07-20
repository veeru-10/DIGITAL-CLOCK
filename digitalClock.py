import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase
class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.clock_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()
    def initUI(self):
        self.setWindowTitle("Digital clock")
        self.setGeometry(600, 400, 600, 200)
        self.setStyleSheet("background-color: black;")
        self.clock_label.setStyleSheet("font-size: 100px;"
                                       "color: green;")
        font_id = QFontDatabase.addApplicationFont("DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 200)
        self.clock_label.setFont(my_font)
        self.clock_label.setAlignment(Qt.AlignCenter)
        vbox = QVBoxLayout()
        vbox.addWidget(self.clock_label)
        self.setLayout(vbox)
        self.update_time()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.clock_label.setText(current_time)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())

