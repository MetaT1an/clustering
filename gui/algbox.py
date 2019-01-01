from PyQt5.Qt import *


class AlgGroupBox(QGroupBox):
    def __init__(self, name):
        super().__init__(name)
        self.layout = QGridLayout()
        self.km = QCheckBox("k-means")
        self.db = QCheckBox("DBSCAN")
        self.k_lb = QLabel("k:")
        self.eps_lb = QLabel("Eps:")
        self.minp_lb = QLabel("MinPts:")

        self.k_val_lb = QLabel("3")
        self.eps_val_lb = QLabel("3")
        self.minp_val_lb = QLabel("2")

        self.k_slider = QSlider(Qt.Horizontal)
        self.eps_slider = QSlider(Qt.Horizontal)
        self.minp_slider = QSlider(Qt.Horizontal)
        self.k_slider.setStyleSheet("color:green;")

        self.set_ui()
        self.set_event()

    @classmethod
    def set_unable(cls, li, flag):
        val = True if flag == 2 else False
        for widget in li:
            widget.setEnabled(val)

    def set_ui(self):
        self.k_slider.setRange(3, 10)
        self.eps_slider.setRange(3, 10)
        self.minp_slider.setRange(2, 9)

        self.layout.addWidget(self.km, 0, 0, 1, 3)
        self.layout.addWidget(self.db, 0, 3, 1, 3)
        self.layout.addWidget(self.k_lb, 1, 0, 1, 1)
        self.layout.addWidget(self.k_val_lb, 1, 1, 1, 1)
        self.layout.addWidget(self.k_slider, 1, 2, 1, 1)
        self.layout.addWidget(self.eps_lb, 1, 3, 1, 1)
        self.layout.addWidget(self.eps_val_lb, 1, 4, 1, 1)
        self.layout.addWidget(self.eps_slider, 1, 5, 1, 1)
        self.layout.addWidget(self.minp_lb, 2, 3, 1, 1)
        self.layout.addWidget(self.minp_val_lb, 2, 4, 1, 1)
        self.layout.addWidget(self.minp_slider, 2, 5, 1, 1)

        self.layout.setSpacing(10)
        self.layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.layout)

    def set_event(self):
        items_k = [self.k_lb, self.k_val_lb, self.k_slider]
        items_db = [self.eps_lb, self.eps_slider, self.minp_slider, self.eps_val_lb, self.minp_val_lb, self.minp_lb]
        self.set_unable(items_k, 0)
        self.set_unable(items_db, 0)

        self.km.stateChanged.connect(lambda flag: self.set_unable(items_k, flag))
        self.db.stateChanged.connect(lambda flag: self.set_unable(items_db, flag))

        self.k_slider.valueChanged.connect(lambda val: self.k_val_lb.setNum(val))
        self.eps_slider.valueChanged.connect(lambda val: self.eps_val_lb.setNum(val))
        self.minp_slider.valueChanged.connect(lambda val: self.minp_val_lb.setNum(val))

    def get_k_val(self):
        return self.k_slider.value()

    def get_db_params(self):
        return self.eps_slider.value(), self.minp_slider.value()

    def is_km_selected(self):
        return self.km.isChecked()

    def is_db_selected(self):
        return self.db.isChecked()


# module test
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    alg_goup = AlgGroupBox("Algorithm selection")
    alg_goup.show()

    sys.exit(app.exec())
