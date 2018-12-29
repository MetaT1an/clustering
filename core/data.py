"""
data module
this module provide a Data class
to read data from data-file to convert it
to a python object in memory
"""


class Data(object):
    """
    this module
    """
    def __init__(self):
        self.data_size = 0
        self.data_set = []
        self.dim_size = 0
        self.dim_type = []

    def init_params(self):
        self.data_size = 0
        self.data_set = []
        self.dim_size = 0
        self.dim_type = []

    def txt_to_data(self, path):
        """
        :param path: the absolute-path of the file containing data
        :return: None
        convert a data-file to a python Data object
        """
        self.init_params()

        with open(path, "r") as f:
            # the first line of the data file stores the types of each dimension
            self.dim_type = f.readline().strip().split(",")
            self.dim_size = len(self.dim_type)

            line = f.readline().strip()
            while line:         # to remove the blank line
                d, line = [], line.split(",")

                for i in range(self.dim_size):
                    if self.dim_type[i] == "cat":   # categorical type
                        d.append(line[i])
                    elif self.dim_type[i] == "float":   # float type
                        d.append(float(line[i]))
                    elif self.dim_type[i] == "int":     # integer
                        d.append(int(line[i]))
                    else:
                        pass
                
                self.data_set.append(d)
                self.data_size += 1
                line = f.readline().strip()     # prepare for the next item

    # if data is visible, it can be displayed in 2-dimension graph
    def is_visible(self):
        visible_dim = ["int", "float"]
        return self.data_size == 2 and self.dim_type[0] in visible_dim and self.dim_type[1] in visible_dim


# single pattern
data = Data()

# module test
# if __name__ == '__main__':
#     data = Data()
#     data.txt_to_data("/home/tc/Desktop/data/Teaching_Assistant_Evaluation/tea.txt")
#     print(data.data_size, data.dim_size, data.dim_type)
