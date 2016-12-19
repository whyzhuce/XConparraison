# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xconparraison.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
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
        XConparraison.resize(834, 609)
        self.centralwidget = QtGui.QWidget(XConparraison)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_4 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget = QtGui.QWidget(self.splitter)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(153, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.leftInput = QtGui.QLineEdit(self.widget)
        self.leftInput.setObjectName(_fromUtf8("leftInput"))
        self.verticalLayout.addWidget(self.leftInput)
        spacerItem1 = QtGui.QSpacerItem(20, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.CmpValue = QtGui.QPushButton(self.splitter)
        self.CmpValue.setObjectName(_fromUtf8("CmpValue"))
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        self.leftSelect = QtGui.QComboBox(self.centralwidget)
        self.leftSelect.setObjectName(_fromUtf8("leftSelect"))
        self.gridLayout.addWidget(self.leftSelect, 1, 0, 1, 1)
        self.leftTbl = QtGui.QTableView(self.centralwidget)
        self.leftTbl.setObjectName(_fromUtf8("leftTbl"))
        self.gridLayout.addWidget(self.leftTbl, 2, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.rightSelect = QtGui.QComboBox(self.centralwidget)
        self.rightSelect.setObjectName(_fromUtf8("rightSelect"))
        self.gridLayout_2.addWidget(self.rightSelect, 1, 0, 1, 1)
        self.rightTbl = QtGui.QTableView(self.centralwidget)
        self.rightTbl.setObjectName(_fromUtf8("rightTbl"))
        self.gridLayout_2.addWidget(self.rightTbl, 2, 0, 1, 1)
        self.splitter_2 = QtGui.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.CmpFormula = QtGui.QPushButton(self.splitter_2)
        self.CmpFormula.setObjectName(_fromUtf8("CmpFormula"))
        self.layoutWidget_2 = QtGui.QWidget(self.splitter_2)
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(153, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.rightInput = QtGui.QLineEdit(self.layoutWidget_2)
        self.rightInput.setObjectName(_fromUtf8("rightInput"))
        self.verticalLayout_2.addWidget(self.rightInput)
        spacerItem3 = QtGui.QSpacerItem(20, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.gridLayout_2.addWidget(self.splitter_2, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        XConparraison.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(XConparraison)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        XConparraison.setStatusBar(self.statusbar)

        self.retranslateUi(XConparraison)
        QtCore.QObject.connect(self.leftInput, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.getLeftWorkBook)
        QtCore.QObject.connect(self.rightInput, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.getRightWorkBook)
        QtCore.QObject.connect(self.leftSelect, QtCore.SIGNAL(_fromUtf8("activated(QString)")), self.showLeftSheet)
        QtCore.QObject.connect(self.rightSelect, QtCore.SIGNAL(_fromUtf8("activated(QString)")), self.showRightSheet)
        QtCore.QObject.connect(self.CmpValue, QtCore.SIGNAL(_fromUtf8("clicked()")), self.compareValue)
        QtCore.QObject.connect(self.CmpFormula, QtCore.SIGNAL(_fromUtf8("clicked()")), self.compareFormula)
        QtCore.QMetaObject.connectSlotsByName(XConparraison)

    def getLeftWorkBook(self):
        self.left = self.getWorkBook(str(self.leftInput.text()))
        self.leftSelect.clear()
        self.leftSelect.addItems(self.left.keys())

    def getRightWorkBook(self):
        self.right = self.getWorkBook(str(self.rightInput.text()))
        self.rightSelect.clear()
        self.rightSelect.addItems(self.right.keys())

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
        self.CmpValue.setText(_translate("XConparraison", "Compare Value", None))
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
        else:
            painter.setBrush(QtGui.QBrush(Qt.white))
        painter.drawRect(option.rect)

        # # set text color
        painter.setPen(QtGui.QPen(Qt.black))

        painter.restore()
        QtGui.QItemDelegate.paint(self, painter, option, index)


class PandasModel(QtCore.QAbstractTableModel):
    def __init__(self, data, header, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._data = data
        self.header = header

    def rowCount(self, *args, **kwargs):
        return len(self._data.values)

    def columnCount(self, *args, **kwargs):
        return self._data.columns.size

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid:
            if role == Qt.DisplayRole:
                return QtCore.QVariant(self._data.values[index.row()][index.column()])
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

