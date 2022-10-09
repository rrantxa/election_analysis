counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == "Denver":
    print(counties[1])

if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso are not in the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

for county in counties:
    print(county)

for i in range(len(counties)):
    print(counties[i])

counties_tuples = ("Arapahoe","Denver","Jefferson")

for i in range(len(counties_tuples)):
    print(counties_tuples[i])

counties_dict = {"Arapahoe":422829, "Denver":463353, "Jefferson":432438}

for voters in counties_dict.values():
    print(voters)

for county in counties_dict.keys():
    print(county)

for key, value in counties_dict.items():
    #print(key + " county has " + str(value) + " registered voters.")
    print(f"{key} county has {value} of registered voters")

voting_data = [{"county":"Arapahoe","registered_voters":422829},
                {"county":"Denver","registered_voters":463353},
                {"county":"Jefferson","registered_voters":432438}]

for county_dict in voting_data:
    print(county_dict)

for i in range(len(voting_data)):
    print(voting_data[i]['county'])

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for i in range(len(voting_data)):
    print(voting_data[i]['registered_voters'])

for county_dict in voting_data:
    print(county_dict['county'])

for county_dict in voting_data:
    print(county_dict['registered_voters'])

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
#print("I received " + str(percentage_votes)+"% of the total votes.")
print(f"I received {my_votes /total_votes * 100:,.2f}% of the total votes.")

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
f"You received {candidate_votes:,} votes."
    f" The total number of votes in the election was {total_votes:,}."
    f" You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)

for key, value in counties_dict.items():
    print(f"{key} county has {value:,} registered voters.")

for i in range(len(voting_data)):
    print(f"{voting_data[i]['county']} has {voting_data[i]['registered_voters']:,} registered voters.")