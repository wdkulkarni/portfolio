from table import *

table = Table(title="Robotics Team")
table.addrow({"Jack" : []})
table.addrow({"Leo" : []})
table.addrow({"Vyoma" : []})
table.addrow({'Mason' : []})
table.addrow({'Joe' : []})
table.addcolumn({"Main Role" : ['Captain', 'Builder', 'Coder', 'Assistant Builder', 'Notebook']})
table.addcolumn({"Other Role" : ['Driver', 'Backup Driver', 'Assistant Builder', None, 'Assistant Coder']})
print(table)