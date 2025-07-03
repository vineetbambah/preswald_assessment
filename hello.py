from preswald import connect, get_df, text, query,table, slider, plotly, sidebar, Workflow
import plotly.express as px
from collections import Counter
    
connect()  
workflow = Workflow()
df = get_df('movies_csv')

sidebar(
    defaultopen=False,
    logo="https://images.emojiterra.com/google/noto-emoji/unicode-16.0/color/1024px/263a.png",
)

## all movies

text("# Exploratory analysis of movies on IMDb")

sql = """SELECT *
FROM (
    SELECT *
    FROM movies_csv
    WHERE CAST(vote_count AS INTEGER) > 50
)
ORDER BY vote_average DESC
LIMIT 50;"""
query_df = query(sql, "movies_csv")

text("## List of all movies")
text("This is a frequency table analysis of movies from the IMDb website. These are the top 50 movies on the website arranged by Vote Average.")
table(query_df, title="Movies Database")

## number of movies per language

freq_query = """
   SELECT original_language, COUNT(*) AS frequency
FROM (
    SELECT *
    FROM movies_csv
    ORDER BY vote_average DESC
    LIMIT 50
) AS top_50
GROUP BY original_language
ORDER BY frequency DESC;
"""
query_freq = query(freq_query,"movies_csv")
fig1 = px.bar(query_freq, x="original_language", y="frequency", title="Number of Movies for every language")


text("## Visualization of movies according to language")
text("Throughout the database of movies available on IMDb, ")
plotly(fig1)


# decade wise analysis

text("## Visualization of movie's popularity vs release time")
text("Visualization of movie's popularity vs release time")

min_popularity = slider(
        label="min popularity to Display",
        min_val=10,
        max_val=80,
        step=5,
        default=40
    )
dec_query = f"""
SELECT 
        *
    FROM (
    SELECT *
    FROM movies_csv
    ORDER BY vote_average DESC
    LIMIT 50
) AS top_50
    WHERE 
        CAST(popularity AS FLOAT) > {min_popularity}
"""
query_dec=query(dec_query,"movies_csv")
table(query_dec,title="Movies with populairty higher than ")
text(dec_query)