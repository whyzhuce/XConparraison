# -*- coding: utf-8 -*-

import os
from pandas import read_excel
from PyQt4 import QtCore, QtGui
Qt = QtCore.Qt

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


def column_string(n):
    div=n+1
    string=""
    while div>0:
        module=(div-1)%26
        string=chr(65+module)+string
        div=int((div-module)/26)
    return string


class Ui_XConparraison(object):
    def setupUi(self, XConparraison):
        XConparraison.setObjectName(_fromUtf8("XConparraison"))
        XConparraison.resize(900, 600)
        self.centralwidget = QtGui.QWidget(XConparraison)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.mainGrid = QtGui.QVBoxLayout(self.centralwidget)
        self.mainGrid.setObjectName(_fromUtf8("mainGrid"))

        self.leftInput = QtGui.QLineEdit()
        self.leftInput.setObjectName(_fromUtf8("leftInput"))
        self.leftBrowse = QtGui.QToolButton()
        self.leftBrowse.setObjectName(_fromUtf8("leftBrowse"))
        leftinputLayout = QtGui.QHBoxLayout()
        leftinputLayout.setSpacing(0)
        leftinputLayout.addWidget(self.leftInput)
        leftinputLayout.addWidget(self.leftBrowse)
        self.leftSelect = QtGui.QComboBox()
        self.leftSelect.setObjectName(_fromUtf8("leftSelect"))
        leftselectLayout = QtGui.QVBoxLayout()
        leftselectLayout.setObjectName(_fromUtf8("leftselectLayout"))
        leftselectLayout.addLayout(leftinputLayout)
        leftselectLayout.addWidget(self.leftSelect)
        self.CmpValue = QtGui.QPushButton()
        self.CmpValue.setObjectName(_fromUtf8("CmpValue"))
        self.CmpValue.setSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        self.CmpFormula = QtGui.QPushButton()
        self.CmpFormula.setObjectName(_fromUtf8("CmpFormula"))
        self.CmpFormula.setSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        self.rightInput = QtGui.QLineEdit()
        self.rightInput.setObjectName(_fromUtf8("rightInput"))
        self.rightBrowse = QtGui.QToolButton()
        self.rightBrowse.setObjectName(_fromUtf8("rightBrowse"))
        rightinputLayout = QtGui.QHBoxLayout()
        rightinputLayout.setSpacing(0)
        rightinputLayout.addWidget(self.rightInput)
        rightinputLayout.addWidget(self.rightBrowse)
        self.rightSelect = QtGui.QComboBox()
        self.rightSelect.setObjectName(_fromUtf8("rightSelect"))
        rightselectLayout = QtGui.QVBoxLayout()
        rightselectLayout.setObjectName(_fromUtf8("rightselectLayout"))
        rightselectLayout.addLayout(rightinputLayout)
        rightselectLayout.addWidget(self.rightSelect)
        self.tools = QtGui.QWidget()
        self.tools.setObjectName(_fromUtf8("tools"))
        self.tools.setFixedWidth(100)
        self.hideEqual = QtGui.QCheckBox("Hide Equal Cells", self.tools)
        self.hideEqual.setObjectName(_fromUtf8("hideEqual"))

        self.inputWidget = QtGui.QWidget()
        self.inputWidget.setObjectName(_fromUtf8("inputWidget"))
        inputGrid = QtGui.QHBoxLayout(self.inputWidget)
        inputGrid.addLayout(leftselectLayout)
        inputGrid.addWidget(self.CmpValue)
        inputGrid.addWidget(self.CmpFormula)
        inputGrid.addLayout(rightselectLayout)
        inputGrid.addWidget(self.tools)
        self.inputWidget.setFixedHeight(70)

        self.leftTbl = QtGui.QTableView()
        self.leftTbl.setObjectName(_fromUtf8("leftTbl"))
        self.rightTbl = QtGui.QTableView()
        self.rightTbl.setObjectName(_fromUtf8("rightTbl"))
        self.minimap = QtGui.QTableView()
        self.minimap.setObjectName(_fromUtf8("minimap"))
        self.minimap.setFixedWidth(110)
        self.tables = QtGui.QSplitter(Qt.Horizontal)
        self.tables.addWidget(self.leftTbl)
        self.tables.addWidget(self.rightTbl)
        self.tables.addWidget(self.minimap)

        self.mainGrid.addWidget(self.inputWidget)
        self.mainGrid.addWidget(self.tables)

        XConparraison.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(XConparraison)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        XConparraison.setStatusBar(self.statusbar)

        self.retranslateUi(XConparraison)
        self.leftInput.returnPressed.connect(self.getLeftWorkBook)
        self.leftBrowse.clicked.connect(self.getLeftFile)
        self.rightInput.returnPressed.connect(self.getRightWorkBook)
        self.rightBrowse.clicked.connect(self.getRightFile)
        self.leftSelect.activated.connect(self.showLeftSheet)
        self.rightSelect.activated.connect(self.showRightSheet)
        self.CmpValue.clicked.connect(self.compareValue)
        self.CmpFormula.clicked.connect(self.compareFormula)
        QtCore.QMetaObject.connectSlotsByName(XConparraison)

    def getLeftWorkBook(self):
        self.left = self.getWorkBook(str(self.leftInput.text()))
        self.leftSelect.clear()
        self.leftSelect.addItems(self.left.keys())
        self.showLeftSheet()

    def getLeftFile(self):
        fname = QtGui.QFileDialog.getOpenFileName(self.centralwidget, 'Open file',
                                            os.getcwd(), "Excel files (*.xls*)")
        self.leftInput.setText(str(fname))
        self.getLeftWorkBook()

    def getRightWorkBook(self):
        self.right = self.getWorkBook(str(self.rightInput.text()))
        self.rightSelect.clear()
        self.rightSelect.addItems(self.right.keys())
        self.showRightSheet()

    def getRightFile(self):
        fname = QtGui.QFileDialog.getOpenFileName(self.centralwidget, 'Open file',
                                            os.getcwd(), "Excel files (*.xls*)")
        self.rightInput.setText(str(fname))
        self.getRightWorkBook()

    def getWorkBook(self, input):
        wb = read_excel(input, header=None, sheetname=None)
        return wb

    def showLeftSheet(self):
        self.showSheet(self.left, str(self.leftSelect.currentText()), self.leftTbl)

    def showRightSheet(self):
        self.showSheet(self.right, str(self.rightSelect.currentText()), self.rightTbl)

    def showSheet(self, wb, sh, tbl):
        df = wb[sh].fillna("")
        header = map(column_string, map(int, df.columns))
        tbl.setModel(PandasModel(df, header))
        tbl.setItemDelegate(CompareDelegate())

    def compareValue(self):
        dl = self.left[str(self.leftSelect.currentText())].fillna("")
        dr = self.right[str(self.rightSelect.currentText())].fillna("")
        mask = dl.eq(dr)
        compare_delegate = CompareDelegate(mask=mask)
        self.leftTbl.setItemDelegate(compare_delegate)
        self.rightTbl.setItemDelegate(compare_delegate)

    def compareFormula(self):
        pass

    def retranslateUi(self, XConparraison):
        XConparraison.setWindowTitle(_translate("XConparraison", "XConparraison", None))
        self.leftBrowse.setText(_translate("Xconparraison", "...", None))
        self.rightBrowse.setText(_translate("Xconparraison", "...", None))
        self.CmpValue.setText(_translate("XConparraison", "Compare Values", None))
        self.CmpFormula.setText(_translate("XConparraison", "Compare Formula", None))


