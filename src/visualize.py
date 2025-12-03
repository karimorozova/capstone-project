import yaml
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

with open("data/security_comparison.yaml", "r") as file:
    data = yaml.safe_load(file)

df = pd.DataFrame(data["messengers"])

binary_fields = ["e2ee_default", "e2ee_available", "audited"]
binary_df = df[["name"] + binary_fields].copy()

# Перетворення булевих значень у 0/1
for col in binary_fields:
    binary_df[col] = binary_df[col].astype(int)

binary_df = binary_df.set_index("name")

# --- HEATMAP ---
plt.figure(figsize=(6, 4))
sns.heatmap(binary_df, annot=True, cmap="Greens", vmin=0, vmax=1)
plt.title("Secure Features Comparison")
plt.tight_layout()
plt.savefig("output/heatmap.png")
print("Heatmap saved to output/heatmap.png")
