# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'template_fields_screen.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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

class Ui_TelaCamposTemplate(object):
    def setupUi(self, TelaCamposTemplate):
        if not TelaCamposTemplate.objectName():
            TelaCamposTemplate.setObjectName(u"TelaCamposTemplate")
        TelaCamposTemplate.resize(800, 600)
        self.verticalLayout = QVBoxLayout(TelaCamposTemplate)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_titulo = QLabel(TelaCamposTemplate)
        self.label_titulo.setObjectName(u"label_titulo")
        self.label_titulo.setAlignment(Qt.AlignCenter)
        self.label_titulo.setMargin(0)
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_titulo.setFont(font)

        self.verticalLayout.addWidget(self.label_titulo)

        self.scrollArea = QScrollArea(TelaCamposTemplate)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.verticalLayout_campos = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_campos.setObjectName(u"verticalLayout_campos")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_campos.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_voltar = QPushButton(TelaCamposTemplate)
        self.btn_voltar.setObjectName(u"btn_voltar")

        self.horizontalLayout.addWidget(self.btn_voltar)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_avancar = QPushButton(TelaCamposTemplate)
        self.btn_avancar.setObjectName(u"btn_avancar")

        self.horizontalLayout.addWidget(self.btn_avancar)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(TelaCamposTemplate)

        QMetaObject.connectSlotsByName(TelaCamposTemplate)
    # setupUi

    def retranslateUi(self, TelaCamposTemplate):
        TelaCamposTemplate.setWindowTitle(QCoreApplication.translate("TelaCamposTemplate", u"Campos do Template", None))
        self.label_titulo.setText(QCoreApplication.translate("TelaCamposTemplate", u"Passo 3: Campos do Template", None))
        self.btn_voltar.setText(QCoreApplication.translate("TelaCamposTemplate", u"Voltar", None))
        self.btn_avancar.setText(QCoreApplication.translate("TelaCamposTemplate", u"Avan\u00e7ar", None))
    # retranslateUi

