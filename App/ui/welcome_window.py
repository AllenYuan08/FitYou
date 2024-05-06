# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'welcome_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import App.configs.icons_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1114, 867)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-6, -5, 1131, 881))
        # self.label.setStyleSheet(u"background-image:url(:/images/blur.jpg)")
        # self.label.setPixmap(QPixmap(u"../Data/UI_icons/blur.jpg"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(440, 20, 241, 71))
        self.label_2.setStyleSheet(u"font: italic 28pt \"Lucida Fax\";\n"
"font: 22pt \"Goudy Old Style\";")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(310, 220, 121, 31))
        self.label_3.setStyleSheet(u"font: 14pt \"Lucida Fax\";")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(310, 280, 121, 31))
        self.label_4.setStyleSheet(u"font: 14pt \"Lucida Fax\";")
        self.username = QLineEdit(Dialog)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(460, 220, 261, 31))
        self.username.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")
        self.password = QLineEdit(Dialog)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(460, 280, 261, 31))
        self.password.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.Login = QPushButton(Dialog)
        self.Login.setObjectName(u"Login")
        self.Login.setGeometry(QRect(520, 380, 121, 51))
        self.Login.setStyleSheet(u"background-color:transparent;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"border-radius:20px;\n"
"border-style:solid;\n"
"border-color:black;\n"
"border-width:2px;")
        self.Signup = QPushButton(Dialog)
        self.Signup.setObjectName(u"Signup")
        self.Signup.setGeometry(QRect(520, 540, 121, 51))
        self.Signup.setStyleSheet(u"background-color:transparent;\n"
"border-radius:20px;\n"
"border-style:solid;\n"
"border-color:black;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"border-width:2px;\n"
"")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(520, 480, 141, 31))
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(560, 500, 61, 31))
        self.error = QLabel(Dialog)
        self.error.setObjectName(u"error")
        self.error.setGeometry(QRect(460, 330, 261, 20))
        self.error.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color:rgb(255, 0, 0)")
        self.error.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"FitYouLogin", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"FitYou: Please login!", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Username: ", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Password:", None))
        self.Login.setText(QCoreApplication.translate("Dialog", u"Login", None))
        self.Signup.setText(QCoreApplication.translate("Dialog", u"Sign Up", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Don't have an account?", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Sign Up !!", None))
        self.error.setText("")
    # retranslateUi

