import csv



def open_with_csv(filename, d=','):
    data = []
    with open(filename, encoding='utf-8') as tsvin:
        list_reader = csv.reader(tsvin, delimiter=d)
        for line in list_reader:
            data.append(line)
    return data

FIELDNAMES = ['HeroRank', 'VillainRank', 'CharacterID', 'CharacterName', 'CharacterType', 'Actor', 'ActorID', 'Gender', 'Film', 'FilmCode', 'FilmReleaseYear', 'Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Drama', 'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Sport', 'Thriller', 'War', 'Western', 'RTCriticScore', 'RTAudienceScore']

data_from_csv = open_with_csv('Hero_Villain.csv')
print(data_from_csv[0])

with open('Hero_Villain.csv', newline='') as f:
    my_csv = csv.reader(f)
    for row in my_csv:
        print(row)