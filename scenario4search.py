from time import time
from functools import lru_cache

unisex_fld = [0.11496007733872045, 0.033093753553561006, 0.06283094959786474, 0.034682927937531444, 0.07475139833647483, 0.026709625710111255, 0.024884440336132664, 0.04748530911180312, 0.028774114444886298, 0.0899280879759246, 0.03774961805645674, 0.0754755782315965, 0.08621921732623261, 0.025228590308668836, 0.028829654587952627, 0.01771189300608217, 0.0005466618819125479, 0.05018881507866309, 0.06493722402503493, 0.03924376858210682, 0.0013474028563640237, 0.005369447382759467, 0.010963489784795473, 0.0007106858716543938, 0.0041952006572002366, 0.013182068019509148]


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



with open("mieliestronk.txt", mode="r") as f:
    word_list = f.read().splitlines()
word_list = [w for w in word_list if len(w)>2]


max_size = max(len(x) for x in word_list)
grouped  = [[] for _ in range(max_size)]
for i in word_list:
    grouped[len(i)-1].append(i)


values = [10]

for k in values:
    print(k)
    print()
    
    for l in range(1, 9):
        ans = []
        for word in grouped[l]:
            answer = presolution(unisex_fld, word, k)
            ans.append((word, answer))
        ans.sort(key=lambda x: x[1] ,reverse=True)

        for a,b in ans[:10]:
            print(f"{a}: {b:.4g}")
        print()

print(time()-s)

