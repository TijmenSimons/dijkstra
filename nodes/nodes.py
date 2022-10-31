import array


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Node():
    def __init__(self, name) -> None:
        self.name = name
        self.cons = []

    def connect(self, node, length):
        _a = AppendNode(node, length)
        self.cons.append(_a)

        _b = AppendNode(self, length)
        node.cons.append(_b)

    def print(self):
        print("\n=-----\nName:", self.name)
        print("Connections:")
        for i in self.cons:
            print(f"\t- {i.node.name}\t: {i.length}")
        print()


class AppendNode():
    def __init__(self, node, length) -> None:
        self.node = node
        self.length = length


class ResultNode():
    def __init__(self, node: Node) -> None:
        self.node = node
        self.is_checked = False
        self.length = None
        self.prev_node = None
        self.history = []


class HistoryResultNode():
    def __init__(self, length, prev_node) -> None:
        self.length = length
        self.prev_node = prev_node


class ResultNodeTable():
    def __init__(self) -> None:
        pass

    def get_in_progress(self) -> array:
        """Get every ResultNode which has a previous Node but is not finished."""
        result = []
        for x in self.__dict__.keys():
            res_node: ResultNode = self.__dict__.get(x)
            if not res_node.is_checked and res_node.prev_node != None:
                result.append(res_node)
        return result

    def get_shortest_previous_chain(self, node) -> array:
        """Get a chain of ResultNodes that are in previous to eachother.
        Input is the end node.
        """
        result = [node]
        # get Node where Previous == prev_node

        def get_prev(node):
            shortest_node = None
            # making sure the length is high enough to start with, could've put "9**9**9**9" but you never know (oh also that equation takes WAY too long lmao)
            shortest_path_length = sum([self.__dict__.get(x).length if self.__dict__.get(
                x).length != None else 0 for x in self.__dict__.keys()])

            list = [getattr(self, x) for x in self.__dict__.keys() if getattr(
                self, x).node == node and getattr(self, x).length != None]

            x: ResultNode
            for x in list:
                if x.length < shortest_path_length:
                    shortest_node = x.prev_node
                    shortest_path_length = x.length
            return shortest_node

        while True:
            prev = get_prev(result[-1])
            if not prev:
                result.reverse()
                return result
            result.append(prev)

    def print(self) -> None:
        """Print out the table"""
        titles = ["Node", "Length", "Previous"]
        name_len = len(titles[0])
        length_len = len(titles[1])
        prev_node_length = len(titles[2])

        ct = correction_string = " > "

        # get the longest lengths so I can space out the table borders far enough
        for x in self.__dict__.keys():
            res_node: ResultNode = self.__dict__.get(x)

            # + 2 comes from the whitespace + check- or x-mark
            name_len = len(res_node.node.name) + 2 \
                if len(res_node.node.name) + 2 > name_len else name_len

            temp_length_str = ""
            temp_prev_node_str = ""
            temp_length_len = 0
            temp_prev_node_len = 0
            if len(res_node.history) > 0:
                i: HistoryResultNode
                for i in res_node.history:
                    temp_length_str = f"{temp_length_str}{i.length}{ct}"
                temp_length_len += len(temp_length_str)

                for i in res_node.history:
                    temp_prev_node_str = f"{temp_prev_node_str}{i.prev_node.name}{ct}"
                temp_prev_node_len += len(temp_prev_node_str)

            temp_len = len(str(res_node.length)) + \
                temp_length_len if res_node.length != None else 0
            length_len = temp_len if temp_len > length_len else length_len

            temp_len = len(res_node.prev_node.name) + \
                temp_prev_node_len if res_node.prev_node != None else 0
            prev_node_length = temp_len if temp_len > prev_node_length else prev_node_length

        m = 2  # margin
        row = "=-" + "-"*(name_len+m) + "-=-" + "-" * \
            (length_len+m) + "-=-" + "-"*(prev_node_length+m) + "-="

        print(row+"\n| "
              + titles[0] + " "*(name_len-len(titles[0])+m) + " | "
              + titles[1] + " "*(length_len-len(titles[1])+m) + " | "
              + titles[2] + " "*(prev_node_length-len(titles[2])+m) + " |"
              )

        for x in self.__dict__.keys():
            print(f"{bcolors.ENDC}{row}")
            res_node = self.__dict__.get(x)

            name = res_node.node.name + \
                (" ✓" if res_node.is_checked else " ✗") + \
                " "*(name_len-len(res_node.node.name)+m-2)

            length = "-"+" "*(length_len-1+m)
            if res_node.length != None:
                temp_length_str = ""
                for i in res_node.history:
                    temp_length_str = f"{temp_length_str}{i.length}{ct}"

                length = temp_length_str + str(res_node.length)
                length += " "*(length_len-len(length)+m)

            prev_node = "-"+" "*(prev_node_length-1+m)
            if res_node.prev_node != None:
                temp_prev_node_str = ""
                for i in res_node.history:
                    temp_prev_node_str = f"{temp_prev_node_str}{i.prev_node.name}{ct}"
                prev_node = temp_prev_node_str + res_node.prev_node.name
                prev_node += " "*(prev_node_length-len(prev_node)+m)

            print(
                f"{bcolors.OKGREEN if res_node.is_checked else bcolors.ENDC}| {name} | {length} | {prev_node} |")
        print(f"{bcolors.ENDC}{row}")
