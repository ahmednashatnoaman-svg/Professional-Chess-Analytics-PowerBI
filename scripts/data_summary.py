import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('games.csv')

# Basic Stats
total_games = len(df)
winner_counts = df['winner'].value_counts()
win_rate = (winner_counts / total_games * 100).round(2)

# Opening Stats
top_openings = df['opening_name'].value_counts().head(5)

# Rating Stats
avg_white_rating = df['white_rating'].mean().round(0)
avg_black_rating = df['black_rating'].mean().round(0)

# Victory Status
victory_types = df['victory_status'].value_counts()

print(f"--- Chess Dataset Summary ---")
print(f"Total Games Analyzed: {total_games}")
print(f"\nWin Rates:")
for winner, rate in win_rate.items():
    print(f"  - {winner.capitalize()}: {rate}%")

print(f"\nTop 5 Openings:")
for opening, count in top_openings.items():
    print(f"  - {opening}: {count} games")

print(f"\nAverage Ratings:")
print(f"  - White: {avg_white_rating}")
print(f"  - Black: {avg_black_rating}")

print(f"\nVictory Status Distribution:")
for status, count in victory_types.items():
    print(f"  - {status.capitalize()}: {count}")
