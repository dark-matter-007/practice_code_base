# THIS IS THE PYTHON FILE FOR DECLARING THE TABULATION DATA CLASS WHILE KEEPING IT REUSABLE

class TabulationData:
    def __init__(self, headers=None, rows=None):
        super().__init__()

        if headers is None:
            self.__headers = ["Your input", "Bound Function"]
        else:
            self.__headers, self.__rows = headers, rows

        if rows is None:
            self.__rows = [
                ["1", "View image"],
                ["2", "Resize Image"],
                ["3", "Drop Image"],
                ["4", "Apply Filter"],
                ["0", "Exit Script"]
            ]
        else:
            self.__rows, self.__rows = rows, rows

    def get_headers(self):
        return self.__headers

    def get_rows(self):
        return self.__rows

    def get_all_data(self):
        return self.__headers, self.__rows
