# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'template_screen.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_TelaTemplate(object):
    def setupUi(self, TelaTemplate):
        if not TelaTemplate.objectName():
            TelaTemplate.setObjectName(u"TelaTemplate")
        TelaTemplate.resize(600, 400)
        self.verticalLayout = QVBoxLayout(TelaTemplate)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_titulo = QLabel(TelaTemplate)
        self.label_titulo.setObjectName(u"label_titulo")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_titulo.setFont(font)
        self.label_titulo.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_titulo)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_caminho_template = QLineEdit(TelaTemplate)
        self.lineEdit_caminho_template.setObjectName(u"lineEdit_caminho_template")
        self.lineEdit_caminho_template.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEdit_caminho_template)

        self.btn_carregar = QPushButton(TelaTemplate)
        self.btn_carregar.setObjectName(u"btn_carregar")

        self.horizontalLayout.addWidget(self.btn_carregar)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_avancar = QPushButton(TelaTemplate)
        self.btn_avancar.setObjectName(u"btn_avancar")

        self.horizontalLayout_2.addWidget(self.btn_avancar)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(TelaTemplate)

        QMetaObject.connectSlotsByName(TelaTemplate)
    # setupUi

    def retranslateUi(self, TelaTemplate):
        TelaTemplate.setWindowTitle(QCoreApplication.translate("TelaTemplate", u"Assistente de Laudo", None))
        self.label_titulo.setText(QCoreApplication.translate("TelaTemplate", u"Carregar Template", None))
        self.lineEdit_caminho_template.setPlaceholderText(QCoreApplication.translate("TelaTemplate", u"Caminho do arquivo de template...", None))
        self.btn_carregar.setText(QCoreApplication.translate("TelaTemplate", u"Carregar...", None))
        self.btn_avancar.setText(QCoreApplication.translate("TelaTemplate", u"Avan\u00e7ar", None))
    # retranslateUi

