from query import query1, query2, query3, query4, query5, query6_1, query6_2, query7
import sqlite3
import pandas as pd


conn = sqlite3.connect(r'./DB/vivino.db')

# register each request into a csv for the data analysis

# df = pd.read_sql_query (query1, conn).to_csv("/CSV/csv_10_wines.csv", index=False)
# df = pd.read_sql_query (query2, conn).to_csv("../CSV/csv_10_wines.csv", index=False)
# df = pd.read_sql_query (query3, conn).to_csv("/CSV/csv_top3_wineries_top1.csv", index=False)
# df = pd.read_sql_query (query4, conn).to_csv("../CSV/csv_10_wines.csv", index=False)
df = pd.read_sql_query (query5, conn).to_csv("./CSV/best_rated_wines_most_common_grapes.csv", index=False)
# df = pd.read_sql_query (query6, conn).to_csv("/CSV/csv_10_wines.csv", index=False)
# df = pd.read_sql_query (query7, conn).to_csv("/CSV/csv_10_wines.csv", index=False)



