country = {
    "Ukraine": "Kyiv",
    "Japan": "Tokio",
    "Poland": "Warshaw"
}

print(country["Ukraine"])

student = {
    "Alex": 95,
    "Oleg": 45,
    "Tolik": 0
}

student["Max"] = 65
student["Alex"] = 45

print(student["Max"])
print(student["Alex"])

for key, values in country.items():
    print(f"{key} - {values}")

i = country.pop("Poland")
print(i)

for key, values in country.items():
    print(f"{key} - {values}")

print("France" in country)