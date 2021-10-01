from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QApplication, QLineEdit, QScrollArea, QFrame, QScrollBar
from main import get_data


class Calc:
    def __init__(self):
        self.wind = QWidget()
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        wind = QWidget()
        self.lay = QVBoxLayout()
        wind.setLayout(self.lay)
        scroll.setWidget(wind)
        self.lay.addWidget(QLabel("Hello from SetCalc\n\
The universal set: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']"))
        self.scroll = scroll
        self.input = QLineEdit()
        self.btn = QPushButton("Go!")
        self.btn.clicked.connect(self.hello)
        layaot = QVBoxLayout()
        layaot.addWidget(scroll)
        layaot.addWidget(self.input)
        layaot.addWidget(self.btn)
        self.wind.setMinimumSize(300, 400)
        self.wind.setLayout(layaot)
        self.wind.setWindowTitle("Calc")
        self.wind.move(300, 100)
        self.wind.show()

    def hello(self):
        line = "There are some err"
        try:
            line = get_data(self.input.text().strip())
        except:
            pass
        self.input.setText("")
        l = QLabel(str(line))
        self.lay.insertWidget(0, l)


app = QApplication([])
c = Calc()
app.exec()
