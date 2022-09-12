# Some basic CSV reading without using the CSV module
#                                    ~ Zackery .R. Smith

def csv_get_column(csv:str, col:int, strip_title:bool=False, delim:str=",") -> list:
    """csv_get_column(csv, col, strip_title=False, delim=",")
    
Get a specfic column in a CSV
csv:         An absolute or relitive path to the csv.
col:         The column number of which you'd like to grab (works in reverse with negitive numbers).
strip_title: Takes the title of the column out of the returned data.
delim:       The delimiter to split by, not all people seperate their values with commas.  
    """
    try:
        with open(csv) as f:
            # Get file contents
            c = [x.strip("\n").split(delim) for x in f.readlines()]
            
            if   col >= len(c[0]) : c = []
            elif col == 0         : c = [[c[i][j-1] for i in range(len(c))][(1 if strip_title else 0):] for j in range(len(c))]
            elif col-1 <= len(c)  : c = [c[i][col if col < 0 else col-1] for i in range(len(c))][(1 if strip_title else 0):]
            
            return c
    except (ValueError, IndexError, FileNotFoundError): return []

def csv_get_row(csv:str, row:int, delim:str=","):
    """csv_get_row(csv, row, delim=",")

Get a specfic column in a CSV
csv:   An absolute or relitive path to the csv.
row:   The row you'd like to grab (works in reverse with negitive numbers).
delim: The delimiter to split by, not all people seperate their values with commas.
    """
    try:
        with open(csv) as f:
            c = [x.strip("\n").split(delim) for x in f.readlines()]
            
            if   row >= len(c[0]) : c = []
            elif row == 0         : pass
            elif row-1 <= len(c)  : c = c[row if row < 0 else row-1]
            
            return c
    except (ValueError, IndexError, FileNotFoundError): return []
