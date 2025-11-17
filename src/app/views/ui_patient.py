# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'patient_screen.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_TelaPaciente(object):
    def setupUi(self, TelaPaciente):
        if not TelaPaciente.objectName():
            TelaPaciente.setObjectName(u"TelaPaciente")
        TelaPaciente.resize(800, 626)
        self.verticalLayout = QVBoxLayout(TelaPaciente)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_titulo = QLabel(TelaPaciente)
        self.label_titulo.setObjectName(u"label_titulo")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_titulo.setFont(font)
        self.label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

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

        self.label_idade_crono = QLabel(self.groupBox)
        self.label_idade_crono.setObjectName(u"label_idade_crono")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_idade_crono)

        self.lineEdit_idade_crono = QLineEdit(self.groupBox)
        self.lineEdit_idade_crono.setObjectName(u"lineEdit_idade_crono")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.lineEdit_idade_crono)

        self.label_escola = QLabel(self.groupBox)
        self.label_escola.setObjectName(u"label_escola")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_escola)

        self.lineEdit_escola = QLineEdit(self.groupBox)
        self.lineEdit_escola.setObjectName(u"lineEdit_escola")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.lineEdit_escola)

        self.label_turma = QLabel(self.groupBox)
        self.label_turma.setObjectName(u"label_turma")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_turma)

        self.lineEdit_turma = QLineEdit(self.groupBox)
        self.lineEdit_turma.setObjectName(u"lineEdit_turma")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.lineEdit_turma)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(TelaPaciente)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setEnabled(True)
        self.formLayout_2 = QFormLayout(self.groupBox_3)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_resp1_nome = QLabel(self.groupBox_3)
        self.label_resp1_nome.setObjectName(u"label_resp1_nome")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_resp1_nome)

        self.label_resp1_escolaridade = QLabel(self.groupBox_3)
        self.label_resp1_escolaridade.setObjectName(u"label_resp1_escolaridade")

        self.formLayout_2.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_resp1_escolaridade)

        self.lineEdit_resp1_nome = QLineEdit(self.groupBox_3)
        self.lineEdit_resp1_nome.setObjectName(u"lineEdit_resp1_nome")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineEdit_resp1_nome)

        self.lineEdit_resp1_escolaridade = QLineEdit(self.groupBox_3)
        self.lineEdit_resp1_escolaridade.setObjectName(u"lineEdit_resp1_escolaridade")

        self.formLayout_2.setWidget(5, QFormLayout.ItemRole.FieldRole, self.lineEdit_resp1_escolaridade)

        self.label_resp1_idade = QLabel(self.groupBox_3)
        self.label_resp1_idade.setObjectName(u"label_resp1_idade")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_resp1_idade)

        self.label_resp1_profissao = QLabel(self.groupBox_3)
        self.label_resp1_profissao.setObjectName(u"label_resp1_profissao")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_resp1_profissao)

        self.lineEdit_resp1_idade = QLineEdit(self.groupBox_3)
        self.lineEdit_resp1_idade.setObjectName(u"lineEdit_resp1_idade")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.lineEdit_resp1_idade)

        self.lineEdit_resp1_profissao = QLineEdit(self.groupBox_3)
        self.lineEdit_resp1_profissao.setObjectName(u"lineEdit_resp1_profissao")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.FieldRole, self.lineEdit_resp1_profissao)


        self.gridLayout.addWidget(self.groupBox_3, 0, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.formLayout_3 = QFormLayout(self.groupBox_4)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_resp2_nome = QLabel(self.groupBox_4)
        self.label_resp2_nome.setObjectName(u"label_resp2_nome")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_resp2_nome)

        self.label_resp2_escolaridade = QLabel(self.groupBox_4)
        self.label_resp2_escolaridade.setObjectName(u"label_resp2_escolaridade")

        self.formLayout_3.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_resp2_escolaridade)

        self.label_resp2_profissao = QLabel(self.groupBox_4)
        self.label_resp2_profissao.setObjectName(u"label_resp2_profissao")

        self.formLayout_3.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_resp2_profissao)

        self.label_resp2_idade = QLabel(self.groupBox_4)
        self.label_resp2_idade.setObjectName(u"label_resp2_idade")

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_resp2_idade)

        self.lineEdit_resp2_nome = QLineEdit(self.groupBox_4)
        self.lineEdit_resp2_nome.setObjectName(u"lineEdit_resp2_nome")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineEdit_resp2_nome)

        self.lineEdit_resp2_idade = QLineEdit(self.groupBox_4)
        self.lineEdit_resp2_idade.setObjectName(u"lineEdit_resp2_idade")

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lineEdit_resp2_idade)

        self.lineEdit_resp2_profissao = QLineEdit(self.groupBox_4)
        self.lineEdit_resp2_profissao.setObjectName(u"lineEdit_resp2_profissao")

        self.formLayout_3.setWidget(2, QFormLayout.ItemRole.FieldRole, self.lineEdit_resp2_profissao)

        self.lineEdit_resp2_escolaridade = QLineEdit(self.groupBox_4)
        self.lineEdit_resp2_escolaridade.setObjectName(u"lineEdit_resp2_escolaridade")

        self.formLayout_3.setWidget(3, QFormLayout.ItemRole.FieldRole, self.lineEdit_resp2_escolaridade)


        self.gridLayout.addWidget(self.groupBox_4, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_5 = QGroupBox(TelaPaciente)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.formLayout_4 = QFormLayout(self.groupBox_5)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_solicitante_nome = QLabel(self.groupBox_5)
        self.label_solicitante_nome.setObjectName(u"label_solicitante_nome")

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_solicitante_nome)

        self.label_solicitante_crp = QLabel(self.groupBox_5)
        self.label_solicitante_crp.setObjectName(u"label_solicitante_crp")

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_solicitante_crp)

        self.lineEdit_solicitante_nome = QLineEdit(self.groupBox_5)
        self.lineEdit_solicitante_nome.setObjectName(u"lineEdit_solicitante_nome")

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineEdit_solicitante_nome)

        self.lineEdit_solicitante_crp = QLineEdit(self.groupBox_5)
        self.lineEdit_solicitante_crp.setObjectName(u"lineEdit_solicitante_crp")

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lineEdit_solicitante_crp)


        self.verticalLayout.addWidget(self.groupBox_5)

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
        self.label_titulo.setText(QCoreApplication.translate("TelaPaciente", u"Dados do Paciente", None))
        self.groupBox.setTitle(QCoreApplication.translate("TelaPaciente", u"Informa\u00e7\u00f5es do paciente", None))
        self.label_nome.setText(QCoreApplication.translate("TelaPaciente", u"Nome Completo:", None))
        self.label_nascimento.setText(QCoreApplication.translate("TelaPaciente", u"Data de Nascimento:", None))
        self.dateEdit_nascimento.setDisplayFormat(QCoreApplication.translate("TelaPaciente", u"dd/MM/yyyy", None))
        self.label_idade_crono.setText(QCoreApplication.translate("TelaPaciente", u"Idade Cronol\u00f3gica:", None))
        self.label_escola.setText(QCoreApplication.translate("TelaPaciente", u"Institui\u00e7\u00e3o de Ensino:", None))
        self.label_turma.setText(QCoreApplication.translate("TelaPaciente", u"Turma:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("TelaPaciente", u"Informa\u00e7\u00f5es dos respons\u00e1veis", None))
        self.groupBox_3.setTitle("")
        self.label_resp1_nome.setText(QCoreApplication.translate("TelaPaciente", u"1\u00b0 Respons\u00e1vel:", None))
        self.label_resp1_escolaridade.setText(QCoreApplication.translate("TelaPaciente", u"Escolaridade:", None))
        self.label_resp1_idade.setText(QCoreApplication.translate("TelaPaciente", u"Idade:", None))
        self.label_resp1_profissao.setText(QCoreApplication.translate("TelaPaciente", u"Profiss\u00e3o:", None))
        self.groupBox_4.setTitle("")
        self.label_resp2_nome.setText(QCoreApplication.translate("TelaPaciente", u"2\u00b0 Respons\u00e1vel:", None))
        self.label_resp2_escolaridade.setText(QCoreApplication.translate("TelaPaciente", u"Escolaridade:", None))
        self.label_resp2_profissao.setText(QCoreApplication.translate("TelaPaciente", u"Profiss\u00e3o:", None))
        self.label_resp2_idade.setText(QCoreApplication.translate("TelaPaciente", u"Idade:", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("TelaPaciente", u"Informa\u00e7\u00f5es da solicitante", None))
        self.label_solicitante_nome.setText(QCoreApplication.translate("TelaPaciente", u"Nome Completo:", None))
        self.label_solicitante_crp.setText(QCoreApplication.translate("TelaPaciente", u"CRP:", None))
        self.btn_voltar.setText(QCoreApplication.translate("TelaPaciente", u"Voltar", None))
        self.btn_avancar.setText(QCoreApplication.translate("TelaPaciente", u"Avan\u00e7ar", None))
    # retranslateUi

