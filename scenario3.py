unisex_fld = [0.11496007733872045, 0.033093753553561006, 0.06283094959786474, 0.034682927937531444, 0.07475139833647483, 0.026709625710111255, 0.024884440336132664, 0.04748530911180312, 0.028774114444886298, 0.0899280879759246, 0.03774961805645674, 0.0754755782315965, 0.08621921732623261, 0.025228590308668836, 0.028829654587952627, 0.01771189300608217, 0.0005466618819125479, 0.05018881507866309, 0.06493722402503493, 0.03924376858210682, 0.0013474028563640237, 0.005369447382759467, 0.010963489784795473, 0.0007106858716543938, 0.0041952006572002366, 0.013182068019509148]

def scenario3(fld, word, k):
    word = word.upper()
    prob = 1
    for letter in word:
        p =fld[ord(letter)-65]
        prob *= 1-pow(1-p, k)
    return prob

values = list(range(1,11))+[15, 20, 30, 40, 50, 100, 500]
fld = [1/26 for _ in range(26)]
word = "bermuda"
for k in values:
    answer = scenario3(unisex_fld, word, k)
    print(f"{k: 5d} {answer:.4g}")



with open("mieliestronk.txt", mode="r") as f:
    word_list = f.read().splitlines()
word_list = [w for w in word_list if len(w)>2]


max_size = max(len(x) for x in word_list)
grouped  = [[] for _ in range(max_size)]
for i in word_list:
    grouped[len(i)-1].append(i)


values = [1,2,3,4,5,10,20, 50, 100]

for k in values:
    print(f"\nk={k}")
    ans = []
    for word in grouped[4]:
        answer = scenario3(unisex_fld, word, k)
        ans.append((word, answer))
    ans.sort(key=lambda x: x[1] ,reverse=True)
    for a,b in ans[:10]:
        print(f"{a}: {b : 4g}")


