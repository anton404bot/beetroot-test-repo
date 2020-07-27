from PyQt5 import (QtCore,
                   QtWidgets,
                   QtSql,
                   QtGui)
import sys

app = QtWidgets.QApplication(sys.argv)


class Form(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.id = QtWidgets.QLineEdit()
        self.id.setObjectName('id')
        self.id.setText('ID (int)')

        self.fn = QtWidgets.QLineEdit()
        self.fn.setObjectName("firstname")
        self.fn.setText("First name")

        self.ln = QtWidgets.QLineEdit()
        self.ln.setObjectName("lastname")
        self.ln.setText("Last name")

        self.dob = QtWidgets.QLineEdit()
        self.dob.setInputMask('D999.B9.99;_')
        self.dob.setObjectName('dob')



        self.submit = QtWidgets.QPushButton()
        self.submit.setObjectName("submit")
        self.submit.setText("Submit")

        layout = QtWidgets.QFormLayout()
        layout.addWidget(self.id)
        layout.addWidget(self.fn)
        layout.addWidget(self.ln)
        layout.addWidget(self.dob)
        layout.addWidget(self.submit)

        self.setLayout(layout)
        self.submit.clicked.connect(self.button_click)

        self.setWindowTitle("Add to PG")

    def button_click(self):
        idstring = self.id.text()
        fnstring = self.fn.text()
        lnstring = self.ln.text()
        dobstring = self.dob.text()
        request = "INSERT INTO public.person (id, first_name, last_name, dob) VALUES('" + idstring + "','" + fnstring + "','" + lnstring + "','" + dobstring +"');"
        print(request)

        db = QtSql.QSqlDatabase.addDatabase("QPSQL")
        db.setHostName('localhost')
        db.setPort(5433)
        db.setDatabaseName('postgres')
        db.setUserName('postgres')
        db.setPassword('postgres')
        if db.isOpen():
            db.close()
        if not db.open():
            raise Exception("Error opening database: {0}".format(db.lastError().text()))
        query = QtSql.QSqlQuery()
        query.exec_(request)


form = Form()


def create_form():
    form.show()


def refresh():
    sqm.setQuery('SELECT * FROM public.person ORDER by last_name')


table = QtWidgets.QTableView()
table.setWindowTitle('QSqlQueryModel')

con = QtSql.QSqlDatabase.addDatabase('QPSQL')
con.setDatabaseName('postgres')
con.setHostName('127.0.0.1')
con.setUserName('postgres')
con.setPassword('postgres')
con.setPort(5433)
con.open()

sqm = QtSql.QSqlQueryModel(parent=table)
refresh()

sqm.setHeaderData(0, QtCore.Qt.Horizontal, 'First Name')
sqm.setHeaderData(1, QtCore.Qt.Horizontal, 'Last Name')
sqm.setHeaderData(2, QtCore.Qt.Horizontal, 'Date of birth')
sqm.setHeaderData(3, QtCore.Qt.Horizontal, 'ID')

btnCreate = QtWidgets.QPushButton('Create')
btnCreate.clicked.connect(create_form)

form.submit.clicked.connect(refresh)

table.setModel(sqm)
table.setColumnWidth(0, 66)
table.setColumnWidth(1, 150)
table.setColumnWidth(2, 90)
table.setColumnWidth(3, 44)

table.resize(370, 200)

hbox = QtWidgets.QVBoxLayout()
hbox.addWidget(table)
hbox.addWidget(btnCreate)

window = QtWidgets.QWidget()
window.setLayout(hbox)
window.resize(400, 444)

ico = QtGui.QIcon('sun.png')
window.setWindowIcon(ico)
app.setWindowIcon(ico)

window.show()
sys.exit(app.exec())
