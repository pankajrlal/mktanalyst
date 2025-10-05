import os
import pandas as pd 
from sqlmesh import model

@model(
    "holdings.groww_raw", 
    kind="FULL",
    columns = {
        "Stock Name": "str",
        "ISIN": "str",
        "Quantity": "float",
        "Average buy price": "float",
        "Buy value": "float",
        "Closing price": "float",
        "Closing value": "float",
        "Unrealised P&L": "float",
        "holdings_date": "datetime",
    }
)
def groww_holdings(context, **kwargs)-> pd.DataFrame:
    """
    Extract the current holdings from "seeds/groww/holdings_YYYYMMDD.csv" 

    Args:
        context: The model context provided by the framework.

    Returns:
        list: A pandas DataFrame containing the current holdings.
    """

    # Scan the files in the seeds/groww directory 
    # For each file, check if it matches the pattern "holdings_YYYYMMDD.csv"
    # Extract the date from the filename and keep track of the latest date 
    # Read the CSV file into a pandas DataFrame 
    # Add a new column 'holdings_date' to the DataFrame with the extracted date
    # Return the DataFrame


    seed_dir = "seeds/groww/"
    all_dfs = []

    for filename in os.listdir(seed_dir):
        date = None
        if filename.startswith("holdings_") and filename.endswith(".csv"):
            date_str = filename[len("holdings_"):-len(".csv")]
            try:
                date = pd.to_datetime(date_str, format="%Y%m%d")
            except ValueError:
                continue
            df = pd.read_csv(os.path.join(seed_dir, filename))
            my_df  = df.copy()
            my_df['holdings_date'] = date
            all_dfs.append(my_df)

    all_dfs = pd.concat(all_dfs)
    return all_dfs
