#เป็นการ add ข้อมูล nesting dictionaires เข้ามาใน dictionaries

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(add_country, add_visits, add_cities):
  new_country = {}
  new_country["country"] = add_country
  new_country["visits"] = add_visits
  new_country["cities"] = add_cities
  travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
