# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Repos\ModOrganizer-Plugins\src\plugin\shortcutter\ui\shortcutter_creator.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(388, 205)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QtWidgets.QWidget(Form)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget_3)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.txtName = QtWidgets.QLineEdit(self.widget_3)
        self.txtName.setObjectName("txtName")
        self.horizontalLayout.addWidget(self.txtName)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.ddlProfile = QtWidgets.QComboBox(self.widget)
        self.ddlProfile.setObjectName("ddlProfile")
        self.horizontalLayout_2.addWidget(self.ddlProfile)
        self.verticalLayout.addWidget(self.widget)
        self.widget_4 = QtWidgets.QWidget(Form)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.ddlApplication = QtWidgets.QComboBox(self.widget_4)
        self.ddlApplication.setObjectName("ddlApplication")
        self.horizontalLayout_3.addWidget(self.ddlApplication)
        self.verticalLayout.addWidget(self.widget_4)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.imgIcon = QtWidgets.QLabel(self.widget_2)
        self.imgIcon.setMinimumSize(QtCore.QSize(32, 32))
        self.imgIcon.setMaximumSize(QtCore.QSize(32, 32))
        self.imgIcon.setText("")
        self.imgIcon.setObjectName("imgIcon")
        self.horizontalLayout_4.addWidget(self.imgIcon)
        self.lblIconPath = QtWidgets.QLabel(self.widget_2)
        self.lblIconPath.setObjectName("lblIconPath")
        self.horizontalLayout_4.addWidget(self.lblIconPath)
        self.btnIconPath = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnIconPath.sizePolicy().hasHeightForWidth())
        self.btnIconPath.setSizePolicy(sizePolicy)
        self.btnIconPath.setObjectName("btnIconPath")
        self.horizontalLayout_4.addWidget(self.btnIconPath)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_5 = QtWidgets.QWidget(Form)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btnLocation = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnLocation.sizePolicy().hasHeightForWidth())
        self.btnLocation.setSizePolicy(sizePolicy)
        self.btnLocation.setObjectName("btnLocation")
        self.horizontalLayout_5.addWidget(self.btnLocation)
        self.lblLocation = QtWidgets.QLabel(self.widget_5)
        self.lblLocation.setObjectName("lblLocation")
        self.horizontalLayout_5.addWidget(self.lblLocation)
        self.btnCreate = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCreate.sizePolicy().hasHeightForWidth())
        self.btnCreate.setSizePolicy(sizePolicy)
        self.btnCreate.setObjectName("btnCreate")
        self.horizontalLayout_5.addWidget(self.btnCreate)
        self.verticalLayout.addWidget(self.widget_5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Name"))
        self.label_2.setText(_translate("Form", "Profile"))
        self.label_3.setText(_translate("Form", "Application"))
        self.label_4.setText(_translate("Form", "Icon"))
        self.lblIconPath.setText(_translate("Form", "..."))
        self.btnIconPath.setText(_translate("Form", "Select"))
        self.btnLocation.setText(_translate("Form", "Location"))
        self.lblLocation.setText(_translate("Form", "..."))
        self.btnCreate.setText(_translate("Form", "Create"))
