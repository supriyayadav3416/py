names = ["Riya","Amit","Sneha","Karan","Priya"]
scores = [78,56,90,65,72]
pass_mark = 60

print("Student Scores:")
for n,s in zip(names,scores):
    print(f"{n}: {s}")

high = max(scores); low = min(scores)
print(f"\nHighest: {names[scores.index(high)]} ({high})")
print(f"Lowest: {names[scores.index(low)]} ({low})")
print(f"Passed: {sum(s>pass_mark for s in scores)}")
