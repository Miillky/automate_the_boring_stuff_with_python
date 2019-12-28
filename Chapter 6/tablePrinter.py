tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'Davit'],
            ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    col_widths = [0] * len(table)
    for i in range(len(tableData)):
        for item in tableData[i]:
           if len(item) > col_widths[i]:
               col_widths[i] = len(item)

    for j in range(len(tableData[0])):
        for k in range(len(tableData)):
            print( tableData[k][j].rjust(col_widths[k]), end=" " )
        print()

printTable(tableData)