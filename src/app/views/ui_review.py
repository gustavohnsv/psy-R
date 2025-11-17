# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'review_screen.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_TelaRevisao(object):
    def setupUi(self, TelaRevisao):
        if not TelaRevisao.objectName():
            TelaRevisao.setObjectName(u"TelaRevisao")
        TelaRevisao.resize(600, 450)
        self.verticalLayout_2 = QVBoxLayout(TelaRevisao)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_titulo = QLabel(TelaRevisao)
        self.label_titulo.setObjectName(u"label_titulo")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_titulo.setFont(font)
        self.label_titulo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_titulo)

        self.scrollArea = QScrollArea(TelaRevisao)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 576, 325))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_revisao = QLabel(self.scrollAreaWidgetContents)
        self.label_revisao.setObjectName(u"label_revisao")
        self.label_revisao.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_revisao.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_revisao)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_voltar = QPushButton(TelaRevisao)
        self.btn_voltar.setObjectName(u"btn_voltar")

        self.horizontalLayout.addWidget(self.btn_voltar)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_gerar_laudo = QPushButton(TelaRevisao)
        self.btn_gerar_laudo.setObjectName(u"btn_gerar_laudo")
        font1 = QFont()
        font1.setBold(True)
        self.btn_gerar_laudo.setFont(font1)

        self.horizontalLayout.addWidget(self.btn_gerar_laudo)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(TelaRevisao)

        QMetaObject.connectSlotsByName(TelaRevisao)
    # setupUi

    def retranslateUi(self, TelaRevisao):
        TelaRevisao.setWindowTitle(QCoreApplication.translate("TelaRevisao", u"Form", None))
        self.label_titulo.setText(QCoreApplication.translate("TelaRevisao", u"Revis\u00e3o e Gera\u00e7\u00e3o do Laudo", None))
        self.label_revisao.setText(QCoreApplication.translate("TelaRevisao", u"Aqui ser\u00e3o exibidos todos os dados inseridos para a confer\u00eancia final...", None))
        self.btn_voltar.setText(QCoreApplication.translate("TelaRevisao", u"Voltar", None))
        self.btn_gerar_laudo.setText(QCoreApplication.translate("TelaRevisao", u"Confirmar e Gerar Laudo", None))
    # retranslateUi

