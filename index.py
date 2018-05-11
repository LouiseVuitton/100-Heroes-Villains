import sqlite3
import pandas as pd
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.plotting import figure, show, output_file

conn = sqlite3.connect("db/SQLiteHeroVillain.db")
HV = pd.read_sql_query("SELECT * FROM Hero_Villain", conn)
conn.close()

df = pd.read_csv("Hero_Villain.csv")
ds = ColumnDataSource(df)

output_file = "index.html"

HV["CharacterID"] = HV["CharacterID"].astype(int)
HV["FilmReleaseYear"] = HV["FilmReleaseYear"].astype(int)

TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select"

plot = figure(title="AFI's 100 Years...100 Heroes & Villains", tools=TOOLS,
              plot_width=800, plot_height=800)

plot.circle(source=ds, x="FilmReleaseYear", y="CharacterID",
            fill_color="#87ceeb", line_color="#87ceeb",
            hover_fill_color="#8a0707", hover_line_color="#8a0707",
            fill_alpha=0.4,hover_alpha=1, size=25)


plot.select_one(HoverTool).tooltips = [("Character", "@CharacterName"),
                                       ("Actor", "@Actor"),
                                       ("Film", "@Film"),
                                       ("Year", "@FilmReleaseYear"),
                                       ("Rank", "@TotalRank")]

plot.xaxis.axis_label = "Film Release Year"
plot.xaxis.axis_label_standoff = 30

plot.yaxis.axis_label = "Film Characters"
plot.yaxis.axis_label_standoff = 30

plot.title.align = "center"
plot.title.text_font_size = "30px"

show(plot)