import TreeMinMax as t
from PyQt5.QtWidgets import QApplication, QGridLayout, QMainWindow, QFrame, QSizePolicy, QSpinBox, QLabel, QVBoxLayout, QWidget, QTextBrowser, QPushButton, QComboBox, QPlainTextEdit
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
        self.title = "Kursa darbs 1. variants 3.risinājuma POC"
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

        self.lblxstart = QLabel("sākuma bits:", self)
        self.lblxstart.setGeometry(30, 30+10, 50, 30)
        self.inpxstart = QSpinBox(self)
        self.inpxstart.setMinimum(0)
        self.inpxstart.setMaximum(len(self.tree.struct[0][0].status)-2)
        self.inpxstart.setValue(150)
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
        self.leStatus.setPlainText(self.tree.struct[0][0].status)
        self.leStatus.setGeometry(self.lblyend.geometry().x()+self.lblyend.geometry().width(), self.ddlwhofirst.geometry().y()+30+10, 50, 100)
        self.leStatus.textChanged.connect(self.statusChanged)

        self.lblstep = QLabel("solis:", self)
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
        #self.textBrowser.setGeometry( self.textBrowser.geometry().x(), self.textBrowser.geometry().y(), 2220, 5220)
        self.show()

    @pyqtSlot(int)
    def valChanged(self, value):
        tex = self.tree.struct[0][0].status[0:self.inpxstart.value()]+'<span style="color: red; font-style: italic;">' + \
        self.tree.struct[0][0].status[self.inpxstart.value():self.inpxstart.value()+2]+"</span>"+ \
            self.tree.struct[0][0].status[self.inpxstart.value()+2:len(self.tree.struct[0][0].status)]
        self.textBrowser.setHtml('<h1 style="font-size: 36">'+tex+'</h1> <br /> # Varbūt gājinu vēsture?? <span style="color:red;">aaa!</span>[asdfasd] <a href="http://www.google.com">hmm</a>')
        #self.textBrowser.setMarkdown('# Hello <span style="color:red;">aaa!</span>[asdfasd](http://www.google.com)')
    
    @pyqtSlot()
    def clickedMove(self):
        print("speletajs izdara gajienu")
    
    @pyqtSlot()
    def clickedNewGame(self):
        print("~~~jauna spēle~~")
    
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
    n = t.node()
    n.letter = t.ord(0)
    n.status="110010"
    thetree = t.populate(n)
    tree = thetree
    t.do_action_to_subnodes_and_this(n, t.try_set_novertejumu, True)
    for nd, kv in thetree.struct.items():
        for k, v in kv.items():
            a =""
            for cn in v.children:
                a+= " ("+str(cn.level)+":"+str(cn.location)+") "
            print(v.letter+"|"+str(v.level)+":"+str(v.location)+"|"+" -> "+v.status+" "+("["+str(v.evaluation)+"]" if hasattr(v, 'evaluation') else "")+a)
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