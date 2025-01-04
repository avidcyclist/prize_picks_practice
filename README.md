# Prize Picks Practice Project

## Overview

This project simulates a sports betting environment to analyze various betting strategies and their outcomes. The goal is to generate mock data that mimics real-world betting scenarios, calculate payouts, and determine the net profit for the sportsbook. The project also aims to provide insights into the effectiveness of different betting strategies.

## Data Generation

The mock data is generated using a Jupyter Notebook that creates random user IDs, bet amounts, and betting outcomes. The notebook also calculates the implied probabilities based on American odds and simulates the outcomes of each bet. The following steps outline the data generation process:

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

- **notebooks/**: Contains Jupyter notebooks for data generation, interactive data analysis, and visualization.
- **data/**: Contains the generated mock data in CSV format.

### notebooks/

- `new_notebook.ipynb`: Jupyter notebook for generating mock betting data, calculating payouts, profits, and net profits, and performing interactive data analysis.

### data/

- `prize_pick_practice1.csv`: Generated mock data containing user IDs, bet amounts, outcomes, payouts, profits, and net profits.

## How to Run the Project

1. **Generate Mock Data**: Open the `new_notebook.ipynb` notebook and run all the cells to generate the mock data and save it to the `data/` folder.
   ```bash
   jupyter notebook notebooks/new_notebook.ipynb


### Explanation:
- **Overview**: Describes the purpose and goals of the project.
- **Data Generation**: Outlines the steps taken to generate the mock data.
- **Project Structure**: Describes the organization of the project, including the notebooks and data folders.
- **How to Run the Project**: Provides instructions on how to run the notebook to generate data and perform analysis.
- **Goals and Objectives**: Lists the primary objectives of the project.
- **Conclusion**: Summarizes the project's contributions and insights.

Feel free to customize this README further to better fit your project's specifics. If you have any further questions or need additional assistance, feel free to ask!
### Explanation:
- **Overview**: Describes the purpose and goals of the project.
- **Data Generation**: Outlines the steps taken to generate the mock data.
- **Project Structure**: Describes the organization of the project, including the notebooks and data folders.
- **How to Run the Project**: Provides instructions on how to run the notebook to generate data and perform analysis.
- **Goals and Objectives**: Lists the primary objectives of the project.
- **Conclusion**: Summarizes the project's contributions and insights.

Feel free to customize this README further to better fit your project's specifics. If you have any further questions or need additional assistance, feel free to ask!
