import pandas as pd

df = pd.read_csv("./example-basketball-data.csv")

def func1(first_basket_player, row):
    '''Returns bool: whether first basket player made any of the first 3 shots'''
    for c in ["First Shot Player", "Second Shot Player", "Third Shot Player"]:
        if first_basket_player == row[c]:
            return True
    return False

def func2(first_basket_player, row):
    '''Returns int: number of first 3 shots made by first basket player'''
    r = 0
    for c in ["First Shot Player", "Second Shot Player", "Third Shot Player"]:
        if first_basket_player == row[c]:
            r += 1
    return r

def func3(row):
    '''Returns int: number of the first 3 shots that match both player and type of first basket'''
    first_basket_player = row['First Basket Player']
    first_basket_type = row['First Basket Type']

    r = 0
    for n in ["First", "Second", "Third"]:
        if first_basket_player == row[n + " Shot Player"] and first_basket_type == row[n + " Shot Type"]:
            r += 1
    return r

for i, row in df.iterrows():
    first_basket_player = row['First Basket Player']
    print(f"Game {row['Game']}: first basket was {row['First Basket Type']} by {first_basket_player}")
    print(f"Did {first_basket_player} make any of the first 3 shots? {func1(first_basket_player, row)}")
    print(f"How many of the first 3 shots were made by {first_basket_player}? {func2(first_basket_player, row)}")
    print(f"How many of the first 3 shots were a {row['First Basket Type']} made by {first_basket_player}? {func3(row)}")
    print("\n---\n")
