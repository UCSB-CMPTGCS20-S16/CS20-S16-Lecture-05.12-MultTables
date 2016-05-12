
def separator_row(numCols):
    return "---+" * (numCols + 1)

def header_row(numCols):
    x = "   |"
    for i in range(1,numCols+1):
        x = x + " " + str(i) + " |"
    return x

def table_row(rowNumber,numCols):
    x = " " + str(rowNumber) + " |"
    for i in range(1,numCols+1):
        x = x + ( "%3d" % (i*rowNumber) ) + "|"
    return x

def mult_table(num_rows, num_cols):
    x = header_row(num_cols) + "\n" + separator_row(num_cols) + "\n"
    for i in range(1,num_rows+1):
        x = x + table_row(i,num_cols) + "\n"
        x = x + separator_row(num_cols) + "\n"
    return x

    
