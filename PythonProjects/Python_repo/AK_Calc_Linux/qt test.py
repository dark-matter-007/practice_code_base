import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel,  QPushButton, QRadioButton

# or
# from PySide2.QtWidgets import QApplication, QMainWindow, QLabel

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("My App")
window.setGeometry(100, 100, 400, 300)

label = QLabel("Hello, World!", window)
label.move(100, 100)

button = QPushButton(window, text="Button1")
button.text = "Button"
button.move(100,50)

button2 = QPushButton(window)
button2.move(100,150)

window.show()

sys.exit(app.exec_())
