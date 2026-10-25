import numpy as np
import pandas as pd

# Load existing dataset
df = pd.read_csv("data/raw/iris_v1.csv")

# Generate Gaussian noise for data augmentation
rng = np.random.default_rng(42)
noise = rng.normal(0, 0.05, size=(20, 4))

# Sample 20 rows and apply noise to feature columns
sample = df.sample(20, random_state=42).reset_index(drop=True)
sample.iloc[:, :4] = sample.iloc[:, :4].values + noise

# Combine original dataset with synthetic samples
augmented = pd.concat([df, sample], ignore_index=True)

# Save augmented dataset back to CSV
augmented.to_csv("data/raw/iris_v1.csv", index=False)
print(f"Dataset now has {len(augmented)} rows")
