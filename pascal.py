def printPascal(n):  
    for line in range(1, n + 1):  
        C = 1; # used to represent C(line, i)
        print(f"{' '*(n-line)}", end="");    
        for i in range(1, line + 1):  
              
            # The first value in a  
            # line is always 1  
            print(C, end = " ");  
            C = int(C * (line - i) / i);
        print()
  
# Driver code  
n = int(input("Enter the number of rows: "))  
printPascal(n);