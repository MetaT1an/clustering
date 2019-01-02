from PyQt5.Qt import QThread, pyqtSignal
from gui import mainwindow
from core import data as dt
from core import kmeans as km, dbscan as db


class ComputeThread(QThread):
    sig_out = pyqtSignal(bool)

    def __init__(self):
        super(ComputeThread, self).__init__()

    def run(self):
        # computation
        if mainwindow.mw.is_km_selected():
            km.k_means(dt.data)
        if mainwindow.mw.is_db_selected():
            db.dbscan(dt.data)

        # notify mw to change progress style
        self.sig_out.emit(dt.data.is_visible())
