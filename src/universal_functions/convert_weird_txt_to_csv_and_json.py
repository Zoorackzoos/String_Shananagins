import pandas as pd

# Read line by line and split on backslash
with open("../../sheets/grady_ward_sheet/mobypos.txt", "r", encoding="utf-8") as f:
    lines = [line.strip().split("\\", 1) for line in f if line.strip()]

df = pd.DataFrame(lines, columns=["word", "pos_codes"])

# Save CSV and JSON
df.to_csv("moby_pos_raw_parsed.csv", index=False)
df.to_json("moby_pos_raw_parsed.json", orient="records", indent=2)