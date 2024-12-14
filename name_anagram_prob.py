# from nltk.corpus import words
import pandas
import math

#  nltk.download('words')
# Find First letter frequency using column "Name", and "2020 Count"

sex = "f"
year = 1996
boynames = pandas.read_csv(f"{sex}-babynames1996to2021.csv")


def get_freq_dist(input_df, year):
    col_name = f"{year} Count"
    freq = [0 for _ in range(26)]
    df = input_df[["Name", col_name]]

    letter_to_index = {chr(x+65):x for x in range(26)}

    for ind in df.index:
        try:
            letter = df["Name"][ind][0]
            index = letter_to_index[letter]

            if df[col_name][ind] != "[x]":
                freq[index]+=int(df[col_name][ind].replace(',', ''))
        except TypeError:
            print("ERROR: ", df["Name"][ind])

    return freq


def get_prob_dist(input_df, year):
    freq = get_freq_dist(input_df, year)
    count = sum(freq)
    prob_dist = [x/count for x in freq]
    return prob_dist, count


def multi_year_prob_data(input_df, years):
    freq = [0 for _ in range(26)]
    for year in years:
        cur_freq = get_freq_dist(input_df, year)
        for i in range(26):
            freq[i] += cur_freq[i]
    count = sum(freq)
    prob_dist = [x/count for x in freq]
    return prob_dist, count

prob_dist, count = get_prob_dist(boynames, year)

print(f"The following statistics are from {count} (assigned) male babies born in 2000 in England and Wales")
print()
for i in prob_dist:
    print(f"{i:.3f}", end=" ")



with open("mieliestronk.txt", mode="r") as f:
    word_list = f.read().splitlines()
word_list = [w for w in word_list if len(w)>2]

by_size = sorted(word_list, key=len)
letter_to_index = {chr(x+97):x for x in range(26)}

# assuming average number is 5 (for partners, friend, etc
max_size = 32
average = 5
poisson_dist = [pow(math.e, -average)*pow(average,x)/math.factorial(x) for x in range(max_size+1)]


records = []
for word in by_size:
    prob = 1
    for letter in word:
        try:
            prob *= prob_dist[letter_to_index[letter]]
        except KeyError:
            pass
    normalised = pow(prob, 1/len(word))
    poisson_normalised = prob*poisson_dist[len(word)]

    records.append((word, prob, normalised, poisson_normalised))
new_df = pandas.DataFrame(records)
new_df.columns = ["word", "prob", "normalised", "poisson"]

new_df = new_df.sort_values("poisson", ascending=False)
print(new_df[:50])
