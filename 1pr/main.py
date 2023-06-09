import TreeMinMax as t
from PyQt5.QtWidgets import QApplication, QGridLayout, QMainWindow, QFrame, QSizePolicy, QSpinBox, QLabel, QVBoxLayout, QWidget, QTextBrowser, QPushButton, QComboBox, QPlainTextEdit, QMessageBox
from PyQt5.QtCore import  Qt, pyqtSlot, QCoreApplication
import sys
from PyQt5 import QtGui
from IPython import get_ipython
import re

tree=object
    
class Window(QMainWindow):
    textBrowser: QTextBrowser 
    def __init__(self, *args):
        super().__init__()
        self.tree = tree
        self.title = "1. praktiskais darbs Mākslīgā Intelekta Pamatos (3KP)"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
 
 
        self.InitWindow()
 
 
    def InitWindow(self):
        self.xdrawstart = 130
        self.ydrawstart = 0
        self.plotrange = 9999
        self.setWindowIcon(QtGui.QIcon("diskb.ico"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.centralwi = QWidget(self)
        self.sideBar = QFrame()
        self.sideBarLayout = QVBoxLayout()
        self.plotBar = QFrame()
        self.plotBarLayout = QVBoxLayout()
        self.grid = QGridLayout() 
        self.plotdpi = 100
        
        self.moveNr = 0
        self.status = self.tree.struct[0][0].status
        self.backlog = ""

        self.lblxstart = QLabel("sākuma bits:", self)
        self.lblxstart.setGeometry(30, 30+10, 50, 30)
        self.inpxstart = QSpinBox(self)
        self.inpxstart.setMinimum(0)
        self.inpxstart.setMaximum(len(self.status)-2)
        self.inpxstart.setValue(len(self.status)-2)
        self.inpxstart.setGeometry(self.lblxstart.geometry().x()+self.lblxstart.geometry().width(), 30+10, 50, 30)
        self.inpxstart.valueChanged[int].connect(self.valChanged)

        self.lblystart = QLabel("apstiprināt gājienu:", self)
        self.lblystart.setGeometry(30, self.inpxstart.geometry().y()+30+10, 50, 30)
        self.btndomove = QPushButton(self)
        self.btndomove.setText("i e t")
        self.btndomove.setGeometry(self.lblystart.geometry().x()+self.lblystart.geometry().width(), self.inpxstart.geometry().y()+30+10, 50, 30)
        self.btndomove.clicked.connect(self.clickedMove)

        self.lblxend = QLabel("kurš sāk?:", self)
        self.lblxend.setGeometry(30, self.btndomove.geometry().y()+30+10, 50, 30)
        self.ddlwhofirst =  QComboBox(self)
        self.ddlwhofirst.addItem("ES")
        self.ddlwhofirst.addItem("AI")
        self.ddlwhofirst.currentTextChanged[str].connect(self.ddlvalChanged)

        self.lblyend = QLabel("sākuma stāvoklis:", self)
        self.lblyend.setGeometry(30, self.ddlwhofirst.geometry().y()+30+10, 50, 30)
        self.leStatus = QPlainTextEdit(self)
        self.leStatus.setPlainText(self.status)
        self.leStatus.setGeometry(self.lblyend.geometry().x()+self.lblyend.geometry().width(), self.ddlwhofirst.geometry().y()+30+10, 50, 100)
        self.leStatus.textChanged.connect(self.statusChanged)

        self.lblstep = QLabel("apstiprināt:", self)
        self.lblstep.setGeometry(30, self.leStatus.geometry().y()+30+10, 50, 30)
        self.btnStartGame = QPushButton(self)
        self.btnStartGame.setText("jauna spēle!")
        self.btnStartGame.setGeometry(self.lblstep.geometry().x()+self.lblstep.geometry().width(), self.leStatus.geometry().y()+30+10, 50, 30)
        self.btnStartGame.clicked.connect(self.clickedNewGame)

        self.sideBarLayout.addWidget(self.lblxstart)
        self.sideBarLayout.addWidget(self.inpxstart)
        self.sideBarLayout.addWidget(self.lblystart)
        self.sideBarLayout.addWidget(self.btndomove)
        self.sideBarLayout.addWidget(self.lblxend)
        self.sideBarLayout.addWidget(self.ddlwhofirst)
        self.sideBarLayout.addWidget(self.lblyend)
        self.sideBarLayout.addWidget(self.leStatus)
        self.sideBarLayout.addWidget(self.lblstep)
        self.sideBarLayout.addWidget(self.btnStartGame)

        self.sideBarLayout.addStretch()
        self.sideBar.setLayout(self.sideBarLayout)
        self.sideBar.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.textBrowser = QTextBrowser()
        
        self.plotBarLayout.addWidget(self.textBrowser)
        self.plotBar.setLayout(self.plotBarLayout)
        self.plotBar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.grid.addWidget(self.sideBar, 1, 0, 1, 1)
        #self.grid.addWidget(self.toolbar, 0, 1, 1, 1, Qt.AlignLeft)
        self.grid.addWidget(self.plotBar, 1, 1, 1, 1, Qt.AlignLeft)
        self.centralwi.setLayout(self.grid)
        self.setCentralWidget(self.centralwi)
        self.updateGameField()
        #self.textBrowser.setGeometry( self.textBrowser.geometry().x(), self.textBrowser.geometry().y(), 2220, 5220)
        self.show()
    
    def updateGameField(self):
        tex = self.status[0:self.inpxstart.value()]+'<span style="color: red; font-style: italic;">' + \
        self.status[self.inpxstart.value():self.inpxstart.value()+2]+"</span>"+ \
            self.status[self.inpxstart.value()+2:len(self.status)]
        self.textBrowser.setHtml('<h1 style="font-size: 36">'+tex+'</h1> <br />'+ self.backlog)

    @pyqtSlot(int)
    def valChanged(self, value):
        self.updateGameField()
        #self.textBrowser.setMarkdown('# Hello <span style="color:red;">aaa!</span>[asdfasd](http://www.google.com)')
    
    @pyqtSlot()
    def clickedMove(self):
        print("speletajs izdara gajienu")
        if(not t.isvalidmove(self.status,self.inpxstart.value(), self.inpxstart.value()+2)):
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowIcon(QtGui.QIcon("diskb.ico"))
            msgBox.setText("Šis nav derīgs gājiens!")
            msgBox.setStandardButtons(QMessageBox.Ok )
            msgBox.exec()
            return
        newstatus = t.do_move(self.status,self.inpxstart.value(), self.inpxstart.value()+2)
        self.backlog = self.backlog + "<br /> #"+ str(self.moveNr)+"-&gt; <span style='color:#115D08;'>ES</span> :: "+ newstatus
        self.status = newstatus
        self.inpxstart.setMaximum(len(self.status)-2)
        self.updateGameField()
        thenode = t.find_by_status(self.tree, newstatus, self.moveNr+1)
        if(t.is_game_over_for_node(thenode)):
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setWindowTitle("Rezultāts:")
            msgBox.setWindowIcon(QtGui.QIcon("diskb.ico"))
            msgBox.setText("Uzvarēja <br /><span style='color:#F27D00; font-weight: 800; font-size: 26;'>AI</span>" if(thenode.evaluation == 1) else "Uzvarēju <br /><span style='color:#115D08;'>ES</span>" if (thenode.evaluation == -1) else "Neizšķirts")
            msgBox.setStandardButtons(QMessageBox.Ok )
            msgBox.exec()
            self.clickedNewGame()
        else:
            self.moveNr = self.moveNr+1
            self.do_ai_move()
    
    def do_ai_move(self):
            thenode = t.find_by_status(self.tree, self.status, self.moveNr)
            thenode = t.get_a_child_from_childs_with_max_novertejums(thenode)
            self.status = thenode.status
            self.backlog = self.backlog + "<br /> #"+ str(self.moveNr)+"-&gt; <span style='color:#F27D00;'>AI</span> :: "+ self.status
            self.moveNr =self.moveNr+1
            self.inpxstart.setMaximum(len(self.status)-2)
            self.updateGameField()
            if(t.is_game_over_for_node(thenode)):
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setWindowTitle("Rezultāts:")
                msgBox.setWindowIcon(QtGui.QIcon("diskb.ico"))
                msgBox.setText("Uzvarēja <br /><span style='color:#F27D00; font-weight: 800; font-size: 26;'>AI</span>" if(thenode.evaluation == 1) else "Uzvarēju <br /><span style='color:#115D08;'>ES</span>" if (thenode.evaluation == -1) else "Neizšķirts")
                msgBox.setStandardButtons(QMessageBox.Ok )
                msgBox.exec()
                self.clickedNewGame()
                
    
    @pyqtSlot()
    def clickedNewGame(self):
        print("~~~~~~~~~~~~~~~jauna spēle~~~~~~~~~~~~~~~~~~")
        self.moveNr = 0
        self.backlog = ""
        n = t.tree.root_node_factory(self.leStatus.toPlainText ())
        thetree = t.populate(n)
        self.tree = thetree
        self.status = self.tree.struct[0][0].status
        self.inpxstart.setMaximum(len(self.status)-2)
        self.tree.a_log_of_tree()
        t.do_action_to_subnodes_and_this(n, t.try_set_novertejumu, self.ddlwhofirst.currentText()=="AI")
        self.tree.a_log_of_tree()
        if(self.ddlwhofirst.currentText()=="AI"):
            self.do_ai_move()
        else:
            self.updateGameField()
    
    @pyqtSlot(str)
    def ddlvalChanged(self, string):
        print(string)
    
    @pyqtSlot()
    def statusChanged(self):
        currtext = self.leStatus.toPlainText ()
        replacedtx = re.sub('[^01]', '', currtext)
        if(currtext != replacedtx):
            self.leStatus.setPlainText(replacedtx)
        print("startStatus ->:>:> "+self.leStatus.toPlainText ())

def main():
    global tree
    n = t.tree.root_node_factory("110010")
    thetree = t.populate(n)
    tree = thetree
    #default is ES therefore minimiser.
    t.do_action_to_subnodes_and_this(n, t.try_set_novertejumu, False)
    tree.a_log_of_tree()

    if get_ipython():
        App = QCoreApplication.instance()
        if App is None:
            App = QApplication(sys.argv)
    else:
        App =  QApplication(sys.argv)
    window = Window()
    #lai izietu no loopa vajag sys.exit https://stackoverflow.com/a/38285497/16769661
    # quit : It's good practice to always connect signals to this slot using a QueuedConnection. If a signal connected (non-queued) to this slot is emitted before control enters the main event loop (such as before "int main" calls exec()), the slot has no effect and the application never exits. 
    # exit : It's good practice to always connect signals to this slot using a QueuedConnection. If a signal connected (non-queued) to this slot is emitted before control enters the main event loop (such as before "int main" calls exec()), the slot has no effect and the application never exits.
    # tagad paliks atmiņā ja ipythonā palaista.. bet nemetīs kļūtu toties :D
    if get_ipython():
        QApplication.setQuitOnLastWindowClosed(True)
        App.exec()
    else:
        sys.exit(App.exec())
    
    
if __name__ == "__main__":
    main()