from preswald import connect, get_df, text, query,table, checkbox, plotly, sidebar
import plotly.express as px
    
connect()  
df = get_df('movies_csv')

sidebar(
    defaultopen=False,
    logo="https://images.emojiterra.com/google/noto-emoji/unicode-16.0/color/1024px/263a.png",
)
text("# Exploratory analysis of Top 50 Movies on IMDb with votes higher than 10000")

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
table(query_df, title="Movies Database")

text("## Visualization of movies according to language")

english = checkbox(label="en",default="true")
hindi = checkbox(label="hi",default="true")
japanese = checkbox(label="ja",default="true")
korean = checkbox(label="ko",default="true")
italian = checkbox(label="it",default="true")
spanish = checkbox(label="es",default="true")
zh=checkbox(label="zh",default="true")

data = {"Languages": ["en","hi","ja","ko","it","pt","zh","es"] , "Values": [10, 20, 30,32,43,34,44,32]}
fig = px.bar(data, x="Languages", y="Values", title="Number of Movies for every language")

# Embed the bar chart
plotly(fig)