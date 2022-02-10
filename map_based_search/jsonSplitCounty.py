import json

file = open('county.json')

states =[("01","AL"),("02","AK"),("04","AZ"),("05","AR"),("06","CA"),("08","CO"),("09","CT"),("10","DE"),("11","DC"),("12","FL"),("13","GA"),("15","HI"),("16","ID"),("17","IL"),("18","IN"),("19","IA"),("20","KS"),("21","KY"),("22","LA"),("23","ME"),("24","MD"),("25","MA"),("26","MI"),("27","MN"),("28","MS"),("29","MO"),("30","MT"),("31","NE"),("32","NV"),("33","NH"),("34","NJ"),("35","NM"),("36","NY"),("37","NC"),("38","ND"),("39","OH"),("40","OK"),("41","OR"),("42","PA"),("72","PR"),("44","RI"),("45","SC"),("46","SD"),("47","TN"),("48","TX"),("49","UT"),("50","VT"),("51","VA"),("78","VI"),("53","WA"),("54","WV"),("55","WI"),("56","WY")]

regions = {"west": ["WA", "OR", "CA", "NV", "ID", "MT", "WY", "UT", "CO", "AK", "HI"],
           "south_west": ["AZ", "NM", "OK", "TX"],
           "mid_west": ["ND", "SD", "NE", "KS", "MN", "IA", "MO", "WI", "MI", "IL", "IN", "OH"],
            "north_east" : ["NY", "PA", "MD","NJ", "DA", "ME", "NH", "MA", "RI", "CT", "NJ", "DE", "VT"],
            "south_east": ["AR", "LA", "MS", "AL", "TN", "KY", "WV", "DC", "VA", "NC", "SC", "GA", "FL"]}

# Transform json input to python objects
input_dict = json.loads(file.read())


def get_value(code):
    for s in states:
        if(code in s):
            return s[0]

for re in regions:
    temp = []
    print(re)

    for s in regions[re]:
        # # # Filter python objects with list comprehensions
        for x in input_dict["features"]:
          if x["properties"]["STATEFP"] == get_value(s):
            x["properties"]["STATEFP"] = s
            output_dict = [x]
            temp.extend(output_dict)

    # # Transform python object back into json
    with open(f'{re}.json', "w+") as file_ca:
        file_obj = {'type': 'FeatureCollection', 'features': temp }
        json.dump(file_obj , file_ca)
        #
        # # Show json
    file_ca.close()
