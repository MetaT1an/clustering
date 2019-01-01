from PyQt5.Qt import QWidget, QVBoxLayout, QApplication

from gui.algbox import AlgGroupBox
from gui.filebox import FileGroupBox
from gui.computebox import ComputeGroupBox
from gui.displayBox import DisplayGroupBox


from control.computethread import ComputeThread
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.alg_box = AlgGroupBox("Algorithm selection  ")
        self.file_box = FileGroupBox("Data-file selection  ")
        self.compute_box = ComputeGroupBox("Computation  ")
        self.display_box = DisplayGroupBox("Result display  ")
        self.layout = QVBoxLayout()

        self.compute_thread = ComputeThread()
        self.compute_thread.sig_out.connect(self.set_progress_finished)
        self.set_ui()

    def set_ui(self):
        self.setFixedWidth(500)

        self.layout.addWidget(self.alg_box)
        self.layout.addWidget(self.file_box)
        self.layout.addWidget(self.compute_box)
        self.layout.addWidget(self.display_box)

        self.layout.setSpacing(24)
        self.setLayout(self.layout)

    def get_cmpt_btn(self):
        return self.compute_box.get_btn()

    def get_k(self):
        return self.alg_box.get_k_val()

    def get_db_params(self):
        return self.alg_box.get_db_params()

    def is_km_selected(self):
        return self.alg_box.is_km_selected()

    def is_db_selected(self):
        return self.alg_box.is_db_selected()

    def set_progress_busy(self):
        self.compute_box.set_progress_busy()

    def set_progress_hide(self):
        self.compute_box.set_progress_hide()

    def set_progress_finished(self, vision_flag):
        self.compute_box.set_progress_finished()
        self.compute_box.set_enable_compute(True)
        self.display_box.set_btns_enable(True, vision_flag)

    def get_path(self):
        return self.file_box.get_file_path()

    def get_file_select(self):
        return self.file_box.get_file_select()

    def set_enable_compute(self, flag):
        self.compute_box.set_enable_compute(flag)

    def get_file_dialog(self):
        return self.file_box.get_file_dialog()

    def set_display_btns_enable(self, flag, vision_flag):
        self.display_box.set_btns_enable(flag, vision_flag)

    def get_save_dialog(self):
        return self.display_box.get_save_dialog()

    def get_file_name(self):
        return self.file_box.get_file_name()

    def get_time_btn(self):
        return self.display_box.get_time_btn()

    def get_save_btn(self):
        return self.display_box.get_save_btn()

    def get_vision_btn(self):
        return self.display_box.get_vision_btn()

    def get_clsinfo_btn(self):
        return self.display_box.get_clsinfo_btn()


app = QApplication(sys.argv)
mw = MainWindow()
