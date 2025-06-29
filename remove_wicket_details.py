import pandas as pd

df = pd.read_csv("bowling_detailed.csv")
if "wicket_details" in df.columns:
    df = df.drop(columns=["wicket_details"])
df.to_csv("bowling_detailed.csv", index=False)
print("Removed 'wicket_details' column and saved the CSV.")