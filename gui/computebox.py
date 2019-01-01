from PyQt5.Qt import QVBoxLayout, QPushButton, QProgressBar, QGroupBox


class ComputeGroupBox(QGroupBox):
    def __init__(self, name):
        super().__init__(name)
        self.layout = QVBoxLayout()
        self.progress = QProgressBar()
        self.btn = QPushButton("Compute and Analyze")

        self.set_ui()

    def set_ui(self):
        self.progress.hide()
        self.set_enable_compute(False)

        self.layout.addWidget(self.progress)
        self.layout.addWidget(self.btn)

        self.layout.setSpacing(10)
        self.setLayout(self.layout)

    def get_btn(self):
        return self.btn

    def get_progress(self):
        return self.progress

    def set_progress_busy(self):
        self.progress.setRange(0, 0)
        self.progress.show()

    def set_progress_finished(self):
        self.progress.setRange(0, 100)
        self.progress.setValue(100)
        self.progress.setFormat("Completed")
        self.progress.show()

    def set_progress_hide(self):
        self.progress.hide()

    def set_enable_compute(self, flag):
        self.btn.setEnabled(flag)


