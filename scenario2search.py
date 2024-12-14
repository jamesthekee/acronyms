from time import time

unisex_fld = [0.11496007733872045, 0.033093753553561006, 0.06283094959786474, 0.034682927937531444, 0.07475139833647483, 0.026709625710111255, 0.024884440336132664, 0.04748530911180312, 0.028774114444886298, 0.0899280879759246, 0.03774961805645674, 0.0754755782315965, 0.08621921732623261, 0.025228590308668836, 0.028829654587952627, 0.01771189300608217, 0.0005466618819125479, 0.05018881507866309, 0.06493722402503493, 0.03924376858210682, 0.0013474028563640237, 0.005369447382759467, 0.010963489784795473, 0.0007106858716543938, 0.0041952006572002366, 0.013182068019509148]



with open("mieliestronk.txt", mode="r") as f:
    word_list = f.read().splitlines()
word_list = [w for w in word_list if len(w)>2]


max_size = max(len(x) for x in word_list)
grouped  = [[] for _ in range(max_size)]
for i in word_list:
    grouped[len(i)-1].append(i)


def fact(x):
    if x == 0:
        return 1
    return x*fact(x-1)

def multi(xs):
    a = 1
    s = 0
    for i in xs:
        a *= fact(i)
        s += i
    return fact(s)//a


for length in range(1, 10):
    ws = grouped[length-1]
    res = []
    for w in ws:
        counts = [0 for _ in range(26)]
        prob = 1
        for letter in w:
            prob *= unisex_fld[ord(letter)-97]
        res.append((w, prob))
    res.sort(key=lambda x: x[1],reverse=True)
    for a,b in res[:10]:
        print(f"{a}: {b:.4g}")
