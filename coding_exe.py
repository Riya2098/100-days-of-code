# # travel_log=[
# #   {
# #   "Country":"France",
# #   "cities_visited":{"Paris", "Lille", "Dijon"},
# #    "total_visits":12
# #    },
# #   {
# #   "Country":"Germany",
# #   "cities_visited":["Berlin", "Hamburg", "Stuggart"],
# #   "total_visits":25
# #   },
# # ]

# # print(travel_log)


# # country = input() # Add country name
# # visits = int(input()) # Number of visits
# # list_of_cities = eval(input()) # create list from formatted string

# travel_log = [
#   {
#     "country": "France",
#     "visits": 12,
#     "cities": ["Paris", "Lille", "Dijon"]
#   },
#   {
#     "country": "Germany",
#     "visits": 5,
#     "cities": ["Berlin", "Hamburg", "Stuttgart"]
#   },
# ]
# # Do NOT change the code above 👆

# # TODO: Write the function that will allow new countries
# # to be added to the travel_log. 

# def add_new_country(country, visits, list_of_cities):
#   my_dict={}
#   my_dict["country"]=country
#   my_dict["visits"]=visits
#   my_dict["cities"]=list_of_cities
  
#   travel_log.append(my_dict)
#   # print(travel_log)
#   my_dict={}


# add_new_country("India", 4, ["Delhi", "Mumbai"])

# Do not change the code below 👇
# add_new_country(country, visits, list_of_cities)
# print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
# print(f"My favourite city was {travel_log[2]['cities'][0]}.")

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  
# TODO: Add more code here 👇
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  is_it_leap= is_leap(year)
  if(is_it_leap):
    month_days[1]=29
  return month_days[month-1]
  
#🚨 Do NOT change any of the code below 
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)