class CompareDelegate(QtGui.QItemDelegate):
    def __init__(self, parent=None, mask=None, *args):
        QtGui.QItemDelegate.__init__(self, parent, *args)
        self.mask = mask

    def paint(self, painter, option, index):
        painter.save()

        # set background color
        painter.setPen(QtGui.QPen(Qt.NoPen))
        if option.state & (self.mask is not None):
            if self.mask.iloc[index.row(), index.column()] == False:
                painter.setBrush(QtGui.QBrush(Qt.red))
        painter.drawRect(option.rect)

        # set text color
        painter.setPen(QtGui.QPen(Qt.black))

        painter.restore()
        QtGui.QItemDelegate.paint(self, painter, option, index)


class PandasModel(QtCore.QAbstractTableModel):
    def __init__(self, data, header, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._data = data
        self.header = header

    def rowCount(self, *args, **kwargs):
        return len(self._data.index)

    def columnCount(self, *args, **kwargs):
        return self._data.columns.size

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return QtCore.QVariant(self._data.iloc[index.row(), index.column()])
        return QtCore.QVariant()

    def headerData(self, i, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QtCore.QVariant(self.header[i])
        return QtCore.QAbstractTableModel.headerData(self, i, orientation, role)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    XConparraison = QtGui.QMainWindow()
    ui = Ui_XConparraison()
    ui.setupUi(XConparraison)
    XConparraison.show()
    sys.exit(app.exec_())

