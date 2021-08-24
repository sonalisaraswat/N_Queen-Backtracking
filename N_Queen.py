N = int(input())
arr = []

for i in range (N):
    arr_t= list('.'*N)
    arr.append(arr_t)

def isSafe(arr,row,col):
    #checking vertically through all rows
    for e in range(N):
        if arr[e][col] == 'Q':
            return False

    #checking upper left
    r_m = row-1
    c_m = col-1
    while r_m>=0 and c_m>=0:
        if arr[r_m][c_m] == 'Q':
            return False
        r_m -= 1
        c_m -= 1

    #checking upper right
    r_m = row-1
    c_p = col+1
    while r_m>=0 and c_p<N:
        if arr[r_m][c_p] == 'Q':
            return False
        r_m -= 1
        c_p += 1
        
    #checking lower left
    r_p = row+1
    c_m = col-1
    while r_p<N and c_m>=0:
        if arr[r_p][c_m] == 'Q':
            return False
        r_p += 1
        c_m -= 1
        
    #checking lower right
    r_p = row+1
    c_p = col+1
    while r_p<N and c_p<N:
        if arr[r_p][c_p] == 'Q':
            return False
        r_p += 1
        c_p += 1

    return True

def N_Queen(arr,row):
    if row == N:
        return True
    for C in range(N):
        if (isSafe(arr,row,C)):
            arr[row][C] = 'Q'
            if (N_Queen(arr,row+1)):
                return True
            arr[row][C] = '.'
    return False

if (N_Queen(arr,0)):
    print(N)
    for row in arr:
        print(''.join(row))
else:
    print("Not Posssible")
