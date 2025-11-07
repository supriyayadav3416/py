import os

data = [l.strip().split(",") for l in open("students.txt") if "," in l]
if not data:
    print("⚠️ No valid data found in students.txt")
else:
    s = {n:int(m) for n,m in data}
    avg = sum(s.values())/len(s)
    p = os.path.abspath("result.txt")
    open(p,"w").write("\n".join(f"{n}: {m}" for n,m in s.items()) + f"\n\nAverage: {avg:.2f}")
    print("✅ Result written successfully!\n📁 File saved at:", p)
    os.startfile(p)
