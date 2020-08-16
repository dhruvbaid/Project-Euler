"""
Name Scores - What is the total of all the name scores in the file?
"""

def nameScores():
    # process input into an array of names in alphabetical order
    with open('022_input.txt') as f:
        raw = f.readlines()
    arr = raw[0].split(',')
    for i in range(len(arr)):
        arr[i] = arr[i][1:-1]
    arr.sort()

    # create array of scores with default value 0
    scores = []
    for i in range(len(arr)):
        scores.append(0)

    # update scores for each name
    for i in range(len(scores)):
        name = arr[i]
        for x in name:
            scores[i] += (ord(x) - 64)

    # account for alphabetical position of name
    for i in range(len(scores)):
        scores[i] *= (i + 1)

    print(sum(scores))

nameScores()
