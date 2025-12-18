import pandas as pd

def analyze_transactions(file):
    df = pd.read_csv(file.file)

    summary = {
        "total_transactions": len(df),
        "total_spent": df["amount"].sum(),
        "top_category": df["category"].mode()[0]
    }

    return summary
