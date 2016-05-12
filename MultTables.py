
def separator_row(numCols):
    return "---+" * (numCols + 1)

def header_row(numCols):
    x = "   |"
    for i in range(1,numCols+1):
        x = x + " " + str(i) + " |"
    return x

def table_row(rowNumber,numCols):
    return "stub"
