import sqlite3
from sqlalchemy import create_engine
import pandas as pd

conn = sqlite3.connect(r'./DB/vivino.db')

query10 = """DROP TABLE IF EXISTS wines_grape;"""

table = """CREATE TABLE wines_grape (
    wine_id INTEGER,
    grape_id INTEGER,
    name VARCHAR(255),
    FOREIGN KEY (wine_id) REFERENCES wines(winery_id),
    FOREIGN KEY (grape_id) REFERENCES most_used_grapes_per_country(grape_id)
);
"""
engine = create_engine('sqlite:///../DB/vivino.db')

df = pd.read_csv('../CSV/wine.csv')
df.to_sql('wines_grape', con=engine, if_exists='append', index=False)
