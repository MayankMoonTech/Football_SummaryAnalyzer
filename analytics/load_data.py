import pandas as pd
import os

def load_match_data():

    # Get project root folder
    base_dir = os.path.dirname(os.path.dirname(__file__))

    # Build correct dataset path
    file_path = os.path.join(base_dir, "data", "match_events.csv")

    # Load dataset
    df = pd.read_csv(file_path)

    return df