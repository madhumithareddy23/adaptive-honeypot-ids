# dataset_to_logs.py
import random, os

IN = "KDDTrain+_20Percent.txt"   # ensure file is present in this folder
OUT = "logs/demo.log"

os.makedirs("logs", exist_ok=True)
src_ips = ["192.168.56.10","192.168.56.11","192.168.56.12","192.168.56.13"]

print("[*] Converting dataset to logs ->", OUT)
with open(IN, "r", errors="ignore") as fin, open(OUT, "w") as fout:
    for i, line in enumerate(fin):
        line = line.strip()
        if not line:
            continue
        parts = line.split(",")
        attack = parts[-1].strip().strip(".")
        src = random.choice(src_ips)
        fout.write(f"{i} SRC={src} ATTACK={attack}\n")
print("[*] Done. Wrote logs/demo.log")
