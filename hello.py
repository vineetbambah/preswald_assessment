from preswald import connect, get_df, text, query,table
    
connect()  
df = get_df('sample_csv')

text("# Exploratory analysis of Disasters in India from 1970 to 2021")

sql = "SELECT * FROM sample_csv"
filtered_df = query(sql, "sample_csv")

text("# My Data Analysis App")
table(filtered_df, title="Filtered Data")