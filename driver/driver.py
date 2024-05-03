# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'driver.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 900)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 0))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bodyFrame = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.bodyFrame.setFont(font)
        self.bodyFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bodyFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bodyFrame.setObjectName("bodyFrame")
        self.bodyFrameverticalLayout = QtWidgets.QVBoxLayout(self.bodyFrame)
        self.bodyFrameverticalLayout.setContentsMargins(10, 0, 10, 0)
        self.bodyFrameverticalLayout.setSpacing(0)
        self.bodyFrameverticalLayout.setObjectName("bodyFrameverticalLayout")
        self.headerFrame = QtWidgets.QFrame(self.bodyFrame)
        self.headerFrame.setMinimumSize(QtCore.QSize(0, 50))
        self.headerFrame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.headerFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.headerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.headerFrame.setObjectName("headerFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.headerFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.headerFrame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.headerText = QtWidgets.QLabel(self.frame_2)
        self.headerText.setMinimumSize(QtCore.QSize(0, 0))
        self.headerText.setObjectName("headerText")
        self.verticalLayout_2.addWidget(self.headerText, 0, QtCore.Qt.AlignVCenter)
        self.horizontalLayout.addWidget(self.frame_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.frame = QtWidgets.QFrame(self.headerFrame)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.minimize = QtWidgets.QPushButton(self.frame)
        self.minimize.setObjectName("minimize")
        self.horizontalLayout_2.addWidget(self.minimize)
        self.closeButton = QtWidgets.QPushButton(self.frame)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_2.addWidget(self.closeButton)
        self.horizontalLayout.addWidget(self.frame, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.bodyFrameverticalLayout.addWidget(self.headerFrame)
        self.scrollAreaFrame = QtWidgets.QFrame(self.bodyFrame)
        self.scrollAreaFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scrollAreaFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrollAreaFrame.setObjectName("scrollAreaFrame")
        self.scrollAreaFrameverticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaFrame)
        self.scrollAreaFrameverticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollAreaFrameverticalLayout.setSpacing(0)
        self.scrollAreaFrameverticalLayout.setObjectName("scrollAreaFrameverticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.scrollAreaFrame)
        self.scrollArea.setStyleSheet("background-color: rgb(55,55,55);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaContents = QtWidgets.QWidget()
        self.scrollAreaContents.setGeometry(QtCore.QRect(0, 0, 1174, 794))
        self.scrollAreaContents.setStyleSheet("")
        self.scrollAreaContents.setObjectName("scrollAreaContents")
        self.scrollAreaContentsverticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaContents)
        self.scrollAreaContentsverticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollAreaContentsverticalLayout.setSpacing(0)
        self.scrollAreaContentsverticalLayout.setObjectName("scrollAreaContentsverticalLayout")
        self.scrollArea.setWidget(self.scrollAreaContents)
        self.scrollAreaFrameverticalLayout.addWidget(self.scrollArea)
        self.bodyFrameverticalLayout.addWidget(self.scrollAreaFrame)
        self.verticalLayout.addWidget(self.bodyFrame)
        self.footFrame = QtWidgets.QFrame(self.centralwidget)
        self.footFrame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.footFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footFrame.setObjectName("footFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.footFrame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.generateConfigPushButton = QtWidgets.QPushButton(self.footFrame)
        self.generateConfigPushButton.setObjectName("generateConfigPushButton")
        self.horizontalLayout_4.addWidget(self.generateConfigPushButton)
        self.lockConfigPushButton = QtWidgets.QPushButton(self.footFrame)
        self.lockConfigPushButton.setObjectName("lockConfigPushButton")
        self.horizontalLayout_4.addWidget(self.lockConfigPushButton)
        self.addMatrixPushButton = QtWidgets.QPushButton(self.footFrame)
        self.addMatrixPushButton.setObjectName("addMatrixPushButton")
        self.horizontalLayout_4.addWidget(self.addMatrixPushButton)
        self.verticalLayout.addWidget(self.footFrame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.closeButton.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.headerText.setText(_translate("MainWindow", "Inventvm :~ Realy Matrix"))
        self.minimize.setText(_translate("MainWindow", "-"))
        self.closeButton.setText(_translate("MainWindow", "x"))
        self.generateConfigPushButton.setText(_translate("MainWindow", "Generate Config"))
        self.lockConfigPushButton.setText(_translate("MainWindow", "Lock Config"))
        self.addMatrixPushButton.setText(_translate("MainWindow", "Add Matrix"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
