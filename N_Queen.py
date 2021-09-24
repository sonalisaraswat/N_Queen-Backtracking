def isSafe(arr,row,col):
                                               #checking vertically through all rows of given col
    for e in range(N):
        if arr[e][col] == 'Q':
            return False

                                               #checking upper left
    r_up = row-1
    c_left = col-1
    while (r_up >= 0) and (c_left >= 0):
        if arr[r_up][c_left] == 'Q':
            return False
        r_up -= 1
        c_left -= 1

                                               #checking upper right
    r_up = row-1
    c_right = col+1
    while (r_up >= 0) and (c_right < N):
        if arr[r_up][c_right] == 'Q':
            return False
        r_up -= 1
        c_right += 1

    return True


                                               # going through all rows
def N_Queen(arr,row):
    
    if row == N:                              # BASE CONDITION: all rows checked so return True
        return True
    
    for C in range(N):                        # Check for all cols in a given row.
        if (isSafe(arr,row,C)):               # if we get a safe col in the given row.
            arr[row][C] = 'Q'                 # assign that col in the given row as Q.
            if (N_Queen(arr,row+1)):          # run N queen for next set of rows.
                return True
            arr[row][C] = 'x'                 # BACKTRACKING POINT: if any next rows return False: set the col of that row back to X.
    
    return False


                                              # main start
N = int(input())

arr = []
for i in range (N):
    arr_t= list('x'*N)
    arr.append(arr_t)

if (N_Queen(arr,0)):
    for row in arr:
        print(' '.join(row))
else:
    print("Not Posssible")
