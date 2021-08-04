from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from os import system , path , name , remove


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(570, 309)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tab_4 = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_4.setGeometry(QtCore.QRect(0, 0, 571, 311))
        self.tab_4.setObjectName("tab_4")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 160, 531, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.line3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.line3.setObjectName("line3")
        self.horizontalLayout_3.addWidget(self.line3)
        self.O_make = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.O_make.setObjectName("O_make")
        self.horizontalLayout_3.addWidget(self.O_make)
        self.O_push = QtWidgets.QPushButton(self.tab)
        self.O_push.setGeometry(QtCore.QRect(210, 220, 131, 31))
        self.O_push.setObjectName("O_push")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 110, 531, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.line2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.line2.setInputMask("")
        self.line2.setText("")
        self.line2.setObjectName("line2")
        self.horizontalLayout_2.addWidget(self.line2)
        self.O_save = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.O_save.setObjectName("O_save")
        self.horizontalLayout_2.addWidget(self.O_save)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(20, 10, 531, 51))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.line1 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line1.setFont(font)
        self.line1.setInputMask("")
        self.line1.setText("")
        self.line1.setMaxLength(32767)
        self.line1.setFrame(True)
        self.line1.setDragEnabled(False)
        self.line1.setReadOnly(True)
        self.line1.setClearButtonEnabled(False)
        self.line1.setObjectName("line1")
        self.horizontalLayout_4.addWidget(self.line1)
        self.O_browse = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.O_browse.setObjectName("O_browse")
        self.horizontalLayout_4.addWidget(self.O_browse)
        self.O_start = QtWidgets.QPushButton(self.tab)
        self.O_start.setGeometry(QtCore.QRect(210, 70, 131, 31))
        self.O_start.setDefault(False)
        self.O_start.setObjectName("O_start")
        self.tab_4.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.OS_refresh = QtWidgets.QPushButton(self.tab_3)
        self.OS_refresh.setGeometry(QtCore.QRect(0, 0, 561, 31))
        self.OS_refresh.setObjectName("OS_refresh")
        self.status_text = QtWidgets.QPlainTextEdit(self.tab_3)
        self.status_text.setGeometry(QtCore.QRect(0, 30, 561, 241))
        self.status_text.setReadOnly(True)
        self.status_text.setObjectName("status_test")
        self.tab_4.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.OL_refresh = QtWidgets.QPushButton(self.tab_2)
        self.OL_refresh.setGeometry(QtCore.QRect(0, 0, 561, 31))
        self.OL_refresh.setObjectName("OL_refresh")
        self.log_text = QtWidgets.QPlainTextEdit(self.tab_2)
        self.log_text.setGeometry(QtCore.QRect(0, 30, 561, 241))
        self.log_text.setReadOnly(True)
        self.log_text.setObjectName("log_text")
        self.tab_4.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.tab_4.setCurrentIndex(0)
        self.OL_refresh.clicked.connect(self.Lrefresh)
        self.OS_refresh.clicked.connect(self.Srefresh)
        self.O_make.clicked.connect(self.make)
        self.O_push.clicked.connect(self.push)
        self.O_save.clicked.connect(self.save)
        self.O_start.clicked.connect(self.start)
        self.O_browse.clicked.connect(self.browse)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def browse(self):
        '''
            it opens the directory which the project is in it
            and add the directory to the QLineEdit

            if  ".git"  were in that directory :
                The start button will be hidden
        '''
        global dir_
        dir_ = QFileDialog.getExistingDirectory(None, 'Select a folder:', '', QFileDialog.ShowDirsOnly)
        self.line1.setText(dir_)
        #         for windows           |          for linux
        if path.isdir(fr"{dir_}\.git") or path.isdir(f"{dir_}/.git") :
            self.O_start.hide()
        else :
            self.O_start.show()




    def Lrefresh(self):
        '''
            Log Refresh :
            1) clear the text box
            2) read the log file
            3) add to the text box

        '''
        def add_to_the_textBox(file):
            for line in file.readlines():
                log = ""
                things = line.split()
                self.log_text.appendPlainText(things[1])
                self.log_text.appendPlainText(f"{things[2]}  -  {things[3]}")
                for i in things[6:]:
                    log += i + " "
                self.log_text.appendPlainText(log)
                self.log_text.appendPlainText('\n'+'-'*90)
            file.close()

        self.log_text.clear()
        try:
            if name == 'nt' : # for windows
                file = open(fr"{dir_}\.git\logs\HEAD")
                add_to_the_textBox(file)

            elif name == 'posix' : # for linux
                file = open(f"{dir_}/.git/logs/HEAD")
                add_to_the_textBox(file)
        except:
            self.log_text.appendPlainText("\nat first Browse the project file")



    def Srefresh(self):
        '''
            Status Refresh :
            1) clear the text box
            2) get the output of "git status" and save it in "temp.txt"
            3) add to the text box
            4) remove temp file

        '''
        def add_to_the_textBox(file):
            for line in file.readlines():
                self.status_text.appendPlainText(line.strip('\n'))
            file.close()

        self.status_text.clear()
        try:
            if name == 'nt' : # for windows
                system(fr"cd {dir_} && git status > ..\itemp.txt")
                file = open(fr"{dir_}\..\temp.txt")
                add_to_the_textBox(file)
                remove(fr"{dir_}\..\temp.txt")

            elif name == 'posix' : # for linux
                system(f"cd {dir_} && git status > ../temp.txt")
                file = open(f"{dir_}/../temp.txt")
                add_to_the_textBox(file)
                remove(f"{dir_}/../temp.txt")
        except:
            self.status_text.appendPlainText("\nat first Browse the project file")



    def make(self):
        '''
            add origin remote
        '''
        adr = self.line3.text().strip().strip('[').strip(']')
        system(f"cd {dir_} && git remote add origin {adr}")



    def push(self):
        '''
            Not complete
            only works with these names : "origin" "master"
        '''
        system(f"cd {dir_} && git push origin master")



    def save(self):
        '''
            add all the changes to Stage and commit them
        '''
        system(f"cd {dir_} && git add -A")
        com = self.line2.text()
        self.line2.setText('')
        system(f"cd {dir_} && git commit -m '{com}'")



    def start(self):
        '''
           Initialize the git
           and now hide the start button because ".git" maded
        '''
        system(f"cd {dir_} && git init")
        self.O_start.hide()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Git"))

        ############### Line Edit ###############
        self.line1.setPlaceholderText(_translate("MainWindow", "your  project  directory"))
        self.line2.setPlaceholderText(_translate("MainWindow", "comment"))
        self.line3.setPlaceholderText(_translate("MainWindow", "github  repository  address"))

        ############### Push Button ###############
        self.O_make.setText(_translate("MainWindow", "remote"))
        self.O_push.setText(_translate("MainWindow", "PUSH"))
        self.O_save.setText(_translate("MainWindow", "save"))
        self.O_browse.setText(_translate("MainWindow", "browse"))
        self.O_start.setText(_translate("MainWindow", "start"))
        self.OL_refresh.setText(_translate("MainWindow", "Refresh"))
        self.OS_refresh.setText(_translate("MainWindow", "Refresh"))

        ############### Text Box ###############
        self.status_text.setPlainText(_translate("MainWindow", ""))
        self.log_text.setPlainText(_translate("MainWindow", ""))

        ############### Tab ###############
        self.tab_4.setTabText(self.tab_4.indexOf(self.tab), _translate("MainWindow", "main"))
        self.tab_4.setTabText(self.tab_4.indexOf(self.tab_2), _translate("MainWindow", "log"))
        self.tab_4.setTabText(self.tab_4.indexOf(self.tab_3), _translate("MainWindow", "status"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
