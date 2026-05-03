# Advanced Professional DAX Measures for Chess Analysis

Add these measures to a dedicated **'Measures Table'** for a professional structure.

## 1. Elo Expected Win Rate
Calculates the theoretical probability of White winning based on the rating difference.
```dax
Expected Win Rate (White) = 
VAR RatingDiff = SELECTEDVALUE('games'[white_rating]) - SELECTEDVALUE('games'[black_rating])
RETURN
1 / (1 + POWER(10, (-RatingDiff / 400)))
```

## 2. Performance vs. Expectation (PvE)
A measure of whether a player (or opening) is over-performing or under-performing.
```dax
Performance Score = 
VAR ActualWin = IF(SELECTEDVALUE('games'[winner]) = "white", 1, IF(SELECTEDVALUE('games'[winner]) = "draw", 0.5, 0))
VAR ExpectedWin = [Expected Win Rate (White)]
RETURN
ActualWin - ExpectedWin
```

## 3. Rating Volatility
Shows the standard deviation of ratings in the current selection, useful for understanding the competitive range.
```dax
Rating Std Dev = STDEV.P('games'[white_rating])
```

## 4. Opening Efficiency Score
Calculates how much an opening "boosts" a player's expected performance.
```dax
Opening Efficiency = 
AVERAGEX(
    'games',
    [Performance Score]
)
```

## 5. Dynamic Dashboard Title
A professional touch that updates based on the current filters.
```dax
Dashboard Header = 
"Chess Performance Analysis | " & 
IF(ISFILTERED('games'[victory_status]), SELECTEDVALUE('games'[victory_status]), "All Outcomes") & 
" (" & FORMAT(COUNTROWS('games'), "#,##0") & " Games)"
```

## 6. Time Control Category
A calculated column (if not already present) for cleaner filtering.
```dax
Game Speed Category = 
VAR Inc = 'games'[initial_time]
RETURN
SWITCH( TRUE(),
    Inc <= 3, "Blitz",
    Inc <= 10, "Rapid",
    "Classical"
)
```
