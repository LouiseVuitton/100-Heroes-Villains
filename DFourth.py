from CThird import *


#------FILTER BY STRING-------TOTAL HEROES AND VILLAINS
def filter_col_by_bool(data_sample, col, filter_condition):
    matches_search_term = []
    for item in data_sample[1:]:
        if item[col] == filter_condition:
            matches_search_term.append(item)
    return matches_search_term

females = filter_col_by_bool(data_from_csv, 7, "F")
print("There are {} female heroes and villains.".format(number_of_records(females)))

males = filter_col_by_bool(data_from_csv, 7, "M")
print("There are {} male heroes and villains.".format(number_of_records(males)))

animal = filter_col_by_bool(data_from_csv, 7, "A")
print("There are {} animal characters.".format(number_of_records(animal)))

unknown = filter_col_by_bool(data_from_csv, 7, "U")
print("There is {} character of unknown gender.".format(number_of_records(unknown)))

hero = filter_col_by_bool(data_from_csv, 4, "H")
print("There are {} heroes.".format(number_of_records(hero)))

villain = filter_col_by_bool(data_from_csv, 4, "V")
print("There are {} villains.".format(number_of_records(villain)))



#------FILTER BY STRING-------# OF CHARACTERS BY GENRE
def filter_col_by_bool(data_sample, col, filter_condition):
    matches_search_term = []
    for item in data_sample[1:]:
        if item[col] == filter_condition:
            matches_search_term.append(item)
    return matches_search_term

action = filter_col_by_bool(data_from_csv, 11, "Y")
print("{} characters appear in action films.".format(number_of_records(action)))

adventure = filter_col_by_bool(data_from_csv, 12, "Y")
print("{} characters appear in adventure films.".format(number_of_records(adventure)))

animation = filter_col_by_bool(data_from_csv, 13, "Y")
print("{} characters appear in animated films.".format(number_of_records(animation)))

biography = filter_col_by_bool(data_from_csv, 14, "Y")
print("{} characters appear in biographical films.".format(number_of_records(biography)))

comedy = filter_col_by_bool(data_from_csv, 15, "Y")
print("{} characters appear in comedies.".format(number_of_records(comedy)))

crime = filter_col_by_bool(data_from_csv, 16, "Y")
print("{} characters appear in crime films.".format(number_of_records(crime)))

drama = filter_col_by_bool(data_from_csv, 17, "Y")
print("{} characters appear in dramatic films.".format(number_of_records(drama)))

family = filter_col_by_bool(data_from_csv, 18, "Y")
print("{} characters appear in family films.".format(number_of_records(family)))

fantasy = filter_col_by_bool(data_from_csv, 19, "Y")
print("{} characters appear in fantasy films.".format(number_of_records(fantasy)))

film_noir = filter_col_by_bool(data_from_csv, 20, "Y")
print("{} characters appear in film-noir movies.".format(number_of_records(film_noir)))

history = filter_col_by_bool(data_from_csv, 21, "Y")
print("{} characters appear in historical films.".format(number_of_records(history)))

horror = filter_col_by_bool(data_from_csv, 22, "Y")
print("{} characters appear in horror films.".format(number_of_records(horror)))

musical = filter_col_by_bool(data_from_csv, 23, "Y")
print("{} characters appear in musicals.".format(number_of_records(musical)))

mystery = filter_col_by_bool(data_from_csv, 24, "Y")
print("{} characters appear in mystery films.".format(number_of_records(mystery)))

romance = filter_col_by_bool(data_from_csv, 25, "Y")
print("{} characters appear in romance films.".format(number_of_records(romance)))

sci_fi = filter_col_by_bool(data_from_csv, 26, "Y")
print("{} characters appear in science fiction films.".format(number_of_records(sci_fi)))

sport = filter_col_by_bool(data_from_csv, 27, "Y")
print("{} characters appear in sports films.".format(number_of_records(sport)))

thriller = filter_col_by_bool(data_from_csv, 28, "Y")
print("{} characters appear in thrillers.".format(number_of_records(thriller)))

