person = {
    "name": "Duc",
    "age": 21,
    "university": ["FTU"],
    "gf-ex": 3,
}

# key : value,

# 1.READ

# print(person)
# print(person["name"])
# print(person["university"])

# loop by key

# for key in person.keys():
#     print(key)

#loop by value

# for value in person.values():
#     print(value)

#loop by key+value (item)

# for key, value in person.items():
#     print(key, value)

# 2.CREATE OR UPDATE
# person["gender"] = "unknown"
# person["gf-ex"] = 5
# print(person)

# 3.DELETE

# del person["age"]
# print(person)

# 4. Extra
# add item to value list
# uni = person["university"]
# uni.append("HNU")
# print(person)