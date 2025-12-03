import yaml
import pandas as pd
from tabulate import tabulate

with open("data/security_comparison.yaml", "r") as file:
    data = yaml.safe_load(file)

df = pd.DataFrame(data["messengers"])

# Зберігаємо таблицю у CSV для звіту
df.to_csv("output/security_table.csv", index=False)

# --- КРАСИВИЙ ASCII ПРИНТ У КОНСОЛЬ ---
print("\n================ Messengers Security Table ================\n")
print(tabulate(df, headers="keys", tablefmt="grid", showindex=False))
print("\n============================================================\n")
