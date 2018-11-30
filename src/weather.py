# -*- coding: utf-8 -*-

"""
查询天气小demo
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_weather import Ui_MainWindow
import sys
import requests

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        """
        super(MainWindow, self).__init__(parent)
        #self.setupUi(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
       查询天气
        """
        print('*查询天气')
        cityName = self.ui.comboBox.currentText()
        cityId = self.transCityName(cityName)
        rep = requests.get('http://www.weather.com.cn/data/sk/'+ cityId +'.html')
        rep.encoding = 'utf-8'
        print(rep.json())
         
        msg1 = '城市：%s' % rep.json()['weatherinfo']['city'] +'\n'
        msg2 = '风向：%s' % rep.json()['weatherinfo']['WD'] +'\n'
        msg3 = '温度：%s' % rep.json()['weatherinfo']['temp'] +'度' +'\n'
        msg4 = '风力：%s' % rep.json()['weatherinfo']['WS'] +'\n'
        msg5 = '湿度：%s' % rep.json()['weatherinfo']['SD'] +'\n'
         
        result = msg1 + msg2 + msg3 + msg4 + msg5
        self.ui.textEdit.setText(result)
    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
                清除文本内容
        """
        self.ui.textEdit.clear()

      
    
    def transCityName(self,cityName):
        cityId = ''
        if cityName == '北京' :
            cityId  = '101010100'
        elif cityName == '天津':
            cityId = '101030100'
        elif cityName =='上海':
            cityId = '101020100'
        return cityId
        
     
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
