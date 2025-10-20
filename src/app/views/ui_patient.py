# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pacient_screen.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFormLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_TelaPaciente(object):
    def setupUi(self, TelaPaciente):
        if not TelaPaciente.objectName():
            TelaPaciente.setObjectName(u"TelaPaciente")
        TelaPaciente.resize(600, 400)
        self.verticalLayout = QVBoxLayout(TelaPaciente)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_titulo = QLabel(TelaPaciente)
        self.label_titulo.setObjectName(u"label_titulo")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_titulo.setFont(font)
        self.label_titulo.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_titulo)

        self.groupBox = QGroupBox(TelaPaciente)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label_nome = QLabel(self.groupBox)
        self.label_nome.setObjectName(u"label_nome")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_nome)

        self.lineEdit_nome = QLineEdit(self.groupBox)
        self.lineEdit_nome.setObjectName(u"lineEdit_nome")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineEdit_nome)

        self.label_nascimento = QLabel(self.groupBox)
        self.label_nascimento.setObjectName(u"label_nascimento")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_nascimento)

        self.dateEdit_nascimento = QDateEdit(self.groupBox)
        self.dateEdit_nascimento.setObjectName(u"dateEdit_nascimento")
        self.dateEdit_nascimento.setCalendarPopup(True)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.dateEdit_nascimento)

        self.label_responsavel = QLabel(self.groupBox)
        self.label_responsavel.setObjectName(u"label_responsavel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_responsavel)

        self.lineEdit_responsavel = QLineEdit(self.groupBox)
        self.lineEdit_responsavel.setObjectName(u"lineEdit_responsavel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.lineEdit_responsavel)

        self.label_escolaridade = QLabel(self.groupBox)
        self.label_escolaridade.setObjectName(u"label_escolaridade")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_escolaridade)

        self.lineEdit_escolaridade = QLineEdit(self.groupBox)
        self.lineEdit_escolaridade.setObjectName(u"lineEdit_escolaridade")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.lineEdit_escolaridade)


        self.verticalLayout.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_voltar = QPushButton(TelaPaciente)
        self.btn_voltar.setObjectName(u"btn_voltar")

        self.horizontalLayout.addWidget(self.btn_voltar)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_avancar = QPushButton(TelaPaciente)
        self.btn_avancar.setObjectName(u"btn_avancar")

        self.horizontalLayout.addWidget(self.btn_avancar)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(TelaPaciente)

        QMetaObject.connectSlotsByName(TelaPaciente)
    # setupUi

    def retranslateUi(self, TelaPaciente):
        TelaPaciente.setWindowTitle(QCoreApplication.translate("TelaPaciente", u"Form", None))
        self.label_titulo.setText(QCoreApplication.translate("TelaPaciente", u"Passo 2: Dados do Paciente", None))
        self.groupBox.setTitle(QCoreApplication.translate("TelaPaciente", u"Informa\u00e7\u00f5es Pessoais", None))
        self.label_nome.setText(QCoreApplication.translate("TelaPaciente", u"Nome Completo:", None))
        self.label_nascimento.setText(QCoreApplication.translate("TelaPaciente", u"Data de Nascimento:", None))
        self.dateEdit_nascimento.setDisplayFormat(QCoreApplication.translate("TelaPaciente", u"dd/MM/yyyy", None))
        self.label_responsavel.setText(QCoreApplication.translate("TelaPaciente", u"Respons\u00e1vel:", None))
        self.label_escolaridade.setText(QCoreApplication.translate("TelaPaciente", u"Escolaridade:", None))
        self.btn_voltar.setText(QCoreApplication.translate("TelaPaciente", u"Voltar", None))
        self.btn_avancar.setText(QCoreApplication.translate("TelaPaciente", u"Avan\u00e7ar", None))
    # retranslateUi

