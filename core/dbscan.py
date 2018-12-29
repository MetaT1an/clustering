"""
dbscan module
this module provide a method(DBSCAN) to cluster data from Data object
all the relevant data generated while computing stores in D class, for further use
"""
from core import distance


class D(object):
    """
    the class stores parameters relating to this method
    k: the number of clusters after computation
    min_pts: minimum number of items in one area
    eps: radium of each area
    run_time: the running time dbscan algorithm takes
    item_cls: cluster info of each data item
    clusters: info of data-items of each cluster
    """
    k = 0
    min_pts = 3
    eps = 2

    run_time = 0
    item_cls = []   # -1: unvisited, [0, n]: cluster index, -2: noise
    dis_dict = {}   # dict of distances of every two data items
    clusters = {}

    @classmethod
    def set_param(cls, para):
        cls.min_pts = para[1]
        cls.eps = para[0]

    @classmethod
    def get_k(cls):
        return cls.k

    @classmethod
    def get_cls_info(cls):
        return {i: cls.clusters[i] for i in cls.clusters}

    @classmethod
    def init_params(cls, size):
        cls.item_cls = [-1 for i in range(size)]  # init cls info
        cls.dis_dict.clear()  # init dict info


def get_around(dat, item_idx):
    """
    :param dat: [Data], a python object converted from data-file
    :param item_idx: [int], index of data item
    :return: [list], indexes of data items around given data item in its area
    """
    neighbor = []
    for i in range(dat.data_size):
        a, b = (item_idx, i) if item_idx < i else (i, item_idx)
        dis = D.dis_dict.get((a, b))      # first to inquire dict

        if not dis:     # not in the dict
            dis = distance.dif_items(dat.data_set[item_idx], dat.data_set[i], dat.dim_type)
            D.dis_dict[(a, b)] = dis    # add the new distance to the dict
        if dis <= D.eps:
            neighbor.append(i)

    return neighbor


def mark_cls(items, idx_cls):
    """
    :param items: [list], containing indexes of data items belong to one cluster
    :param idx_cls: [int], index of clusters
    :return: None

    mark items with given index of cluster
    """
    for i in items:
        D.item_cls[i] = idx_cls


def new_cache(cache, items, idx_cls):
    """
    :param cache: [list], temporary cluster members
    :param items: [list], potential members in certain cluster
    :param idx_cls: [int], index of certain cluster
    :return: [list], potential members belonging to the same cluster

    add potential members to temporary cluster members
    after filtering via idx_cls
    """
    new = []
    for idx in items:
        if idx not in cache and D.item_cls[idx] != idx_cls:
            new.append(idx)
    return new


def get_cls_info():
    """
    readjust the cluster info, make it easy to inquire
    :return: None
    """
    D.clusters = {i: [] for i in range(D.k)}
    D.clusters[-2] = []     # noise

    for i in range(len(D.item_cls)):
        D.clusters[D.item_cls[i]].append(i)


# decorator
def time_record(fun):
    import time

    def inner(dat):
        start = time.clock()    # start time
        fun(dat)
        end = time.clock()      # end time
        D.run_time = round(end - start, 2)

    return inner


@time_record
def dbscan(dat):
    D.init_params(dat.data_size)
    idx_cls, cache = -1, []    # current index of cluster

    for i in range(dat.data_size):
        if D.item_cls[i] == -2 or D.item_cls[i] >= 0:
            continue

        neighbor = get_around(dat, i)
        if len(neighbor) < D.min_pts:
            D.item_cls[i] = -2      # mark as noise
        else:
            idx_cls += 1
            mark_cls(neighbor, idx_cls)
            cache = neighbor
            while cache:
                side_item_idx = cache.pop()
                neighbor = get_around(dat, side_item_idx)

                if len(neighbor) < D.min_pts:
                    continue
                new = new_cache(cache, neighbor, idx_cls)
                mark_cls(new, idx_cls)
                cache.extend(new)

    D.k = idx_cls + 1
    get_cls_info()  # readjust clusters info


def save_result(path, dat):
    """
    :param path: where to store the result after computation
    :param dat: data set
    :return: None

    this method will store the cluster result generated after computation
    with given file path
    """
    with open(path, "w") as f:
        for i in D.clusters:
            cls_name = "noise:\n" if i == -2 else "cluster {}\n".format(i)
            f.write(cls_name)
            for itm_idx in D.clusters[i]:
                f.write("\t{}\n".format(dat.data_set[itm_idx]))

    f.close()

# # module test
# if __name__ == '__main__':
#     import core.data as dt
#     dt.data.txt_to_data("/home/tc/Desktop/data/Teaching_Assistant_Evaluation/tea.txt")
#     # dat = data.Data("/home/tc/Desktop/data/Teaching_Assistant_Evaluation/tea.txt")
#     # dat = data.Data("/home/tc/Desktop/data/Contraceptive_Method_Choice/cmc.txt")
#     dbscan(dt.data)
#
#     save_result("/home/tc/Desktop/data/test.txt", dt.data)
