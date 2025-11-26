import pandas as pd
import yaml
import os
from tabulate import tabulate

CONFIG_PATH = "config/security_data.yaml"

with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

df = pd.DataFrame(data)

output_dir = "data"
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, "security_comparison.csv")
df.to_csv(output_path, index=False, encoding="utf-8")

print("Table generated successfully:", output_path)

print("\n--- Security Comparison Table ---\n")
print(tabulate(df, headers="keys", tablefmt="fancy_grid"))
