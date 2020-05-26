#!/usr/bin/env python
# 程序的GUI界面功能实现代码，也是主程序，实现了界面定义和功能的分离
# sideui文件只是ui的基础模板。这个才是用户真正使用的gui文件。
# PySide2为第三方库，需要自行通过pip3下载，这里推荐镜像站如:
# pip3 install Pyside2-tools -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
# pyside2的许多模块所在位置和pyqt5不同。同名类包含的子函数也不尽相同，在触类旁通时需要注意。
# pyside2和pyqt5其实我都用过，ui文件是通用的。前者教程少，后者教程多但是问题解决不了，所以退而求其次用了前者。

import sys
from PySide2.QtWidgets import QMainWindow, QApplication
from sideui import Ui_MainWindow  # 导入pyside2 designer设计出的sideui文件作为模板
# 由于designer设计出来的.ui文件需要经过pyside2-uic进行转换，并不包含一切自定义的函数功能
# 将类模板分离作为父类，可以使得函数实现相对独立，修改ui界面重新转换不会影响到已有的函数实现。
from subprocess import Popen, PIPE, STDOUT  # 子进程相关，用于开启主程序


class MyUi(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.setup()
    
    def setup(self):
        self.group = ''
        return 0
    
    def checkBox_On(self):  # 勾选后置为弹幕搜索模式
        if self.checkBox.isChecked():
            self.lineEdit_4.setText('1')
            self.lineEdit_5.setText('1')
            self.group = '1'
        else:
            self.group = ''  # 反选后将group属性清空（恢复回默认值）
    
    def resetButton_Click(self):  # 重置按钮，恢复成初始状态
        self.lineEdit_1.setText("danmu.xml")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("kksk")
        self.lineEdit_4.setText("14")
        self.lineEdit_5.setText("20")
        self.textEdit.clear()
        self.progressBar.setValue(0)
        self.checkBox.setChecked(False)
        self.group = ''
    
    # 实现sideui.py文件声明的pushButton_click()函数，textEdit是界面中预定要输出时间轴的文本框位置
    def pushButton_Click(self):
        self.textEdit.clear()
        # 读入以下文本
        self.inputfile = self.lineEdit_1.text()
        self.outputfile = self.lineEdit_2.text()
        self.keyword = self.lineEdit_3.text()
        self.limit = self.lineEdit_4.text()
        self.interval = self.lineEdit_5.text()
        cmd = r'.\read_kksk_from_text.exe'  # 虽然这句话已经写死了，本来应该放在初始化语句中，但是放在这里未来还有改动余地
        # cmd='python read_kksk_from_text.py'
        # 当你没有把read_kksk_from_text.py转换成exe文件时，请注释掉上一行，改用下面这一行。
        
        # 以下为全局属性赋值
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
        # logger.warning(cmd)
        # cmd.replace("\\","\\").replace('\t','\\t')#这句并没有执行，但是需不需要执行呢？
        s = Popen(cmd, bufsize=0, stdout=PIPE, stdin=PIPE, stderr=STDOUT, universal_newlines=True)
        self.progressBar.setMaximum(int(s.stdout.readline()))
        while True:
            nextline = s.stdout.readline().strip()  # 去除开头和末尾的空白和换行
            if nextline == '':  # 读到文件尾
                break
            self.progressBar.setValue(int(nextline))
            nextline = s.stdout.readline()
            self.textEdit.append(nextline.strip())
            QApplication.processEvents()  # 用于实时显示当前进度条和文本框的更新状况
        self.progressBar.setValue(self.progressBar.maximum())  # 结束时将进度条置为满状态
        self.textEdit.append('Done.')  # 在时间轴末尾发送一条消息，供用户判断读取分析已结束
        # 主要用于让用户能够区分程序进行中和程序虽然结束无满足条件的结果时的程序状态。
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
    # 以上为调试模板，暂时不作使用
    app = QApplication(sys.argv)
    ui = MyUi()
    sys.exit(app.exec_())
