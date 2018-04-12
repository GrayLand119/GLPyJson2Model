from PyQt5.QtCore import pyqtSlot, pyqtSignal, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QVBoxLayout
from PyQt5.QtGui import QKeyEvent
from GLPyJson2Model import *

import sys, json

ONE_TAB = "    "

class GLPyJson2ModelWindows(QMainWindow):

    def __init__(self):
        super(QMainWindow, self).__init__()
        self.ui = Ui_GLPyJson2Model()
        self.ui.setupUi(self)

        testStr1 = "{'user': {'userId': '123456789', 'mobile': '18188888888', 'nickname': 'GrayLand',\
                     'avatar': 'http://xxx/avatar_20180131045411.jpg',\
                     'gender': '1',\
                     'age': '28'}}"
        testStr2 = "{'userId': '123456789', 'mobile': '18188888888', 'nickname': 'GrayLand',\
                     'avatar': 'http://xxx/avatar_20180131045411.jpg',\
                     'gender': '1',\
                     'age': '28'}"

        self.ui.jsonEdit.setText(testStr1)

    @pyqtSlot()
    def onConvert(self):
        jsonStr = self.ui.jsonEdit.toPlainText()
        if len(jsonStr) == 0:
            QMessageBox.warning(self,
                                '提示',
                                "请输入需要转换的Json字符串",
                                QMessageBox.Ok,
                                QMessageBox.Ok)
            return

        jsonStr = jsonStr.replace('\'', '\"')
        # print(jsonStr)
        try:
            pyDict: dict = json.loads(jsonStr)
        except Exception as e:
            QMessageBox.warning(self,
                                '错误',
                                "Json数据格式错误!",
                                QMessageBox.Ok,
                                QMessageBox.Ok)
            return

        # print(pyDict)

        outPutStr = ""
        keys = list(pyDict.keys())
        if len(keys) == 1:
            k1: str = keys[0]
            clsName = k1[0].upper() + k1[1:]
            outPutStr += "class {0}(object):\n".format(clsName)
            jsonDict2 = pyDict.get(k1)

            if len(jsonDict2.keys()) > 0:
                for key, value in jsonDict2.items():
                    outPutStr += ONE_TAB + key + ": str = \"\"\n"


        else:
            outPutStr += "class MyClass(object):\n"
            for key, value in pyDict.items():
                outPutStr += ONE_TAB + key + ": str = \"\"\n"

        outPutStr += '\n'
        outPutStr += ONE_TAB + "def __init__(self):\n"
        outPutStr += ONE_TAB*2 + "super().__init__():\n"

        self.ui.pyEdit.setText(outPutStr)
        self.ui.pyEdit.selectAll()

    def onClose(self):
        reply = QMessageBox.question(self,
                                     '提示',
                                     "是否退出?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.close()

    def keyPressEvent(self, e : QKeyEvent):
        if e.key() == Qt.Key_Escape:
            self.onClose()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    win = GLPyJson2ModelWindows()
    app.setActiveWindow(win)
    win.show()

    sys.exit(app.exec())