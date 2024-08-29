from query import query1, query2, query3, query4, query5, query6_1, query6_2, query7
import sqlite3
import pandas as pd


conn = sqlite3.connect(r'./DB/vivino.db')

# register each request into a csv for the data analysis
df1 = pd.read_sql_query (query1, conn).to_csv("./CSV/1_wine_ratings.csv", index=False)
df2 = pd.read_sql_query (query2, conn).to_csv("./CSV/2_country_marketing.csv", index=False)
# Execute one time and complete manually fir the wineries name
# df3 = pd.read_sql_query (query3, conn).to_csv("/CSV/3_csv_top3_wineries_top1.csv", index=False)
df4 = pd.read_sql_query (query4, conn).to_csv("./CSV/4_keywords_wines.csv", index=False)
df5 = pd.read_sql_query (query5, conn).to_csv("./CSV/5_best_rated_wines_most_common_grapes.csv", index=False)
df6_1 = pd.read_sql_query (query6_1, conn).to_csv("./CSV/6-1_country_ratings.csv", index=False)
df6_2 = pd.read_sql_query (query6_2, conn).to_csv("./CSV/6-2_vintages_wineratings.csv", index=False)
df7 = pd.read_sql_query (query7, conn).to_csv("./CSV/7_Cabernet_Sauvignon.csv", index=False)

