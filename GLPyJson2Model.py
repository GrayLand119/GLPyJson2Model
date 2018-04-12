# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GLPyJson2Model.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GLPyJson2Model(object):
    def setupUi(self, GLPyJson2Model):
        GLPyJson2Model.setObjectName("GLPyJson2Model")
        GLPyJson2Model.resize(789, 589)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GLPyJson2Model.sizePolicy().hasHeightForWidth())
        GLPyJson2Model.setSizePolicy(sizePolicy)
        GLPyJson2Model.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(GLPyJson2Model)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(10, 25, 10, 20)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.jsonEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.jsonEdit.setAcceptRichText(False)
        self.jsonEdit.setObjectName("jsonEdit")
        self.horizontalLayout.addWidget(self.jsonEdit)
        self.pyEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.pyEdit.setReadOnly(False)
        self.pyEdit.setAcceptRichText(False)
        self.pyEdit.setObjectName("pyEdit")
        self.horizontalLayout.addWidget(self.pyEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.convertBtn = QtWidgets.QPushButton(self.centralwidget)
        self.convertBtn.setMinimumSize(QtCore.QSize(150, 60))
        self.convertBtn.setMaximumSize(QtCore.QSize(180, 60))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.convertBtn.setFont(font)
        self.convertBtn.setStyleSheet("QPushButton {\n"
"background-color: rgb(0, 128, 255);\n"
"border-radius: 30px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(0, 128, 255, 200);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(0, 128, 255, 255);\n"
"}")
        self.convertBtn.setObjectName("convertBtn")
        self.horizontalLayout_2.addWidget(self.convertBtn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        GLPyJson2Model.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(GLPyJson2Model)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 789, 22))
        self.menubar.setObjectName("menubar")
        GLPyJson2Model.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(GLPyJson2Model)
        self.statusbar.setObjectName("statusbar")
        GLPyJson2Model.setStatusBar(self.statusbar)

        self.retranslateUi(GLPyJson2Model)
        self.convertBtn.clicked.connect(GLPyJson2Model.onConvert)
        QtCore.QMetaObject.connectSlotsByName(GLPyJson2Model)

    def retranslateUi(self, GLPyJson2Model):
        _translate = QtCore.QCoreApplication.translate
        GLPyJson2Model.setWindowTitle(_translate("GLPyJson2Model", "Python 下的 JSON 转 Model Class "))
        self.label_2.setText(_translate("GLPyJson2Model", "输入Json文本:"))
        self.label.setText(_translate("GLPyJson2Model", "输出Python Model:"))
        self.convertBtn.setText(_translate("GLPyJson2Model", "转 换"))

