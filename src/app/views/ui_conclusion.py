# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'conclusion_screen.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTextBrowser,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_TelaConclusao(object):
    def setupUi(self, TelaConclusao):
        if not TelaConclusao.objectName():
            TelaConclusao.setObjectName(u"TelaConclusao")
        TelaConclusao.resize(700, 500)
        self.verticalLayout = QVBoxLayout(TelaConclusao)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_titulo = QLabel(TelaConclusao)
        self.label_titulo.setObjectName(u"label_titulo")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_titulo.setFont(font)
        self.label_titulo.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_titulo)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox = QGroupBox(TelaConclusao)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.textBrowser_dados = QTextBrowser(self.groupBox)
        self.textBrowser_dados.setObjectName(u"textBrowser_dados")

        self.verticalLayout_2.addWidget(self.textBrowser_dados)


        self.horizontalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(TelaConclusao)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.textEdit_conclusao = QTextEdit(self.groupBox_2)
        self.textEdit_conclusao.setObjectName(u"textEdit_conclusao")

        self.verticalLayout_3.addWidget(self.textEdit_conclusao)


        self.horizontalLayout_2.addWidget(self.groupBox_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_voltar = QPushButton(TelaConclusao)
        self.btn_voltar.setObjectName(u"btn_voltar")

        self.horizontalLayout.addWidget(self.btn_voltar)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_avancar = QPushButton(TelaConclusao)
        self.btn_avancar.setObjectName(u"btn_avancar")

        self.horizontalLayout.addWidget(self.btn_avancar)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(TelaConclusao)

        QMetaObject.connectSlotsByName(TelaConclusao)
    # setupUi

    def retranslateUi(self, TelaConclusao):
        TelaConclusao.setWindowTitle(QCoreApplication.translate("TelaConclusao", u"Form", None))
        self.label_titulo.setText(QCoreApplication.translate("TelaConclusao", u"Passo 4: Conclus\u00e3o", None))
        self.groupBox.setTitle(QCoreApplication.translate("TelaConclusao", u"Dados Calculados para Refer\u00eancia", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("TelaConclusao", u"Conclus\u00e3o e Parecer Psicol\u00f3gico", None))
        self.btn_voltar.setText(QCoreApplication.translate("TelaConclusao", u"Voltar", None))
        self.btn_avancar.setText(QCoreApplication.translate("TelaConclusao", u"Avan\u00e7ar para Revis\u00e3o", None))
    # retranslateUi

