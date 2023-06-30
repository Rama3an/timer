from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setFixedSize(QtCore.QSize(400, 300))
        font = QtGui.QFont()
        font.setFamily("Symbol")
        font.setPointSize(40)
        Dialog.setFont(font)
        Dialog.setMouseTracking(True)
        Dialog.setTabletTracking(True)
        Dialog.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        Dialog.setStyleSheet("background-color: rgb(0,0,0)")
        self.btn_start = QtWidgets.QPushButton(Dialog)
        self.btn_start.setGeometry(QtCore.QRect(75, 160, 100, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_start.sizePolicy().hasHeightForWidth())
        self.btn_start.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(17)
        font.setItalic(False)
        self.btn_start.setFont(font)
        self.btn_start.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_start.setAutoFillBackground(False)
        self.btn_start.setStyleSheet("QPushButton{\n"
                                     "    border-radius: 15px;\n"
                                     "    background-color: white;\n"
                                     "     color: black;\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "    background-color: #666;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed{\n"
                                     "    background-color: #888;\n"
                                     "}")
        self.btn_start.setObjectName("btn_start")
        self.btn_pause = QtWidgets.QPushButton(Dialog)
        self.btn_pause.setGeometry(QtCore.QRect(225, 160, 100, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_pause.sizePolicy().hasHeightForWidth())
        self.btn_pause.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(17)
        font.setItalic(False)
        self.btn_pause.setFont(font)
        self.btn_pause.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_pause.setAutoFillBackground(False)
        self.btn_pause.setStyleSheet("QPushButton{\n"
                                     "    border-radius: 15px;\n"
                                     "    background-color: white;\n"
                                     "     color: black;\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "    background-color: #666;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed{\n"
                                     "    background-color: #888;\n"
                                     "}")
        self.btn_pause.setObjectName("btn_pause")
        self.btn_new_year_time = QtWidgets.QPushButton(Dialog)
        self.btn_new_year_time.setGeometry(QtCore.QRect(225, 230, 100, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_new_year_time.sizePolicy().hasHeightForWidth())
        self.btn_new_year_time.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setItalic(False)
        self.btn_new_year_time.setFont(font)
        self.btn_new_year_time.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_new_year_time.setAutoFillBackground(False)
        self.btn_new_year_time.setStyleSheet("QPushButton{\n"
                                             "    border-radius: 15px;\n"
                                             "    background-color: white;\n"
                                             "     color: black;\n"
                                             "}\n"
                                             "QPushButton:hover{\n"
                                             "    background-color: #666;\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:pressed{\n"
                                             "    background-color: #888;\n"
                                             "}")
        self.btn_new_year_time.setObjectName("btn_new_year_time")
        self.time_text = QtWidgets.QLabel(Dialog)
        self.time_text.setGeometry(QtCore.QRect(75, 70, 250, 45))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(40)
        self.time_text.setFont(font)
        self.time_text.setStyleSheet("color: white;")
        self.time_text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.time_text.setObjectName("time_text")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(400, 330, 160, 180))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_7.setStyleSheet("color:white")
        self.btn_7.setObjectName("btn_7")
        self.gridLayout.addWidget(self.btn_7, 3, 1, 1, 1)
        self.btn_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_3.setStyleSheet("color:white")
        self.btn_3.setObjectName("btn_3")
        self.gridLayout.addWidget(self.btn_3, 4, 0, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_2.setStyleSheet("color:white")
        self.btn_2.setObjectName("btn_2")
        self.gridLayout.addWidget(self.btn_2, 3, 0, 1, 1)
        self.btn_0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_0.setStyleSheet("color:white")
        self.btn_0.setObjectName("btn_0")
        self.gridLayout.addWidget(self.btn_0, 0, 0, 1, 1)
        self.btn_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_4.setStyleSheet("color:white")
        self.btn_4.setObjectName("btn_4")
        self.gridLayout.addWidget(self.btn_4, 5, 0, 1, 1)
        self.btn_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_8.setStyleSheet("color:white")
        self.btn_8.setObjectName("btn_8")
        self.gridLayout.addWidget(self.btn_8, 4, 1, 1, 1)
        self.btn_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_9.setStyleSheet("color:white")
        self.btn_9.setObjectName("btn_9")
        self.gridLayout.addWidget(self.btn_9, 5, 1, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_5.setStyleSheet("color:white")
        self.btn_5.setObjectName("btn_5")
        self.gridLayout.addWidget(self.btn_5, 0, 1, 1, 1)
        self.btn_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_1.setStyleSheet("color:white")
        self.btn_1.setObjectName("btn_1")
        self.gridLayout.addWidget(self.btn_1, 1, 0, 1, 1)
        self.btn_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_6.setStyleSheet("color:white")
        self.btn_6.setObjectName("btn_6")
        self.gridLayout.addWidget(self.btn_6, 1, 1, 1, 1)
        self.btn_backspace = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_backspace.setStyleSheet("color:white")
        self.btn_backspace.setObjectName("btn_backspace")
        self.gridLayout.addWidget(self.btn_backspace, 2, 0, 1, 1)
        self.time_data = QtWidgets.QLabel(Dialog)
        self.time_data.setGeometry(QtCore.QRect(100, 30, 200, 20))
        self.time_data.setStyleSheet("color: grey")
        self.time_data.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.time_data.setObjectName("time_data")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, 120, 120, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: grey")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.btn_remove = QtWidgets.QPushButton(Dialog)
        self.btn_remove.setGeometry(QtCore.QRect(75, 230, 100, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_remove.sizePolicy().hasHeightForWidth())
        self.btn_remove.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(17)
        font.setItalic(False)
        self.btn_remove.setFont(font)
        self.btn_remove.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_remove.setAutoFillBackground(False)
        self.btn_remove.setStyleSheet("QPushButton{\n"
                                      "    border-radius: 15px;\n"
                                      "    background-color: white;\n"
                                      "     color: black;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "    background-color: #666;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed{\n"
                                      "    background-color: #888;\n"
                                      "}")
        self.btn_remove.setObjectName("btn_remove")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_start.setText(_translate("Dialog", "Старт"))
        self.btn_start.setShortcut(_translate("Dialog", "Return"))
        self.btn_pause.setText(_translate("Dialog", "Пауза"))
        self.btn_pause.setShortcut(_translate("Dialog", "Space"))
        self.btn_new_year_time.setText(_translate("Dialog", "Отсчет\n"
                                                            "до нового года"))
        self.time_text.setText(_translate("Dialog", "00:00:00:00"))
        self.btn_7.setText(_translate("Dialog", "7"))
        self.btn_7.setShortcut(_translate("Dialog", "7"))
        self.btn_3.setText(_translate("Dialog", "3"))
        self.btn_3.setShortcut(_translate("Dialog", "3"))
        self.btn_2.setText(_translate("Dialog", "2"))
        self.btn_2.setShortcut(_translate("Dialog", "2"))
        self.btn_0.setText(_translate("Dialog", "0"))
        self.btn_0.setShortcut(_translate("Dialog", "0"))
        self.btn_4.setText(_translate("Dialog", "4"))
        self.btn_4.setShortcut(_translate("Dialog", "4"))
        self.btn_8.setText(_translate("Dialog", "8"))
        self.btn_8.setShortcut(_translate("Dialog", "8"))
        self.btn_9.setText(_translate("Dialog", "9"))
        self.btn_9.setShortcut(_translate("Dialog", "9"))
        self.btn_5.setText(_translate("Dialog", "5"))
        self.btn_5.setShortcut(_translate("Dialog", "5"))
        self.btn_1.setText(_translate("Dialog", "1"))
        self.btn_1.setShortcut(_translate("Dialog", "1"))
        self.btn_6.setText(_translate("Dialog", "6"))
        self.btn_6.setShortcut(_translate("Dialog", "6"))
        self.btn_backspace.setText(_translate("Dialog", "<-"))
        self.btn_backspace.setShortcut(_translate("Dialog", "Backspace"))
        self.time_data.setText(_translate("Dialog", "Сутки:Часы:Минуты:Секунды"))
        self.label.setText(_translate("Dialog", "Ввод с клавиатуры"))
        self.btn_remove.setText(_translate("Dialog", "Сброс"))
        self.btn_remove.setShortcut(_translate("Dialog", "Esc"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
