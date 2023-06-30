import time
from PyQt6.QtMultimedia import QSoundEffect
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QTimer, QUrl
from time_designer import Ui_MainWindow


class Timer(QMainWindow):
    def __init__(self):
        super(Timer, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Таймер')
        self.is_start = False
        self.is_start_new_year = False

        #sound
        self.sound_timer = QSoundEffect()
        self.sound_timer.setSource(QUrl.fromLocalFile('/Users/rama/Python/pythonProject1/timer_pack/song_finish.wav'))

        # digits
        self.ui.btn_0.clicked.connect(lambda: self.add_digit('0'))
        self.ui.btn_1.clicked.connect(lambda: self.add_digit('1'))
        self.ui.btn_2.clicked.connect(lambda: self.add_digit('2'))
        self.ui.btn_3.clicked.connect(lambda: self.add_digit('3'))
        self.ui.btn_4.clicked.connect(lambda: self.add_digit('4'))
        self.ui.btn_5.clicked.connect(lambda: self.add_digit('5'))
        self.ui.btn_6.clicked.connect(lambda: self.add_digit('6'))
        self.ui.btn_7.clicked.connect(lambda: self.add_digit('7'))
        self.ui.btn_8.clicked.connect(lambda: self.add_digit('8'))
        self.ui.btn_9.clicked.connect(lambda: self.add_digit('9'))

        # actions
        self.ui.btn_remove.clicked.connect(lambda: self.timer_clear())
        self.ui.btn_backspace.clicked.connect(lambda: self.clear_one_symbol())
        self.ui.btn_start.clicked.connect(lambda: self.timer_start())
        self.ui.btn_pause.clicked.connect(lambda: self.timer_pause())
        self.ui.btn_new_year_time.clicked.connect(lambda: self.timer_start_new_year())

        # timer actions
        self.timer_log = QTimer()
        self.timer_log.timeout.connect(lambda: self.timer_func())
        self.timer_log.start(1000)

        self.timer_check = QTimer()
        self.timer_check.timeout.connect(lambda: self.timer_check_digits())
        self.timer_check.start(1)

        self.timer_check_ny = QTimer()
        self.timer_check_ny.timeout.connect(lambda: self.timer_new_year())
        self.timer_check_ny.start(1000)

    def add_digit(self, btn_text: str) -> None:
        if self.ui.time_text.text() == '00:00:00:00':
            self.ui.time_text.setText(btn_text)
            self.ui.time_text.setStyleSheet('color: white;')
        else:
            if len(self.ui.time_text.text()) % 3 == 2 and len(self.ui.time_text.text()) < 11:
                self.ui.time_text.setText(self.ui.time_text.text() + ':' + btn_text)
            elif len(self.ui.time_text.text()) < 11:
                self.ui.time_text.setText(self.ui.time_text.text() + btn_text)

    def timer_clear(self) -> None:
        self.ui.time_text.setText('00:00:00:00')
        self.ui.time_text.setStyleSheet('color: white')
        self.sound_timer.stop()
        self.timer_pause()

    def clear_one_symbol(self) -> None:
        self.ui.time_text.setText(self.ui.time_text.text()[:-1])

    def timer_check_digits(self) -> None:
        if (self.ui.time_text.text()[:2] != '00' and self.ui.time_text.text()[3:5] > '23' or
                self.ui.time_text.text()[:5] != '00:00' and self.ui.time_text.text()[6:8] > '59' or
                self.ui.time_text.text()[:8] != '00:00:00' and self.ui.time_text.text()[9:] > '59'):
            self.clear_one_symbol()

    def timer_start(self) -> None:
        self.is_start = True
        while len(self.ui.time_text.text()) != 11:
            self.add_digit('0')

    def timer_start_new_year(self) -> None:
        self.is_start_new_year = True
        self.ui.time_text.setStyleSheet('color: white;')

    def timer_pause(self) -> None:
        self.is_start = False
        self.is_start_new_year = False
        self.ui.btn_backspace.setEnabled(True)

    def timer_func(self) -> None:
        if self.is_start:
            self.ui.btn_backspace.setEnabled(False)
            if self.ui.time_text.text() != '00:00:00:00':
                if self.ui.time_text.text()[9:] != '00':  # работа с секундами
                    self.ui.time_text.setText(
                        self.ui.time_text.text()[:9] + '0' * (
                                2 - len(str(int(self.ui.time_text.text()[9:]) - 1))) + str(
                            int(self.ui.time_text.text()[9:]) - 1))
                elif self.ui.time_text.text()[6:8] == '00' and self.ui.time_text.text()[3:5] != '00':  # работа с часами
                    self.ui.time_text.setText(
                        self.ui.time_text.text()[:3] + '0' * (
                                2 - len(str(int(self.ui.time_text.text()[3:5]) - 1))) + str(
                            int(self.ui.time_text.text()[3:5]) - 1) + ':59:59')
                elif self.ui.time_text.text()[6:8] == '00':  # работа с сутками
                    self.ui.time_text.setText('0' * (2 - len(str(int(self.ui.time_text.text()[:2]) - 1))) + str(
                        int(self.ui.time_text.text()[:2]) - 1) + ':23:59:59')
                else:  # работа с минутами
                    self.ui.time_text.setText(
                        self.ui.time_text.text()[:6] + '0' * (
                                2 - len(str(int(self.ui.time_text.text()[6:8]) - 1))) + str(
                            int(self.ui.time_text.text()[6:8]) - 1) + ':59')
            else:
                self.ui.time_text.setStyleSheet('color: #622;')
                self.sound_timer.play()
                self.is_start = False

    def timer_new_year(self) -> None:
        if self.is_start_new_year:
            self.ui.btn_backspace.setEnabled(False)
            now_time = time.localtime()
            now_month = now_time.tm_mon
            now_days = now_time.tm_mday
            now_hours = now_time.tm_hour
            now_minutes = now_time.tm_min
            now_seconds = now_time.tm_sec
            if now_month != 12:
                self.ui.time_text.setText('99:' + '0' * (
                        2 - len(str(23 - now_hours))) + str(23 - now_hours) + ':' + '0' * (
                                                  2 - len(str(59 - now_minutes))) + str(
                    59 - now_minutes) + ':' + '0' * (2 - len(str(59 - now_seconds))) + str(59 - now_seconds))
            else:
                self.ui.time_text.setText('0' * (2 - len(str(30 - now_days))) + str(30 - now_days) + ':' + '0' * (
                            2 - len(str(23 - now_hours))) + str(23 - now_hours) + ':' + '0' * (
                                                      2 - len(str(59 - now_minutes))) + str(
                        59 - now_minutes) + ':' + '0' * (2 - len(str(59 - now_seconds))) + str(59 - now_seconds))
            if self.ui.time_text.text() == '00:00:00:00':
                self.ui.time_text.setStyleSheet('color: #570;')
                self.sound_timer.play()
                self.is_start_new_year = False


app = QApplication([])
application = Timer()
application.show()
app.exec()
