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
    
    if row == N:
        return True
    
    for C in range(N):
        if (isSafe(arr,row,C)):
            arr[row][C] = 'Q'
            if (N_Queen(arr,row+1)):
                return True
            arr[row][C] = 'x'
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
