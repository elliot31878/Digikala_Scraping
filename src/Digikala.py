from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import re
from bs4 import BeautifulSoup
import sqlite3
from xlsxwriter.workbook import Workbook
#-------------------------------------------------------------
#varible
lst_price=[]
lst_mobile=[]
#-------------------------------------------------------------
#sql
class DataBase(object):
    """
    This Class For Database
    """
    def __init__(self,database_file_name,sql_command):
        self.sql_command=sql_command
        self.database_file_name=database_file_name
        connction=sqlite3.connect(self.database_file_name)
        cursor=connction.cursor()
        cursor.execute(self.sql_command)
        connction.commit()
        connction.close()
    def INSERT(self,sql_command,database_file_name):
        """
        this Function For Insert To DB
        """
        self.sql_command=sql_command
        self.database_file_name=database_file_name
        connction=sqlite3.connect(self.database_file_name)
        cursor=connction.cursor()
        cursor.execute(self.sql_command)
        connction.commit()
        connction.close()
    def ConverDbFileToExcel(self,database_file_name,select_command):
        """
        this Function For Convert To DB
        """
        self.database_file_name=database_file_name
        self.select_command=select_command
        workbook=Workbook("DigiKalaMobile.xlsx")
        worksheet=workbook.add_worksheet()
        connction=sqlite3.connect(self.database_file_name)
        cursor=connction.cursor()
        cursor.execute(self.select_command)
        mysel=cursor.execute(self.select_command)
        for i, row in enumerate(mysel):
            for j, value in enumerate(row):
                worksheet.write(i, j, value)
        workbook.close()
        connction.commit()
        connction.close()
#----------------------------------------------------------------
class Ui_Digikala_Form(object):
    def setupUi(self, Digikala_Form):
        #--------------------Method---------------------------------------
        prog_value=1
        def start():
            """this Function For show ListMobile"""
            for i in range(0,lst_mobile.__len__()):
                self.listWidget.addItem("ردیف : "+str(i)+"  موبایل : "+lst_mobile[i]+"  قیمت : "+lst_price[i])
        def getInfo():
            """
            this function for get information form the site
            """
            global prog_value 
            prog_value=0
            self.progressBar.setVisible(True)
            for i in range(1,6):
                self.progressBar.setProperty("value", prog_value)
                get_requerst=requests.get("https://www.digikala.com/search/category-mobile-phone/?has_selling_stock=1&pageno="+str(i)+"&sortby=21")
                soup=BeautifulSoup(get_requerst.text,"html.parser")
                #
                get_mobile=soup.find_all("div",attrs={"class":"c-product-box__content--row"})
                get_price=soup.find_all("div",attrs={"class":"c-price__value-wrapper"})
                for mobile in get_mobile:
                    if not prog_value>100:
                        prog_value+=1  
                    mobile=mobile.text.strip()
                    lst_mobile.append(mobile)
                for price in get_price:
                    price=re.sub(r"\s","",price.text).strip()
                    lst_price.append(price)
            self.progressBar.setProperty("value", 100)
            self.progressBar.setVisible(False)
            self.pushButton.setEnabled(True)
            self.pushButton_3.setEnabled(True)
           
        
        def toDbAndExcel():
            #this function FOR add information to db and Convert to ExcelFile
            command_create="""
            CREATE TABLE IF NOT EXISTS GOODS (
            id INTIGER PRIMARY KEY,
            gname TEXT,
            gprice TEXT
            );
            """
            self.progressBar.setVisible(True)
            db=DataBase("myTable",command_create)
            for i in range(0,lst_mobile.__len__()):
                if i<100:
                    self.progressBar.setProperty("value", 1+i)
                command_insert="INSERT OR REPLACE  INTO GOODS VALUES ("+str(i)+",'"+lst_mobile[i]+"','"+lst_price[i]+"');"
                db.INSERT(command_insert,"myTable")
            db.ConverDbFileToExcel("myTable","SELECT * FROM GOODS")
            self.progressBar.setProperty("value", 100)
            self.progressBar.setVisible(False)
        #-----------------------------------------------------------------
        Digikala_Form.setObjectName("Digikala_Form")
        Digikala_Form.resize(713, 738)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Digikala_Form.setWindowIcon(icon)
        Digikala_Form.setStyleSheet("background-color: rgb(39, 44, 52);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Digikala_Form)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("assets/digikala.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.listWidget.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(False)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setText("AddToDB & Excle")
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.verticalLayout.addWidget(self.pushButton_3)

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", prog_value)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setVisible(False)
        self.verticalLayout.addWidget(self.progressBar)
        Digikala_Form.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Digikala_Form)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 713, 26))
        self.menubar.setObjectName("menubar")
        Digikala_Form.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Digikala_Form)
        self.statusbar.setObjectName("statusbar")
        Digikala_Form.setStatusBar(self.statusbar)
        self.retranslateUi(Digikala_Form)
        QtCore.QMetaObject.connectSlotsByName(Digikala_Form)
        #setEvents
        self.pushButton_2.clicked.connect(getInfo)
        self.pushButton.clicked.connect(start)
        self.pushButton_3.clicked.connect(toDbAndExcel)

    def retranslateUi(self, Digikala_Form):
        _translate = QtCore.QCoreApplication.translate
        Digikala_Form.setWindowTitle(_translate("Digikala_Form", "Digikala-getInfo"))
        self.pushButton_2.setText(_translate("Digikala_Form", "GetInformation"))
        self.pushButton.setText(_translate("Digikala_Form", "Start"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Digikala_Form = QtWidgets.QMainWindow()
    ui = Ui_Digikala_Form()
    ui.setupUi(Digikala_Form)
    Digikala_Form.show()
    sys.exit(app.exec_())
