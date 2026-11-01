from copy import deepcopy

class Table():
    def __init__(self, title=None):
        self.title = title
        self.table = [[None]]
        self.rows = [None]
        self.columns = [None]

    def __str__(self):
        if len(self.columns) == 0 or self.columns[0] == None or len(self.rows) == 0 or self.rows[0] == None or len(self.table) == 0 or self.table[0][0] == None:
            raise ValueError("Empty table cannot be printed.")
        table = deepcopy(self)
        for i in range(len(table.table)):
            for j in range(len(table.table[i])):
                table.table[i][j] = str(table.table[i][j])
            table.rows[i] = str(table.rows[i])
            try:
                table.rows[i] = str(table.rows[i])
            except:
                ...
        maxlen = 0
        for i in range(len(table.table)):
            for value in table.table[i]:
                if len(value) > maxlen:
                    maxlen = len(value)
            if len(table.rows[i]) > maxlen:
                maxlen = len(table.rows[i])
            try:
                if len(table.columns[i]) > maxlen:
                    maxlen = len(table.columns[i])
            except:
                ...
        bars = ((maxlen * (len(table.columns) + 1)) + (len(table.columns)) + 2) * "_"
        string = (int((len(bars) - len(table.title)) / 2) * " ") + table.title + (int((len(bars) - len(table.title)) / 2) * " ") + "\n" if table.title != None else ""
        string += bars + "\n" + "|" + (maxlen * " ")
        for i in range(len(table.columns)):
            string += "|" + table.columns[i] + ((maxlen - len(table.columns[i])) * " ")
        for i in range(len(table.table)):
            for j in range(len(table.table[i]) + 1):
                if j == 0:
                    string += "|" + "\n" + bars + "\n" + "|" + table.rows[i] + ((maxlen - len(table.rows[i])) * " ")
                else:
                    string += "|" + table.table[i][j - 1] + ((maxlen - len(table.table[i][j - 1])) * " ")
        string += "|" + "\n" + bars
        return string

    def __eq__(self, other):
        return self.table == other.table and self.columns == other.columns and self.rows == other.rows

    def addrow(self, row):
        self.dictcheck(row)
        self.rows.append(list(row.keys())[0])
        rvalues = list(list(row.values())[0])
        #self.rocolcheck(rvalues, "row")
        self.table.append(rvalues)
        if self.rows[0] == None:
            self.removerow(None)

    def addcolumn(self, column):
        self.dictcheck(column)
        self.columns.append(list(column.keys())[0])
        cvalues = list(list(column.values())[0])
        #self.rocolcheck(cvalues, "column")
        for i in range(len(self.table)):
            self.table[i].append(cvalues[i])
        if self.columns[0] == None:
            self.columns.remove(None)

    def removerow(self, row):
        index = self.rows.index(row)
        self.rows.remove(row)
        self.table.pop(index)

    def removecolumn(self, column):
        index = self.columns.index(column)
        self.columns.remove(column)
        for i in range(len(self.table)):
            self.table[i].pop(index)

    def update(self, row, column, value):
        if not row in self.rows and not column in self.columns:
            raise KeyError("Either specified row or specified column is not in the table.")
        coord = []
        for i in range(len(self.rows)):
            if self.rows[i] == row:
                coord.append(i)
        for i in range(len(self.columns)):
            if self.columns[i] == column:
                coord.append(i)
        self.table[coord[0]][coord[1]] = value

    def get(self, row, column):
        if not row in self.rows and not column in self.columns:
            raise KeyError("Either specified row or specified column is not in the table.")
        coord = []
        for i in range(len(self.rows)):
            if self.rows[i] == row:
                coord.append(i)
        for i in range(len(self.columns)):
            if self.columns[i] == column:
                coord.append(i)
        return self.table[coord[0]][coord[1]]

    def dictcheck(self, value):
        if not isinstance(value, dict):
            raise TypeError("Dict not passed.")
        if len(value) != 1:
            raise IndexError("Dict does not have length of one.")

    def rocolcheck(self, value, roc):
        if roc == "column" and len(value) != len(self.table):
            raise IndexError("Column argument not right length.")
        elif roc == "row" and len(value) != len(self.table[0]):
            raise IndexError("Row argument not right length.")

    def fromcsv(self, file):
        try:
            contents = file.read().splitlines()
        except:
            raise FileNotFoundError("File not in read mode.")
        print(contents)