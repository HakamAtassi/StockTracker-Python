import yfinance as yf
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QApplication, QMainWindow
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sys

tickerSymbol = 'BTC-USD'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1m')

currentPrice= str(list(tickerDf['Close'])).strip("[]")







class Ui_MainWindow(object):




    def setupUi(self, MainWindow):




        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stock = QtWidgets.QLabel(self.centralwidget)
        self.stock.setGeometry(QtCore.QRect(20, 40, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stock.setFont(font)
        self.stock.setObjectName("stock")
        self.refreshButton = QtWidgets.QPushButton(self.centralwidget)
        self.refreshButton.setGeometry(QtCore.QRect(320, 480, 151, 61))
        self.refreshButton.setObjectName("refreshButton")
        self.promptText = QtWidgets.QLabel(self.centralwidget)
        self.promptText.setGeometry(QtCore.QRect(10, 390, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.promptText.setFont(font)
        self.promptText.setObjectName("promptText")
        self.priceBox = QtWidgets.QLabel(self.centralwidget)
        self.priceBox.setGeometry(QtCore.QRect(80, 40, 170, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.priceBox.setFont(font)
        self.priceBox.setObjectName("priceBox")
        self.newTicker = QtWidgets.QLineEdit(self.centralwidget)
        self.newTicker.setGeometry(QtCore.QRect(10, 430, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.newTicker.setFont(font)
        self.newTicker.setObjectName("newTicker")
        self.estimateValue = QtWidgets.QLineEdit(self.centralwidget)
        self.estimateValue.setGeometry(QtCore.QRect(420, 70, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.estimateValue.setFont(font)
        self.estimateValue.setObjectName("estimateValue")
        self.inputBitcoin = QtWidgets.QLabel(self.centralwidget)
        self.inputBitcoin.setGeometry(QtCore.QRect(420,40, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inputBitcoin.setFont(font)
        self.inputBitcoin.setObjectName("inputBitcoin")
        self.bitcoinValue = QtWidgets.QLabel(self.centralwidget)
        self.bitcoinValue.setGeometry(QtCore.QRect(420, 110, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bitcoinValue.setFont(font)
        self.bitcoinValue.setText("")
        self.bitcoinValue.setObjectName("bitcoinValue")
        self.getBTCButton = QtWidgets.QPushButton(self.centralwidget)
        self.getBTCButton.setGeometry(QtCore.QRect(690, 80, 71, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.getBTCButton.setFont(font)
        self.getBTCButton.setObjectName("getBTCButton")
        self.AddTickerButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddTickerButton.setGeometry(QtCore.QRect(10, 470, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.AddTickerButton.setFont(font)
        self.AddTickerButton.setObjectName("AddTickerButton")
        self.Ticker2 = QtWidgets.QLabel(self.centralwidget)
        self.Ticker2.setGeometry(QtCore.QRect(20, 80, 100, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Ticker2.setFont(font)
        self.Ticker2.setText("")
        self.Ticker2.setObjectName("Ticker2")
        self.Ticker3 = QtWidgets.QLabel(self.centralwidget)
        self.Ticker3.setGeometry(QtCore.QRect(20, 120, 100, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Ticker3.setFont(font)
        self.Ticker3.setText("")
        self.Ticker3.setObjectName("Ticker3")
        self.Ticker4 = QtWidgets.QLabel(self.centralwidget)
        self.Ticker4.setGeometry(QtCore.QRect(20, 160, 100, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Ticker4.setFont(font)
        self.Ticker4.setText("")
        self.Ticker4.setObjectName("Ticker4")
        self.Ticker5 = QtWidgets.QLabel(self.centralwidget)
        self.Ticker5.setGeometry(QtCore.QRect(20, 200, 100, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Ticker5.setFont(font)
        self.Ticker5.setText("")
        self.Ticker5.setObjectName("Ticker5")
        self.Ticker6 = QtWidgets.QLabel(self.centralwidget)
        self.Ticker6.setGeometry(QtCore.QRect(20, 240, 100, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Ticker6.setFont(font)
        self.Ticker6.setText("")
        self.Ticker6.setObjectName("Ticker6")
        self.Ticker7 = QtWidgets.QLabel(self.centralwidget)
        self.Ticker7.setGeometry(QtCore.QRect(20, 280, 100, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Ticker7.setFont(font)
        self.Ticker7.setText("")
        self.Ticker7.setObjectName("Ticker7")
        self.TickerPrice6 = QtWidgets.QLabel(self.centralwidget)
        self.TickerPrice6.setGeometry(QtCore.QRect(150, 240, 100, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TickerPrice6.setFont(font)
        self.TickerPrice6.setText("")
        self.TickerPrice6.setObjectName("TickerPrice6")
        self.TickerPrice5 = QtWidgets.QLabel(self.centralwidget)
        self.TickerPrice5.setGeometry(QtCore.QRect(150, 200, 100, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TickerPrice5.setFont(font)
        self.TickerPrice5.setText("")
        self.TickerPrice5.setObjectName("TickerPrice5")
        self.TickerPrice4 = QtWidgets.QLabel(self.centralwidget)
        self.TickerPrice4.setGeometry(QtCore.QRect(150, 160, 100, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TickerPrice4.setFont(font)
        self.TickerPrice4.setText("")
        self.TickerPrice4.setObjectName("TickerPrice4")
        self.TickerPrice2 = QtWidgets.QLabel(self.centralwidget)
        self.TickerPrice2.setGeometry(QtCore.QRect(150, 80, 100, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TickerPrice2.setFont(font)
        self.TickerPrice2.setText("")
        self.TickerPrice2.setObjectName("TickerPrice2")
        self.TickerPrice7 = QtWidgets.QLabel(self.centralwidget)
        self.TickerPrice7.setGeometry(QtCore.QRect(150, 280, 100, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TickerPrice7.setFont(font)
        self.TickerPrice7.setText("")
        self.TickerPrice7.setObjectName("TickerPrice7")
        self.TickerPrice3 = QtWidgets.QLabel(self.centralwidget)
        self.TickerPrice3.setGeometry(QtCore.QRect(150, 120, 100, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TickerPrice3.setFont(font)
        self.TickerPrice3.setText("")
        self.TickerPrice3.setObjectName("TickerPrice3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)




        """"mat plot lib stuff"""
        #TODO: Embed matplot lib into actual application and retrieve data from Yfinance




        #click events
        self.refreshButton.clicked.connect(self.clickedRefresh)
        self.getBTCButton.clicked.connect(self.takeinputs)
        self.AddTickerButton.clicked.connect(self.addTicker)

        self.counter=0
        self.allTickers = []
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.stock.setText(_translate("MainWindow", "Bitcoin:"))
        self.refreshButton.setText(_translate("MainWindow", "Refresh"))
        self.promptText.setText(_translate("MainWindow", "Input new Ticker symbol (eg. AAPL):"))
        self.priceBox.setText(_translate("MainWindow", "$"+currentPrice+"/BTC"))
        self.inputBitcoin.setText(_translate("MainWindow", "Input BTC amount for estimate: "))
        self.getBTCButton.setText(_translate("MainWindow", "Caclulate"))
        self.AddTickerButton.setText(_translate("MainWindow", "Add Asset"))

    def takeinputs(self):
        bitcoinAmount = float(self.estimateValue.text())
        bitcoinWorth=str(float(bitcoinAmount)*float(currentPrice))
        self.bitcoinValue.setText("$"+bitcoinWorth)
        print(bitcoinAmount)
        newTicker=str(self.newTicker.text())



    def addTicker(self):
        newTickerStr = str(self.newTicker.text())


        self.allTickers.append(newTickerStr)
        print("New ticker added",self.allTickers)
        newTickerData=yf.Ticker(self.allTickers[self.counter])
        newTickerDf = newTickerData.history(period='1m')
        self.CurrentPrice = str(list(newTickerDf['Close'])).strip("[]")



        print(self.allTickers)


        if self.counter ==0:
            self.TickerPrice2.setText("$"+self.CurrentPrice[0:8])
            self.Ticker2.setText(self.allTickers[self.counter])
        if self.counter ==1:
            self.TickerPrice3.setText("$"+self.CurrentPrice[0:8])
            self.Ticker3.setText(self.allTickers[self.counter])
        if self.counter ==2:
            self.TickerPrice4.setText("$"+self.CurrentPrice[0:8])
            self.Ticker4.setText(self.allTickers[self.counter])
        if self.counter ==3:
            self.TickerPrice5.setText("$"+self.CurrentPrice[0:8])
            self.Ticker5.setText(self.allTickers[self.counter])
        if self.counter ==4:
            self.TickerPrice6.setText("$"+self.CurrentPrice[0:8])
            self.Ticker6.setText(self.allTickers[self.counter])
        if self.counter ==5:
            self.TickerPrice7.setText("$"+self.CurrentPrice[0:8])
            self.Ticker7.setText(self.allTickers[self.counter])

        self.counter += 1

    def clickedRefresh(self):

        refreshTickerData = yf.Ticker("BTC-USD")
        refreshTickerDf = refreshTickerData.history(period='1m')
        refreshCurrentPrice = str(list(refreshTickerDf['Close'])).strip("[]")
        self.priceBox.setText("$" + refreshCurrentPrice+"/BTC")
        print("bitcoin refreshed")

        for i in range(len(self.allTickers)):

            if i==0:
                refreshTickerData = yf.Ticker(self.allTickers[i])
                refreshTickerDf = refreshTickerData.history(period='1m')
                refreshCurrentPrice = str(list(refreshTickerDf['Close'])).strip("[]")
                self.TickerPrice2.setText("$"+refreshCurrentPrice[0:8])
                print(refreshCurrentPrice)
            if i == 1:
                refreshTickerData = yf.Ticker(self.allTickers[i])
                refreshTickerDf = refreshTickerData.history(period='1m')
                refreshCurrentPrice = str(list(refreshTickerDf['Close'])).strip("[]")
                self.TickerPrice3.setText("$" + refreshCurrentPrice[0:8])
                print(refreshCurrentPrice)
            if i == 2:
                refreshTickerData = yf.Ticker(self.allTickers[i])
                refreshTickerDf = refreshTickerData.history(period='1m')
                refreshCurrentPrice = str(list(refreshTickerDf['Close'])).strip("[]")
                self.TickerPrice4.setText("$" + refreshCurrentPrice[0:8])
                print(refreshCurrentPrice)
            if i == 3:
                refreshTickerData = yf.Ticker(self.allTickers[i])
                refreshTickerDf = refreshTickerData.history(period='1m')
                refreshCurrentPrice = str(list(refreshTickerDf['Close'])).strip("[]")
                self.TickerPrice5.setText("$" + refreshCurrentPrice[0:8])
                print(refreshCurrentPrice)
            if i == 4:
                refreshTickerData = yf.Ticker(self.allTickers[i])
                refreshTickerDf = refreshTickerData.history(period='1m')
                refreshCurrentPrice = str(list(refreshTickerDf['Close'])).strip("[]")
                self.TickerPrice6.setText("$" + refreshCurrentPrice[0:8])
                print(refreshCurrentPrice)
            if i == 5:
                refreshTickerData = yf.Ticker(self.allTickers[i])
                refreshTickerDf = refreshTickerData.history(period='1m')
                refreshCurrentPrice = str(list(refreshTickerDf['Close'])).strip("[]")
                self.TickerPrice7.setText("$" + refreshCurrentPrice[0:8])
                print(refreshCurrentPrice)







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



