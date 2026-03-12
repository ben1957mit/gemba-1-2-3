import pandas as pd
import os

DATA_DIR = "data"
ISSUE_FILE = os.path.join(DATA_DIR, "issues.csv")
FEEDBACK_FILE = os.path.join(DATA_DIR, "feedback.csv")

os.makedirs(DATA_DIR, exist_ok=True)

def load_csv(path, columns):
    if os.path.exists(path):
        try:
            return pd.read_csv(path)
        except Exception:
            return pd.DataFrame(columns=columns)
    return pd.DataFrame(columns=columns)

def save_csv(df, path):
    df.to_csv(path, index=False)
