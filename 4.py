import csv

with open("students.csv") as f:
    data = list(csv.DictReader(f))

ages = [int(s["age"]) for s in data]

print("=== CSV File Data Processing ===")
print("Total Students:", len(data))
print(f"Average Age: {sum(ages)/len(ages):.2f}")

oldest  = max(data, key=lambda s: int(s["age"]))
youngest = min(data, key=lambda s: int(s["age"]))

print(f"Oldest Student: {oldest['name']} ({oldest['age']})")
print(f"Youngest Student: {youngest['name']} ({youngest['age']})")
