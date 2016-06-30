# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/interf_qtcreator.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ScanFacture(object):
    def setupUi(self, ScanFacture):
        ScanFacture.setObjectName(_fromUtf8("ScanFacture"))
        ScanFacture.resize(625, 738)
        self.centralwidget = QtGui.QWidget(ScanFacture)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 110, 581, 611))
        self.textBrowser.setSearchPaths(['/home/innopolis/Documents/IdentitesNommees/data'])
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 50, 571, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        ScanFacture.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(ScanFacture)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 625, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFichier = QtGui.QMenu(self.menubar)
        self.menuFichier.setObjectName(_fromUtf8("menuFichier"))
        self.menuManuel = QtGui.QMenu(self.menubar)
        self.menuManuel.setObjectName(_fromUtf8("menuManuel"))
        self.menuPDF_vers_Excel = QtGui.QMenu(self.menuManuel)
        self.menuPDF_vers_Excel.setObjectName(_fromUtf8("menuPDF_vers_Excel"))
        self.menuOutils = QtGui.QMenu(self.menubar)
        self.menuOutils.setObjectName(_fromUtf8("menuOutils"))
        self.menuAide = QtGui.QMenu(self.menubar)
        self.menuAide.setObjectName(_fromUtf8("menuAide"))
        ScanFacture.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(ScanFacture)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        ScanFacture.setStatusBar(self.statusbar)
        self.actionOuvrir = QtGui.QAction(ScanFacture)
        self.actionOuvrir.setObjectName(_fromUtf8("actionOuvrir"))
        self.actionDerni_res_factures = QtGui.QAction(ScanFacture)
        self.actionDerni_res_factures.setObjectName(_fromUtf8("actionDerni_res_factures"))
        self.actionQuitter = QtGui.QAction(ScanFacture)
        self.actionQuitter.setObjectName(_fromUtf8("actionQuitter"))
        self.actionAutomatiquement = QtGui.QAction(ScanFacture)
        self.actionAutomatiquement.setObjectName(_fromUtf8("actionAutomatiquement"))
        self.actionPr_f_rences = QtGui.QAction(ScanFacture)
        self.actionPr_f_rences.setObjectName(_fromUtf8("actionPr_f_rences"))
        self.actionManuellement_2 = QtGui.QAction(ScanFacture)
        self.actionManuellement_2.setObjectName(_fromUtf8("actionManuellement_2"))
        self.actionAutomatiquement_2 = QtGui.QAction(ScanFacture)
        self.actionAutomatiquement_2.setObjectName(_fromUtf8("actionAutomatiquement_2"))
        self.actionAide_pour_ScanFacture = QtGui.QAction(ScanFacture)
        self.actionAide_pour_ScanFacture.setObjectName(_fromUtf8("actionAide_pour_ScanFacture"))
        self.actionA_propos_de_Algonano = QtGui.QAction(ScanFacture)
        self.actionA_propos_de_Algonano.setObjectName(_fromUtf8("actionA_propos_de_Algonano"))
        self.menuFichier.addAction(self.actionOuvrir)
        self.menuFichier.addAction(self.actionDerni_res_factures)
        self.menuFichier.addAction(self.actionQuitter)
        self.menuPDF_vers_Excel.addAction(self.actionManuellement_2)
        self.menuPDF_vers_Excel.addAction(self.actionAutomatiquement_2)
        self.menuManuel.addAction(self.actionAutomatiquement)
        self.menuManuel.addAction(self.menuPDF_vers_Excel.menuAction())
        self.menuOutils.addAction(self.actionPr_f_rences)
        self.menuAide.addAction(self.actionAide_pour_ScanFacture)
        self.menuAide.addAction(self.actionA_propos_de_Algonano)
        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuManuel.menuAction())
        self.menubar.addAction(self.menuOutils.menuAction())
        self.menubar.addAction(self.menuAide.menuAction())

        self.retranslateUi(ScanFacture)
        QtCore.QMetaObject.connectSlotsByName(ScanFacture)

    def retranslateUi(self, ScanFacture):
        ScanFacture.setWindowTitle(_translate("ScanFacture", "NonoFact", None))
        self.pushButton.setText(_translate("ScanFacture", "Ouvrir Facture PDF", None))
        self.menuFichier.setTitle(_translate("ScanFacture", "Fichier", None))
        self.menuManuel.setTitle(_translate("ScanFacture", "Générer", None))
        self.menuPDF_vers_Excel.setTitle(_translate("ScanFacture", "PDF vers Excel", None))
        self.menuOutils.setTitle(_translate("ScanFacture", "Configuration", None))
        self.menuAide.setTitle(_translate("ScanFacture", "Aide", None))
        self.actionOuvrir.setText(_translate("ScanFacture", "Ouvrir", None))
        self.actionDerni_res_factures.setText(_translate("ScanFacture", "Dernières factures ouvertes", None))
        self.actionQuitter.setText(_translate("ScanFacture", "Quitter", None))
        self.actionAutomatiquement.setText(_translate("ScanFacture", "Excel vers PDF", None))
        self.actionPr_f_rences.setText(_translate("ScanFacture", "Préférences", None))
        self.actionManuellement_2.setText(_translate("ScanFacture", "Manuellement", None))
        self.actionAutomatiquement_2.setText(_translate("ScanFacture", "Automatiquement", None))
        self.actionAide_pour_ScanFacture.setText(_translate("ScanFacture", "Aide pour ScanFacture", None))
        self.actionA_propos_de_Algonano.setText(_translate("ScanFacture", "A propos de Algonano", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ScanFacture = QtGui.QMainWindow()
    ui = Ui_ScanFacture()
    ui.setupUi(ScanFacture)
    ScanFacture.show()
    sys.exit(app.exec_())

