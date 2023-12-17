from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QColorDialog
import sys


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('task5.ui', self)
        self.setFixedSize(350, 290)

        self.checkbox_actions = {
            'firstBox': self.change_color,
            'secondBox': self.change_text,
            'thirdBox': self.enlarge_button,
            'fourthBox': self.hide_button,
            'fifthBox': self.set_inactive
        }
        
        for checkbox, action in self.checkbox_actions.items():
            getattr(self, checkbox).stateChanged.connect(action)

    def change_color(self):
        if self.firstBox.isChecked():
            color = QColorDialog.getColor()
            self.pushButton.setStyleSheet(f'background-color: {color.name()}')
        else:
            self.pushButton.setStyleSheet('QPushButton {background-color: #fdfdfd}')

    def change_text(self):
        if self.secondBox.isChecked():
            self.pushButton.setText('New Text')
        else:
            self.pushButton.setText('Accept')

    def enlarge_button(self):
        if self.thirdBox.isChecked():
            self.pushButton.setGeometry(120, 200, 186, 56)
        else:
            self.pushButton.setGeometry(120, 200, 93, 28)

    def hide_button(self):
        if self.fourthBox.isChecked():
            self.pushButton.setHidden(True)
        else:
            self.pushButton.setHidden(False)

    def set_inactive(self):
        if self.fifthBox.isChecked():
            self.pushButton.setEnabled(False)
        else:
            self.pushButton.setEnabled(True)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
