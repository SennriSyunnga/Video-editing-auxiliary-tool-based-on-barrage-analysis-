#!/usr/bin/env python
import sys
from PySide2.QtWidgets import QMainWindow,QApplication
from sideui import Ui_MainWindow
from subprocess import Popen,PIPE,STDOUT

class MyUi(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.setup()
    def setup(self):
        self.group = ''
        return 0
        
    def checkBox_On(self):
        if self.checkBox.isChecked():
            self.lineEdit_4.setText('1')
            self.lineEdit_5.setText('1')
            self.group = '1'
        else :self.group = ''
        
    def resetButton_Click(self):
        self.lineEdit_1.setText("danmu.xml")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("kksk")
        self.lineEdit_4.setText("14")
        self.lineEdit_5.setText("20")
        self.textEdit.clear()
        self.progressBar.setValue(0)
        self.checkBox.setChecked(False)
        self.group = ''


    #实现pushButton_click()函数，textEdit是我们放上去的文本框的id
    def pushButton_Click(self):
        self.textEdit.clear()
        self.inputfile=self.lineEdit_1.text()
        self.outputfile=self.lineEdit_2.text()
        self.keyword=self.lineEdit_3.text()
        self.limit=self.lineEdit_4.text()
        self.interval=self.lineEdit_5.text()
        cmd = r'.\read_kksk_from_text.exe'
        #cmd='python read_kksk_from_text.py'
        if self.outputfile:
            cmd = cmd + ' -o ' + self.outputfile
        if self.inputfile:
            cmd = cmd + ' -i ' + self.inputfile
        if self.keyword:
            cmd = cmd + ' -w ' + self.keyword
        if self.limit:
            cmd = cmd + ' -l ' + self.limit
        if self.interval:
            cmd = cmd + ' -v ' + self.interval
        if self.group:
            cmd = cmd + ' -g ' + self.group
        cmd += ' -f 1'
        #logger.warning(cmd)
        #cmd.replace("\\","\\").replace('\t','\\t')#这句并没有执行，但是需不需要执行呢？
        #p = Popen(cmd,stdout=PIPE,stdin=PIPE,stderr=STDOUT)
        s=Popen(cmd,bufsize=0,stdout=PIPE,stdin=PIPE,stderr=STDOUT,universal_newlines=True)
        self.progressBar.setMaximum(int(s.stdout.readline()))
        while True:
            nextline=s.stdout.readline().strip()
            if nextline == '':
                break
            self.progressBar.setValue(int(nextline))
            nextline=s.stdout.readline()
            self.textEdit.append(nextline.strip())
            QApplication.processEvents()    
        self.progressBar.setValue(self.progressBar.maximum())#结束时将进度条置为满状态
        self.textEdit.append('Done.')
        return None

if __name__ == '__main__':
    '''import logging
    logger = logging.getLogger(__name__)
    logger.setLevel(level = logging.INFO)
    handler = logging.FileHandler("log.txt")
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    logger.addHandler(handler)
    logger.addHandler(console)
    logger.info("Start print log")
    logger.debug("Do something")
    logger.warning("Something maybe fail.")
    logger.info("Finish")'''
    
    app = QApplication(sys.argv)
    ui = MyUi()
    sys.exit(app.exec_())
