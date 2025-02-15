import pandas as pd
from pathlib import Path

DATA_DIR = Path().resolve() / 'data'

def load_data(filepath=DATA_DIR / "dados_sensores_5000.parquet"):
    """Loads the Parquet file into a Pandas DataFrame."""
    try:
        df = pd.read_parquet(filepath, engine="pyarrow")
        df = df.rename(columns={"energia_kwh":"energia", "agua_m3":"agua", "co2_emissoes":"emissoes"}, errors="raise")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None