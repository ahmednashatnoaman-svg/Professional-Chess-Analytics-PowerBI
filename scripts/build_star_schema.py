import pandas as pd
import numpy as np

def build_advanced_star_schema(input_file='games.csv'):
    print("Loading data...")
    df = pd.read_csv(input_file)
    df.drop_duplicates(inplace=True)

    print("--- 1. Building Enhanced Dim_Openings ---")
    dim_openings = df[['opening_eco', 'opening_name', 'opening_ply']].drop_duplicates().reset_index(drop=True)
    dim_openings['Opening_ID'] = dim_openings.index + 1
    
    # Extract Opening Family (Everything before the colon)
    dim_openings['Opening_Family'] = dim_openings['opening_name'].apply(lambda x: x.split(':')[0].strip() if ':' in x else x.split('|')[0].strip())
    
    # Categorize Complexity based on ply depth
    dim_openings['Complexity_Level'] = pd.cut(
        dim_openings['opening_ply'], 
        bins=[-1, 3, 7, 100], 
        labels=['Basic', 'Intermediate', 'Advanced']
    )
    
    df = df.merge(dim_openings[['opening_eco', 'opening_name', 'opening_ply', 'Opening_ID']], 
                  on=['opening_eco', 'opening_name', 'opening_ply'], how='left')

    print("--- 2. Building Enhanced Dim_TimeControls ---")
    dim_time = df[['increment_code', 'total_time', 'initial_time', 'increment', 'type']].drop_duplicates().reset_index(drop=True)
    dim_time['Time_ID'] = dim_time.index + 1
    dim_time.rename(columns={'type': 'Speed_Category'}, inplace=True)
    df = df.merge(dim_time[['increment_code', 'Time_ID']], on=['increment_code'], how='left')

    print("--- 3. Building Enhanced Dim_Players ---")
    # We need to aggregate stats for every unique player
    white_players = df[['white_id', 'white_rating', 'winner']].copy()
    white_players['is_win'] = (white_players['winner'] == 'white').astype(int)
    white_players.rename(columns={'white_id': 'Player_ID', 'white_rating': 'Rating'}, inplace=True)

    black_players = df[['black_id', 'black_rating', 'winner']].copy()
    black_players['is_win'] = (black_players['winner'] == 'black').astype(int)
    black_players.rename(columns={'black_id': 'Player_ID', 'black_rating': 'Rating'}, inplace=True)

    all_players = pd.concat([white_players, black_players])
    
    dim_players = all_players.groupby('Player_ID').agg(
        Total_Games=('Player_ID', 'count'),
        Total_Wins=('is_win', 'sum'),
        Average_Rating=('Rating', 'mean')
    ).reset_index()
    
    dim_players['Win_Rate_%'] = (dim_players['Total_Wins'] / dim_players['Total_Games'] * 100).round(2)
    dim_players['Average_Rating'] = dim_players['Average_Rating'].round(0)
    
    # Player Tiers
    dim_players['Player_Tier'] = pd.cut(
        dim_players['Average_Rating'], 
        bins=[0, 1200, 1500, 1800, 2200, 3000], 
        labels=['Beginner', 'Casual', 'Club Player', 'Expert', 'Master']
    )

    print("--- 4. Building Enhanced Fact_Games ---")
    fact_games = df[['id', 'rated', 'turns', 'victory_status', 'winner', 
                     'white_id', 'white_rating', 'black_id', 'black_rating', 
                     'Opening_ID', 'Time_ID']].copy()
    
    # Calculate Rating Difference
    fact_games['Rating_Difference'] = fact_games['white_rating'] - fact_games['black_rating']
    
    # Calculate Upset Flag (Did the underdog win?)
    conditions = [
        (fact_games['winner'] == 'white') & (fact_games['Rating_Difference'] < -50), # Black was favorite, White won
        (fact_games['winner'] == 'black') & (fact_games['Rating_Difference'] > 50)   # White was favorite, Black won
    ]
    fact_games['Is_Upset'] = np.select(conditions, [1, 1], default=0)

    print("Saving enriched files...")
    dim_openings.to_csv('Dim_Openings.csv', index=False)
    dim_time.to_csv('Dim_TimeControls.csv', index=False)
    dim_players.to_csv('Dim_Players.csv', index=False)
    fact_games.to_csv('Fact_Games.csv', index=False)

    print("✅ Advanced Expert Star Schema generated successfully!")

if __name__ == "__main__":
    build_advanced_star_schema()
