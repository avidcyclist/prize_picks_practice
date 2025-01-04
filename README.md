# Prize Picks Practice Project

## Overview

This project simulates a sports betting environment to analyze various betting strategies and their outcomes. The goal is to generate mock data that mimics real-world betting scenarios, calculate payouts, and determine the net profit for the sportsbook. The project also aims to provide insights into the effectiveness of different betting strategies.

## Data Generation

The mock data is generated using a Python script that creates random user IDs, bet amounts, and betting outcomes. The script also calculates the implied probabilities based on American odds and simulates the outcomes of each bet. The following steps outline the data generation process:

1. **Generate Random Data**: Create mock data for user IDs, number of bets, and bet amounts.
2. **Generate Random Odds**: Generate random American odds for each entry.
3. **Convert American Odds to Implied Probabilities**: Calculate the implied probabilities for each bet.
4. **Simulate Bet Outcomes**: Simulate the outcomes of each bet based on the implied probabilities.
5. **Calculate Commission**: Calculate the casino's commission as 10% of the bet amount.
6. **Calculate Effective Bet Amount**: Subtract the commission from the total bet amount to get the effective bet amount.
7. **Calculate Payouts**: Calculate the payouts based on the effective bet amount and the number of wins.
8. **Calculate Profit**: Calculate the profit as the difference between the payout and the bet amount.
9. **Calculate Net Profit for the Sportsbook**: Calculate the net profit for the sportsbook by subtracting the payouts and commission from the total bet amount.

## Project Structure

The project is organized into the following folders:

- **scripts/**: Contains Python scripts used for data generation and analysis.
- **notebooks/**: Contains Jupyter notebooks for interactive data analysis and visualization.
- **data/**: Contains the generated mock data in CSV format.

### scripts/

- `generate_mock_data.py`: Script to generate mock betting data and calculate payouts, profits, and net profits.
- `analyze_data.py`: Script to analyze the generated data and provide insights into betting strategies.

### notebooks/

- `data_analysis.ipynb`: Jupyter notebook for interactive data analysis and visualization.
- `strategy_evaluation.ipynb`: Jupyter notebook to evaluate the effectiveness of different betting strategies.

### data/

- `prize_pick_practice1.csv`: Generated mock data containing user IDs, bet amounts, outcomes, payouts, profits, and net profits.

## How to Run the Project

1. **Generate Mock Data**: Run the `generate_mock_data.py` script to generate the mock data and save it to the `data/` folder.
   ```bash
   python scripts/generate_mock_data.py
