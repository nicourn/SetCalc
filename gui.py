from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QApplication, QLineEdit
from main import get_data
class Calc:
    def __init__(self):
        self.wind = QWidget()
        self.label = QLabel("Hi")
        self.input = QLineEdit()
        self.btn = QPushButton("Go!")
        self.btn.clicked.connect(self.hello)
        layaot = QVBoxLayout()
        layaot.addWidget(self.label)
        layaot.addWidget(self.input)
        layaot.addWidget(self.btn)
        self.wind.setLayout(layaot)
        self.wind.setWindowTitle("Calc")
        self.wind.move(600, 300)
        self.wind.show()
    
    def hello(self):
        line = "There are some err"
        try: 
            line = get_data(self.input.text().strip())
        except:
            pass
        self.input.setText("")
        self.label.setText(str(line))
        

app = QApplication([])
c = Calc()
app.exec()