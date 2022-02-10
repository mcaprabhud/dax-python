import json

file = open('area_codeq.json')

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE",  "NV", "NH", "NJ",  "NM", "NY", "NC",  "ND","OH","OK", "OR", "PA", "PR",  "RI", "SC","SD","TN","TX","UT","VT","VA","VI","WA","WV","WI","WY"]


regions = {"west": ["WA", "OR", "CA", "NV", "ID", "MT", "WY", "UT", "CO", "AK"],
           "south_west": ["AZ", "NM", "OK", "TX"],
           "mid_west": ["ND", "SD", "NE", "KS", "MN", "IA", "MO", "WI", "MI", "IL", "IN", "OH"],
            "north_east" : ["NY", "PA", "MD","NJ", "DA", "ME", "NH", "MA", "RI", "CT", "NJ", "DE"],
            "south_east": ["AR", "LA", "MS", "AL", "TN", "KY", "WV", "DC", "VA", "NC", "SC", "GA", "FL"]
}

# Transform json input to python objects
input_dict = json.loads(file.read())

for re in regions:
    temp = []
    print(re)

    for s in regions[re]:
        # # # Filter python objects with list comprehensions
        output_dict = [x for x in input_dict["features"] if x["properties"]["STATE"] == s]
        temp.extend(output_dict)

    # # Transform python object back into json
    with open(f'{re}.json', "w+") as file_ca:
        file_obj = {'type': 'FeatureCollection', 'features': temp }
        json.dump(file_obj , file_ca)
        #
        # # Show json
    # file_ca.write(output_json)
    file_ca.close()
