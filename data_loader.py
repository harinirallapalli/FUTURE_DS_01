import pandas as pd


def load_data(file_path):
    try:
        df = pd.read_csv(file_path, encoding='latin1')
        print("Dataset Loaded Successfully")
        return df

    except Exception as e:
        print(f"Error Loading Dataset: {e}")
        return None


def clean_data(df):

    df.drop_duplicates(inplace=True)

    df.dropna(inplace=True)

    df['Order Date'] = pd.to_datetime(df['Order Date'])

    df['Ship Date'] = pd.to_datetime(df['Ship Date'])

    return df