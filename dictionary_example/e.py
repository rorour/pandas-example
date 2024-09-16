import pandas as pd

df = pd.read_csv("./example-data-2.csv")
players = {}
SHOTS = ("First Basket", "Layups", "Dunks")
for _, r in df.iterrows():
    p = r["Player"]
    players[p] = players.get(p, {})
    for s in SHOTS:
        players[p][s] = r[s] + players[p].get(s, 0)

print(f"Results:\n{players}")