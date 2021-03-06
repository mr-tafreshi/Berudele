# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main_win(object):
    def setupUi(self, main_win):
        main_win.setObjectName("main_win")
        main_win.resize(361, 426)
        self.centralwidget = QtWidgets.QWidget(main_win)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.sqlite_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.sqlite_groupBox.setObjectName("sqlite_groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.sqlite_groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.sqlite_label = QtWidgets.QLabel(self.sqlite_groupBox)
        self.sqlite_label.setObjectName("sqlite_label")
        self.gridLayout.addWidget(self.sqlite_label, 0, 0, 1, 1)
        self.sqlite_lineEdit = QtWidgets.QLineEdit(self.sqlite_groupBox)
        self.sqlite_lineEdit.setReadOnly(True)
        self.sqlite_lineEdit.setObjectName("sqlite_lineEdit")
        self.gridLayout.addWidget(self.sqlite_lineEdit, 0, 1, 1, 1)
        self.sqlite_toolButton = QtWidgets.QToolButton(self.sqlite_groupBox)
        self.sqlite_toolButton.setObjectName("sqlite_toolButton")
        self.gridLayout.addWidget(self.sqlite_toolButton, 0, 2, 1, 1)
        self.gridLayout_4.addWidget(self.sqlite_groupBox, 2, 0, 1, 1)
        self.mysql_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.mysql_groupBox.setObjectName("mysql_groupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.mysql_groupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.username_lineEdit = QtWidgets.QLineEdit(self.mysql_groupBox)
        self.username_lineEdit.setText("")
        self.username_lineEdit.setClearButtonEnabled(True)
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.gridLayout_3.addWidget(self.username_lineEdit, 2, 1, 1, 1)
        self.host_lineEdit = QtWidgets.QLineEdit(self.mysql_groupBox)
        self.host_lineEdit.setClearButtonEnabled(True)
        self.host_lineEdit.setObjectName("host_lineEdit")
        self.gridLayout_3.addWidget(self.host_lineEdit, 0, 1, 1, 1)
        self.port_label = QtWidgets.QLabel(self.mysql_groupBox)
        self.port_label.setObjectName("port_label")
        self.gridLayout_3.addWidget(self.port_label, 1, 0, 1, 1)
        self.show_hide_password_pushButton = QtWidgets.QPushButton(self.mysql_groupBox)
        self.show_hide_password_pushButton.setText("")
        self.show_hide_password_pushButton.setFlat(True)
        self.show_hide_password_pushButton.setObjectName("show_hide_password_pushButton")
        self.gridLayout_3.addWidget(self.show_hide_password_pushButton, 3, 2, 1, 1)
        self.host_label = QtWidgets.QLabel(self.mysql_groupBox)
        self.host_label.setObjectName("host_label")
        self.gridLayout_3.addWidget(self.host_label, 0, 0, 1, 1)
        self.port_spinBox = QtWidgets.QSpinBox(self.mysql_groupBox)
        self.port_spinBox.setMaximum(999999999)
        self.port_spinBox.setProperty("value", 3306)
        self.port_spinBox.setObjectName("port_spinBox")
        self.gridLayout_3.addWidget(self.port_spinBox, 1, 1, 1, 1)
        self.username_label = QtWidgets.QLabel(self.mysql_groupBox)
        self.username_label.setObjectName("username_label")
        self.gridLayout_3.addWidget(self.username_label, 2, 0, 1, 1)
        self.password_lineEdit = QtWidgets.QLineEdit(self.mysql_groupBox)
        self.password_lineEdit.setText("")
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineEdit.setClearButtonEnabled(True)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.gridLayout_3.addWidget(self.password_lineEdit, 3, 1, 1, 1)
        self.password_label = QtWidgets.QLabel(self.mysql_groupBox)
        self.password_label.setObjectName("password_label")
        self.gridLayout_3.addWidget(self.password_label, 3, 0, 1, 1)
        self.database_label = QtWidgets.QLabel(self.mysql_groupBox)
        self.database_label.setObjectName("database_label")
        self.gridLayout_3.addWidget(self.database_label, 4, 0, 1, 1)
        self.database_lineEdit = QtWidgets.QLineEdit(self.mysql_groupBox)
        self.database_lineEdit.setText("")
        self.database_lineEdit.setClearButtonEnabled(True)
        self.database_lineEdit.setObjectName("database_lineEdit")
        self.gridLayout_3.addWidget(self.database_lineEdit, 4, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.mysql_groupBox, 1, 0, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.connect_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.connect_pushButton.setObjectName("connect_pushButton")
        self.gridLayout_6.addWidget(self.connect_pushButton, 0, 0, 1, 1)
        self.close_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.close_pushButton.setObjectName("close_pushButton")
        self.gridLayout_6.addWidget(self.close_pushButton, 0, 2, 1, 1)
        self.about_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.about_pushButton.setObjectName("about_pushButton")
        self.gridLayout_6.addWidget(self.about_pushButton, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem, 0, 3, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_6, 5, 0, 1, 1)
        self.logo_label = QtWidgets.QLabel(self.centralwidget)
        self.logo_label.setText("")
        self.logo_label.setPixmap(QtGui.QPixmap("../../Untitled2.png"))
        self.logo_label.setAlignment(QtCore.Qt.AlignCenter)
        self.logo_label.setObjectName("logo_label")
        self.gridLayout_4.addWidget(self.logo_label, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_4.addWidget(self.line, 4, 0, 1, 1)
        self.mode_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.mode_groupBox.setObjectName("mode_groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.mode_groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.sqlite_to_mysql_radioButton = QtWidgets.QRadioButton(self.mode_groupBox)
        self.sqlite_to_mysql_radioButton.setChecked(True)
        self.sqlite_to_mysql_radioButton.setObjectName("sqlite_to_mysql_radioButton")
        self.gridLayout_2.addWidget(self.sqlite_to_mysql_radioButton, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        self.mysql_to_sqlite_radioButton = QtWidgets.QRadioButton(self.mode_groupBox)
        self.mysql_to_sqlite_radioButton.setObjectName("mysql_to_sqlite_radioButton")
        self.gridLayout_2.addWidget(self.mysql_to_sqlite_radioButton, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.mode_groupBox, 3, 0, 1, 1)
        main_win.setCentralWidget(self.centralwidget)
        self.help_action = QtWidgets.QAction(main_win)
        self.help_action.setObjectName("help_action")
        self.about_action = QtWidgets.QAction(main_win)
        self.about_action.setObjectName("about_action")
        self.exit_action = QtWidgets.QAction(main_win)
        self.exit_action.setObjectName("exit_action")

        self.retranslateUi(main_win)
        QtCore.QMetaObject.connectSlotsByName(main_win)
        main_win.setTabOrder(self.host_lineEdit, self.port_spinBox)
        main_win.setTabOrder(self.port_spinBox, self.username_lineEdit)
        main_win.setTabOrder(self.username_lineEdit, self.password_lineEdit)
        main_win.setTabOrder(self.password_lineEdit, self.database_lineEdit)
        main_win.setTabOrder(self.database_lineEdit, self.sqlite_lineEdit)
        main_win.setTabOrder(self.sqlite_lineEdit, self.sqlite_toolButton)
        main_win.setTabOrder(self.sqlite_toolButton, self.sqlite_to_mysql_radioButton)
        main_win.setTabOrder(self.sqlite_to_mysql_radioButton, self.mysql_to_sqlite_radioButton)
        main_win.setTabOrder(self.mysql_to_sqlite_radioButton, self.connect_pushButton)
        main_win.setTabOrder(self.connect_pushButton, self.about_pushButton)
        main_win.setTabOrder(self.about_pushButton, self.close_pushButton)
        main_win.setTabOrder(self.close_pushButton, self.show_hide_password_pushButton)

    def retranslateUi(self, main_win):
        _translate = QtCore.QCoreApplication.translate
        main_win.setWindowTitle(_translate("main_win", "Berudele"))
        self.sqlite_groupBox.setTitle(_translate("main_win", "SQLite:"))
        self.sqlite_label.setText(_translate("main_win", "Database:"))
        self.sqlite_toolButton.setText(_translate("main_win", "..."))
        self.mysql_groupBox.setTitle(_translate("main_win", "MySQL:"))
        self.host_lineEdit.setText(_translate("main_win", "127.0.0.1"))
        self.port_label.setText(_translate("main_win", "Port:"))
        self.host_label.setText(_translate("main_win", "Host:"))
        self.username_label.setText(_translate("main_win", "Username:"))
        self.password_label.setText(_translate("main_win", "Password:"))
        self.database_label.setText(_translate("main_win", "Database:"))
        self.connect_pushButton.setText(_translate("main_win", "Continue"))
        self.close_pushButton.setText(_translate("main_win", "Close"))
        self.about_pushButton.setText(_translate("main_win", "About..."))
        self.mode_groupBox.setTitle(_translate("main_win", "Mode:"))
        self.sqlite_to_mysql_radioButton.setText(_translate("main_win", "SQLite to MySQL"))
        self.mysql_to_sqlite_radioButton.setText(_translate("main_win", "MySQL to SQLite"))
        self.help_action.setText(_translate("main_win", "Help"))
        self.about_action.setText(_translate("main_win", "About"))
        self.exit_action.setText(_translate("main_win", "Exit"))


