# prize_picks_practice
Testing my skills on a mock data set of betting users to perform statistical analysis to see where the company can improve


I started this when I saw an open job for BI Finance Analyst. I started by trying to find public data but ended up asking for a mock data script to work on.

## Data Generation

The mock data used in this project was generated using the `mock_user_picks.py` script. This script simulates user bets, including both single bets and parlays, and calculates the outcomes based on random selections and predefined probabilities.

### How the Data Was Generated

The `mock_user_picks.py` script generates mock user picks with the following steps:
1. **Load Existing Data**: Load user and player data from CSV files.
2. **Generate User Picks**: Simulate a specified number of bets, randomly selecting users and players for each bet.
3. **Determine Bet Type**: Randomly choose between single bets and parlays, with a 70% chance of single bets and a 30% chance of parlays.
4. **Calculate Outcomes**: Determine the outcome of each bet based on random selections and predefined probabilities.
5. **Calculate Payouts and Profits**: Calculate the payout, profit, and ROI for each bet.
6. **Save to CSV**: Save the generated data to a CSV file for analysis.

For more details, refer to the `mock_user_picks.py` script in this repository.
