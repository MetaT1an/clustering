from gui.mainwindow import mw


def set_qss(obj, path):
    with open(path, "r") as f:
        style = f.read()
        obj.setStyleSheet(style)
    f.close()


def load_style():
    set_qss(mw, "./src/test.qss")
