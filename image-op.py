from __future__ import print_function
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import numpy as np


image_path = "./girl.jpg"
image = cv2.imread(image_path)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 556)
        MainWindow.setMinimumSize(QtCore.QSize(800, 556))
        MainWindow.setMaximumSize(QtCore.QSize(800, 556))
        MainWindow.setBaseSize(QtCore.QSize(800, 556))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        MainWindow.setStyleSheet("background-color: rgb(210, 221, 231);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 50, 394, 42))
        font = QtGui.QFont()
        font.setFamily("MathJax_Caligraphic")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 105, 158);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(490, 130, 96, 31))
        self.pushButton.clicked.connect(self.translation)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(146, 159, 171);")
        self.pushButton.setObjectName("pushButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(150, 100, 481, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 41))
        self.frame.setStyleSheet("background-color: rgb(250, 83, 250);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 230, 80, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(146, 159, 171);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.flipping)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(490, 180, 80, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(146, 159, 171);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.rotation)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(490, 410, 111, 31))
        self.pushButton_5.clicked.connect(self.open_folder)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(146, 159, 171);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 431, 321))
        self.label_2.setText("")
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label.raise_()
        self.pushButton.raise_()
        self.frame.raise_()
        self.line.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_5.raise_()
        self.label_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.label_2.setPixmap(QtGui.QPixmap("girl.jpg"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Typing Speed Test"))
        self.label.setText(_translate("MainWindow", "Image Manipulator"))
        self.pushButton.setText(_translate("MainWindow", "Translate"))
        self.pushButton_2.setText(_translate("MainWindow", "Flip"))
        self.pushButton_3.setText(_translate("MainWindow", "Rotate"))
        self.pushButton_5.setText(_translate("MainWindow", "Add Image"))


    def open_folder(self):
        # dir = QtWidgets.QFileDialog.getExistingDirectory(None, "Select folder", "/home/", QtWidgets.QFileDialog.ShowDirsOnly)   #Opening a folder
        # img = QtWidgets.QFileDialog.getOpenFileName(None, "Open File", "/home/", "Image files (*.jpg *.gif)")
        # img = self.label_2
        self.label_2.setScaledContents(True)
        self.label_2.setPixmap(QtGui.QPixmap("girl.jpg"))
        self.label_2.show()

    def translation(self):
        translationMatrix = np.float32([[1, 0, 50], [0, 1, 20]])
        movedImage = cv2.warpAffine(self.label_2, translationMatrix, (image.shape[1], image.shape[0]))  # moving the image
        cv2.imshow("Moved Image", movedImage)
        cv2.waitKey(0)

    def rotation(self):
        (h, w) = self.label_2.shape[:2]
        centre = (h // 2, w // 2)
        angle = -45
        scale = 1.0

        rotationMatrix = cv2.getRotationMatrix2D(centre, angle, scale)
        rotatedImage = cv2.warpAffine(self.label_2, rotationMatrix, (self.label_2.shape[1], self.label_2.shape[0]))

        cv2.imshow("Rotated Image", rotatedImage)
        cv2.waitKey(0)

    def flipping(self):
        flippedHorizontally = cv2.flip(self.label_2, -1)  # 1 = horizontally, 0 = vertically, -1 = horizontally then vertically
        cv2.imshow("Flipped Horizontally", flippedHorizontally)
        cv2.waitKey(-1)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

