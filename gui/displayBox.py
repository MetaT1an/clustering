from PyQt5.Qt import QGridLayout, QPushButton, QGroupBox, QFileDialog, QApplication


class DisplayGroupBox(QGroupBox):
    def __init__(self, name):
        super().__init__(name)
        self.layout = QGridLayout()
        self.time_btn = QPushButton("Running time")
        self.cls_info_btn = QPushButton("Clusters info")
        self.vision_btn = QPushButton("Visualize")
        self.save_bth = QPushButton("Save result")
        self.save_file_dialog = QFileDialog()

        self.set_ui()
        self.set_events()

    def set_ui(self):
        self.layout.addWidget(self.time_btn, 0, 0)
        self.layout.addWidget(self.cls_info_btn, 0, 1)
        self.layout.addWidget(self.vision_btn, 1, 0)
        self.layout.addWidget(self.save_bth, 1, 1)

        self.set_btns_enable(False, False)

        self.save_file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        self.save_file_dialog.setNameFilter("txt(*.txt)")

        self.layout.setSpacing(10)
        self.setLayout(self.layout)

    def set_events(self):
        self.save_bth.clicked.connect(self.save_file_dialog.open)

    def set_btns_enable(self, flag, vision_flag):
        self.time_btn.setEnabled(flag)
        self.cls_info_btn.setEnabled(flag)
        self.save_bth.setEnabled(flag)

        # whether the data is visible two dimension
        self.vision_btn.setEnabled(vision_flag)

    def get_save_dialog(self):
        return self.save_file_dialog

    def get_time_btn(self):
        return self.time_btn

    def get_save_btn(self):
        return self.save_bth

    def get_vision_btn(self):
        return self.vision_btn

    def get_clsinfo_btn(self):
        return self.cls_info_btn


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    x = DisplayGroupBox("xx")
    x.show()

    sys.exit(app.exec())
