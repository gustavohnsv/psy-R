# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tests_screen.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_TelaTestes(object):
    def setupUi(self, TelaTestes):
        if not TelaTestes.objectName():
            TelaTestes.setObjectName(u"TelaTestes")
        TelaTestes.resize(750, 500)
        self.verticalLayout_2 = QVBoxLayout(TelaTestes)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_titulo = QLabel(TelaTestes)
        self.label_titulo.setObjectName(u"label_titulo")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_titulo.setFont(font)
        self.label_titulo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_titulo)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox_botoes = QGroupBox(TelaTestes)
        self.groupBox_botoes.setObjectName(u"groupBox_botoes")
        self.verticalLayout = QVBoxLayout(self.groupBox_botoes)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_teste1 = QPushButton(self.groupBox_botoes)
        self.btn_teste1.setObjectName(u"btn_teste1")

        self.verticalLayout.addWidget(self.btn_teste1)

        self.btn_teste2 = QPushButton(self.groupBox_botoes)
        self.btn_teste2.setObjectName(u"btn_teste2")

        self.verticalLayout.addWidget(self.btn_teste2)

        self.btn_teste3 = QPushButton(self.groupBox_botoes)
        self.btn_teste3.setObjectName(u"btn_teste3")

        self.verticalLayout.addWidget(self.btn_teste3)

        self.btn_teste4 = QPushButton(self.groupBox_botoes)
        self.btn_teste4.setObjectName(u"btn_teste4")

        self.verticalLayout.addWidget(self.btn_teste4)

        self.btn_teste5 = QPushButton(self.groupBox_botoes)
        self.btn_teste5.setObjectName(u"btn_teste5")

        self.verticalLayout.addWidget(self.btn_teste5)

        self.btn_teste6 = QPushButton(self.groupBox_botoes)
        self.btn_teste6.setObjectName(u"btn_teste6")

        self.verticalLayout.addWidget(self.btn_teste6)

        self.btn_teste7 = QPushButton(self.groupBox_botoes)
        self.btn_teste7.setObjectName(u"btn_teste7")

        self.verticalLayout.addWidget(self.btn_teste7)

        self.btn_teste8 = QPushButton(self.groupBox_botoes)
        self.btn_teste8.setObjectName(u"btn_teste8")

        self.verticalLayout.addWidget(self.btn_teste8)

        self.btn_teste9 = QPushButton(self.groupBox_botoes)
        self.btn_teste9.setObjectName(u"btn_teste9")

        self.verticalLayout.addWidget(self.btn_teste9)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.groupBox_botoes)

        self.stackedWidget_formularios = QStackedWidget(TelaTestes)
        self.stackedWidget_formularios.setObjectName(u"stackedWidget_formularios")
        self.page_inicial = QWidget()
        self.page_inicial.setObjectName(u"page_inicial")
        self.verticalLayout_4 = QVBoxLayout(self.page_inicial)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_2 = QSpacerItem(20, 128, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.label = QLabel(self.page_inicial)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label)

        self.verticalSpacer_3 = QSpacerItem(20, 127, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.stackedWidget_formularios.addWidget(self.page_inicial)
        self.page_form_teste1 = QWidget()
        self.page_form_teste1.setObjectName(u"page_form_teste1")
        self.verticalLayout_3 = QVBoxLayout(self.page_form_teste1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_titulo_teste1 = QLabel(self.page_form_teste1)
        self.label_titulo_teste1.setObjectName(u"label_titulo_teste1")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_titulo_teste1.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_titulo_teste1)

        self.groupBox_faixa_etaria = QGroupBox(self.page_form_teste1)
        self.groupBox_faixa_etaria.setObjectName(u"groupBox_faixa_etaria")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_faixa_etaria)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.radioButton_pre_escolar = QRadioButton(self.groupBox_faixa_etaria)
        self.radioButton_pre_escolar.setObjectName(u"radioButton_pre_escolar")

        self.horizontalLayout_3.addWidget(self.radioButton_pre_escolar)

        self.radioButton_escolar = QRadioButton(self.groupBox_faixa_etaria)
        self.radioButton_escolar.setObjectName(u"radioButton_escolar")
        self.radioButton_escolar.setChecked(True)

        self.horizontalLayout_3.addWidget(self.radioButton_escolar)

        self.radioButton_adulto = QRadioButton(self.groupBox_faixa_etaria)
        self.radioButton_adulto.setObjectName(u"radioButton_adulto")

        self.horizontalLayout_3.addWidget(self.radioButton_adulto)


        self.verticalLayout_3.addWidget(self.groupBox_faixa_etaria)

        self.groupBox_dados_teste = QGroupBox(self.page_form_teste1)
        self.groupBox_dados_teste.setObjectName(u"groupBox_dados_teste")
        self.formLayout = QFormLayout(self.groupBox_dados_teste)
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.groupBox_dados_teste)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.spinBox = QSpinBox(self.groupBox_dados_teste)
        self.spinBox.setObjectName(u"spinBox")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.spinBox)

        self.label_3 = QLabel(self.groupBox_dados_teste)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.spinBox_2 = QSpinBox(self.groupBox_dados_teste)
        self.spinBox_2.setObjectName(u"spinBox_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.spinBox_2)


        self.verticalLayout_3.addWidget(self.groupBox_dados_teste)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.stackedWidget_formularios.addWidget(self.page_form_teste1)
        self.page_form_teste2 = QWidget()
        self.page_form_teste2.setObjectName(u"page_form_teste2")
        self.verticalLayout_3_2 = QVBoxLayout(self.page_form_teste2)
        self.verticalLayout_3_2.setObjectName(u"verticalLayout_3_2")
        self.label_titulo_teste2 = QLabel(self.page_form_teste2)
        self.label_titulo_teste2.setObjectName(u"label_titulo_teste2")
        self.label_titulo_teste2.setFont(font1)

        self.verticalLayout_3_2.addWidget(self.label_titulo_teste2)

        self.groupBox_faixa_etaria_2 = QGroupBox(self.page_form_teste2)
        self.groupBox_faixa_etaria_2.setObjectName(u"groupBox_faixa_etaria_2")
        self.horizontalLayout_3_2 = QHBoxLayout(self.groupBox_faixa_etaria_2)
        self.horizontalLayout_3_2.setObjectName(u"horizontalLayout_3_2")
        self.radioButton_pre_escolar_2 = QRadioButton(self.groupBox_faixa_etaria_2)
        self.radioButton_pre_escolar_2.setObjectName(u"radioButton_pre_escolar_2")

        self.horizontalLayout_3_2.addWidget(self.radioButton_pre_escolar_2)

        self.radioButton_escolar_2 = QRadioButton(self.groupBox_faixa_etaria_2)
        self.radioButton_escolar_2.setObjectName(u"radioButton_escolar_2")
        self.radioButton_escolar_2.setChecked(True)

        self.horizontalLayout_3_2.addWidget(self.radioButton_escolar_2)

        self.radioButton_adulto_2 = QRadioButton(self.groupBox_faixa_etaria_2)
        self.radioButton_adulto_2.setObjectName(u"radioButton_adulto_2")

        self.horizontalLayout_3_2.addWidget(self.radioButton_adulto_2)


        self.verticalLayout_3_2.addWidget(self.groupBox_faixa_etaria_2)

        self.groupBox_dados_teste_2 = QGroupBox(self.page_form_teste2)
        self.groupBox_dados_teste_2.setObjectName(u"groupBox_dados_teste_2")
        self.formLayout_2 = QFormLayout(self.groupBox_dados_teste_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_2_2 = QLabel(self.groupBox_dados_teste_2)
        self.label_2_2.setObjectName(u"label_2_2")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_2_2)

        self.spinBox_3 = QSpinBox(self.groupBox_dados_teste_2)
        self.spinBox_3.setObjectName(u"spinBox_3")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.spinBox_3)

        self.label_3_2 = QLabel(self.groupBox_dados_teste_2)
        self.label_3_2.setObjectName(u"label_3_2")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_3_2)

        self.spinBox_2_2 = QSpinBox(self.groupBox_dados_teste_2)
        self.spinBox_2_2.setObjectName(u"spinBox_2_2")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.spinBox_2_2)


        self.verticalLayout_3_2.addWidget(self.groupBox_dados_teste_2)

        self.verticalSpacer_4_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3_2.addItem(self.verticalSpacer_4_2)

        self.stackedWidget_formularios.addWidget(self.page_form_teste2)
        self.page_form_teste3 = QWidget()
        self.page_form_teste3.setObjectName(u"page_form_teste3")
        self.verticalLayout_3_3 = QVBoxLayout(self.page_form_teste3)
        self.verticalLayout_3_3.setObjectName(u"verticalLayout_3_3")
        self.label_titulo_teste3 = QLabel(self.page_form_teste3)
        self.label_titulo_teste3.setObjectName(u"label_titulo_teste3")
        self.label_titulo_teste3.setFont(font1)

        self.verticalLayout_3_3.addWidget(self.label_titulo_teste3)

        self.groupBox_faixa_etaria_3 = QGroupBox(self.page_form_teste3)
        self.groupBox_faixa_etaria_3.setObjectName(u"groupBox_faixa_etaria_3")
        self.horizontalLayout_3_3 = QHBoxLayout(self.groupBox_faixa_etaria_3)
        self.horizontalLayout_3_3.setObjectName(u"horizontalLayout_3_3")
        self.radioButton_pre_escolar_3 = QRadioButton(self.groupBox_faixa_etaria_3)
        self.radioButton_pre_escolar_3.setObjectName(u"radioButton_pre_escolar_3")

        self.horizontalLayout_3_3.addWidget(self.radioButton_pre_escolar_3)

        self.radioButton_escolar_3 = QRadioButton(self.groupBox_faixa_etaria_3)
        self.radioButton_escolar_3.setObjectName(u"radioButton_escolar_3")
        self.radioButton_escolar_3.setChecked(True)

        self.horizontalLayout_3_3.addWidget(self.radioButton_escolar_3)

        self.radioButton_adulto_3 = QRadioButton(self.groupBox_faixa_etaria_3)
        self.radioButton_adulto_3.setObjectName(u"radioButton_adulto_3")

        self.horizontalLayout_3_3.addWidget(self.radioButton_adulto_3)


        self.verticalLayout_3_3.addWidget(self.groupBox_faixa_etaria_3)

        self.groupBox_dados_teste_3 = QGroupBox(self.page_form_teste3)
        self.groupBox_dados_teste_3.setObjectName(u"groupBox_dados_teste_3")
        self.formLayout_3 = QFormLayout(self.groupBox_dados_teste_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_2_3 = QLabel(self.groupBox_dados_teste_3)
        self.label_2_3.setObjectName(u"label_2_3")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_2_3)

        self.spinBox_4 = QSpinBox(self.groupBox_dados_teste_3)
        self.spinBox_4.setObjectName(u"spinBox_4")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.spinBox_4)

        self.label_3_3 = QLabel(self.groupBox_dados_teste_3)
        self.label_3_3.setObjectName(u"label_3_3")

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_3_3)

        self.spinBox_2_3 = QSpinBox(self.groupBox_dados_teste_3)
        self.spinBox_2_3.setObjectName(u"spinBox_2_3")

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.FieldRole, self.spinBox_2_3)


        self.verticalLayout_3_3.addWidget(self.groupBox_dados_teste_3)

        self.verticalSpacer_4_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3_3.addItem(self.verticalSpacer_4_3)

        self.stackedWidget_formularios.addWidget(self.page_form_teste3)
        self.page_form_teste4 = QWidget()
        self.page_form_teste4.setObjectName(u"page_form_teste4")
        self.verticalLayout_3_4 = QVBoxLayout(self.page_form_teste4)
        self.verticalLayout_3_4.setObjectName(u"verticalLayout_3_4")
        self.label_titulo_teste4 = QLabel(self.page_form_teste4)
        self.label_titulo_teste4.setObjectName(u"label_titulo_teste4")
        self.label_titulo_teste4.setFont(font1)

        self.verticalLayout_3_4.addWidget(self.label_titulo_teste4)

        self.groupBox_faixa_etaria_4 = QGroupBox(self.page_form_teste4)
        self.groupBox_faixa_etaria_4.setObjectName(u"groupBox_faixa_etaria_4")
        self.horizontalLayout_3_4 = QHBoxLayout(self.groupBox_faixa_etaria_4)
        self.horizontalLayout_3_4.setObjectName(u"horizontalLayout_3_4")
        self.radioButton_pre_escolar_4 = QRadioButton(self.groupBox_faixa_etaria_4)
        self.radioButton_pre_escolar_4.setObjectName(u"radioButton_pre_escolar_4")

        self.horizontalLayout_3_4.addWidget(self.radioButton_pre_escolar_4)

        self.radioButton_escolar_4 = QRadioButton(self.groupBox_faixa_etaria_4)
        self.radioButton_escolar_4.setObjectName(u"radioButton_escolar_4")
        self.radioButton_escolar_4.setChecked(True)

        self.horizontalLayout_3_4.addWidget(self.radioButton_escolar_4)

        self.radioButton_adulto_4 = QRadioButton(self.groupBox_faixa_etaria_4)
        self.radioButton_adulto_4.setObjectName(u"radioButton_adulto_4")

        self.horizontalLayout_3_4.addWidget(self.radioButton_adulto_4)


        self.verticalLayout_3_4.addWidget(self.groupBox_faixa_etaria_4)

        self.groupBox_dados_teste_4 = QGroupBox(self.page_form_teste4)
        self.groupBox_dados_teste_4.setObjectName(u"groupBox_dados_teste_4")
        self.formLayout_4 = QFormLayout(self.groupBox_dados_teste_4)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_2_4 = QLabel(self.groupBox_dados_teste_4)
        self.label_2_4.setObjectName(u"label_2_4")

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_2_4)

        self.spinBox_5 = QSpinBox(self.groupBox_dados_teste_4)
        self.spinBox_5.setObjectName(u"spinBox_5")

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.FieldRole, self.spinBox_5)

        self.label_3_4 = QLabel(self.groupBox_dados_teste_4)
        self.label_3_4.setObjectName(u"label_3_4")

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_3_4)

        self.spinBox_2_4 = QSpinBox(self.groupBox_dados_teste_4)
        self.spinBox_2_4.setObjectName(u"spinBox_2_4")

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.FieldRole, self.spinBox_2_4)


        self.verticalLayout_3_4.addWidget(self.groupBox_dados_teste_4)

        self.verticalSpacer_4_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3_4.addItem(self.verticalSpacer_4_4)

        self.stackedWidget_formularios.addWidget(self.page_form_teste4)
        self.page_form_teste5 = QWidget()
        self.page_form_teste5.setObjectName(u"page_form_teste5")
        self.verticalLayout_3_5 = QVBoxLayout(self.page_form_teste5)
        self.verticalLayout_3_5.setObjectName(u"verticalLayout_3_5")
        self.label_titulo_teste5 = QLabel(self.page_form_teste5)
        self.label_titulo_teste5.setObjectName(u"label_titulo_teste5")
        self.label_titulo_teste5.setFont(font1)

        self.verticalLayout_3_5.addWidget(self.label_titulo_teste5)

        self.groupBox_faixa_etaria_5 = QGroupBox(self.page_form_teste5)
        self.groupBox_faixa_etaria_5.setObjectName(u"groupBox_faixa_etaria_5")
        self.horizontalLayout_3_5 = QHBoxLayout(self.groupBox_faixa_etaria_5)
        self.horizontalLayout_3_5.setObjectName(u"horizontalLayout_3_5")
        self.radioButton_pre_escolar_5 = QRadioButton(self.groupBox_faixa_etaria_5)
        self.radioButton_pre_escolar_5.setObjectName(u"radioButton_pre_escolar_5")

        self.horizontalLayout_3_5.addWidget(self.radioButton_pre_escolar_5)

        self.radioButton_escolar_5 = QRadioButton(self.groupBox_faixa_etaria_5)
        self.radioButton_escolar_5.setObjectName(u"radioButton_escolar_5")
        self.radioButton_escolar_5.setChecked(True)

        self.horizontalLayout_3_5.addWidget(self.radioButton_escolar_5)

        self.radioButton_adulto_5 = QRadioButton(self.groupBox_faixa_etaria_5)
        self.radioButton_adulto_5.setObjectName(u"radioButton_adulto_5")

        self.horizontalLayout_3_5.addWidget(self.radioButton_adulto_5)


        self.verticalLayout_3_5.addWidget(self.groupBox_faixa_etaria_5)

        self.groupBox_dados_teste_5 = QGroupBox(self.page_form_teste5)
        self.groupBox_dados_teste_5.setObjectName(u"groupBox_dados_teste_5")
        self.formLayout_5 = QFormLayout(self.groupBox_dados_teste_5)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_2_5 = QLabel(self.groupBox_dados_teste_5)
        self.label_2_5.setObjectName(u"label_2_5")

        self.formLayout_5.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_2_5)

        self.spinBox_6 = QSpinBox(self.groupBox_dados_teste_5)
        self.spinBox_6.setObjectName(u"spinBox_6")

        self.formLayout_5.setWidget(0, QFormLayout.ItemRole.FieldRole, self.spinBox_6)

        self.label_3_5 = QLabel(self.groupBox_dados_teste_5)
        self.label_3_5.setObjectName(u"label_3_5")

        self.formLayout_5.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_3_5)

        self.spinBox_2_5 = QSpinBox(self.groupBox_dados_teste_5)
        self.spinBox_2_5.setObjectName(u"spinBox_2_5")

        self.formLayout_5.setWidget(1, QFormLayout.ItemRole.FieldRole, self.spinBox_2_5)


        self.verticalLayout_3_5.addWidget(self.groupBox_dados_teste_5)

        self.verticalSpacer_4_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3_5.addItem(self.verticalSpacer_4_5)

        self.stackedWidget_formularios.addWidget(self.page_form_teste5)
        self.page_form_teste6 = QWidget()
        self.page_form_teste6.setObjectName(u"page_form_teste6")
        self.verticalLayout_3_6 = QVBoxLayout(self.page_form_teste6)
        self.verticalLayout_3_6.setObjectName(u"verticalLayout_3_6")
        self.label_titulo_teste6 = QLabel(self.page_form_teste6)
        self.label_titulo_teste6.setObjectName(u"label_titulo_teste6")
        self.label_titulo_teste6.setFont(font1)

        self.verticalLayout_3_6.addWidget(self.label_titulo_teste6)

        self.groupBox_faixa_etaria_6 = QGroupBox(self.page_form_teste6)
        self.groupBox_faixa_etaria_6.setObjectName(u"groupBox_faixa_etaria_6")
        self.horizontalLayout_3_6 = QHBoxLayout(self.groupBox_faixa_etaria_6)
        self.horizontalLayout_3_6.setObjectName(u"horizontalLayout_3_6")
        self.radioButton_pre_escolar_6 = QRadioButton(self.groupBox_faixa_etaria_6)
        self.radioButton_pre_escolar_6.setObjectName(u"radioButton_pre_escolar_6")

        self.horizontalLayout_3_6.addWidget(self.radioButton_pre_escolar_6)

        self.radioButton_escolar_6 = QRadioButton(self.groupBox_faixa_etaria_6)
        self.radioButton_escolar_6.setObjectName(u"radioButton_escolar_6")
        self.radioButton_escolar_6.setChecked(True)

        self.horizontalLayout_3_6.addWidget(self.radioButton_escolar_6)

        self.radioButton_adulto_6 = QRadioButton(self.groupBox_faixa_etaria_6)
        self.radioButton_adulto_6.setObjectName(u"radioButton_adulto_6")

        self.horizontalLayout_3_6.addWidget(self.radioButton_adulto_6)


        self.verticalLayout_3_6.addWidget(self.groupBox_faixa_etaria_6)

        self.groupBox_dados_teste_6 = QGroupBox(self.page_form_teste6)
        self.groupBox_dados_teste_6.setObjectName(u"groupBox_dados_teste_6")
        self.formLayout_6 = QFormLayout(self.groupBox_dados_teste_6)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.label_2_6 = QLabel(self.groupBox_dados_teste_6)
        self.label_2_6.setObjectName(u"label_2_6")

        self.formLayout_6.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_2_6)

        self.spinBox_7 = QSpinBox(self.groupBox_dados_teste_6)
        self.spinBox_7.setObjectName(u"spinBox_7")

        self.formLayout_6.setWidget(0, QFormLayout.ItemRole.FieldRole, self.spinBox_7)

        self.label_3_6 = QLabel(self.groupBox_dados_teste_6)
        self.label_3_6.setObjectName(u"label_3_6")

        self.formLayout_6.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_3_6)

        self.spinBox_2_6 = QSpinBox(self.groupBox_dados_teste_6)
        self.spinBox_2_6.setObjectName(u"spinBox_2_6")

        self.formLayout_6.setWidget(1, QFormLayout.ItemRole.FieldRole, self.spinBox_2_6)


        self.verticalLayout_3_6.addWidget(self.groupBox_dados_teste_6)

        self.verticalSpacer_4_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3_6.addItem(self.verticalSpacer_4_6)

        self.stackedWidget_formularios.addWidget(self.page_form_teste6)
        self.page_form_teste7 = QWidget()
        self.page_form_teste7.setObjectName(u"page_form_teste7")
        self.verticalLayout_3_7 = QVBoxLayout(self.page_form_teste7)
        self.verticalLayout_3_7.setObjectName(u"verticalLayout_3_7")
        self.label_titulo_teste7 = QLabel(self.page_form_teste7)
        self.label_titulo_teste7.setObjectName(u"label_titulo_teste7")
        self.label_titulo_teste7.setFont(font1)

        self.verticalLayout_3_7.addWidget(self.label_titulo_teste7)

        self.groupBox_faixa_etaria_7 = QGroupBox(self.page_form_teste7)
        self.groupBox_faixa_etaria_7.setObjectName(u"groupBox_faixa_etaria_7")
        self.horizontalLayout_3_7 = QHBoxLayout(self.groupBox_faixa_etaria_7)
        self.horizontalLayout_3_7.setObjectName(u"horizontalLayout_3_7")
        self.radioButton_pre_escolar_7 = QRadioButton(self.groupBox_faixa_etaria_7)
        self.radioButton_pre_escolar_7.setObjectName(u"radioButton_pre_escolar_7")

        self.horizontalLayout_3_7.addWidget(self.radioButton_pre_escolar_7)

        self.radioButton_escolar_7 = QRadioButton(self.groupBox_faixa_etaria_7)
        self.radioButton_escolar_7.setObjectName(u"radioButton_escolar_7")
        self.radioButton_escolar_7.setChecked(True)

        self.horizontalLayout_3_7.addWidget(self.radioButton_escolar_7)

        self.radioButton_adulto_7 = QRadioButton(self.groupBox_faixa_etaria_7)
        self.radioButton_adulto_7.setObjectName(u"radioButton_adulto_7")

        self.horizontalLayout_3_7.addWidget(self.radioButton_adulto_7)


        self.verticalLayout_3_7.addWidget(self.groupBox_faixa_etaria_7)

        self.groupBox_dados_teste_7 = QGroupBox(self.page_form_teste7)
        self.groupBox_dados_teste_7.setObjectName(u"groupBox_dados_teste_7")
        self.formLayout_7 = QFormLayout(self.groupBox_dados_teste_7)
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.label_2_7 = QLabel(self.groupBox_dados_teste_7)
        self.label_2_7.setObjectName(u"label_2_7")

        self.formLayout_7.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_2_7)

        self.spinBox_8 = QSpinBox(self.groupBox_dados_teste_7)
        self.spinBox_8.setObjectName(u"spinBox_8")

        self.formLayout_7.setWidget(0, QFormLayout.ItemRole.FieldRole, self.spinBox_8)

        self.label_3_7 = QLabel(self.groupBox_dados_teste_7)
        self.label_3_7.setObjectName(u"label_3_7")

        self.formLayout_7.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_3_7)

        self.spinBox_2_7 = QSpinBox(self.groupBox_dados_teste_7)
        self.spinBox_2_7.setObjectName(u"spinBox_2_7")

        self.formLayout_7.setWidget(1, QFormLayout.ItemRole.FieldRole, self.spinBox_2_7)


        self.verticalLayout_3_7.addWidget(self.groupBox_dados_teste_7)

        self.verticalSpacer_4_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3_7.addItem(self.verticalSpacer_4_7)

        self.stackedWidget_formularios.addWidget(self.page_form_teste7)
        self.page_form_teste8 = QWidget()
        self.page_form_teste8.setObjectName(u"page_form_teste8")
        self.verticalLayout_3_8 = QVBoxLayout(self.page_form_teste8)
        self.verticalLayout_3_8.setObjectName(u"verticalLayout_3_8")
        self.label_titulo_teste8 = QLabel(self.page_form_teste8)
        self.label_titulo_teste8.setObjectName(u"label_titulo_teste8")
        self.label_titulo_teste8.setFont(font1)

        self.verticalLayout_3_8.addWidget(self.label_titulo_teste8)

        self.groupBox_faixa_etaria_8 = QGroupBox(self.page_form_teste8)
        self.groupBox_faixa_etaria_8.setObjectName(u"groupBox_faixa_etaria_8")
        self.horizontalLayout_3_8 = QHBoxLayout(self.groupBox_faixa_etaria_8)
        self.horizontalLayout_3_8.setObjectName(u"horizontalLayout_3_8")
        self.radioButton_pre_escolar_8 = QRadioButton(self.groupBox_faixa_etaria_8)
        self.radioButton_pre_escolar_8.setObjectName(u"radioButton_pre_escolar_8")

        self.horizontalLayout_3_8.addWidget(self.radioButton_pre_escolar_8)

        self.radioButton_escolar_8 = QRadioButton(self.groupBox_faixa_etaria_8)
        self.radioButton_escolar_8.setObjectName(u"radioButton_escolar_8")
        self.radioButton_escolar_8.setChecked(True)

        self.horizontalLayout_3_8.addWidget(self.radioButton_escolar_8)

        self.radioButton_adulto_8 = QRadioButton(self.groupBox_faixa_etaria_8)
        self.radioButton_adulto_8.setObjectName(u"radioButton_adulto_8")

        self.horizontalLayout_3_8.addWidget(self.radioButton_adulto_8)


        self.verticalLayout_3_8.addWidget(self.groupBox_faixa_etaria_8)

        self.groupBox_dados_teste_8 = QGroupBox(self.page_form_teste8)
        self.groupBox_dados_teste_8.setObjectName(u"groupBox_dados_teste_8")
        self.formLayout_8 = QFormLayout(self.groupBox_dados_teste_8)
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.label_2_8 = QLabel(self.groupBox_dados_teste_8)
        self.label_2_8.setObjectName(u"label_2_8")

        self.formLayout_8.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_2_8)

        self.spinBox_9 = QSpinBox(self.groupBox_dados_teste_8)
        self.spinBox_9.setObjectName(u"spinBox_9")

        self.formLayout_8.setWidget(0, QFormLayout.ItemRole.FieldRole, self.spinBox_9)

        self.label_3_8 = QLabel(self.groupBox_dados_teste_8)
        self.label_3_8.setObjectName(u"label_3_8")

        self.formLayout_8.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_3_8)

        self.spinBox_2_8 = QSpinBox(self.groupBox_dados_teste_8)
        self.spinBox_2_8.setObjectName(u"spinBox_2_8")

        self.formLayout_8.setWidget(1, QFormLayout.ItemRole.FieldRole, self.spinBox_2_8)


        self.verticalLayout_3_8.addWidget(self.groupBox_dados_teste_8)

        self.verticalSpacer_4_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3_8.addItem(self.verticalSpacer_4_8)

        self.stackedWidget_formularios.addWidget(self.page_form_teste8)
        self.page_form_teste9 = QWidget()
        self.page_form_teste9.setObjectName(u"page_form_teste9")
        self.verticalLayout_3_9 = QVBoxLayout(self.page_form_teste9)
        self.verticalLayout_3_9.setObjectName(u"verticalLayout_3_9")
        self.label_titulo_teste9 = QLabel(self.page_form_teste9)
        self.label_titulo_teste9.setObjectName(u"label_titulo_teste9")
        self.label_titulo_teste9.setFont(font1)

        self.verticalLayout_3_9.addWidget(self.label_titulo_teste9)

        self.groupBox_faixa_etaria_9 = QGroupBox(self.page_form_teste9)
        self.groupBox_faixa_etaria_9.setObjectName(u"groupBox_faixa_etaria_9")
        self.horizontalLayout_3_9 = QHBoxLayout(self.groupBox_faixa_etaria_9)
        self.horizontalLayout_3_9.setObjectName(u"horizontalLayout_3_9")
        self.radioButton_pre_escolar_9 = QRadioButton(self.groupBox_faixa_etaria_9)
        self.radioButton_pre_escolar_9.setObjectName(u"radioButton_pre_escolar_9")

        self.horizontalLayout_3_9.addWidget(self.radioButton_pre_escolar_9)

        self.radioButton_escolar_9 = QRadioButton(self.groupBox_faixa_etaria_9)
        self.radioButton_escolar_9.setObjectName(u"radioButton_escolar_9")
        self.radioButton_escolar_9.setChecked(True)

        self.horizontalLayout_3_9.addWidget(self.radioButton_escolar_9)

        self.radioButton_adulto_9 = QRadioButton(self.groupBox_faixa_etaria_9)
        self.radioButton_adulto_9.setObjectName(u"radioButton_adulto_9")

        self.horizontalLayout_3_9.addWidget(self.radioButton_adulto_9)


        self.verticalLayout_3_9.addWidget(self.groupBox_faixa_etaria_9)

        self.groupBox_dados_teste_9 = QGroupBox(self.page_form_teste9)
        self.groupBox_dados_teste_9.setObjectName(u"groupBox_dados_teste_9")
        self.formLayout_9 = QFormLayout(self.groupBox_dados_teste_9)
        self.formLayout_9.setObjectName(u"formLayout_9")
        self.label_2_9 = QLabel(self.groupBox_dados_teste_9)
        self.label_2_9.setObjectName(u"label_2_9")

        self.formLayout_9.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_2_9)

        self.spinBox_10 = QSpinBox(self.groupBox_dados_teste_9)
        self.spinBox_10.setObjectName(u"spinBox_10")

        self.formLayout_9.setWidget(0, QFormLayout.ItemRole.FieldRole, self.spinBox_10)

        self.label_3_9 = QLabel(self.groupBox_dados_teste_9)
        self.label_3_9.setObjectName(u"label_3_9")

        self.formLayout_9.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_3_9)

        self.spinBox_2_9 = QSpinBox(self.groupBox_dados_teste_9)
        self.spinBox_2_9.setObjectName(u"spinBox_2_9")

        self.formLayout_9.setWidget(1, QFormLayout.ItemRole.FieldRole, self.spinBox_2_9)


        self.verticalLayout_3_9.addWidget(self.groupBox_dados_teste_9)

        self.verticalSpacer_4_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3_9.addItem(self.verticalSpacer_4_9)

        self.stackedWidget_formularios.addWidget(self.page_form_teste9)

        self.horizontalLayout_2.addWidget(self.stackedWidget_formularios)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_voltar = QPushButton(TelaTestes)
        self.btn_voltar.setObjectName(u"btn_voltar")

        self.horizontalLayout.addWidget(self.btn_voltar)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_avancar = QPushButton(TelaTestes)
        self.btn_avancar.setObjectName(u"btn_avancar")

        self.horizontalLayout.addWidget(self.btn_avancar)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(TelaTestes)

        self.stackedWidget_formularios.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TelaTestes)
    # setupUi

    def retranslateUi(self, TelaTestes):
        TelaTestes.setWindowTitle(QCoreApplication.translate("TelaTestes", u"Form", None))
        self.label_titulo.setText(QCoreApplication.translate("TelaTestes", u"Passo 3: Inserir Dados dos Testes", None))
        self.groupBox_botoes.setTitle(QCoreApplication.translate("TelaTestes", u"Testes", None))
        self.btn_teste1.setText(QCoreApplication.translate("TelaTestes", u"Teste 1", None))
        self.btn_teste2.setText(QCoreApplication.translate("TelaTestes", u"Teste 2", None))
        self.btn_teste3.setText(QCoreApplication.translate("TelaTestes", u"Teste 3", None))
        self.btn_teste4.setText(QCoreApplication.translate("TelaTestes", u"Teste 4", None))
        self.btn_teste5.setText(QCoreApplication.translate("TelaTestes", u"Teste 5", None))
        self.btn_teste6.setText(QCoreApplication.translate("TelaTestes", u"Teste 6", None))
        self.btn_teste7.setText(QCoreApplication.translate("TelaTestes", u"Teste 7", None))
        self.btn_teste8.setText(QCoreApplication.translate("TelaTestes", u"Teste 8", None))
        self.btn_teste9.setText(QCoreApplication.translate("TelaTestes", u"Teste 9", None))
        self.label.setText(QCoreApplication.translate("TelaTestes", u"Selecione um teste \u00e0 esquerda para preencher os dados.", None))
        self.label_titulo_teste1.setText(QCoreApplication.translate("TelaTestes", u"Formul\u00e1rio - Teste 1", None))
        self.groupBox_faixa_etaria.setTitle(QCoreApplication.translate("TelaTestes", u"Faixa Et\u00e1ria", None))
        self.radioButton_pre_escolar.setText(QCoreApplication.translate("TelaTestes", u"Pr\u00e9-escolar", None))
        self.radioButton_escolar.setText(QCoreApplication.translate("TelaTestes", u"Escolar", None))
        self.radioButton_adulto.setText(QCoreApplication.translate("TelaTestes", u"Adulto", None))
        self.groupBox_dados_teste.setTitle(QCoreApplication.translate("TelaTestes", u"Dados do Teste", None))
        self.label_2.setText(QCoreApplication.translate("TelaTestes", u"Escore Bruto:", None))
        self.label_3.setText(QCoreApplication.translate("TelaTestes", u"Percentil:", None))
        self.label_titulo_teste2.setText(QCoreApplication.translate("TelaTestes", u"Formul\u00e1rio - Teste 2", None))
        self.groupBox_faixa_etaria_2.setTitle(QCoreApplication.translate("TelaTestes", u"Faixa Et\u00e1ria", None))
        self.radioButton_pre_escolar_2.setText(QCoreApplication.translate("TelaTestes", u"Pr\u00e9-escolar", None))
        self.radioButton_escolar_2.setText(QCoreApplication.translate("TelaTestes", u"Escolar", None))
        self.radioButton_adulto_2.setText(QCoreApplication.translate("TelaTestes", u"Adulto", None))
        self.groupBox_dados_teste_2.setTitle(QCoreApplication.translate("TelaTestes", u"Dados do Teste", None))
        self.label_2_2.setText(QCoreApplication.translate("TelaTestes", u"Escore Bruto:", None))
        self.label_3_2.setText(QCoreApplication.translate("TelaTestes", u"Percentil:", None))
        self.label_titulo_teste3.setText(QCoreApplication.translate("TelaTestes", u"Formul\u00e1rio - Teste 3", None))
        self.groupBox_faixa_etaria_3.setTitle(QCoreApplication.translate("TelaTestes", u"Faixa Et\u00e1ria", None))
        self.radioButton_pre_escolar_3.setText(QCoreApplication.translate("TelaTestes", u"Pr\u00e9-escolar", None))
        self.radioButton_escolar_3.setText(QCoreApplication.translate("TelaTestes", u"Escolar", None))
        self.radioButton_adulto_3.setText(QCoreApplication.translate("TelaTestes", u"Adulto", None))
        self.groupBox_dados_teste_3.setTitle(QCoreApplication.translate("TelaTestes", u"Dados do Teste", None))
        self.label_2_3.setText(QCoreApplication.translate("TelaTestes", u"Escore Bruto:", None))
        self.label_3_3.setText(QCoreApplication.translate("TelaTestes", u"Percentil:", None))
        self.label_titulo_teste4.setText(QCoreApplication.translate("TelaTestes", u"Formul\u00e1rio - Teste 4", None))
        self.groupBox_faixa_etaria_4.setTitle(QCoreApplication.translate("TelaTestes", u"Faixa Et\u00e1ria", None))
        self.radioButton_pre_escolar_4.setText(QCoreApplication.translate("TelaTestes", u"Pr\u00e9-escolar", None))
        self.radioButton_escolar_4.setText(QCoreApplication.translate("TelaTestes", u"Escolar", None))
        self.radioButton_adulto_4.setText(QCoreApplication.translate("TelaTestes", u"Adulto", None))
        self.groupBox_dados_teste_4.setTitle(QCoreApplication.translate("TelaTestes", u"Dados do Teste", None))
        self.label_2_4.setText(QCoreApplication.translate("TelaTestes", u"Escore Bruto:", None))
        self.label_3_4.setText(QCoreApplication.translate("TelaTestes", u"Percentil:", None))
        self.label_titulo_teste5.setText(QCoreApplication.translate("TelaTestes", u"Formul\u00e1rio - Teste 5", None))
        self.groupBox_faixa_etaria_5.setTitle(QCoreApplication.translate("TelaTestes", u"Faixa Et\u00e1ria", None))
        self.radioButton_pre_escolar_5.setText(QCoreApplication.translate("TelaTestes", u"Pr\u00e9-escolar", None))
        self.radioButton_escolar_5.setText(QCoreApplication.translate("TelaTestes", u"Escolar", None))
        self.radioButton_adulto_5.setText(QCoreApplication.translate("TelaTestes", u"Adulto", None))
        self.groupBox_dados_teste_5.setTitle(QCoreApplication.translate("TelaTestes", u"Dados do Teste", None))
        self.label_2_5.setText(QCoreApplication.translate("TelaTestes", u"Escore Bruto:", None))
        self.label_3_5.setText(QCoreApplication.translate("TelaTestes", u"Percentil:", None))
        self.label_titulo_teste6.setText(QCoreApplication.translate("TelaTestes", u"Formul\u00e1rio - Teste 6", None))
        self.groupBox_faixa_etaria_6.setTitle(QCoreApplication.translate("TelaTestes", u"Faixa Et\u00e1ria", None))
        self.radioButton_pre_escolar_6.setText(QCoreApplication.translate("TelaTestes", u"Pr\u00e9-escolar", None))
        self.radioButton_escolar_6.setText(QCoreApplication.translate("TelaTestes", u"Escolar", None))
        self.radioButton_adulto_6.setText(QCoreApplication.translate("TelaTestes", u"Adulto", None))
        self.groupBox_dados_teste_6.setTitle(QCoreApplication.translate("TelaTestes", u"Dados do Teste", None))
        self.label_2_6.setText(QCoreApplication.translate("TelaTestes", u"Escore Bruto:", None))
        self.label_3_6.setText(QCoreApplication.translate("TelaTestes", u"Percentil:", None))
        self.label_titulo_teste7.setText(QCoreApplication.translate("TelaTestes", u"Formul\u00e1rio - Teste 7", None))
        self.groupBox_faixa_etaria_7.setTitle(QCoreApplication.translate("TelaTestes", u"Faixa Et\u00e1ria", None))
        self.radioButton_pre_escolar_7.setText(QCoreApplication.translate("TelaTestes", u"Pr\u00e9-escolar", None))
        self.radioButton_escolar_7.setText(QCoreApplication.translate("TelaTestes", u"Escolar", None))
        self.radioButton_adulto_7.setText(QCoreApplication.translate("TelaTestes", u"Adulto", None))
        self.groupBox_dados_teste_7.setTitle(QCoreApplication.translate("TelaTestes", u"Dados do Teste", None))
        self.label_2_7.setText(QCoreApplication.translate("TelaTestes", u"Escore Bruto:", None))
        self.label_3_7.setText(QCoreApplication.translate("TelaTestes", u"Percentil:", None))
        self.label_titulo_teste8.setText(QCoreApplication.translate("TelaTestes", u"Formul\u00e1rio - Teste 8", None))
        self.groupBox_faixa_etaria_8.setTitle(QCoreApplication.translate("TelaTestes", u"Faixa Et\u00e1ria", None))
        self.radioButton_pre_escolar_8.setText(QCoreApplication.translate("TelaTestes", u"Pr\u00e9-escolar", None))
        self.radioButton_escolar_8.setText(QCoreApplication.translate("TelaTestes", u"Escolar", None))
        self.radioButton_adulto_8.setText(QCoreApplication.translate("TelaTestes", u"Adulto", None))
        self.groupBox_dados_teste_8.setTitle(QCoreApplication.translate("TelaTestes", u"Dados do Teste", None))
        self.label_2_8.setText(QCoreApplication.translate("TelaTestes", u"Escore Bruto:", None))
        self.label_3_8.setText(QCoreApplication.translate("TelaTestes", u"Percentil:", None))
        self.label_titulo_teste9.setText(QCoreApplication.translate("TelaTestes", u"Formul\u00e1rio - Teste 9", None))
        self.groupBox_faixa_etaria_9.setTitle(QCoreApplication.translate("TelaTestes", u"Faixa Et\u00e1ria", None))
        self.radioButton_pre_escolar_9.setText(QCoreApplication.translate("TelaTestes", u"Pr\u00e9-escolar", None))
        self.radioButton_escolar_9.setText(QCoreApplication.translate("TelaTestes", u"Escolar", None))
        self.radioButton_adulto_9.setText(QCoreApplication.translate("TelaTestes", u"Adulto", None))
        self.groupBox_dados_teste_9.setTitle(QCoreApplication.translate("TelaTestes", u"Dados do Teste", None))
        self.label_2_9.setText(QCoreApplication.translate("TelaTestes", u"Escore Bruto:", None))
        self.label_3_9.setText(QCoreApplication.translate("TelaTestes", u"Percentil:", None))
        self.btn_voltar.setText(QCoreApplication.translate("TelaTestes", u"Voltar", None))
        self.btn_avancar.setText(QCoreApplication.translate("TelaTestes", u"Avan\u00e7ar", None))
    # retranslateUi

