from core import kmeans as km, dbscan as db
from core.data import data as dt
from display import chart as ct
from gui.mainwindow import mw


def pass_alg_params():
    km.K.set_k(mw.get_k())
    db.D.set_param(mw.get_db_params())


def gen_data():
    path = mw.get_path()
    dt.txt_to_data(path)


def sava_data(path):
    # save data to given path

    path = path.split("/")  # list now
    f_name = path.pop()

    if mw.is_km_selected():
        f_name_km = "/" + f_name + "_km.txt"
        path_km = "/".join(path) + f_name_km
        km.save_result(path_km)

    if mw.is_db_selected():
        f_name_db = "/" + f_name + "_db.txt"
        path_db = "/".join(path) + f_name_db
        db.save_result(path_db, dt)


def compute_events():
    # 1.computation button events

    # 1.1 change progress bar style to busy
    mw.set_progress_busy()

    # 1.2 pass parameters to relevant module
    pass_alg_params()

    # 1.3 generate python Data object
    gen_data()

    # 1.4 disenable computation button
    mw.set_enable_compute(False)

    # 1.5 compute
    mw.compute_thread.start()

    # 1.6 change progress bar style to finished
    # 1.7 enable computation button
    # 1.8 enable display button
    # dealt with in compute thread, waiting for its finished signal


def file_selection_events():
    # hide progress bar
    mw.set_progress_hide()


def file_dialog_events(file_path):
    mw.compute_box.set_enable_compute(True)


def display_time():
    km_t = km.K.run_time if mw.is_km_selected() else 0
    db_t = db.D.run_time if mw.is_db_selected() else 0

    ct.show_time(mw.get_file_name(), km_t, db_t, "k-means", "DBSCAN")


def display_result():
    # prepare arguments required

    km_cls_nums = [len(km.K.cls_info[i]["elements"]) for i in km.K.cls_info] if mw.is_km_selected() else []
    db_cls_nums = [len(db.D.clusters[i]) for i in db.D.clusters] if mw.is_db_selected() else []

    ct.show_clusters(km_cls_nums, db_cls_nums, "k-means", "DBSCAN", mw.get_file_name())


def display_vision():
    # prepare arguments required
    km_info = {i: km.K.cls_info[i]["elements"] for i in km.K.cls_info} if mw.is_km_selected() else {}
    db_info = {i: db.D.clusters[i] for i in db.D.clusters} if mw.is_db_selected() else {}

    ct.show_scatter(dt.data_set, km_info, db_info, "k-means", "DBSCAN", mw.get_file_name())


def display_events():
    # to save result of clustering after path was chosen
    mw.get_save_dialog().fileSelected.connect(sava_data)

    # running time displaying button
    mw.get_time_btn().clicked.connect(display_time)

    # cluster info displaying button
    mw.get_clsinfo_btn().clicked.connect(display_result)

    # 2 dimension data visualization
    mw.get_vision_btn().clicked.connect(display_vision)


def load_events():

    # compute button
    mw.get_cmpt_btn().clicked.connect(compute_events)

    # file-selection button
    mw.get_file_select().clicked.connect(file_selection_events)

    mw.get_file_dialog().fileSelected.connect(file_dialog_events)

    # display buttons
    display_events()

