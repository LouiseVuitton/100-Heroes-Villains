import sqlite3
import pandas as pd
from bokeh.io import output_file, show
from bokeh.plotting import figure

conn = sqlite3.connect("SQLiteHeroVillain.db")
HV = pd.read_sql_query("SELECT CharacterName, FilmReleaseYear, CharacterID FROM Hero_Villain", conn)
conn.close()

output_file = ("AFI_Heroes_Villains.html")
file = "Hero_Villain.csv"

HV["CharacterID"] = HV["CharacterID"].astype(int)
HV["FilmReleaseYear"] = HV["FilmReleaseYear"].astype(int)



#GRAPH SETUP
all_char = figure(plot_width=400, plot_height=400, title="All Characters", toolbar_location="below", tools="pan,box_zoom,reset,hover")
all_char.scatter(HV["CharacterID"], HV["FilmReleaseYear"], fill_color, line_width, fill_alpha)
# all_char.scatter(HV["CharacterID" - X axis], HV["FilmReleaseYear" - y axis], fill_color, line_width, fill_alpha)



# all_char.circle(x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104], y=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90,91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104], size=10)

show(all_char)

# genres = figure(plot_width=400, plot_height=400, title="All Genres", toolbar_location="below", tools="pan,box_zoom,reset,hover")

genres.vbar(x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], width=0.5, bottom=0, top=[26, 26, 3, 20, 3, 32, 74, 7, 8, 7, 11, 7, 2, 9, 13, 11, 2, 35, 5, 6], color="#C0392B")

show(genres)