war = filter_col_by_bool(data_from_csv, 29, "Y")
print("{} characters appear in war films.".format(number_of_records(war)))

western = filter_col_by_bool(data_from_csv, 30, "Y")
print("{} characters appear in western films.".format(number_of_records(western)))

# --------------------------------------------------------
# --------------------------------------------------------
# --------------------------------------------------------
# ------FILTER BY STRING------- HEROES AND VILLAINS BY GENDER
# def filter_col_by_bool(data_sample, col, filter_condition):
#     matches_search_term = []
#     for item in data_sample[1:]:
#         if item[col] == filter_condition:
#             matches_search_term.append(item)
#     return matches_search_term
#
# # # IS THIS RIGHT?
# female_hero = filter_two_col_by_bool(data_from_csv, 4, "H")
# print("There are {} female heroes".format(number_of_records(female_hero)))

# male_hero = filter_col_by_string(data_from_csv, "CharacterType", "H", "Gender", "M")
# print("There are {} male heroes".format(number_of_records(male_hero)))
#
# female_villain = filter_col_by_string(data_from_csv, "CharacterType", "V", "Gender", "F")
# print("There are {} female villains".format(number_of_records(female_villain)))
#
# male_hero = filter_col_by_string(data_from_csv, "CharacterType", "V", "Gender", "M")
# print("There are {} male villains".format(number_of_records(male_villain)))
# --------------------------------------------------------
# --------------------------------------------------------
# --------------------------------------------------------






#------FILTER BY FLOAT-------RELEASE DATES AND ROTTEN TOMATOES SCORES
# FOR AFI, MAY WANT TO USE INT INSTEAD


# def filter_year_col_by_bool(data_sample, col, cond, filter_condition):
#     matches_search_term = []
#
#     for item in data_sample[1:]:
#         if item[col] == "<":
#             cond < filter_condition
#         matches_search_term.append(item)
#     return matches_search_term


# before_1970 = filter_year_col_by_bool(data_from_csv, 10, "<", 1970)
# print("There are {} films released before 1970.".format(number_of_records(before_1970)))
#
# before_1940 = filter_col_by_float(data_from_csv, "FilmYear", "<", 1940)
# print("There are {} films released before 1940".format(number_of_records(before_1940)))
#
# after_and_1980 = filter_col_by_float(data_from_csv, "FilmYear", ">=", 1980)
# print("There are {} films released from 1980 onward".format(number_of_records(after_and_1980)))
#
# after_and_1990 = filter_col_by_float(data_from_csv, "FilmYear", ">=", 1990)
# print("There are {} films released from 1990 onward".format(number_of_records(after_and_1990)))
#
# RT_critic_rotten = filter_col_by_float(data_from_csv, "RTCriticScore", "<", 60)
# print("There are {} films critics deemed Rotten with a score of 59% or lower.".format(number_of_records(RT_critic_rotten)))
#
# RT_critic_fresh = filter_col_by_float(data_from_csv, "RTCriticScore", ">=", 60)
# print("There are {} films critics deemed Fresh with a score of 60% or higher.".format(number_of_records(RT_critic_fresh)))
#
# RT_critic_cert_fresh = filter_col_by_float(data_from_csv, "RTCriticScore", ">=", 75)
# print("There are {} films critics deemed Certified Fresh with a score of 75% or higher.".format(number_of_records(RT_critic_cert_fresh)))
#
# RT_audience_rotten = filter_col_by_float(data_from_csv, "RTAudienceScore", "<", 60)
# print("There are {} films filmgoers deemed Rotten with a score of 59% or lower.".format(number_of_records(RT_audience_rotten)))
#
# RT_audience_fresh = filter_col_by_float(data_from_csv, "RTAudienceScore", ">=", 60)
# print("There are {} films filmgoers deemed Fresh with a score of 60% or higher.".format(number_of_records(RT_audience_fresh)))
#
# RT_audience_cert_fresh = filter_col_by_float(data_from_csv, "RTAudienceScore", ">=", 75)
# print("There are {} films filmgoers deemed Certified Fresh with a score of 75% or higher.".format(number_of_records(RT_audience_cert_fresh)))