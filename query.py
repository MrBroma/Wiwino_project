# File with all the different queries to qnswers the questions

# import of the different library
import sqlite3



# Questions:
# 1. We want to highlight 10 wines to increase our sales. Which ones should we choose and why?
# 2. We have a limited marketing budget for this year. Which country should we prioritise and why?
# 3. We would like to give awards to the best wineries. Come up with 3 relevant ones. Which wineries should we choose and why?
# 4. We detected that a big cluster of customers likes a specific combination of tastes. We identified a few 
# keywords that match these tastes: coffee, toast, green apple, cream, and citrus (note that these keywords are case sensitive ⚠️). 
# We would like you to find all the wines that are related to these keywords. Check that at least 10 users confirm those keywords,
# to ensure the accuracy of the selection. Additionally, identify an appropriate group name for this cluster.
# 5. We would like to select wines that are easy to find all over the world. Find the top 3 most common grapes all over the world 
# and for each grape, give us the the 5 best rated wines.
# 6. We would like to create a country leaderboard. Come up with a visual that shows the average wine rating for each country. Do the same for the vintages.
# 7. One of our VIP clients likes Cabernet Sauvignon and would like our top 5 recommendations. Which wines would you recommend to him?


# Query for 1.
query1 = """SELECT v.name AS wine_name,
       MIN(v.year) AS year,
       MIN(v.price_euros) AS price_euros,
       MAX(v.ratings_average) AS ratings_average,
       MAX(wines.ratings_count) AS ratings_count
FROM vintages v
JOIN wines ON v.wine_id = wines.id
JOIN vintage_toplists_rankings ON v.id = vintage_toplists_rankings.vintage_id
WHERE v.price_euros < 300
GROUP BY wines.name
ORDER BY MIN(vintage_toplists_rankings.rank) ASC
LIMIT 10;
"""

# Query for 2.
query2 = """SELECT *
FROM countries
ORDER BY users_count DESC LIMIT 3
"""


# Query for 3.
query3 = """SELECT 
    t.vintage_id, 
    vintages.name, 
    wines.url, 
    t.rank, 
    t.previous_rank, 
    (t.previous_rank - t.rank) AS rank_difference
FROM vintage_toplists_rankings t
JOIN vintages
    ON t.vintage_id = vintages.id
JOIN wines
    ON vintages.wine_id = wines.id
WHERE t.rank = 1
GROUP BY vintages.name, t.vintage_id, wines.url, t.rank, t.previous_rank
ORDER BY rank_difference DESC
LIMIT 3;
"""

# Query for 4.
query4 = """
"""

# Query for 5.
query5 = """WITH top_grapes AS (
    SELECT
        grape_id,
        COUNT(DISTINCT country_code) AS country_count
    FROM most_used_grapes_per_country
    GROUP BY grape_id
    ORDER BY country_count DESC
    LIMIT 3
),
ranked_wines AS (
    SELECT
        wines.id AS wine_id,
        wines.name AS wine_name,
        v.name AS vintage_name,
        v.ratings_average,
        regions.name AS region_name,
        countries.name AS country_name,
        grapes.name AS grape_name,
        ROW_NUMBER() OVER (PARTITION BY grapes.id ORDER BY v.ratings_average DESC) AS wine_rank
    FROM wines
    JOIN vintages v ON wines.id = v.wine_id
    JOIN regions ON wines.region_id = regions.id
    JOIN countries ON regions.country_code = countries.code
    JOIN most_used_grapes_per_country top ON countries.code = top.country_code
    JOIN grapes ON top.grape_id = grapes.id
    WHERE grapes.id IN (SELECT grape_id FROM top_grapes)
)
SELECT
    wine_name,
    vintage_name,
    ratings_average,
    region_name,
    country_name,
    grape_name
FROM ranked_wines
WHERE wine_rank <= 5
ORDER BY grape_name, ratings_average DESC
LIMIT 15; 
"""

# Query for 6-1.
query6_1="""SELECT countries.name AS country,
    wines.ratings_average AS avg_wine_rating
FROM wines
JOIN regions
    ON wines.region_id = regions.id
JOIN countries
    ON regions.country_code = countries.code
GROUP BY countries.name
ORDER BY avg_wine_rating DESC;
"""

# Query for 6-2.
query6_2="""SELECT DISTINCT SUBSTR(vintages.name, 1, LENGTH(vintages.name) - 5) AS vintages,
       wines.ratings_average AS avg_wine_rating 
FROM wines 
JOIN vintages ON wines.id = vintages.wine_id 
ORDER BY avg_wine_rating  DESC
LIMIT 20;
"""

# Query for 7.
query7="""

"""