Prize Picks Practice Project
Overview
This project simulates a sports betting environment to analyze various betting strategies and their outcomes. The goal is to generate mock data that mimics real-world betting scenarios, calculate payouts, and determine the net profit for the sportsbook. The project also aims to provide insights into the effectiveness of different betting strategies.

Data Generation
The mock data is generated using a Python script that creates random user IDs, bet amounts, and betting outcomes. The script also calculates the implied probabilities based on American odds and simulates the outcomes of each bet. The following steps outline the data generation process:

'Generate Random Data': Create mock data for user IDs, number of bets, and bet amounts.
Generate Random Odds: Generate random American odds for each entry.
Convert American Odds to Implied Probabilities: Calculate the implied probabilities for each bet.
Simulate Bet Outcomes: Simulate the outcomes of each bet based on the implied probabilities.
Calculate Commission: Calculate the casino's commission as 10% of the bet amount.
Calculate Effective Bet Amount: Subtract the commission from the total bet amount to get the effective bet amount.
Calculate Payouts: Calculate the payouts based on the effective bet amount and the number of wins.
Calculate Profit: Calculate the profit as the difference between the payout and the bet amount.
Calculate Net Profit for the Sportsbook: Calculate the net profit for the sportsbook by subtracting the payouts and commission from the total bet amount.
Project Structure
The project is organized into the following folders:

scripts/: Contains Python scripts used for data generation and analysis.
notebooks/: Contains Jupyter notebooks for interactive data analysis and visualization.
data/: Contains the generated mock data in CSV format.
