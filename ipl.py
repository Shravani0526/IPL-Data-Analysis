import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("matches.csv")

print("Dataset Preview:")
print(df.head())

wins = df['winner'].value_counts()
print("\nMost Winning Teams:\n", wins)

wins.plot(kind='bar', title="Most Wins by Teams")
plt.xlabel("Teams")
plt.ylabel("Wins")
plt.show()

toss_match = df[df['toss_winner'] == df['winner']]
print("\nMatches where Toss Winner also Won:", len(toss_match))

toss_decision = df['toss_decision'].value_counts()
toss_decision.plot(kind='pie', autopct='%1.1f%%', title="Toss Decision Distribution")
plt.show()

venue_count = df['venue'].value_counts()
venue_count.plot(kind='bar', title="Matches per Venue")
plt.show()