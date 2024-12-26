import pandas as pd
import random

# Load existing data
users_df = pd.read_csv("mock_users.csv")
players_df = pd.read_csv("mock_players.csv")


# Parameters
num_bets = 10000  # Total number of bets to generate

# Generate user picks
user_picks = []
pick_id_counter = 1

for _ in range(num_bets):
    user = users_df.sample(1).iloc[0]  # Random user
    bet_type = random.choices(["Single", "Parlay"], weights=[0.7, 0.3], k=1)[0]  # 70% single, 30% parlay
    num_picks = 1 if bet_type == "Single" else random.randint(2, 4)  # Parlay has 2–4 picks

    # Generate picks for the bet
    parlay_picks = []
    parlay_odds = 1
    for _ in range(num_picks):
        player = players_df.sample(1).iloc[0]  # Random player
        projection = player["Projection"]
        actual_stat = player["Actual_Stat"]
        user_pick = random.choice(["Over", "Under"])
        
        # Determine result
        result = "Win" if (user_pick == "Over" and actual_stat > projection) or \
                         (user_pick == "Under" and actual_stat < projection) else "Loss"
        
        # Assign random odds (single bet odds)
        single_odds = round(random.uniform(1.5, 3.0), 2)
        parlay_odds *= single_odds  # Multiply odds for parlay bets
        
        # Append individual pick details
        parlay_picks.append({
            "Pick_ID": pick_id_counter,
            "User_ID": user["User_ID"],
            "Player_ID": player["Player_ID"],
            "Stat_Type": player["Stat_Type"],
            "User_Pick": user_pick,
            "Projection": projection,
            "Actual_Stat": actual_stat,
            "Result": result,
            "Single_Odds": single_odds
        })
        pick_id_counter += 1

    # Add parlay-level details
    bet_amount = round(random.uniform(10, 1000) if user["User_Type"] == "High Roller" else
                       random.uniform(10, 200), 2)
    overall_result = "Win" if all(pick["Result"] == "Win" for pick in parlay_picks) else "Loss"
    payout = bet_amount * parlay_odds if overall_result == "Win" else 0
    profit = payout - bet_amount
    roi = round(profit / bet_amount, 3) if bet_amount > 0 else 0

    # Add parlay summary
    user_picks.append({
        "Bet_Type": bet_type,
        "User_ID": user["User_ID"],
        "Bet_Amount": bet_amount,
        "Odds": round(parlay_odds, 2),
        "Payout": round(payout, 2),
        "Profit": round(profit, 2),
        "ROI": roi,
        "Overall_Result": overall_result,
        "Parlay_Details": parlay_picks
    })

# Convert to DataFrame
user_picks_df = pd.DataFrame(user_picks)

# Save to CSV
user_picks_df.to_csv("mock_user_picks.csv", index=False)
print("Mock user picks with parlays generated and saved to mock_user_picks.csv!")
