
import pandas
import math

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

def multi_year_prob_data(input_df, years):
    freq = [0 for _ in range(26)]
    for year in years:
        cur_freq = get_freq_dist(input_df, year)
        for i in range(26):
            freq[i] += cur_freq[i]
    count = sum(freq)
    prob_dist = [x/count for x in freq]
    return prob_dist, count

years = list(range(1996,2022))
boynames = pandas.read_csv("m-babynames1996to2021.csv")
girlnames = pandas.read_csv("f-babynames1996to2021.csv")



boy_prob_dist, _ = multi_year_prob_data(boynames, years)
girl_prob_dist, _ = multi_year_prob_data(girlnames, years)

unisex_fld = [(a+b)/2 for (a,b) in zip(boy_prob_dist, girl_prob_dist)]