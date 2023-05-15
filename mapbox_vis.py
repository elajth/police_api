import plotly.express as px
import pandas as pd
import sqlite3

# Opening a connection to the sqlite database
print("Getting data..")
filename = "eventdata.sqlite"
sql = ("SELECT DISTINCT etime,"
    " name,"
    " type,"
    " summary,"
    " lat,"
    " lon"
    " FROM events"
    )
try:
    conn = sqlite3.connect(filename)
    df = pd.read_sql(sql, conn)
    print(df)

    fig = px.scatter_mapbox(df,
        lon = df['lat'],
        lat = df['lon'],
        zoom = 4,
        #width = 900,
        #height = 600,
        title = "Swedish Police API of event visualisation",
        hover_name = "type",

        )
    fig.update_layout(mapbox_style = "open-street-map")
    fig.update_mapboxes(center_lat = 61.980000, center_lon = 15.304722)
    fig.show()
    print("Plot completed")

except Exception as e:
    print(e)

# Execute close db connection regardless of try clause result
finally:
    if conn:
        conn.close()
        print("Connection closed")

print("done")