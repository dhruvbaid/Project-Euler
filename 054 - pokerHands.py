"""
Poker Hands: Given a list of hands, how many does Player 1 win?
"""

cOrder = ['2','3','4','5','6','7','8','9','T','J','Q','K', 'A']
rOrder = ["High Card", "One Pair", "Two Pairs", "Three of a Kind", "Straight",
          "Flush", "Full House", "Four of a Kind", "Straight Flush",
          "Royal Flush"]

# ranked : given a hand (list of cards), return a list [rank, rankHighCard,
#          hand]
def ranked(hand: list) -> list:
    hand = sorted(hand, key = lambda x: cOrder.index(x[0]))

    n0 = hand[0][0]
    n1 = hand[1][0]
    n2 = hand[2][0]
    n3 = hand[3][0]
    n4 = hand[4][0]
    s0 = hand[0][1]
    s1 = hand[1][1]
    s2 = hand[2][1]
    s3 = hand[3][1]
    s4 = hand[4][1]
    
    if(([n0, n1, n2, n3, n4] == ['T','J','Q','K','A']) and
       (s0 == s1 == s2 == s3 == s4)):
        return ["Royal Flush", 'A', hand]
    elif((s0 == s1 == s2 == s3 == s4) and
         ((cOrder.index(n0) + 1 == cOrder.index(n1)) and
          (cOrder.index(n1) + 1 == cOrder.index(n2)) and
          (cOrder.index(n2) + 1 == cOrder.index(n3)) and
          (cOrder.index(n3) + 1 == cOrder.index(n4)))):
        return ["Straight Flush", n4, hand]
    elif((n0 == n1 == n2 == n3) or
         (n1 == n2 == n3 == n4)):
        return ["Four of a Kind", n2, hand]
    elif(((n0 == n1 == n2) and (n3 == n4)) or
         ((n0 == n1) and (n2 == n3 == n4))):
        return ["Full House", n4, hand]
    elif s0 == s1 == s2 == s3 == s4:
        return ["Flush", n4, hand]
    elif((cOrder.index(n0) + 1 == cOrder.index(n1)) and
         (cOrder.index(n1) + 1 == cOrder.index(n2)) and
         (cOrder.index(n2) + 1 == cOrder.index(n3)) and
         (cOrder.index(n3) + 1 == cOrder.index(n4))):
        return ["Straight", n4, hand]
    elif((n0 == n1 == n2) or
         (n1 == n2 == n3) or
         (n2 == n3 == n4)):
        if n0 == n1 == n2:
            mNum = n2
        elif n1 == n2 == n3:
            mNum = n3
        else:
            mNum = n4
        return ["Three of a Kind", mNum, hand]
    elif(((n0 == n1) and (n2 == n3)) or
         ((n0 == n1) and (n3 == n4)) or
         ((n1 == n2) and (n3 == n4))):
        return ["Two Pairs", n3, hand]
    elif((n0 == n1) or (n1 == n2) or (n2 == n3) or (n3 == n4)):
        for i in range(len(hand)):
            if hand[i][0] == hand[i+1][0]:
                return ["One Pair", hand[i][0], hand]
    else:
        return ["High Card", n4, hand]

# main : given an input file representing 2 players' hands, return the number of
#        games player 1 wins
def main():
    # obtain input lines
    with open("054_input.txt", mode = 'r') as f:
        lines = f.readlines()

    # convert each line into an array of 10 cards
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
        lines[i] = lines[i].split(" ")

    # wins is a list of winners ("p1" if player 1 won, "p2" if player 2 won)
    wins = []

    # loop through each game to determine the winner
    for i in range(len(lines)):
        p1 = lines[i][:5]
        p2 = lines[i][5:]

        # obtain the rank each player can make
        p1R = ranked(p1)
        p2R = ranked(p2)

        # compare hands
        if p1R[0] == p2R[0]:
            # same rank
            if p1R[1] == p2R[1]:
                # same rankHighCard - loop through all cards in descending order
                # and add winner as plater with highest card
                for i in range(len(p1) - 1, -1, -1):
                    cNum1 = p1[i][0]
                    cNum2 = p2[i][0]
                    if cOrder.index(cNum1) < cOrder.index(cNum2):
                        curWin = "p2"
                        break
                    elif cOrder.index(cNum1) < cOrder.index(cNum2):
                        curWin = "p1"
                        break
                    else:
                        continue
            else:
                # different rankHighCards - compare rankHighCards, add winner as
                # player with highest card
                if cOrder.index(p1R[1]) < cOrder.index(p2R[1]):
                    curWin = "p2"
                else:
                    curWin = "p1"
        else:
            # different ranks, winner is player with higher rank
            curWinOrder = sorted([p1R,p2R], key = lambda x: rOrder.index(x[0]))
            if curWinOrder[1] == p1R:
                curWin = "p1"
            else:
                curWin = "p2"

        # append winner to wins
        wins.append(curWin)

    c1 = wins.count("p1")
    print(f"Player 1 won {c1} games!")
    return
