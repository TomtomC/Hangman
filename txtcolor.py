

#code adjusted from:
# https://www.geeksforgeeks.org/print-colors-python-terminal/

#ANSI method

def txtRed(skk):
    print("\033[91m {}\033[00m" .format(skk))
 
def txtGreen(skk):
    print("\033[92m {}\033[00m" .format(skk))
 
 
def txtYellow(skk):
    print("\033[93m {}\033[00m" .format(skk))
 
 
def txtLightPurple(skk):
    print("\033[94m {}\033[00m" .format(skk))
 
 
def txtPurple(skk):
    print("\033[95m {}\033[00m" .format(skk))
 
 
def txtCyan(skk):
    print("\033[96m {}\033[00m" .format(skk))
 
 
def txtLightGray(skk):
    print("\033[97m {}\033[00m" .format(skk))
 
 
def txtBlack(skk):
    print("\033[98m {}\033[00m" .format(skk))