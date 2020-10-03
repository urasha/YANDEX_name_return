import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic


class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('person.ui', self)
        self.pushButton.clicked.connect(self.set_candels)
        self.pushButton_2.clicked.connect(self.take_rocks)

    def set_candels(self):
        self.number = int(self.spinBox.text())
        self.lcdNumber.display(self.number)
        self.plainTextEdit.clear()
        self.label_3.setText('Победил: ____________')

    def take_rocks(self):
        self.computer_number = self.number if self.number in range(1, 4) else random.randint(1, 3)
        try:
            self.player_number = int(self.lineEdit.text())
            if self.player_number > 3 or self.player_number < 1:
                raise Exception

            self.number -= self.computer_number
            self.lcdNumber.display(self.number if self.number > 0 else 0)

            if not self.check_win():
                self.label_3.setText('Победил: компьютер')
                if not self.plainTextEdit.isReadOnly():
                    self.plainTextEdit.appendPlainText(f'ИИ взял - {self.computer_number}')
                    self.plainTextEdit.setReadOnly(True)
                return

            self.number -= self.player_number
            self.lcdNumber.display(self.number if self.number > 0 else 0)

            if not self.check_win():
                self.label_3.setText('Победил: игрок')
                self.plainTextEdit.appendPlainText(f'Игрок взял - {self.player_number}')
                return

            self.plainTextEdit.appendPlainText(f'ИИ взял - {self.computer_number}')
            self.plainTextEdit.appendPlainText(f'Игрок взял - {self.player_number}')

        except Exception:
            self.label_4.setText('Введите кол-во камней от 1 до 3')

    def check_win(self):
        return self.number > 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_form = MainForm()
    main_form.show()
    sys.exit(app.exec())
