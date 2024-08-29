import sqlite3

conn = sqlite3.connect(r'./DB/vivino.db')

query10 = """DROP TABLE IF EXISTS wines_grape;"""

table