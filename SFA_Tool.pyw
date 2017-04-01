from PyQt4 import QtCore, QtGui
import sys
import re
from SFA_Bot import *
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_SFA_Result(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, SFA_Result):
        SFA_Result.setObjectName(_fromUtf8("SFA_Result"))
        SFA_Result.resize(606, 501)
        SFA_Result.setMinimumSize(QtCore.QSize(606, 501))
        SFA_Result.setMaximumSize(QtCore.QSize(606, 501))
        self.label = QtGui.QLabel(SFA_Result)
        self.label.setGeometry(QtCore.QRect(10, 10, 581, 18))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Hack"))
        font.setPointSize(14)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(SFA_Result)
        self.label_2.setGeometry(QtCore.QRect(10, 330, 581, 18))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Hack"))
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tableWidget = QtGui.QTableWidget(SFA_Result)
        self.tableWidget.setGeometry(QtCore.QRect(10, 30, 581, 291))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.listWidget = QtGui.QListWidget(SFA_Result)
        self.listWidget.setGeometry(QtCore.QRect(10, 350, 581, 141))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.retranslateUi(SFA_Result)
        QtCore.QMetaObject.connectSlotsByName(SFA_Result)

    def retranslateUi(self, SFA_Result):
        SFA_Result.setWindowTitle(_translate("SFA_Result", "SFA_Result", None))
        self.label.setText(_translate("SFA_Result", "Report", None))
        self.label_2.setText(_translate("SFA_Result", "Private accounts", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("SFA_Result", "Friend", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("SFA_Result", "Common Friends", None))
        self.tableWidget.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Fixed)
        self.tableWidget.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Fixed)
        self.tableWidget.setColumnWidth(0, 420)
        self.tableWidget.setColumnWidth(1, 120)


class Ui_SFA_Tool(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, SFA_Tool):
        SFA_Tool.setObjectName(_fromUtf8("SFA_Tool"))
        SFA_Tool.resize(335, 87)
        SFA_Tool.setMinimumSize(QtCore.QSize(335, 87))
        SFA_Tool.setMaximumSize(QtCore.QSize(335, 87))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        SFA_Tool.setFont(font)
        self.gridLayout = QtGui.QGridLayout(SFA_Tool)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit = QtGui.QLineEdit(SFA_Tool)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtGui.QPushButton(SFA_Tool)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(SFA_Tool)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.progressBar = QtGui.QProgressBar(SFA_Tool)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.horizontalLayout_2.addWidget(self.progressBar)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(SFA_Tool)
        QtCore.QMetaObject.connectSlotsByName(SFA_Tool)

    def retranslateUi(self, SFA_Tool):
        SFA_Tool.setWindowTitle(_translate("SFA_Tool", "SFA_Tool v1.1", None))
        self.lineEdit.setText(_translate("SFA_Tool", "Enter Steam account url", None))
        self.pushButton.setText(_translate("SFA_Tool", "Run bot", None))
        self.label.setText(_translate("SFA_Tool", "Progress", None))
        self.lineEdit.selectAll()
        self.lineEdit.returnPressed.connect(bot)
        self.pushButton.clicked.connect(bot)


def bot():
    if re.match(r"https?://steamcommunity.com/id/\w\/?", sfa_tool.lineEdit.text()) \
            or re.match(r"https?://steamcommunity.com/profiles/[0-9]\/?", sfa_tool.lineEdit.text()):
        user = sfa_tool.lineEdit.text()
        result = {}
        private = []
        api_key = '07814D6A28FF029D746FEB6450DBDFC5'

        if re.match(r"https?://steamcommunity.com/id/\w\/?", sfa_tool.lineEdit.text()):
            try:
                user_id = getUserId(user, api_key)
            except urllib.error.HTTPError as err:
                # private account does not provide any information
                if err.code == 401:
                    alert = QtGui.QMessageBox()
                    alert.setText("private account")
                    alert.exec_()
                    sfa_tool.close()
        else:
            # id allready provided
            user_id = user.split('/')[4]

        try:
            user_friends = getUserFriends(user_id, api_key)
        except:
            alert = QtGui.QMessageBox()
            alert.setText("network error occured")
            alert.exec_()
            sfa_tool.close()

        i = 0
        for friend in user_friends:
            QtCore.QCoreApplication.processEvents()
            try:
                friend_friends = getUserFriends(friend.split('/')[4], api_key)
                common = commonFriends(user_friends, friend_friends)
                result[friend] = common
                sfa_tool.progressBar.setValue((100 * i) / len(user_friends))
                i += 1
            except urllib.error.HTTPError as err:
                # private account does not provide any information
                if err.code == 401:
                    private.append(friend)
                else:
                    alert = QtGui.QMessageBox()
                    alert.setText("network error occured")
                    alert.exec_()
                    sfa_tool.close()
        sfa_tool.progressBar.setValue(100)

        sfa_tool.close()

        result_counted = []

        for item in result.keys():
            tmp = item, len(result[item])
            result_counted.append(tmp)

        sfa_result.tableWidget.setRowCount(len(result_counted))

        result_counted = bubbleSort(result_counted)

        i = 0
        for item in result_counted:
            sfa_result.tableWidget.setItem(i, 0, QtGui.QTableWidgetItem(item[0]))
            sfa_result.tableWidget.setItem(i, 1, QtGui.QTableWidgetItem(str(item[1])))
            i += 1

        for item in private:
            sfa_result.listWidget.addItem(item)

        sfa_result.show()

    else:
        alert = QtGui.QMessageBox()
        alert.setText("Invalid URL!")
        alert.exec_()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    sfa_tool = Ui_SFA_Tool()
    sfa_result = Ui_SFA_Result()
    sfa_tool.show()
    sys.exit(app.exec_())
