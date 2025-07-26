import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtCore import QTimer, QTime, Qt


class StopWatch(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("stopWatch")
        self.title_label = QLabel("Stopwatch ⏲️", self)
        self.title_label.setGeometry(0,0,600,100)

        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel("00:00:00:00", self)
        self.start_button = QPushButton("start", self)
        self.stop_button = QPushButton("stop", self)
        self.reset_button = QPushButton("reset", self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.time_label.setObjectName("time_label")
        self.title_label.setObjectName("title")

        # self.title_name.setStyleSheet("")
        self.time_label.setAlignment(Qt.AlignCenter)


        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)



        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        vbox.addLayout(hbox)


        self.setStyleSheet("""
        QLabel, QPushButton{
            font-family: times new roman;
            font_weight: bold;
            padding: 20px;
        }
        QLabel#time_label {
            background-color: rgb(236, 19, 214);
            font-size: 120px;
            border-radius: 20px;
            margin-top: 50px;
        }
        
        QPushButton{
            font-size: 30px;
            padding: 10px;
        }
        #title {
            font-size: 30px;
            color: purple;
            padding: 0;
            margin-bottom: 30px;
            margin-left: 10px;
        }
        """)

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)

    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time_label.setText("00:00:00.00")

    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        sec = time.second()
        milliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{sec:02}:{milliseconds:02}"


    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = StopWatch()
    stopwatch.show()
    sys.exit(app.exec_())