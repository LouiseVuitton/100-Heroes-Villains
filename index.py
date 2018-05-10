import sqlite3
import numpy as np
import pandas as pd
from bokeh.models import ColumnDataSource, HoverTool, LinearColorMapper
from bokeh.plotting import figure, show, output_file
# from bokeh.palettes import Magma3

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

plot.circle(source=ds, x="FilmReleaseYear", y="CharacterID",fill_color="#9370DB",
            line_color="#9370DB", fill_alpha=0.4, hover_fill_color="#FFD700",
            hover_line_color="#FFD700", hover_alpha=1, size=25)

# colors = ["#8a0707", "#b3456b", "#b987ba", "#c1c4e8", "#f0f8ff"]

# mapper = LinearColorMapper(palette="Magma3", low=df.CharacterID.min(),
#                            high=df.CharacterID.max())

plot.select_one(HoverTool).tooltips = [("Character", "@CharacterName"),
                                       ("Actor", "@Actor"),
                                       ("Film", "@Film"),
                                       ("Year", "@FilmReleaseYear"),
                                       ("Character Type","@CharacterType"),
                                       ("Hero Rank", "@HeroRank"),
                                       ("Villain Rank", "@VillainRank")
                                       ]

plot.xaxis.axis_label = "Film Release Year"
plot.xaxis.axis_label_standoff = 30

plot.yaxis.axis_label = "Film Characters"
plot.yaxis.axis_label_standoff = 30

plot.title.align = "center"
plot.title.text_font_size = "30px"

show(plot)