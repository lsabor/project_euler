"""
## Number Sequence Game
Problem 477

The number sequence game starts with a sequence S of N numbers written on a line.  

Two players alternate turns. The players on their respective turns must select and remove either the first or the last number remaining in the sequence.  

A player's own score is (determined by) the sum of all the numbers that player has taken. Each player attempts to maximize their own sum.  
If N = 4 and S = {1, 2, 10, 3}, then each player maximizes their own score as follows:  

    Player 1: removes the first number (1)  
    Player 2: removes the last number from the remaining sequence (3)  
    Player 1: removes the last number from the remaining sequence (10)  
    Player 2: removes the remaining number (2)  

Player 1 score is 1 + 10 = 11.  

Let F(N) be the score of player 1 if both players follow the optimal strategy for the sequence S = {s1, s2, ..., sN} defined as:
  
    s1 = 0  
    s_(i+1) = (s_i^2 + 45) modulo 1 000 000 007  

The sequence begins with S = {0, 45, 2070, 4284945, 753524550, 478107844, 894218625, ...}.  

You are given F(2) = 45, F(4) = 4284990, F(100) = 26365463243, F(10^4) = 2495838522951.  
Find F(10^8).


Link: https://projecteuler.net/problem=477

Date solved:  
2022/XX/XX
"""

ANSWER = 0

# imports

from maths.sequences import Problem0477_Numbers


# solution


# setting up PN - no need to run

# s1 = 0

# def get_next(s):
#     return ((s**2 + 45) % 1000000007)

# current = s1
# S = [s1]
# for _ in range(int(1e8)):
#     current = get_next(current)
#     S.append(current)

# S

# PN = Problem0477_Numbers()
# PN.seq = S
# PN.update_cache()

PN = Problem0477_Numbers()


def play_game_eosums(S: list[int]):
    scores = [0, 0]
    evens_sum = sum(S[1::2])
    odds_sum = sum(S[::2])

    mindex = 0
    maxdex = len(S) - 1

    while maxdex - mindex > 1:
        # player 0 goes
        if evens_sum > odds_sum:
            # pick last item
            picked = S[maxdex]
            maxdex -= 1
            evens_sum -= picked
        else:
            # pick first item
            picked = S[mindex]
            mindex += 1
            odds_sum -= picked
            # evens and odd switch
            temp = evens_sum
            evens_sum = odds_sum
            odds_sum = temp
        scores[0] += picked

        # player 1 goes now
        # select the option that minimizes difference
        # between even_sum and odd_sum
        pick_first = max((odds_sum - S[mindex]), evens_sum)
        pick_last = max((odds_sum - S[maxdex]), evens_sum)
        if pick_last < pick_first:
            # pick last item
            picked = S[maxdex]
            maxdex -= 1
            odds_sum -= picked
        else:
            picked = S[mindex]
            mindex += 1
            odds_sum -= picked
            # evens and odd switch
            temp = evens_sum
            evens_sum = odds_sum
            odds_sum = temp
        scores[1] += picked

    scores[0] += max(S[mindex : mindex + 2])
    scores[1] += min(S[mindex : mindex + 2])

    return scores[0]


def create_taken_pattern(indicies_taken, length):
    taken_pattern = "["
    for i in range(length):
        taken_pattern += "X, " if i in indicies_taken else "_, "
    taken_pattern += "]"
    return taken_pattern


def play_game_bestpair(S: list[int]):
    scores = [0, 0]

    mindex = 0
    maxdex = len(S) - 1

    indecies_taken = []

    while maxdex - mindex > 1:

        # player 0 goes
        nums = S[mindex : mindex + 2] + S[maxdex - 1 : maxdex + 1]
        evens_sum = nums[1] + nums[3]
        odds_sum = nums[0] + nums[2]
        ends_sum = nums[0] + nums[3]
        max_sum = max([evens_sum, odds_sum, ends_sum])

        if (evens_sum == max_sum) or ((ends_sum == max_sum) and (nums[3] > nums[0])):
            # pick last item
            picked = maxdex
            maxdex -= 1
            evens_sum -= picked
        else:
            # pick first item
            picked = mindex
            mindex += 1
            odds_sum -= picked
            # evens and odd switch
            temp = evens_sum
            evens_sum = odds_sum
            odds_sum = temp
        indecies_taken.append(picked)
        scores[0] += S[picked]

        # player 0 goes
        # SAME AS ABOVE
        nums = S[mindex : mindex + 2] + S[maxdex - 1 : maxdex + 1]
        evens_sum = nums[1] + nums[3]
        odds_sum = nums[0] + nums[2]
        ends_sum = nums[0] + nums[3]
        max_sum = max([evens_sum, odds_sum, ends_sum])

        if (evens_sum == max_sum) or ((ends_sum == max_sum) and (nums[3] > nums[0])):
            # pick last item
            picked = maxdex
            maxdex -= 1
            evens_sum -= picked
        else:
            # pick first item
            picked = mindex
            mindex += 1
            odds_sum -= picked
            # evens and odd switch
            temp = evens_sum
            evens_sum = odds_sum
            odds_sum = temp
        scores[1] += S[picked]

    f1 = S[mindex]
    f2 = S[maxdex]
    if f1 > f2:
        scores[0] += f1
        scores[1] += f2
        indecies_taken.append(f1)
    else:
        scores[0] += f2
        scores[1] += f1
        indecies_taken.append(f2)

    taken_pattern = create_taken_pattern(indecies_taken, len(S))

    return scores[0], taken_pattern


# Tests

play_game = play_game_bestpair

cases = [
    ([0, 1], 1),
    ([1, 0], 1),
    ([1, 0, 1, 0, 0, 2, 0, 2, 1, 0, 1, 0], 6),
    ([2, 0, 2, 3], 5),
    (PN[:2], 45),
    (PN[:4], 4284990),
    (PN[:100], 26365463243),
]

for case in cases:
    print()
    S = case[0]
    out, taken_pattern = play_game(S)
    if out == case[1]:
        print("CORRECT")
        print(f"{S=} -> {out}")
        print(f"T={taken_pattern}")
    else:
        print("NO")
        print("NO")
        print(f"{S=} -> {case[1]}")
        print(f"You did: {out}")
        print(f"T={taken_pattern}")
        print("NO")
        print("NO")

numbers = 4

S = PN[:numbers]


def play_game(S: list[int]):
    scores = [0, 0]
    player = False  # player 0

    mindex = 0
    maxdex = len(S) - 1

    while maxdex - mindex > 1:
        print("mindex/maxdex:", mindex, maxdex)
        print(S[mindex : mindex + 2])
        print(S[maxdex - 2 : maxdex])
        odd_sum = S[mindex] + S[maxdex - 1]
        print("odd_sum", odd_sum)
        even_sum = S[mindex + 1] + S[maxdex]
        print("even_sum", even_sum)
        if odd_sum > even_sum:
            to_add = S[mindex]
            mindex += 1
        else:
            to_add = S[maxdex]
            maxdex -= 1
        print("player, to_add", player, to_add)
        scores[player] += to_add
        player = not player

        print("mindex/maxdex:", mindex, maxdex)
        print()

    print("finally left:", S[mindex : mindex + 2])
    scores[player] += max(S[mindex : mindex + 2])
    scores[not player] += min(S[mindex : mindex + 2])

    return scores


play_game(S)


def solution():


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution()
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
