# This contains parser for Zerodha broker tradebook CSV files

import pandas as pd
import os
from mktanalyst.tb_parser.st_tb import STANDARD_TRADEBOOK_HEADERS

def parse_tradebook(file_path: str) -> pd.DataFrame:
    """
    Load a tradebook CSV into a pandas DataFrame.
    
    Args:
        csv_path (str): Path to the CSV file.
    
    Returns:
        pd.DataFrame: Parsed DataFrame with correct date parsing if present.
    """
    try:
        df = pd.read_csv(file_path, parse_dates=True)
        return df
    except Exception as e:
        print(f"Error reading file: {e}")
        return pd.DataFrame()

here = os.path.dirname(os.path.abspath(__file__))
ZERODHA_TRADEBOOK = os.path.join(here, "..", "..", "..", "tests", "data", "tb_zerodha.csv")

def convert_to_standard_format(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert Zerodha tradebook DataFrame to standard format.
    
    Args:
        df (pd.DataFrame): DataFrame with Zerodha tradebook data.
    
    Returns:
        pd.DataFrame: DataFrame in standard format.
    """
    # Mapping Zerodha columns to standard columns
    column_mapping = {
        "Symbol": "symbol",
        "trade_date": "date",
        "exchange": "exchange",
        "trade_type": "transaction_type",
        "quantity": "quantity",
        "price": "price"
    }
    
    df_standard = df.rename(columns=column_mapping)
    
    # Ensure all standard headers are present
    for col in STANDARD_TRADEBOOK_HEADERS:
        if col not in df_standard.columns:
            df_standard[col] = None  # or appropriate default value
    # Reorder columns to match standard headers    and give only standard headers columns
    df_standard = df_standard[STANDARD_TRADEBOOK_HEADERS]
    return df_standard
    
def adjust_for_splits(symbol: str, df: pd.DataFrame, split_info: dict) -> pd.DataFrame:
    """
    Adjust trade quantities for stock splits.
    
    Args:
        symbol (str): Stock symbol to adjust.
        df (pd.DataFrame): DataFrame with trade data.
        split_info (dict): Dictionary with split dates as keys and split ratios as values.
    
    Returns:
        pd.DataFrame: Adjusted DataFrame.
    """
    df = df.copy()
    for split_date, ratio in split_info.items():
        mask = (df['symbol'] == symbol) & (df['date'] < pd.to_datetime(split_date))
        df.loc[mask, 'quantity'] *= ratio
    return df

def adjust_for_bonuses(symbol: str,  df: pd.DataFrame, bonus_info: dict) -> pd.DataFrame:
    """
    Adjust trade quantities for stock bonuses.
    
    Args:
        symbol (str): Stock symbol to adjust.
        df (pd.DataFrame): DataFrame with trade data.
        bonus_info (dict): Dictionary with bonus dates as keys and bonus ratios as values.
    
    Returns:
        pd.DataFrame: Adjusted DataFrame.
    """
    df = df.copy()
    for bonus_date, ratio in bonus_info.items():
        mask = (df['symbol'] == symbol) & (df['date'] < pd.to_datetime(bonus_date))
        df.loc[mask, 'quantity'] *= ratio
    return df

if __name__ == "__main__":
    # Example usage
    tradebook_df = parse_tradebook(ZERODHA_TRADEBOOK)
    standard_df = convert_to_standard_format(tradebook_df)
