"""
## Poker hands
Problem 54

In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:  
Hand_| Player 1___________________________________________ | Player 2_________________________________________________ | Winner  
1____ | 5C 6S 7S KD Pair of Fives __________________________ | 2C 3S 8S 8D TD Pair of Eights _________________________ | Player 2  
2____ | 5D 8C 9S JS AC Highest card Ace___________________ | 2C 5C 7D 8S QH Highest card Queen _______________ | Player 1  
3____ | 2D 9C AS AH AC Three Aces _______________________ | 3D 6D 7D TD QDFlush with Diamonds _______________ | Player 2  
4____ | 4D 6S 9H QH QC Pair of Queens Highest card Nine | 3D 6D 7H QD QS Pair of Queens Highest card Seven | Player 1  
5____ | 2H 2D 4C 4D 4S Full House With Three Fours ______ | 3C 3D 3S 9S 9D Full House with Three Threes _______ | Player 1  

The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?


Link: https://projecteuler.net/problem=54

Date solved:  
2022/07/25
"""

ANSWER = 376

# imports

from collections import Counter

# solution

file_name = "problem_files/p054_poker.txt"
with open(file_name, "r") as f:
    hands = f.read()
hands = hands.split("\n")


def no_str(integer):
    num = str(integer)
    return num if len(num) == 2 else "0" + num


def high_value(snum):
    return "".join(map(no_str, snum[::-1]))


def score_hand(hand):
    num_key = {
        "T": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14,
    }
    letters = []
    numbers = []
    for card in hand:
        letter = card[1]
        letters.append(letter)
        num = card[0]
        try:
            number = int(num)
        except:
            number = num_key[num]
        numbers.append(number)
    snum = sorted(numbers)  # Sorted for ease
    rnum = Counter(numbers)  # We count repetitions for each number
    mfreq = rnum.most_common()[0][1]  # largest 'X of a kind'
    rlet = [letters.count(i) for i in letters]  # We count repetitions for each letter
    dif = max(numbers) - min(
        numbers
    )  # The difference between the greater and smaller number in the hand

    if snum == [2, 3, 4, 5, 14]:  # makes Ace low in this case
        snum = [1, 2, 3, 4, 5]
        dif = 4

    if rlet[0] == 5:
        if dif == 4 and mfreq == 1:
            handtype = "straight_flush"
            score = float("8." + high_value(snum))
        else:
            handtype = "flush"
            score = float("5." + high_value(snum))
    elif mfreq == 4:
        handtype = "four of a kind"
        v4 = no_str(rnum.most_common()[0][0])
        score = float("7." + v4 + high_value(snum))
    elif snum == [2, 2, 3, 3, 3]:
        handtype = "full house"
        v3 = no_str(rnum.most_common()[0][0])
        v2 = no_str(rnum.most_common()[1][0])
        score = float("6." + v3 + v2 + high_value(snum))
    elif dif == 4 and mfreq == 1:
        handtype = "straight"
        score = float("4." + high_value(snum))
    elif mfreq == 3:
        handtype = "three of a kind"
        v3 = no_str(rnum.most_common()[0][0])
        score = float("3." + v3 + high_value(snum))
    elif (rnum.most_common()[0][1] == 2) and (rnum.most_common()[1][1] == 2):
        handtype = "two pair"
        commons = [rnum.most_common()[0][0], rnum.most_common()[1][0]]
        v2h = no_str(max(commons))
        v2l = no_str(min(commons))
        score = float("2." + v2h + v2l + high_value(snum))
    elif rnum.most_common()[0][1] == 2:
        handtype = "pair"
        v2 = no_str(rnum.most_common()[0][0])
        score = float("1." + v2 + high_value(snum))
    else:
        handtype = "high card"
        score = float("0." + high_value(snum))
    #     print(hand,'this hand is a %s:, with score: %s' % (handtype,score))
    return score


def count_p1_wins():
    p1_wins = 0

    for hand in hands:
        p1_hand = hand[:14].split(" ")
        p2_hand = hand[15:].split(" ")

        p1_val = score_hand(p1_hand)
        p2_val = score_hand(p2_hand)

        p1_wins += p1_val > p2_val

    return p1_wins


def solution():

    return count_p1_wins()


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution()
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
