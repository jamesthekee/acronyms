

def upper_bound(word, k):
  n = len(word)
  total = 1 
  for i in range(n):
      total *= 1 - pow(1-(n-i)/26, k)
  return total

word = "bermuda"
for k in [15,20,30,40,50,100,500]:
  print(k,upper_bound(word, k))