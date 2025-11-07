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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QGroupBox,
    QHBoxLayout, QLabel, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QStackedWidget, QVBoxLayout, QWidget)

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
        self.label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_titulo)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox_botoes = QGroupBox(TelaTestes)
        self.groupBox_botoes.setObjectName(u"groupBox_botoes")
        self.verticalLayout = QVBoxLayout(self.groupBox_botoes)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_wisc4 = QPushButton(self.groupBox_botoes)
        self.btn_wisc4.setObjectName(u"btn_wisc4")

        self.verticalLayout.addWidget(self.btn_wisc4)

        self.btn_ravlt = QPushButton(self.groupBox_botoes)
        self.btn_ravlt.setObjectName(u"btn_ravlt")

        self.verticalLayout.addWidget(self.btn_ravlt)

        self.btn_bpa2 = QPushButton(self.groupBox_botoes)
        self.btn_bpa2.setObjectName(u"btn_bpa2")

        self.verticalLayout.addWidget(self.btn_bpa2)

        self.btn_neupsilin = QPushButton(self.groupBox_botoes)
        self.btn_neupsilin.setObjectName(u"btn_neupsilin")

        self.verticalLayout.addWidget(self.btn_neupsilin)

        self.btn_srs2 = QPushButton(self.groupBox_botoes)
        self.btn_srs2.setObjectName(u"btn_srs2")

        self.verticalLayout.addWidget(self.btn_srs2)

        self.btn_etdah = QPushButton(self.groupBox_botoes)
        self.btn_etdah.setObjectName(u"btn_etdah")

        self.verticalLayout.addWidget(self.btn_etdah)

        self.btn_cars2 = QPushButton(self.groupBox_botoes)
        self.btn_cars2.setObjectName(u"btn_cars2")

        self.verticalLayout.addWidget(self.btn_cars2)

        self.btn_htp = QPushButton(self.groupBox_botoes)
        self.btn_htp.setObjectName(u"btn_htp")

        self.verticalLayout.addWidget(self.btn_htp)

        self.btn_fdt = QPushButton(self.groupBox_botoes)
        self.btn_fdt.setObjectName(u"btn_fdt")

        self.verticalLayout.addWidget(self.btn_fdt)

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
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label)

        self.verticalSpacer_3 = QSpacerItem(20, 127, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.stackedWidget_formularios.addWidget(self.page_inicial)
        self.page_form_wisc4 = QWidget()
        self.page_form_wisc4.setObjectName(u"page_form_wisc4")
        self.verticalLayout_wisc4 = QVBoxLayout(self.page_form_wisc4)
        self.verticalLayout_wisc4.setObjectName(u"verticalLayout_wisc4")
        self.label_titulo_wisc4 = QLabel(self.page_form_wisc4)
        self.label_titulo_wisc4.setObjectName(u"label_titulo_wisc4")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_titulo_wisc4.setFont(font1)

        self.verticalLayout_wisc4.addWidget(self.label_titulo_wisc4)

        self.groupBox_faixa_etaria_wisc4 = QGroupBox(self.page_form_wisc4)
        self.groupBox_faixa_etaria_wisc4.setObjectName(u"groupBox_faixa_etaria_wisc4")
        self.horizontalLayout_wisc4 = QHBoxLayout(self.groupBox_faixa_etaria_wisc4)
        self.horizontalLayout_wisc4.setObjectName(u"horizontalLayout_wisc4")
        self.checkBox_incluir_wisc4 = QCheckBox(self.groupBox_faixa_etaria_wisc4)
        self.checkBox_incluir_wisc4.setObjectName(u"checkBox_incluir_wisc4")

        self.horizontalLayout_wisc4.addWidget(self.checkBox_incluir_wisc4)

        self.radioButton_pre_escolar_wisc4 = QRadioButton(self.groupBox_faixa_etaria_wisc4)
        self.radioButton_pre_escolar_wisc4.setObjectName(u"radioButton_pre_escolar_wisc4")

        self.horizontalLayout_wisc4.addWidget(self.radioButton_pre_escolar_wisc4)

        self.radioButton_escolar_wisc4 = QRadioButton(self.groupBox_faixa_etaria_wisc4)
        self.radioButton_escolar_wisc4.setObjectName(u"radioButton_escolar_wisc4")
        self.radioButton_escolar_wisc4.setChecked(True)

        self.horizontalLayout_wisc4.addWidget(self.radioButton_escolar_wisc4)

        self.radioButton_adulto_wisc4 = QRadioButton(self.groupBox_faixa_etaria_wisc4)
        self.radioButton_adulto_wisc4.setObjectName(u"radioButton_adulto_wisc4")

        self.horizontalLayout_wisc4.addWidget(self.radioButton_adulto_wisc4)


        self.verticalLayout_wisc4.addWidget(self.groupBox_faixa_etaria_wisc4)

        self.scrollArea = QScrollArea(self.page_form_wisc4)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 584, 446))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_dados_teste_wisc4 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_dados_teste_wisc4.setObjectName(u"groupBox_dados_teste_wisc4")
        self.groupBox_dados_teste_wisc4.setMouseTracking(False)
        self.formLayout_wisc4 = QFormLayout(self.groupBox_dados_teste_wisc4)
        self.formLayout_wisc4.setObjectName(u"formLayout_wisc4")
        self.label_icv_wisc4 = QLabel(self.groupBox_dados_teste_wisc4)
        self.label_icv_wisc4.setObjectName(u"label_icv_wisc4")

        self.formLayout_wisc4.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_icv_wisc4)

        self.spinBox_icv_wisc4 = QSpinBox(self.groupBox_dados_teste_wisc4)
        self.spinBox_icv_wisc4.setObjectName(u"spinBox_icv_wisc4")

        self.formLayout_wisc4.setWidget(0, QFormLayout.ItemRole.FieldRole, self.spinBox_icv_wisc4)

        self.label_iop_wisc4 = QLabel(self.groupBox_dados_teste_wisc4)
        self.label_iop_wisc4.setObjectName(u"label_iop_wisc4")

        self.formLayout_wisc4.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_iop_wisc4)

        self.spinBox_iop_wisc4 = QSpinBox(self.groupBox_dados_teste_wisc4)
        self.spinBox_iop_wisc4.setObjectName(u"spinBox_iop_wisc4")

        self.formLayout_wisc4.setWidget(1, QFormLayout.ItemRole.FieldRole, self.spinBox_iop_wisc4)

        self.label_imo_wisc4 = QLabel(self.groupBox_dados_teste_wisc4)
        self.label_imo_wisc4.setObjectName(u"label_imo_wisc4")

        self.formLayout_wisc4.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_imo_wisc4)

        self.spinBo_imo_wisc4 = QSpinBox(self.groupBox_dados_teste_wisc4)
        self.spinBo_imo_wisc4.setObjectName(u"spinBo_imo_wisc4")

        self.formLayout_wisc4.setWidget(2, QFormLayout.ItemRole.FieldRole, self.spinBo_imo_wisc4)

        self.label_ivp_wisc4 = QLabel(self.groupBox_dados_teste_wisc4)
        self.label_ivp_wisc4.setObjectName(u"label_ivp_wisc4")

        self.formLayout_wisc4.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_ivp_wisc4)

        self.spinBox_ivp_wisc4 = QSpinBox(self.groupBox_dados_teste_wisc4)
        self.spinBox_ivp_wisc4.setObjectName(u"spinBox_ivp_wisc4")

        self.formLayout_wisc4.setWidget(3, QFormLayout.ItemRole.FieldRole, self.spinBox_ivp_wisc4)

        self.label_2 = QLabel(self.groupBox_dados_teste_wisc4)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_wisc4.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.label_3 = QLabel(self.groupBox_dados_teste_wisc4)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_wisc4.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.label_4 = QLabel(self.groupBox_dados_teste_wisc4)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_wisc4.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.label_5 = QLabel(self.groupBox_dados_teste_wisc4)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_wisc4.setWidget(7, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.label_6 = QLabel(self.groupBox_dados_teste_wisc4)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_wisc4.setWidget(8, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.label_7 = QLabel(self.groupBox_dados_teste_wisc4)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_wisc4.setWidget(9, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.label_8 = QLabel(self.groupBox_dados_teste_wisc4)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_wisc4.setWidget(11, QFormLayout.ItemRole.LabelRole, self.label_8)

        self.label_9 = QLabel(self.groupBox_dados_teste_wisc4)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_wisc4.setWidget(12, QFormLayout.ItemRole.LabelRole, self.label_9)

        self.spinBox = QSpinBox(self.groupBox_dados_teste_wisc4)
        self.spinBox.setObjectName(u"spinBox")

        self.formLayout_wisc4.setWidget(4, QFormLayout.ItemRole.FieldRole, self.spinBox)

        self.spinBox_2 = QSpinBox(self.groupBox_dados_teste_wisc4)
        self.spinBox_2.setObjectName(u"spinBox_2")

        self.formLayout_wisc4.setWidget(5, QFormLayout.ItemRole.FieldRole, self.spinBox_2)

        self.spinBox_3 = QSpinBox(self.groupBox_dados_teste_wisc4)
        self.spinBox_3.setObjectName(u"spinBox_3")

        self.formLayout_wisc4.setWidget(6, QFormLayout.ItemRole.FieldRole, self.spinBox_3)

        self.spinBox_4 = QSpinBox(self.groupBox_dados_teste_wisc4)
        self.spinBox_4.setObjectName(u"spinBox_4")

        self.formLayout_wisc4.setWidget(7, QFormLayout.ItemRole.FieldRole, self.spinBox_4)

        self.spinBox_5 = QSpinBox(self.groupBox_dados_teste_wisc4)
        self.spinBox_5.setObjectName(u"spinBox_5")

        self.formLayout_wisc4.setWidget(8, QFormLayout.ItemRole.FieldRole, self.spinBox_5)

        self.spinBox_6 = QSpinBox(self.groupBox_dados_teste_wisc4)
        self.spinBox_6.setObjectName(u"spinBox_6")

        self.formLayout_wisc4.setWidget(9, QFormLayout.ItemRole.FieldRole, self.spinBox_6)

        self.spinBox_7 = QSpinBox(self.groupBox_dados_teste_wisc4)
        self.spinBox_7.setObjectName(u"spinBox_7")

        self.formLayout_wisc4.setWidget(11, QFormLayout.ItemRole.FieldRole, self.spinBox_7)

        self.spinBox_8 = QSpinBox(self.groupBox_dados_teste_wisc4)
        self.spinBox_8.setObjectName(u"spinBox_8")

        self.formLayout_wisc4.setWidget(12, QFormLayout.ItemRole.FieldRole, self.spinBox_8)


        self.verticalLayout_3.addWidget(self.groupBox_dados_teste_wisc4)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_wisc4.addWidget(self.scrollArea)

        self.verticalSpacer_wisc4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_wisc4.addItem(self.verticalSpacer_wisc4)

        self.stackedWidget_formularios.addWidget(self.page_form_wisc4)
        self.page_form_ravlt = QWidget()
        self.page_form_ravlt.setObjectName(u"page_form_ravlt")
        self.verticalLayout_ravlt = QVBoxLayout(self.page_form_ravlt)
        self.verticalLayout_ravlt.setObjectName(u"verticalLayout_ravlt")
        self.label_titulo_ravlt = QLabel(self.page_form_ravlt)
        self.label_titulo_ravlt.setObjectName(u"label_titulo_ravlt")
        self.label_titulo_ravlt.setFont(font1)

        self.verticalLayout_ravlt.addWidget(self.label_titulo_ravlt)

        self.groupBox_faixa_etaria_ravlt = QGroupBox(self.page_form_ravlt)
        self.groupBox_faixa_etaria_ravlt.setObjectName(u"groupBox_faixa_etaria_ravlt")
        self.horizontalLayout_ravlt = QHBoxLayout(self.groupBox_faixa_etaria_ravlt)
        self.horizontalLayout_ravlt.setObjectName(u"horizontalLayout_ravlt")
        self.checkBox_incluir_ravlt = QCheckBox(self.groupBox_faixa_etaria_ravlt)
        self.checkBox_incluir_ravlt.setObjectName(u"checkBox_incluir_ravlt")

        self.horizontalLayout_ravlt.addWidget(self.checkBox_incluir_ravlt)

        self.radioButton_pre_escolar_ravlt = QRadioButton(self.groupBox_faixa_etaria_ravlt)
        self.radioButton_pre_escolar_ravlt.setObjectName(u"radioButton_pre_escolar_ravlt")

        self.horizontalLayout_ravlt.addWidget(self.radioButton_pre_escolar_ravlt)

        self.radioButton_escolar_ravlt = QRadioButton(self.groupBox_faixa_etaria_ravlt)
        self.radioButton_escolar_ravlt.setObjectName(u"radioButton_escolar_ravlt")
        self.radioButton_escolar_ravlt.setChecked(True)

        self.horizontalLayout_ravlt.addWidget(self.radioButton_escolar_ravlt)

        self.radioButton_adulto_ravlt = QRadioButton(self.groupBox_faixa_etaria_ravlt)
        self.radioButton_adulto_ravlt.setObjectName(u"radioButton_adulto_ravlt")

        self.horizontalLayout_ravlt.addWidget(self.radioButton_adulto_ravlt)


        self.verticalLayout_ravlt.addWidget(self.groupBox_faixa_etaria_ravlt)

        self.groupBox_dados_teste_ravlt = QGroupBox(self.page_form_ravlt)
        self.groupBox_dados_teste_ravlt.setObjectName(u"groupBox_dados_teste_ravlt")
        self.formLayout_ravlt = QFormLayout(self.groupBox_dados_teste_ravlt)
        self.formLayout_ravlt.setObjectName(u"formLayout_ravlt")
        self.label_TODO_ravlt = QLabel(self.groupBox_dados_teste_ravlt)
        self.label_TODO_ravlt.setObjectName(u"label_TODO_ravlt")

        self.formLayout_ravlt.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_TODO_ravlt)

        self.spinBox_TODO_ravlt = QSpinBox(self.groupBox_dados_teste_ravlt)
        self.spinBox_TODO_ravlt.setObjectName(u"spinBox_TODO_ravlt")

        self.formLayout_ravlt.setWidget(0, QFormLayout.ItemRole.FieldRole, self.spinBox_TODO_ravlt)


        self.verticalLayout_ravlt.addWidget(self.groupBox_dados_teste_ravlt)

        self.verticalSpacer_ravlt = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_ravlt.addItem(self.verticalSpacer_ravlt)

        self.stackedWidget_formularios.addWidget(self.page_form_ravlt)
        self.page_form_bpa2 = QWidget()
        self.page_form_bpa2.setObjectName(u"page_form_bpa2")
        self.verticalLayout_bpa2 = QVBoxLayout(self.page_form_bpa2)
        self.verticalLayout_bpa2.setObjectName(u"verticalLayout_bpa2")
        self.label_titulo_bpa2 = QLabel(self.page_form_bpa2)
        self.label_titulo_bpa2.setObjectName(u"label_titulo_bpa2")
        self.label_titulo_bpa2.setFont(font1)

        self.verticalLayout_bpa2.addWidget(self.label_titulo_bpa2)

        self.groupBox_faixa_etaria_bpa2 = QGroupBox(self.page_form_bpa2)
        self.groupBox_faixa_etaria_bpa2.setObjectName(u"groupBox_faixa_etaria_bpa2")
        self.horizontalLayout_bpa2 = QHBoxLayout(self.groupBox_faixa_etaria_bpa2)
        self.horizontalLayout_bpa2.setObjectName(u"horizontalLayout_bpa2")
        self.checkBox_incluir_bpa2 = QCheckBox(self.groupBox_faixa_etaria_bpa2)
        self.checkBox_incluir_bpa2.setObjectName(u"checkBox_incluir_bpa2")

        self.horizontalLayout_bpa2.addWidget(self.checkBox_incluir_bpa2)

        self.radioButton_pre_escolar_bpa2 = QRadioButton(self.groupBox_faixa_etaria_bpa2)
        self.radioButton_pre_escolar_bpa2.setObjectName(u"radioButton_pre_escolar_bpa2")

        self.horizontalLayout_bpa2.addWidget(self.radioButton_pre_escolar_bpa2)

        self.radioButton_escolar_bpa2 = QRadioButton(self.groupBox_faixa_etaria_bpa2)
        self.radioButton_escolar_bpa2.setObjectName(u"radioButton_escolar_bpa2")
        self.radioButton_escolar_bpa2.setChecked(True)

        self.horizontalLayout_bpa2.addWidget(self.radioButton_escolar_bpa2)

        self.radioButton_adulto_bpa2 = QRadioButton(self.groupBox_faixa_etaria_bpa2)
        self.radioButton_adulto_bpa2.setObjectName(u"radioButton_adulto_bpa2")

        self.horizontalLayout_bpa2.addWidget(self.radioButton_adulto_bpa2)


        self.verticalLayout_bpa2.addWidget(self.groupBox_faixa_etaria_bpa2)

        self.groupBox_dados_teste_bpa2 = QGroupBox(self.page_form_bpa2)
        self.groupBox_dados_teste_bpa2.setObjectName(u"groupBox_dados_teste_bpa2")
        self.formLayout_bpa2 = QFormLayout(self.groupBox_dados_teste_bpa2)
        self.formLayout_bpa2.setObjectName(u"formLayout_bpa2")
        self.label_ac_bpa2 = QLabel(self.groupBox_dados_teste_bpa2)
        self.label_ac_bpa2.setObjectName(u"label_ac_bpa2")

        self.formLayout_bpa2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_ac_bpa2)

        self.spinBox_ac_bpa2 = QSpinBox(self.groupBox_dados_teste_bpa2)
        self.spinBox_ac_bpa2.setObjectName(u"spinBox_ac_bpa2")

        self.formLayout_bpa2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.spinBox_ac_bpa2)

        self.label_ad_bpa2 = QLabel(self.groupBox_dados_teste_bpa2)
        self.label_ad_bpa2.setObjectName(u"label_ad_bpa2")

        self.formLayout_bpa2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_ad_bpa2)

        self.spinBox_ad_bpa2 = QSpinBox(self.groupBox_dados_teste_bpa2)
        self.spinBox_ad_bpa2.setObjectName(u"spinBox_ad_bpa2")

        self.formLayout_bpa2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.spinBox_ad_bpa2)

        self.spinBox_aa_bpa2 = QSpinBox(self.groupBox_dados_teste_bpa2)
        self.spinBox_aa_bpa2.setObjectName(u"spinBox_aa_bpa2")

        self.formLayout_bpa2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.spinBox_aa_bpa2)

        self.label_aa_bpa2 = QLabel(self.groupBox_dados_teste_bpa2)
        self.label_aa_bpa2.setObjectName(u"label_aa_bpa2")

        self.formLayout_bpa2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_aa_bpa2)


        self.verticalLayout_bpa2.addWidget(self.groupBox_dados_teste_bpa2)

        self.verticalSpacer_bpa2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_bpa2.addItem(self.verticalSpacer_bpa2)

        self.stackedWidget_formularios.addWidget(self.page_form_bpa2)
        self.page_form_neupsilin = QWidget()
        self.page_form_neupsilin.setObjectName(u"page_form_neupsilin")
        self.verticalLayout_neupsilin = QVBoxLayout(self.page_form_neupsilin)
        self.verticalLayout_neupsilin.setObjectName(u"verticalLayout_neupsilin")
        self.label_titulo_neupsilin = QLabel(self.page_form_neupsilin)
        self.label_titulo_neupsilin.setObjectName(u"label_titulo_neupsilin")
        self.label_titulo_neupsilin.setFont(font1)

        self.verticalLayout_neupsilin.addWidget(self.label_titulo_neupsilin)

        self.groupBox_faixa_etaria_neupsilin = QGroupBox(self.page_form_neupsilin)
        self.groupBox_faixa_etaria_neupsilin.setObjectName(u"groupBox_faixa_etaria_neupsilin")
        self.horizontalLayout_neupsilin = QHBoxLayout(self.groupBox_faixa_etaria_neupsilin)
        self.horizontalLayout_neupsilin.setObjectName(u"horizontalLayout_neupsilin")
        self.checkBox_incluir_neupsilin = QCheckBox(self.groupBox_faixa_etaria_neupsilin)
        self.checkBox_incluir_neupsilin.setObjectName(u"checkBox_incluir_neupsilin")

        self.horizontalLayout_neupsilin.addWidget(self.checkBox_incluir_neupsilin)

        self.radioButton_pre_escolar_neupsilin = QRadioButton(self.groupBox_faixa_etaria_neupsilin)
        self.radioButton_pre_escolar_neupsilin.setObjectName(u"radioButton_pre_escolar_neupsilin")

        self.horizontalLayout_neupsilin.addWidget(self.radioButton_pre_escolar_neupsilin)

        self.radioButton_escolar_neupsilin = QRadioButton(self.groupBox_faixa_etaria_neupsilin)
        self.radioButton_escolar_neupsilin.setObjectName(u"radioButton_escolar_neupsilin")
        self.radioButton_escolar_neupsilin.setChecked(True)

        self.horizontalLayout_neupsilin.addWidget(self.radioButton_escolar_neupsilin)

        self.radioButton_adulto_neupsilin = QRadioButton(self.groupBox_faixa_etaria_neupsilin)
        self.radioButton_adulto_neupsilin.setObjectName(u"radioButton_adulto_neupsilin")

        self.horizontalLayout_neupsilin.addWidget(self.radioButton_adulto_neupsilin)


        self.verticalLayout_neupsilin.addWidget(self.groupBox_faixa_etaria_neupsilin)

        self.groupBox_dados_teste_neupsilin = QGroupBox(self.page_form_neupsilin)
        self.groupBox_dados_teste_neupsilin.setObjectName(u"groupBox_dados_teste_neupsilin")
        self.formLayout_neupsilin = QFormLayout(self.groupBox_dados_teste_neupsilin)
        self.formLayout_neupsilin.setObjectName(u"formLayout_neupsilin")
        self.label_TODO_neupsilin = QLabel(self.groupBox_dados_teste_neupsilin)
        self.label_TODO_neupsilin.setObjectName(u"label_TODO_neupsilin")

        self.formLayout_neupsilin.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_TODO_neupsilin)

        self.spinBox_TODO_neupsilin = QSpinBox(self.groupBox_dados_teste_neupsilin)
        self.spinBox_TODO_neupsilin.setObjectName(u"spinBox_TODO_neupsilin")

        self.formLayout_neupsilin.setWidget(0, QFormLayout.ItemRole.FieldRole, self.spinBox_TODO_neupsilin)


        self.verticalLayout_neupsilin.addWidget(self.groupBox_dados_teste_neupsilin)

        self.verticalSpacer_neupsilin = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_neupsilin.addItem(self.verticalSpacer_neupsilin)

        self.stackedWidget_formularios.addWidget(self.page_form_neupsilin)
        self.page_form_srs2 = QWidget()
        self.page_form_srs2.setObjectName(u"page_form_srs2")
        self.verticalLayout_srs2 = QVBoxLayout(self.page_form_srs2)
        self.verticalLayout_srs2.setObjectName(u"verticalLayout_srs2")
        self.label_titulo_srs2 = QLabel(self.page_form_srs2)
        self.label_titulo_srs2.setObjectName(u"label_titulo_srs2")
        self.label_titulo_srs2.setFont(font1)

        self.verticalLayout_srs2.addWidget(self.label_titulo_srs2)

        self.groupBox_faixa_etaria_srs2 = QGroupBox(self.page_form_srs2)
        self.groupBox_faixa_etaria_srs2.setObjectName(u"groupBox_faixa_etaria_srs2")
        self.horizontalLayout_srs2 = QHBoxLayout(self.groupBox_faixa_etaria_srs2)
        self.horizontalLayout_srs2.setObjectName(u"horizontalLayout_srs2")
        self.checkBox_incluir_srs2 = QCheckBox(self.groupBox_faixa_etaria_srs2)
        self.checkBox_incluir_srs2.setObjectName(u"checkBox_incluir_srs2")

        self.horizontalLayout_srs2.addWidget(self.checkBox_incluir_srs2)

        self.radioButton_pre_escolar_srs2 = QRadioButton(self.groupBox_faixa_etaria_srs2)
        self.radioButton_pre_escolar_srs2.setObjectName(u"radioButton_pre_escolar_srs2")

        self.horizontalLayout_srs2.addWidget(self.radioButton_pre_escolar_srs2)

        self.radioButton_escolar_srs2 = QRadioButton(self.groupBox_faixa_etaria_srs2)
        self.radioButton_escolar_srs2.setObjectName(u"radioButton_escolar_srs2")
        self.radioButton_escolar_srs2.setChecked(True)

        self.horizontalLayout_srs2.addWidget(self.radioButton_escolar_srs2)

        self.radioButton_adulto_srs2 = QRadioButton(self.groupBox_faixa_etaria_srs2)
        self.radioButton_adulto_srs2.setObjectName(u"radioButton_adulto_srs2")

        self.horizontalLayout_srs2.addWidget(self.radioButton_adulto_srs2)


        self.verticalLayout_srs2.addWidget(self.groupBox_faixa_etaria_srs2)

        self.groupBox_dados_teste_srs2 = QGroupBox(self.page_form_srs2)
        self.groupBox_dados_teste_srs2.setObjectName(u"groupBox_dados_teste_srs2")
        self.formLayout_srs2 = QFormLayout(self.groupBox_dados_teste_srs2)
        self.formLayout_srs2.setObjectName(u"formLayout_srs2")
        self.label_TODO_srs2 = QLabel(self.groupBox_dados_teste_srs2)
        self.label_TODO_srs2.setObjectName(u"label_TODO_srs2")

        self.formLayout_srs2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_TODO_srs2)

        self.spinBox_TODO_srs2 = QSpinBox(self.groupBox_dados_teste_srs2)
        self.spinBox_TODO_srs2.setObjectName(u"spinBox_TODO_srs2")

        self.formLayout_srs2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.spinBox_TODO_srs2)


        self.verticalLayout_srs2.addWidget(self.groupBox_dados_teste_srs2)

        self.verticalSpacer_srs2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_srs2.addItem(self.verticalSpacer_srs2)

        self.stackedWidget_formularios.addWidget(self.page_form_srs2)
        self.page_form_etdah = QWidget()
        self.page_form_etdah.setObjectName(u"page_form_etdah")
        self.verticalLayout_etdah = QVBoxLayout(self.page_form_etdah)
        self.verticalLayout_etdah.setObjectName(u"verticalLayout_etdah")
        self.label_titulo_etdah = QLabel(self.page_form_etdah)
        self.label_titulo_etdah.setObjectName(u"label_titulo_etdah")
        self.label_titulo_etdah.setFont(font1)

        self.verticalLayout_etdah.addWidget(self.label_titulo_etdah)

        self.groupBox_faixa_etaria_etdah = QGroupBox(self.page_form_etdah)
        self.groupBox_faixa_etaria_etdah.setObjectName(u"groupBox_faixa_etaria_etdah")
        self.horizontalLayout_etdah = QHBoxLayout(self.groupBox_faixa_etaria_etdah)
        self.horizontalLayout_etdah.setObjectName(u"horizontalLayout_etdah")
        self.checkBox_incluir_etdah = QCheckBox(self.groupBox_faixa_etaria_etdah)
        self.checkBox_incluir_etdah.setObjectName(u"checkBox_incluir_etdah")

        self.horizontalLayout_etdah.addWidget(self.checkBox_incluir_etdah)

        self.radioButton_pre_escolar_etdah = QRadioButton(self.groupBox_faixa_etaria_etdah)
        self.radioButton_pre_escolar_etdah.setObjectName(u"radioButton_pre_escolar_etdah")

        self.horizontalLayout_etdah.addWidget(self.radioButton_pre_escolar_etdah)

        self.radioButton_escolar_etdah = QRadioButton(self.groupBox_faixa_etaria_etdah)
        self.radioButton_escolar_etdah.setObjectName(u"radioButton_escolar_etdah")
        self.radioButton_escolar_etdah.setChecked(True)

        self.horizontalLayout_etdah.addWidget(self.radioButton_escolar_etdah)

        self.radioButton_adulto_etdah = QRadioButton(self.groupBox_faixa_etaria_etdah)
        self.radioButton_adulto_etdah.setObjectName(u"radioButton_adulto_etdah")

        self.horizontalLayout_etdah.addWidget(self.radioButton_adulto_etdah)


        self.verticalLayout_etdah.addWidget(self.groupBox_faixa_etaria_etdah)

        self.groupBox_dados_teste_etdah = QGroupBox(self.page_form_etdah)
        self.groupBox_dados_teste_etdah.setObjectName(u"groupBox_dados_teste_etdah")
        self.formLayout_etdah = QFormLayout(self.groupBox_dados_teste_etdah)
        self.formLayout_etdah.setObjectName(u"formLayout_etdah")
        self.label_TODO_etdah = QLabel(self.groupBox_dados_teste_etdah)
        self.label_TODO_etdah.setObjectName(u"label_TODO_etdah")

        self.formLayout_etdah.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_TODO_etdah)

        self.spinBox_TODO_etdah = QSpinBox(self.groupBox_dados_teste_etdah)
        self.spinBox_TODO_etdah.setObjectName(u"spinBox_TODO_etdah")

        self.formLayout_etdah.setWidget(0, QFormLayout.ItemRole.FieldRole, self.spinBox_TODO_etdah)


        self.verticalLayout_etdah.addWidget(self.groupBox_dados_teste_etdah)

        self.verticalSpacer_etdah = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_etdah.addItem(self.verticalSpacer_etdah)

        self.stackedWidget_formularios.addWidget(self.page_form_etdah)
        self.page_form_cars2 = QWidget()
        self.page_form_cars2.setObjectName(u"page_form_cars2")
        self.verticalLayout_cars2 = QVBoxLayout(self.page_form_cars2)
        self.verticalLayout_cars2.setObjectName(u"verticalLayout_cars2")
        self.label_titulo_cars2 = QLabel(self.page_form_cars2)
        self.label_titulo_cars2.setObjectName(u"label_titulo_cars2")
        self.label_titulo_cars2.setFont(font1)

        self.verticalLayout_cars2.addWidget(self.label_titulo_cars2)

        self.groupBox_faixa_etaria_cars2 = QGroupBox(self.page_form_cars2)
        self.groupBox_faixa_etaria_cars2.setObjectName(u"groupBox_faixa_etaria_cars2")
        self.horizontalLayout_cars2 = QHBoxLayout(self.groupBox_faixa_etaria_cars2)
        self.horizontalLayout_cars2.setObjectName(u"horizontalLayout_cars2")
        self.checkBox_incluir_cars2 = QCheckBox(self.groupBox_faixa_etaria_cars2)
        self.checkBox_incluir_cars2.setObjectName(u"checkBox_incluir_cars2")

        self.horizontalLayout_cars2.addWidget(self.checkBox_incluir_cars2)

        self.radioButton_pre_escolar_cars2 = QRadioButton(self.groupBox_faixa_etaria_cars2)
        self.radioButton_pre_escolar_cars2.setObjectName(u"radioButton_pre_escolar_cars2")

        self.horizontalLayout_cars2.addWidget(self.radioButton_pre_escolar_cars2)

        self.radioButton_escolar_cars2 = QRadioButton(self.groupBox_faixa_etaria_cars2)
        self.radioButton_escolar_cars2.setObjectName(u"radioButton_escolar_cars2")
        self.radioButton_escolar_cars2.setChecked(True)

        self.horizontalLayout_cars2.addWidget(self.radioButton_escolar_cars2)

        self.radioButton_adulto_cars2 = QRadioButton(self.groupBox_faixa_etaria_cars2)
        self.radioButton_adulto_cars2.setObjectName(u"radioButton_adulto_cars2")

        self.horizontalLayout_cars2.addWidget(self.radioButton_adulto_cars2)


        self.verticalLayout_cars2.addWidget(self.groupBox_faixa_etaria_cars2)

        self.groupBox_dados_teste_cars2 = QGroupBox(self.page_form_cars2)
        self.groupBox_dados_teste_cars2.setObjectName(u"groupBox_dados_teste_cars2")
        self.formLayout_cars2 = QFormLayout(self.groupBox_dados_teste_cars2)
        self.formLayout_cars2.setObjectName(u"formLayout_cars2")
        self.label_TODO_cars2 = QLabel(self.groupBox_dados_teste_cars2)
        self.label_TODO_cars2.setObjectName(u"label_TODO_cars2")

        self.formLayout_cars2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_TODO_cars2)

        self.spinBox_TODO_cars2 = QSpinBox(self.groupBox_dados_teste_cars2)
        self.spinBox_TODO_cars2.setObjectName(u"spinBox_TODO_cars2")

        self.formLayout_cars2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.spinBox_TODO_cars2)


        self.verticalLayout_cars2.addWidget(self.groupBox_dados_teste_cars2)

        self.verticalSpacer_cars2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_cars2.addItem(self.verticalSpacer_cars2)

        self.stackedWidget_formularios.addWidget(self.page_form_cars2)
        self.page_form_htp = QWidget()
        self.page_form_htp.setObjectName(u"page_form_htp")
        self.verticalLayout_htp = QVBoxLayout(self.page_form_htp)
        self.verticalLayout_htp.setObjectName(u"verticalLayout_htp")
        self.label_titulo_htp = QLabel(self.page_form_htp)
        self.label_titulo_htp.setObjectName(u"label_titulo_htp")
        self.label_titulo_htp.setFont(font1)

        self.verticalLayout_htp.addWidget(self.label_titulo_htp)

        self.groupBox_faixa_etaria_htp = QGroupBox(self.page_form_htp)
        self.groupBox_faixa_etaria_htp.setObjectName(u"groupBox_faixa_etaria_htp")
        self.horizontalLayout_htp = QHBoxLayout(self.groupBox_faixa_etaria_htp)
        self.horizontalLayout_htp.setObjectName(u"horizontalLayout_htp")
        self.checkBox_incluir_htp = QCheckBox(self.groupBox_faixa_etaria_htp)
        self.checkBox_incluir_htp.setObjectName(u"checkBox_incluir_htp")

        self.horizontalLayout_htp.addWidget(self.checkBox_incluir_htp)

        self.radioButton_pre_escolar_htp = QRadioButton(self.groupBox_faixa_etaria_htp)
        self.radioButton_pre_escolar_htp.setObjectName(u"radioButton_pre_escolar_htp")

        self.horizontalLayout_htp.addWidget(self.radioButton_pre_escolar_htp)

        self.radioButton_escolar_htp = QRadioButton(self.groupBox_faixa_etaria_htp)
        self.radioButton_escolar_htp.setObjectName(u"radioButton_escolar_htp")
        self.radioButton_escolar_htp.setChecked(True)

        self.horizontalLayout_htp.addWidget(self.radioButton_escolar_htp)

        self.radioButton_adulto_htp = QRadioButton(self.groupBox_faixa_etaria_htp)
        self.radioButton_adulto_htp.setObjectName(u"radioButton_adulto_htp")

        self.horizontalLayout_htp.addWidget(self.radioButton_adulto_htp)


        self.verticalLayout_htp.addWidget(self.groupBox_faixa_etaria_htp)

        self.groupBox_dados_teste_htp = QGroupBox(self.page_form_htp)
        self.groupBox_dados_teste_htp.setObjectName(u"groupBox_dados_teste_htp")
        self.formLayout_htp = QFormLayout(self.groupBox_dados_teste_htp)
        self.formLayout_htp.setObjectName(u"formLayout_htp")
        self.label_TODO_htp = QLabel(self.groupBox_dados_teste_htp)
        self.label_TODO_htp.setObjectName(u"label_TODO_htp")

        self.formLayout_htp.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_TODO_htp)

        self.spinBox_TODO_htp = QSpinBox(self.groupBox_dados_teste_htp)
        self.spinBox_TODO_htp.setObjectName(u"spinBox_TODO_htp")

        self.formLayout_htp.setWidget(0, QFormLayout.ItemRole.FieldRole, self.spinBox_TODO_htp)


        self.verticalLayout_htp.addWidget(self.groupBox_dados_teste_htp)

        self.verticalSpacer_htp = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_htp.addItem(self.verticalSpacer_htp)

        self.stackedWidget_formularios.addWidget(self.page_form_htp)
        self.page_form_fdt = QWidget()
        self.page_form_fdt.setObjectName(u"page_form_fdt")
        self.verticalLayout_fdt = QVBoxLayout(self.page_form_fdt)
        self.verticalLayout_fdt.setObjectName(u"verticalLayout_fdt")
        self.label_titulo_fdt = QLabel(self.page_form_fdt)
        self.label_titulo_fdt.setObjectName(u"label_titulo_fdt")
        self.label_titulo_fdt.setFont(font1)

        self.verticalLayout_fdt.addWidget(self.label_titulo_fdt)

        self.groupBox_faixa_etaria_fdt = QGroupBox(self.page_form_fdt)
        self.groupBox_faixa_etaria_fdt.setObjectName(u"groupBox_faixa_etaria_fdt")
        self.horizontalLayout_fdt = QHBoxLayout(self.groupBox_faixa_etaria_fdt)
        self.horizontalLayout_fdt.setObjectName(u"horizontalLayout_fdt")
        self.checkBox_incluir_fdt = QCheckBox(self.groupBox_faixa_etaria_fdt)
        self.checkBox_incluir_fdt.setObjectName(u"checkBox_incluir_fdt")

        self.horizontalLayout_fdt.addWidget(self.checkBox_incluir_fdt)

        self.radioButton_pre_escolar_fdt = QRadioButton(self.groupBox_faixa_etaria_fdt)
        self.radioButton_pre_escolar_fdt.setObjectName(u"radioButton_pre_escolar_fdt")

        self.horizontalLayout_fdt.addWidget(self.radioButton_pre_escolar_fdt)

        self.radioButton_escolar_fdt = QRadioButton(self.groupBox_faixa_etaria_fdt)
        self.radioButton_escolar_fdt.setObjectName(u"radioButton_escolar_fdt")
        self.radioButton_escolar_fdt.setChecked(True)

        self.horizontalLayout_fdt.addWidget(self.radioButton_escolar_fdt)

        self.radioButton_adulto_fdt = QRadioButton(self.groupBox_faixa_etaria_fdt)
        self.radioButton_adulto_fdt.setObjectName(u"radioButton_adulto_fdt")

        self.horizontalLayout_fdt.addWidget(self.radioButton_adulto_fdt)


        self.verticalLayout_fdt.addWidget(self.groupBox_faixa_etaria_fdt)

        self.groupBox_dados_teste_fdt = QGroupBox(self.page_form_fdt)
        self.groupBox_dados_teste_fdt.setObjectName(u"groupBox_dados_teste_fdt")
        self.formLayout_fdt = QFormLayout(self.groupBox_dados_teste_fdt)
        self.formLayout_fdt.setObjectName(u"formLayout_fdt")
        self.label_TODO_fdt = QLabel(self.groupBox_dados_teste_fdt)
        self.label_TODO_fdt.setObjectName(u"label_TODO_fdt")

        self.formLayout_fdt.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_TODO_fdt)

        self.spinBox_TODO_fdt = QSpinBox(self.groupBox_dados_teste_fdt)
        self.spinBox_TODO_fdt.setObjectName(u"spinBox_TODO_fdt")

        self.formLayout_fdt.setWidget(0, QFormLayout.ItemRole.FieldRole, self.spinBox_TODO_fdt)


        self.verticalLayout_fdt.addWidget(self.groupBox_dados_teste_fdt)

        self.verticalSpacer_fdt = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_fdt.addItem(self.verticalSpacer_fdt)

        self.stackedWidget_formularios.addWidget(self.page_form_fdt)

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

        self.stackedWidget_formularios.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(TelaTestes)
    # setupUi

    def retranslateUi(self, TelaTestes):
        TelaTestes.setWindowTitle(QCoreApplication.translate("TelaTestes", u"Form", None))
        self.label_titulo.setText(QCoreApplication.translate("TelaTestes", u"Passo 3: Inserir Dados dos Testes", None))
        self.groupBox_botoes.setTitle(QCoreApplication.translate("TelaTestes", u"Testes", None))
        self.btn_wisc4.setText(QCoreApplication.translate("TelaTestes", u"WISC-IV", None))
        self.btn_ravlt.setText(QCoreApplication.translate("TelaTestes", u"RAVLT", None))
        self.btn_bpa2.setText(QCoreApplication.translate("TelaTestes", u"BPA-2", None))
        self.btn_neupsilin.setText(QCoreApplication.translate("TelaTestes", u"Neupsilin", None))
        self.btn_srs2.setText(QCoreApplication.translate("TelaTestes", u"SRS-2", None))
        self.btn_etdah.setText(QCoreApplication.translate("TelaTestes", u"ETDAH-PAIS", None))
        self.btn_cars2.setText(QCoreApplication.translate("TelaTestes", u"CARS-II", None))
        self.btn_htp.setText(QCoreApplication.translate("TelaTestes", u"HTP", None))
        self.btn_fdt.setText(QCoreApplication.translate("TelaTestes", u"FDT", None))
        self.label.setText(QCoreApplication.translate("TelaTestes", u"Selecione um teste \u00e0 esquerda para preencher os dados.", None))
        self.label_titulo_wisc4.setText(QCoreApplication.translate("TelaTestes", u"Formul\u00e1rio - WISC-IV", None))
        self.groupBox_faixa_etaria_wisc4.setTitle(QCoreApplication.translate("TelaTestes", u"Faixa Et\u00e1ria", None))
        self.checkBox_incluir_wisc4.setText(QCoreApplication.translate("TelaTestes", u"Incluir", None))
        self.radioButton_pre_escolar_wisc4.setText(QCoreApplication.translate("TelaTestes", u"Pr\u00e9-escolar", None))
        self.radioButton_escolar_wisc4.setText(QCoreApplication.translate("TelaTestes", u"Escolar", None))
        self.radioButton_adulto_wisc4.setText(QCoreApplication.translate("TelaTestes", u"Adulto", None))
        self.groupBox_dados_teste_wisc4.setTitle(QCoreApplication.translate("TelaTestes", u"Dados do Teste", None))
        self.label_icv_wisc4.setText(QCoreApplication.translate("TelaTestes", u"\u00cdndices de Compreens\u00e3o Verbal", None))
        self.label_iop_wisc4.setText(QCoreApplication.translate("TelaTestes", u"\u00cdndices de Organiza\u00e7\u00e3o Perceptual", None))
        self.label_imo_wisc4.setText(QCoreApplication.translate("TelaTestes", u"\u00cdndices de Mem\u00f3ria Operacional", None))
        self.label_ivp_wisc4.setText(QCoreApplication.translate("TelaTestes", u"\u00cdndice Velocidade Processamento", None))
        self.label_2.setText(QCoreApplication.translate("TelaTestes", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("TelaTestes", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("TelaTestes", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("TelaTestes", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("TelaTestes", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("TelaTestes", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("TelaTestes", u"TextLabel", None))
        self.label_9.setText(QCoreApplication.translate("TelaTestes", u"TextLabel", None))
        self.label_titulo_ravlt.setText(QCoreApplication.translate("TelaTestes", u"Formul\u00e1rio - RAVLT", None))
        self.groupBox_faixa_etaria_ravlt.setTitle(QCoreApplication.translate("TelaTestes", u"Faixa Et\u00e1ria", None))
        self.checkBox_incluir_ravlt.setText(QCoreApplication.translate("TelaTestes", u"Incluir", None))
        self.radioButton_pre_escolar_ravlt.setText(QCoreApplication.translate("TelaTestes", u"Pr\u00e9-escolar", None))
        self.radioButton_escolar_ravlt.setText(QCoreApplication.translate("TelaTestes", u"Escolar", None))
        self.radioButton_adulto_ravlt.setText(QCoreApplication.translate("TelaTestes", u"Adulto", None))
        self.groupBox_dados_teste_ravlt.setTitle(QCoreApplication.translate("TelaTestes", u"Dados do Teste", None))
        self.label_TODO_ravlt.setText(QCoreApplication.translate("TelaTestes", u"TODO", None))
        self.label_titulo_bpa2.setText(QCoreApplication.translate("TelaTestes", u"Formul\u00e1rio - BPA-2", None))
        self.groupBox_faixa_etaria_bpa2.setTitle(QCoreApplication.translate("TelaTestes", u"Faixa Et\u00e1ria", None))
        self.checkBox_incluir_bpa2.setText(QCoreApplication.translate("TelaTestes", u"Incluir", None))
        self.radioButton_pre_escolar_bpa2.setText(QCoreApplication.translate("TelaTestes", u"Pr\u00e9-escolar", None))
        self.radioButton_escolar_bpa2.setText(QCoreApplication.translate("TelaTestes", u"Escolar", None))
        self.radioButton_adulto_bpa2.setText(QCoreApplication.translate("TelaTestes", u"Adulto", None))
        self.groupBox_dados_teste_bpa2.setTitle(QCoreApplication.translate("TelaTestes", u"Dados do Teste", None))
        self.label_ac_bpa2.setText(QCoreApplication.translate("TelaTestes", u"Aten\u00e7\u00e3o Concentrada", None))
        self.label_ad_bpa2.setText(QCoreApplication.translate("TelaTestes", u"Aten\u00e7\u00e3o Dividida", None))
        self.label_aa_bpa2.setText(QCoreApplication.translate("TelaTestes", u"Aten\u00e7\u00e3o Alternada", None))
        self.label_titulo_neupsilin.setText(QCoreApplication.translate("TelaTestes", u"Formul\u00e1rio - Neupsilin", None))
        self.groupBox_faixa_etaria_neupsilin.setTitle(QCoreApplication.translate("TelaTestes", u"Faixa Et\u00e1ria", None))
        self.checkBox_incluir_neupsilin.setText(QCoreApplication.translate("TelaTestes", u"Incluir", None))
        self.radioButton_pre_escolar_neupsilin.setText(QCoreApplication.translate("TelaTestes", u"Pr\u00e9-escolar", None))
        self.radioButton_escolar_neupsilin.setText(QCoreApplication.translate("TelaTestes", u"Escolar", None))
        self.radioButton_adulto_neupsilin.setText(QCoreApplication.translate("TelaTestes", u"Adulto", None))
        self.groupBox_dados_teste_neupsilin.setTitle(QCoreApplication.translate("TelaTestes", u"Dados do Teste", None))
        self.label_TODO_neupsilin.setText(QCoreApplication.translate("TelaTestes", u"TODO", None))
        self.label_titulo_srs2.setText(QCoreApplication.translate("TelaTestes", u"Formul\u00e1rio - SRS-2", None))
        self.groupBox_faixa_etaria_srs2.setTitle(QCoreApplication.translate("TelaTestes", u"Faixa Et\u00e1ria", None))
        self.checkBox_incluir_srs2.setText(QCoreApplication.translate("TelaTestes", u"Incluir", None))
        self.radioButton_pre_escolar_srs2.setText(QCoreApplication.translate("TelaTestes", u"Pr\u00e9-escolar", None))
        self.radioButton_escolar_srs2.setText(QCoreApplication.translate("TelaTestes", u"Escolar", None))
        self.radioButton_adulto_srs2.setText(QCoreApplication.translate("TelaTestes", u"Adulto", None))
        self.groupBox_dados_teste_srs2.setTitle(QCoreApplication.translate("TelaTestes", u"Dados do Teste", None))
        self.label_TODO_srs2.setText(QCoreApplication.translate("TelaTestes", u"TODO", None))
        self.label_titulo_etdah.setText(QCoreApplication.translate("TelaTestes", u"Formul\u00e1rio - ETDAH-PAIS", None))
        self.groupBox_faixa_etaria_etdah.setTitle(QCoreApplication.translate("TelaTestes", u"Faixa Et\u00e1ria", None))
        self.checkBox_incluir_etdah.setText(QCoreApplication.translate("TelaTestes", u"Incluir", None))
        self.radioButton_pre_escolar_etdah.setText(QCoreApplication.translate("TelaTestes", u"Pr\u00e9-escolar", None))
        self.radioButton_escolar_etdah.setText(QCoreApplication.translate("TelaTestes", u"Escolar", None))
        self.radioButton_adulto_etdah.setText(QCoreApplication.translate("TelaTestes", u"Adulto", None))
        self.groupBox_dados_teste_etdah.setTitle(QCoreApplication.translate("TelaTestes", u"Dados do Teste", None))
        self.label_TODO_etdah.setText(QCoreApplication.translate("TelaTestes", u"TODO", None))
        self.label_titulo_cars2.setText(QCoreApplication.translate("TelaTestes", u"Formul\u00e1rio - CARS-II", None))
        self.groupBox_faixa_etaria_cars2.setTitle(QCoreApplication.translate("TelaTestes", u"Faixa Et\u00e1ria", None))
        self.checkBox_incluir_cars2.setText(QCoreApplication.translate("TelaTestes", u"Incluir", None))
        self.radioButton_pre_escolar_cars2.setText(QCoreApplication.translate("TelaTestes", u"Pr\u00e9-escolar", None))
        self.radioButton_escolar_cars2.setText(QCoreApplication.translate("TelaTestes", u"Escolar", None))
        self.radioButton_adulto_cars2.setText(QCoreApplication.translate("TelaTestes", u"Adulto", None))
        self.groupBox_dados_teste_cars2.setTitle(QCoreApplication.translate("TelaTestes", u"Dados do Teste", None))
        self.label_TODO_cars2.setText(QCoreApplication.translate("TelaTestes", u"TODO", None))
        self.label_titulo_htp.setText(QCoreApplication.translate("TelaTestes", u"Formul\u00e1rio - HTP", None))
        self.groupBox_faixa_etaria_htp.setTitle(QCoreApplication.translate("TelaTestes", u"Faixa Et\u00e1ria", None))
        self.checkBox_incluir_htp.setText(QCoreApplication.translate("TelaTestes", u"Incluir", None))
        self.radioButton_pre_escolar_htp.setText(QCoreApplication.translate("TelaTestes", u"Pr\u00e9-escolar", None))
        self.radioButton_escolar_htp.setText(QCoreApplication.translate("TelaTestes", u"Escolar", None))
        self.radioButton_adulto_htp.setText(QCoreApplication.translate("TelaTestes", u"Adulto", None))
        self.groupBox_dados_teste_htp.setTitle(QCoreApplication.translate("TelaTestes", u"Dados do Teste", None))
        self.label_TODO_htp.setText(QCoreApplication.translate("TelaTestes", u"TODO", None))
        self.label_titulo_fdt.setText(QCoreApplication.translate("TelaTestes", u"Formul\u00e1rio - FDT", None))
        self.groupBox_faixa_etaria_fdt.setTitle(QCoreApplication.translate("TelaTestes", u"Faixa Et\u00e1ria", None))
        self.checkBox_incluir_fdt.setText(QCoreApplication.translate("TelaTestes", u"Incluir", None))
        self.radioButton_pre_escolar_fdt.setText(QCoreApplication.translate("TelaTestes", u"Pr\u00e9-escolar", None))
        self.radioButton_escolar_fdt.setText(QCoreApplication.translate("TelaTestes", u"Escolar", None))
        self.radioButton_adulto_fdt.setText(QCoreApplication.translate("TelaTestes", u"Adulto", None))
        self.groupBox_dados_teste_fdt.setTitle(QCoreApplication.translate("TelaTestes", u"Dados do Teste", None))
        self.label_TODO_fdt.setText(QCoreApplication.translate("TelaTestes", u"TODO", None))
        self.btn_voltar.setText(QCoreApplication.translate("TelaTestes", u"Voltar", None))
        self.btn_avancar.setText(QCoreApplication.translate("TelaTestes", u"Avan\u00e7ar", None))
    # retranslateUi

