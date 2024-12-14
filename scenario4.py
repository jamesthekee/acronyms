from time import time
from functools import lru_cache

unisex_fld = [0.11496, 0.03309, 0.06283, 0.03468, 0.07475, 0.02670, 0.02488, 0.04748, 0.02877, 0.08992, 0.03774, 0.07547, 0.08621, 0.02522, 0.02882, 0.01771, 0.00054, 0.05018, 0.06493, 0.03924, 0.00134, 0.00536, 0.01096, 0.00071, 0.00419, 0.01318]

# with open("mieliestronk.txt", mode="r") as f:
#     word_list = f.read().splitlines()
# word_list = [w for w in word_list if len(w)>2]
# 
# by_size = sorted(word_list, key=len)
# letter_to_index = {chr(x+97):x for x in range(26)}

@lru_cache(maxsize=None)
def solution(state, k, fld):
    current_state = list(state)
    if all(x == 0 for x in current_state):
        return 1.0
    total = 0
    cur = 1
    for i in range(len(current_state)):
        if current_state[i] > 0:
            branch_prob = 1-pow(1-fld[i], k)
            current_state[i] -= 1
            total += cur * branch_prob * solution(tuple(current_state), k, fld)
            current_state[i] += 1
            if k > 1:
                cur *= (1-branch_prob)
    return total

# Acronym group case 4 generic case
def presolution(fld, word, k):
    word = word.upper()

    letter_freq = [0 for _ in range(26)]
    for i in word:
        letter_freq[ord(i)-65] += 1
    
    sorted_freq = sorted(zip(letter_freq, fld), key=lambda x: x[1] )
    sorted_state = (x[0] for x in sorted_freq)
    sorted_fld  = sorted(fld)

    return solution(sorted_state, k, tuple(sorted_fld))

s = time()
values = list(range(1,11))+[15, 20, 30, 40, 50, 100, 500]
fld = [1/26 for _ in range(26)]
word = "homosexual"
for k in values:
    answer = presolution(unisex_fld, word, k)
    print(f"{k: 5d} {answer:.4g}")

print(time()-s)

