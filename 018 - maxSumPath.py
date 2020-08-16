"""
Max Path Sum I - Find the maximum total from top to bottom of the triangle
in the input file.
"""

def maxSumPath():
    arr = []

    #read file and get triangle into the final array
    with open('018_input.txt') as f:
        a = f.readlines()
    for i in range(len(a) - 1):
        arr.append(a[i][0:-1])
    arr.append(a[len(a) - 1])

    # make arr contain only lists of integers
    for i in range(len(arr)):
        arr[i] = arr[i].split(' ')
        for j in range(len(arr[i])):
            arr[i][j] = int(arr[i][j])

    # define new array to contain the sums
    sums = arr;
    
    for i in range(len(arr)):
        if(i == 0):
            sums[i] = arr[i]
        else:
            for j in range(len(arr[i])):
                if(j == 0):
                    sums[i][j] = arr[i][j] + sums[i-1][j]
                elif(j == len(arr[i]) - 1):
                    sums[i][j] = arr[i][j] + sums[i-1][j-1]
                else:
                    sums[i][j] = arr[i][j] + max(sums[i-1][j-1], sums[i-1][j])

    return max(sums[len(sums) - 1])
