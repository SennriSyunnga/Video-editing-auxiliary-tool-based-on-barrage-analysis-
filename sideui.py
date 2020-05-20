# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sideui.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import image_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(970, 610)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamily(u"\u4eff\u5b8b")
        font.setPointSize(15)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"C:/Users/\u502a\u5f67\u797a/Desktop/6941c4ef1185d470e5de463fbc1bdfa3f91fd9bd.jpg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QSize(50, 50))
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setIconSize(QSize(25, 25))
        self.tabWidget.setMovable(True)
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.gridLayout_4 = QGridLayout(self.tab_1)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_4.setHorizontalSpacing(25)
        self.gridLayout_4.setVerticalSpacing(30)
        self.gridLayout_4.setContentsMargins(6, 30, 6, 6)
        self.Run_2 = QPushButton(self.tab_1)
        self.Run_2.setObjectName(u"Run_2")
        font1 = QFont()
        font1.setFamily(u"\u601d\u6e90\u9ed1\u4f53 CN Heavy")
        font1.setPointSize(15)
        self.Run_2.setFont(font1)
        self.Run_2.setStyleSheet(u"background-image: url(:/image/1.png);")

        self.gridLayout_4.addWidget(self.Run_2, 4, 2, 1, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_1 = QLabel(self.tab_1)
        self.label_1.setObjectName(u"label_1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy2)
        self.label_1.setFont(font)
        self.label_1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_1)

        self.verticalSpacer_7 = QSpacerItem(20, 70, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_7)

        self.label_2 = QLabel(self.tab_1)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.verticalSpacer_8 = QSpacerItem(20, 70, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_8)

        self.label_3 = QLabel(self.tab_1)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.verticalSpacer_9 = QSpacerItem(20, 70, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_9)

        self.label_4 = QLabel(self.tab_1)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_4)

        self.verticalSpacer_5 = QSpacerItem(20, 70, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.label_5 = QLabel(self.tab_1)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_5)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, 0, -1)
        self.lineEdit_1 = QLineEdit(self.tab_1)
        self.lineEdit_1.setObjectName(u"lineEdit_1")
        sizePolicy.setHeightForWidth(self.lineEdit_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_1.setSizePolicy(sizePolicy)
        self.lineEdit_1.setFont(font)
        self.lineEdit_1.setClearButtonEnabled(False)

        self.verticalLayout.addWidget(self.lineEdit_1)

        self.verticalSpacer_2 = QSpacerItem(20, 70, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.lineEdit_2 = QLineEdit(self.tab_1)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setFont(font)

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.verticalSpacer = QSpacerItem(20, 70, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.lineEdit_3 = QLineEdit(self.tab_1)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setFont(font)

        self.verticalLayout.addWidget(self.lineEdit_3)

        self.verticalSpacer_3 = QSpacerItem(20, 70, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.lineEdit_4 = QLineEdit(self.tab_1)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setFont(font)

        self.verticalLayout.addWidget(self.lineEdit_4)

        self.verticalSpacer_4 = QSpacerItem(20, 70, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.lineEdit_5 = QLineEdit(self.tab_1)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        self.lineEdit_5.setFont(font)

        self.verticalLayout.addWidget(self.lineEdit_5)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.gridLayout_4.addLayout(self.horizontalLayout, 1, 0, 3, 1)

        self.checkBox = QCheckBox(self.tab_1)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setFont(font)
        self.checkBox.setCheckable(True)
        self.checkBox.setChecked(False)
        self.checkBox.setTristate(False)

        self.gridLayout_4.addWidget(self.checkBox, 4, 1, 1, 1)

        self.pushButton = QPushButton(self.tab_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"background-image: url(:/image/1.png);\n"
"color: rgb(123, 194, 200);")

        self.gridLayout_4.addWidget(self.pushButton, 1, 2, 1, 2)

        self.label_6 = QLabel(self.tab_1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout_4.addWidget(self.label_6, 1, 1, 1, 1)

        self.textEdit = QTextEdit(self.tab_1)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QSize(0, 0))
        self.textEdit.setStyleSheet(u"")
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.gridLayout_4.addWidget(self.textEdit, 2, 1, 1, 3)

        self.progressBar = QProgressBar(self.tab_1)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"background-image: url(:/image/1.png);")
        self.progressBar.setValue(0)

        self.gridLayout_4.addWidget(self.progressBar, 4, 0, 1, 1)

        self.gridLayout_4.setColumnStretch(0, 8)
        self.gridLayout_4.setColumnStretch(2, 5)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.textBrowser = QTextBrowser(self.tab_2)
        self.textBrowser.setObjectName(u"textBrowser")

        self.horizontalLayout_2.addWidget(self.textBrowser)

        icon1 = QIcon()
        icon1.addFile(u":/image/1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon1, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 970, 23))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        sizePolicy1.setHeightForWidth(self.menu.sizePolicy().hasHeightForWidth())
        self.menu.setSizePolicy(sizePolicy1)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.Run_2.clicked.connect(MainWindow.pushButton_Click)
        self.checkBox.clicked.connect(MainWindow.checkBox_On)
        self.pushButton.clicked.connect(MainWindow.resetButton_Click)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u8bfb\u5f39\u5e55\uff1a\u4ece\u5c1d\u8bd5\u5230\u653e\u5f03", None))
        self.Run_2.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u6587\u4ef6\u540d\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u6587\u4ef6\u540d\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u7d22\u5173\u952e\u8bcd\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u9608\u503c\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u95f4\u9694\uff1a", None))
        self.lineEdit_1.setText(QCoreApplication.translate("MainWindow", u"danmu.xml", None))
        self.lineEdit_1.setPlaceholderText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"KKSK", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"14", None))
        self.lineEdit_5.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u4ec5\u4f5c\u5f39\u5e55\u5b9a\u4f4d", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u7f6e(reset)", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u65f6\u95f4\u8f74", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"\u5206\u6790", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\u4eff\u5b8b','\u4eff\u5b8b'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u4eff\u5b8b';\">\u7248\u672c1.0.1\uff1a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u4eff\u5b8b';\">0\u3001\u672c\u5de5\u5177\u7b80\u5355\u7c97\u66b4\uff0c\u539f\u7406\u5373\uff1a\u5f53\u524d\u65f6\u523b\u8d77\u8fde\u7eed\u8bfb\u51655s\u5185\u7684\u5f39\u5e55\uff0c\u82e5\u6ee1\u8db3\u641c\u7d22\u6761\u4ef6\u7684\u5f39\u5e55\u4e0d\u5c0f\u4e8elimit\u6570\u91cf\uff0c\u5219\u8bb0\u5f55\u5f53\u524d\u65f6"
                        "\u95f4\u8f74\uff0c\u5e76\u8df3\u8fc7interval\u79d2\u3002\u968f\u540e\u91cd\u590d\u4e0a\u8ff0\u6b65\u9aa4\uff0c\u76f4\u5230\u8bfb\u5b8c\u6240\u6709\u7684\u5f39\u5e55\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u4eff\u5b8b';\">1\u3001\u9ed8\u8ba4\u8bbe\u7f6e\u662f\uff1ainterval=20s\uff0climit=14\uff0ckeywords=KKSK\u3002\u641c\u7d22\u5bf9\u8c61\u4e0d\u533a\u5206\u5927\u5c0f\u5199\uff0c\u8f93\u5165\u548c\u8f93\u51fa\u6587\u4ef6\u540d\u53ef\u4ee5\u81ea\u5df1\u6dfb\u52a0\u6267\u884c\u8def\u5f84\uff0c\u5982'D:\\KaguraMea\\video\\1.xml'\u82e5\u4e0d\u52a0\u8def\u5f84\uff0c\u5219\u9ed8\u8ba4\u5728\u540c\u7ea7\u6587\u4ef6\u5939\u5185\u3002\u6587\u4ef6\u540e\u7f00\u540d\u53ef\u7701\u7565\uff0c\u5c06\u5206\u522b\u5f3a\u5236\u8f6c.xml\u548c.txt\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" "
                        "font-family:'\u4eff\u5b8b';\">2\u3001\u5982\u4e0d\u5b9a\u4e49\u8f93\u51fa\u6587\u4ef6\u7684\u540d\u5b57\uff0c\u5219\u8f93\u51fa\u548c\u8f93\u5165\u6587\u4ef6\u540c\u540d\u7684txt\u6587\u4ef6\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u4eff\u5b8b';\">3\u3001\u5e73\u65f6\u4e0d\u5fc5\u52fe\u9009\u201c\u4ec5\u4f5c\u5f39\u5e55\u5b9a\u4f4d\u201d\uff0c\u52fe\u9009\u540e\uff0c\u5c06\u4e0d\u518d\u8f93\u51fa\u526a\u8f91\u53c2\u8003\u65f6\u95f4\u8f74\uff0c\u800c\u662f\u8f93\u51fa\u641c\u7d22\u7684\u5f39\u5e55\u7684\u5177\u4f53\u4f4d\u7f6e\u3002\u53cd\u9009\u540e\u6062\u590d\u6b63\u5e38\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u4eff\u5b8b';\">4\u3001\u6839\u636e\u5f39\u5e55\u6c60\u7684\u6d53\u5ea6\uff0c\u53ef\u4ee5\u81ea\u884c\u8c03\u6574limit\u7684\u5927\u5c0f\uff0c\u8d8a"
                        "\u6d53limit\u53ef\u4ee5\u8bbe\u5f97\u8d8a\u9ad8\u3002\u5982\u679c\u6ca1\u6709\u5f97\u5230\u641c\u7d22\u7ed3\u679c\uff0c\u8bf7\u52fe\u9009\u4ec5\u4f5c\u5f39\u5e55\u5b9a\u4f4d\u6765\u786e\u8ba4\u5f39\u5e55\u6c60\u4e2d\u662f\u5426\u6709\u6240\u9009\u5f39\u5e55\u3002\u82e5\u6709\uff0c\u8bf7\u964d\u4f4elimit\uff0c\u5df2\u8fbe\u5230\u6ee1\u610f\u7684\u6548\u679c\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u4eff\u5b8b';\">5\u3001\u672c\u5de5\u5177\u9002\u5408\u957f\u89c6\u9891\u9501\u5b9a\u9ad8\u5149\u89c6\u9891\u65f6\u523b\uff0c\u4f5c\u526a\u8f91\u6216\u8005\u8865\u89c6\u9891\u6240\u7528\u3002</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'\u4eff\u5b8b';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:"
                        "0; text-indent:0px;\"><span style=\" font-family:'\u4eff\u5b8b';\">\u73b0\u6709bug\uff1a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u4eff\u5b8b';\">1\u3001\u6218\u80dc\u4e0d\u4e86\u8be5\u5b57\u7b26\u4e32\uff1a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u4eff\u5b8b';\">\uff77\uff80\uff9c\uff67\u2501\u2501\u2501\u2501\u2501\u2501(n'\u2200')\u03b7\u2501\u2501\u2501\u2501\u2501\u2501 !!!!</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u4eff\u5b8b';\">2\u3001\u90e8\u5206\u8f6c\u4e49\u5b57\u7b26\u4e32\u4e0d\u53ef\u641c\u7d22\u3002</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-"
                        "indent:0; text-indent:0px; font-family:'\u4eff\u5b8b';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u4eff\u5b8b';\">\u672a\u6765\u76ee\u6807\uff1a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u4eff\u5b8b';\">\u4e0d\u6b62\u5ffd\u7565\u5927\u5c0f\u5199\uff0c\u540c\u65f6\u80fd\u5c06\u591a\u79cd\u5f39\u5e55\u5185\u5bb9\u8bc6\u522b\u4e3a\u76ee\u6807\u5f39\u5e55\u3002</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'\u4eff\u5b8b';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u4eff\u5b8b'; color:#ffffff;\">\u4e0d\u60f3\u5199\uff0c\u597d\u61d2"
                        "\u3002</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u8bf4\u660e\u6587\u6863", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6ca1\u5b66\u4f1a", None))
    # retranslateUi

