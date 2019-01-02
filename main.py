from PyQt5.Qt import QApplication
import core.data as dt
import gui.mainwindow as mw
import control.eventsctrler as evtctrl
import control.qssctrler as qctrl

import sys

app = QApplication(sys.argv)

# generate Data object, single patten
file_data = dt.data

# connect all events
evtctrl.load_events()

# load self-designed style
qctrl.load_style()

# show main window
mw.mw.setWindowTitle("Clustering and Comparision")

mw.mw.show()

sys.exit(app.exec())
