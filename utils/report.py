import pandas as pd
import os
from datetime import datetime

def generate_report(prompt: str,responses:dict):
    os.makedirs("data/comparision_reports", exist_ok=True)

    row = []
    for model,output in responses.items():
        row.append({
            "Model": model,
            "Prompt": prompt,
            "Response": output,
            "Timestamp": datetime.now().strftime
            ("%Y-%m-%d %H:%M:%S")
        })

    df = pd.DataFrame(row)
    df.to_csv("data/comparision/report.csv",index=False)
    return "data/comparision/report.csv"


