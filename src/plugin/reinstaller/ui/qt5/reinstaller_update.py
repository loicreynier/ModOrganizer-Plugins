# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Repos\ModOrganizer-Plugins\src\plugin\reinstaller\ui\reinstaller_update.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_updateTabWidget(object):
    def setupUi(self, updateTabWidget):
        updateTabWidget.setObjectName("updateTabWidget")
        updateTabWidget.resize(316, 128)
        self.verticalLayout = QtWidgets.QVBoxLayout(updateTabWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkUpdateWidget = QtWidgets.QWidget(updateTabWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkUpdateWidget.sizePolicy().hasHeightForWidth())
        self.checkUpdateWidget.setSizePolicy(sizePolicy)
        self.checkUpdateWidget.setObjectName("checkUpdateWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.checkUpdateWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkUpdateButton = QtWidgets.QPushButton(self.checkUpdateWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkUpdateButton.sizePolicy().hasHeightForWidth())
        self.checkUpdateButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkUpdateButton.setFont(font)
        self.checkUpdateButton.setObjectName("checkUpdateButton")
        self.horizontalLayout.addWidget(self.checkUpdateButton)
        self.checkUpdateLabel = QtWidgets.QLabel(self.checkUpdateWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkUpdateLabel.sizePolicy().hasHeightForWidth())
        self.checkUpdateLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkUpdateLabel.setFont(font)
        self.checkUpdateLabel.setObjectName("checkUpdateLabel")
        self.horizontalLayout.addWidget(self.checkUpdateLabel)
        self.verticalLayout.addWidget(self.checkUpdateWidget)
        self.noUpdateWidget = QtWidgets.QWidget(updateTabWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.noUpdateWidget.sizePolicy().hasHeightForWidth())
        self.noUpdateWidget.setSizePolicy(sizePolicy)
        self.noUpdateWidget.setObjectName("noUpdateWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.noUpdateWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.noUpdateLabel = QtWidgets.QLabel(self.noUpdateWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.noUpdateLabel.sizePolicy().hasHeightForWidth())
        self.noUpdateLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.noUpdateLabel.setFont(font)
        self.noUpdateLabel.setObjectName("noUpdateLabel")
        self.verticalLayout_2.addWidget(self.noUpdateLabel)
        self.verticalLayout.addWidget(self.noUpdateWidget)
        self.updateFoundWidget = QtWidgets.QWidget(updateTabWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.updateFoundWidget.sizePolicy().hasHeightForWidth())
        self.updateFoundWidget.setSizePolicy(sizePolicy)
        self.updateFoundWidget.setObjectName("updateFoundWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.updateFoundWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.updateFoundButton = QtWidgets.QPushButton(self.updateFoundWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.updateFoundButton.sizePolicy().hasHeightForWidth())
        self.updateFoundButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.updateFoundButton.setFont(font)
        self.updateFoundButton.setObjectName("updateFoundButton")
        self.horizontalLayout_2.addWidget(self.updateFoundButton)
        self.updateFoundLabel = QtWidgets.QLabel(self.updateFoundWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.updateFoundLabel.sizePolicy().hasHeightForWidth())
        self.updateFoundLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.updateFoundLabel.setFont(font)
        self.updateFoundLabel.setObjectName("updateFoundLabel")
        self.horizontalLayout_2.addWidget(self.updateFoundLabel)
        self.verticalLayout.addWidget(self.updateFoundWidget)
        self.widget = QtWidgets.QWidget(updateTabWidget)
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(updateTabWidget)
        QtCore.QMetaObject.connectSlotsByName(updateTabWidget)

    def retranslateUi(self, updateTabWidget):
        _translate = QtCore.QCoreApplication.translate
        updateTabWidget.setWindowTitle(_translate("updateTabWidget", "Form"))
        self.checkUpdateButton.setText(_translate("updateTabWidget", "Check"))
        self.checkUpdateLabel.setText(_translate("updateTabWidget", "Check for a new version of Reinstaller"))
        self.noUpdateLabel.setText(_translate("updateTabWidget", "Reinstaller is up to date."))
        self.updateFoundButton.setText(_translate("updateTabWidget", "Download"))
        self.updateFoundLabel.setText(_translate("updateTabWidget", "New version of Reinstaller available!"))
