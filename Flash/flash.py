import sys
from PyQt5 import QtGui, QtCore, QtWidgets, QtTest

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class Dialog(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        geometry = app.desktop().availableGeometry()
        self.setGeometry(geometry)

        layout = QtWidgets.QVBoxLayout()

        # self.b1 = QtWidgets.QPushButton('flash doggo')
        # self.b1.setMaximumSize(100, 50)
        # self.b1.clicked.connect(self.flashSplash)
        # layout.addWidget(self.b1)

        self.setLayout(layout)

    def flashSplash(self, path):
        # Be sure to keep a reference to the SplashScreen
        # otherwise it'll be garbage collected
        # That's why there is 'self.' in front of the name
        self.splash = QtWidgets.QSplashScreen(QtGui.QPixmap(path))

        # SplashScreen will be in the center of the screen by default.
        # You can move it to a certain place if you want.
        # self.splash.move(10,10)
        self.splash.show()


        # Close the image after 100ms
        QtCore.QTimer.singleShot(100, self.splash.close)



    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Space:
            for i in range(5):
                self.flashSplash('./ex.jpg')
                QtTest.QTest.qWait(3000)


    #
    # def keyPressEvent2(self, e):
    #     if e.key() == QtCore.Qt.Key_Escape:
    #         self.flashSplash()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    main = Dialog()
    main.show()

    sys.exit(app.exec_())
