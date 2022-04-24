# Udělal RxiPland

# python 3.9.9

# 2021

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QDialog
import os
from random import choice

class Ui_MainWindow(QDialog):


    def ZobrazitNapovedu(self):

        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setWindowTitle("Nápověda k zapisování")
        msgBox.setText("Může se hodit, pokud si chcete slovo zaznamenat pro pozdější využití. Slova se budou ukládat do stejného poznámkového bloku, dokud ho nesmažete nebo nepřesunete. Poznámkový blok se bude ukládat jako ulozena_morseovka.txt do stejného umístění jako program.")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()


    def ZobrazitNapovedu2(self):

        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setWindowTitle("Nápověda k wordlistům")
        msgBox.setText("Program bere z wordlistu náhodná slova a následně je překládá do morseovky.\nBez vybraného wordlistu program nebude vybírat slova.\n\nCo je wordlist?\n\n-Je to textový dokument (.txt) se slovy\n\nJak si můžu vytvořit vlastní wordlist?\n\n-Vytvořte si nový poznámkový blok a do něho zapište jedno slovo nebo i více na každý řádek. (Program bere slova na jednom řádku jako celek, takže je nutno dávat za každým slovem enter, aby přeskočil na další řádek, ale nemusíte pokud chcete, aby to program chápal jako sousloví)")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()


    def Zapsat(self):

        try:

            global zasifrovano, vylosovane_slovo

            try:

                f = open(r"ulozena_morseovka.txt", "a")
                f.write(zasifrovano + "      " + vylosovane_slovo + "\n")
                f.close()

            except:
                f = open(r"ulozena_morseovka.txt", mode = "w")
                f.write(zasifrovano + "      " + vylosovane_slovo + "\n")
                f.close
            

            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Question)
            msgBox.setWindowTitle("Oznámení")
            msgBox.setText("Slovo bylo úspěšně zapsáno a uloženo.")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()

        except:

            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setWindowTitle("Problém!")
            msgBox.setText("Slovo se nepodařilo zapsat!")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()



    def VybratNovyWordList(self):

        global cesta_k_word_listu

        dlg = QFileDialog.getOpenFileName(self, 'Vyberte textový dokument se slovy:', '',"Textový dokument (*.txt)")


        if dlg != ('',''):

            cesta_k_word_listu = list(dlg)
            cesta_k_word_listu = dlg[0]

            test1 = list(dlg)

            test2 = test1[0]

            filename_with_extension = os.path.basename(test2)

            self.label_4.setText("Aktuální wordlist: " + filename_with_extension)

    def VymazatTabulku2 (self):

        self.plainTextEdit_2.setPlainText("")

    def VybratSlovo(self):

        global cesta_k_word_listu, vylosovane_slovo

        try:

            self.label_4.setStyleSheet("background-color: ")

            with open(cesta_k_word_listu) as file:
                lines = file.readlines()
                lines = [line.rstrip() for line in lines]

            vylosovane_slovo = str(choice(lines))

            vylosovane_slovo = vylosovane_slovo.upper()

            self.VymazatTabulku2()

            self.ConvertovatDoMorseovky()

        except:

            self.label_4.setStyleSheet("background-color: red")

    def PrelozeneSlovo(self):

        global vylosovane_slovo

        try:

            self.plainTextEdit_2.setPlainText(vylosovane_slovo)

        except:

            return


    def ConvertovatDoMorseovky(self):

        global vylosovane_slovo, zasifrovano

        MorsAbeceda = {'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.','F':'..-.', 'G':'--.', 'H':'....','I':'..', 'J':'.---', 'K':'-.-','L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'--.-','R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--','X':'-..-', 'Y':'-.--', 'Z':'--..','1':'.----', '2':'..---', '3':'...--','4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.','0':'-----'}

        zasifrovano = ''
        

        for letter in vylosovane_slovo:
            if letter != ' ':
 
            
                zasifrovano += ' ' + MorsAbeceda[letter] + '  '
            else:
                
                zasifrovano += ' |  '


        self.plainTextEdit.setPlainText(zasifrovano)
    
    
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 517)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(70, 70, 381, 181))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setReadOnly(True)

        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(550, 70, 381, 181))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit_2.setReadOnly(True)


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 40, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")


        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(560, 40, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")


        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 380, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")


        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(720, 410, 261, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(790, 435, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.VybratNovyWordList)


        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 435, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.Zapsat)


        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(70, 270, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.VybratSlovo)



        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(210, 435, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.ZobrazitNapovedu)


        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(660, 270, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.VymazatTabulku2)



        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(300, 270, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.PrelozeneSlovo)


        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(740, 435, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_4")
        self.pushButton_7.clicked.connect(self.ZobrazitNapovedu2)



        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Trénování morseovy abecedy"))
        self.label.setText(_translate("MainWindow", "Text v morseově abecedě:"))
        self.label_2.setText(_translate("MainWindow", "Přeložený text:"))
        self.label_3.setText(_translate("MainWindow", "Zaznamenat aktuální morseovu šifru\na zapsat ji do textového souboru:"))
        self.label_4.setText(_translate("MainWindow", "Aktuální wordlist:"))
        self.pushButton.setText(_translate("MainWindow", "Vybrat jiný wordlist"))
        self.pushButton_2.setText(_translate("MainWindow", "Zapsat"))
        self.pushButton_3.setText(_translate("MainWindow", "Náhodně vybrat nové slovo"))
        self.pushButton_4.setText(_translate("MainWindow", "?"))
        self.pushButton_5.setText(_translate("MainWindow", "Vymazat"))
        self.pushButton_6.setText(_translate("MainWindow", "Přeložit"))
        self.pushButton_7.setText(_translate("MainWindow", "?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
