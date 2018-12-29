"""
this module provide two functions to get distance
1. between two data items
2. between data item and centroid

when calculate the distance on the condition that data item
has categorical and numerical attributes, this module resorts to k-summary
method, and using Manhattan distance

[dif_items] will be mainly used in k-means and DBSCAN
[dif_item_cls] will be mainly used in k-means
"""


def dif_items(item_p, item_q, dim_type):
    """
    :param item_p: [list], data item  p
    :param item_q: [list], data item  q
    :param dim_type: [list], to inquire type of each dimension in p and q
    :return: difference between p and q, using Manhattan distance
    """
    res = 0
    for dim in range(len(item_p)):
        if dim_type[dim] == "cat":
            res += (item_p[dim] != item_q[dim])   # different category, dif = 1; else dif = 0
        elif dim_type[dim] == "int":
            res += abs(item_p[dim] - item_q[dim])
        elif dim_type[dim] == "float":
            res += abs(item_p[dim] - item_q[dim])
        else:
            pass    # in case of more type of dimension in the future

    return res


def dif_item_cls(item_p, cls, dim_type):
    """
    :param item_p: data item p
    :param cls: [dict], cluster object
    :param dim_type: [list], to inquire type of each dimension in p
    :return: difference between p and cls, using Manhattan distance
    """
    res = 0
    for dim in range(len(item_p)):
        dim_vals = [x[dim] for x in cls["elements"]]  # extract values in certain dimension of one cluster
        if dim_type[dim] == "cat":
            res += (1 - dim_vals.count(item_p[dim])/len(dim_vals))
        elif dim_type[dim] == "int":
            res += abs(item_p[dim] - sum(dim_vals)/len(dim_vals))
        elif dim_type[dim] == "float":
            res += abs(item_p[dim] - sum(dim_vals) / len(dim_vals))
        else:
            pass

    return res
