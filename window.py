"""import sys
from PyQt5 import QtGui,QtCore
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from subprocess import Popen
import os

class gui(QMainWindow):
      def __init__(self):
         super(gui, self).__init__()
         self.initUI()

      def dataReady(self):
         cursor = self.output.textCursor()
         cursor.movePosition(cursor.End)
         #cursor.insertText(str(self.process.readAll()))
         cursor.insertText(self.process.readAll().data().decode())
         self.output.ensureCursorVisible()

      def callProgram(self):
         # run the process
         # `start` takes the exec and a list of arguments
         self.process.start('python',['-u','coordinateTesting.py'])

      def stopProgram(self):
         self.process.start.terminate()
         print("Stopped Script")  

      def initUI(self):
         # Layout are better for placing widgets
         layout =  QHBoxLayout()
         self.startButton =  QPushButton('Start')
         self.startButton.clicked.connect(self.callProgram)

         self.stopButton = QPushButton('Stop')
         self.stopButton.clicked.connect(self.stopProgram)

         self.output =  QTextEdit()
         self.setGeometry(400, 60, 400, 400)
         layout.addWidget(self.output)
         layout.addWidget(self.startButton)
         layout.addWidget(self.stopButton)

         centralWidget =  QWidget()
         centralWidget.setLayout(layout)
         self.setCentralWidget(centralWidget)

         # QProcess object for external app
         self.process = QtCore.QProcess(self)
         # QProcess emits `readyRead` when there is data to be read
         self.process.readyRead.connect(self.dataReady)

         # Just to prevent accidentally running multiple times
         # Disable the button when process starts, and enable it when it finishes
         self.process.started.connect(lambda: self.startButton.setEnabled(False))
         self.process.finished.connect(lambda: self.startButton.setEnabled(True))



#Function Main Start
def main():
    app =QApplication(sys.argv)
    ui=gui()
    ui.show()
    sys.exit(app.exec_())
#Function Main END

if __name__ == '__main__':
    main() """





from tkinter import *
from tkinter.ttk import *
from subprocess import Popen
import os
import sys



def loop():
    with open("log.txt", "r") as t:
        Results.config(text=t.read())
    gui.after(500, loop) # run every 500 milliseconds



gui = Tk()
gui.title('Account Changer Testing')
gui.geometry("400x400")

def passStart():
    global process
    print("Starting Pass Farming..")
    process = Popen(["python", "coordinateTesting.py"])

def passStop():
    process.terminate()
    print("Stopped Script")
 
 
#text_box = Text(gui, wrap='word', height = 20, width = 47)
#text_box.place(x = 10, y = 80)


Results = Label(gui, text = "test")
Results.place(x = 10, y = 80)

#def redirector(inputStr):
    #text_box.insert(INSERT, inputStr)

#sys.stdout.write = redirector #whenever sys.stdout.write is called, redirector is called.



startButton = Button (gui, text = "Start", width = 10, command = passStart)
startButton.place(x = 10, y = 10)


stopButton = Button (gui, text = "Stop", width = 10, command = passStop)
stopButton.place(x = 100, y = 10)


loop()
gui.mainloop()
