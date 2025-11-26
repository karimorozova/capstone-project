import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from tabulate import tabulate

CSV_PATH = "data/security_comparison.csv"
OUTPUT_DIR = "data"
OUTPUT_FILE = "security_comparison_heatmap.png"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, OUTPUT_FILE)

df = pd.read_csv(CSV_PATH)

# Numeric mapping for heatmap
mapping = {
    "Low": 1,
    "Medium": 2,
    "High": 3,
    "Yes": 3,
    "No": 1,
    "Partial": 2,
    "Only Secret Chats": 2,
    True: 3,
    False: 1,
    "True": 3,
    "False": 1
}

# Numeric criteria
numeric_criteria = [
    "End-to-end encryption (private chats)",
    "End-to-end encryption (group chats)",
    "Metadata protection level",
    "Known vulnerabilities (historical)"
]

df_numeric = df[df["Criterion"].isin(numeric_criteria)].copy()
messenger_cols = df_numeric.columns[1:]
df_numeric[messenger_cols] = df_numeric[messenger_cols].replace(mapping)

df_numeric[messenger_cols] = df_numeric[messenger_cols].apply(pd.to_numeric, errors='coerce')

df_annot = df[df["Criterion"].isin(numeric_criteria)].set_index("Criterion")
df_numeric.set_index("Criterion", inplace=True)

print("Numeric matrix:\n", df_numeric)
print(df_numeric.dtypes)

os.makedirs(OUTPUT_DIR, exist_ok=True)

plt.figure(figsize=(12, 6))
sns.heatmap(
    df_numeric,
    annot=df_annot,
    fmt="",
    cmap="Blues",
    cbar_kws={"label": "Security Score"}
)
plt.title("Security Feature Comparison of Popular Messengers")
plt.tight_layout()

plt.savefig(OUTPUT_PATH, dpi=300)
plt.show()
plt.close()
print("Heatmap saved to:", OUTPUT_PATH)

print("\n--- Security Comparison Table ---\n")
print(tabulate(df, headers="keys", tablefmt="fancy_grid"))
