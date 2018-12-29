"""
kmeans module
this module provide a method(k-means) to cluster data from Data object
all the relevant data generated while computing stores in K class, for further use
"""
from core import distance


class K(object):
    """
    this class stores the data generated while calculating with k-means
    k: the number of clusters after computation
    run_time: the running time k-means algorithm takes
    """
    k = 3
    run_time = 0
    cls_info = {}

    @classmethod
    def set_k(cls, k_val):
        cls.k = k_val

    @classmethod
    def get_k(cls):
        return cls.k

    @classmethod
    def get_time(cls):
        return cls.run_time

    @classmethod
    def get_cls_info(cls):
        return {i: cls.cls_info[i]["elements"] for i in cls.cls_info}

    @classmethod
    def init_centroid(cls, dat):
        import random
        li = [i for i in range(dat.data_size)]  # a sequence of indexes of data

        cls.cls_info = {i: {"centroid": [], "elements": []} for i in range(cls.k)}

        for j in range(cls.k):
            idx_c = random.choice(li)
            cls.cls_info[j]["centroid"] = dat.data_set[idx_c]   # randomly generate centroid before calculation
            cls.cls_info[j]["elements"].append(dat.data_set[idx_c])
            li.remove(idx_c)


def update_cluster_elements(dat):
    """
    :param dat: [Data], a python object converted from data-file
    :return: new elements in different clusters
    """
    new_elements = [[] for i in K.cls_info]

    # recalculate the distance of each data item between each cluster
    for i in range(dat.data_size):
        difs = [distance.dif_item_cls(dat.data_set[i], K.cls_info[j], dat.dim_type) for j in range(K.k)]
        idx_c = difs.index(min(difs))
        new_elements[idx_c].append(dat.data_set[i])
    return new_elements


def time_record(fun):
    import time

    def inner(dat):
        start = time.clock()    # start time
        fun(dat)
        end = time.clock()      # end time
        K.run_time = round(end - start, 2)

    return inner


@time_record
def k_means(dat):
    """
    :param dat: [Data], a python object converted from data-file
    :return: None
    clustering the dat after several calculate iteration according to given k value
    the clustering info were stored in G.cluster
    """
    go_on = True
    K.init_centroid(dat)  # the centroid is certain item randomly selected in data_set

    # the first time is actually distance between two items
    for i in range(dat.data_size):
        difs = [distance.dif_items(dat.data_set[i], K.cls_info[j]["centroid"], dat.dim_type) for j in range(K.k)]
        idx_c = difs.index(min(difs))       # get index of cluster contributing the minimum difference
        K.cls_info[idx_c]["elements"].append(dat.data_set[i])        # add item to relevant cluster

    while go_on:
        go_on = False
        new_elements = update_cluster_elements(dat)

        # compare each cluster's summary, to check whether it changed
        for key in K.cls_info:
            if new_elements[key] != K.cls_info[key]["elements"]:
                K.cls_info[key]["elements"] = new_elements[key]   # update
                go_on = True


def save_result(path):
    """
    :param path: where to store the result after computation
    :return: None
    this method will store the cluster result generated after computation
    with given file path
    """
    with open(path, "w") as f:
        for i in K.cls_info:
            cls_name = "cluster {}:\n".format(i)
            f.write(cls_name)
            for item in K.cls_info[i]["elements"]:
                f.write("\t{}\n".format(item))

    f.close()

# # module test
# if __name__ == '__main__':
#     import core.data as dt
#     dt.data.txt_to_data("/home/tc/Desktop/data/Teaching_Assistant_Evaluation/tea.txt")
#
#     k_means(dt.data)
#     save_result("/home/tc/Desktop/data/test.txt")
#
#     print(K.run_time)
