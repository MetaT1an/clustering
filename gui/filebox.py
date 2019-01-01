from PyQt5.Qt import *


class FileGroupBox(QGroupBox):
    def __init__(self, name):
        super().__init__(name)
        self.layout = QHBoxLayout()
        self.ok_icon = QLabel()
        self.file_path = QLabel("No file was selected")
        self.file_select = QPushButton("Select")
        self.file_dialog = QFileDialog(self.file_select)

        self.set_ui()
        self.set_event()

    def set_ui(self):
        self.ok_icon.setFixedSize(24, 24)
        self.ok_icon.setScaledContents(True)

        self.file_dialog.setNameFilter("txt(*.txt)")

        self.file_path.setAlignment(Qt.AlignRight | Qt.AlignCenter)

        self.layout.addWidget(self.ok_icon)
        self.layout.addWidget(self.file_path, 1)
        self.layout.addWidget(self.file_select)

        self.layout.setSpacing(10)
        self.setLayout(self.layout)

    def set_event(self):

        def set_path():
            path = self.file_dialog.selectedFiles()[0]
            self.file_path.setText(path)
            self.ok_icon.setPixmap(QPixmap("./src/ok.png"))     # this path is offered for main.py
            # module test path : ../src/ok.png

        self.file_select.clicked.connect(lambda: self.file_dialog.open(set_path))

    def get_file_name(self):
        path = self.file_path.text()
        return path.split("/").pop()

    def get_file_path(self):
        return self.file_path.text()

    def get_file_select(self):
        return self.file_select

    def get_file_dialog(self):
        return self.file_dialog


# module test
if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    file_goup = FileGroupBox("Data-file selection")
    file_goup.show()

    sys.exit(app.exec())
