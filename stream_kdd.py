# stream_kdd.py
import random, time, os

IN = "KDDTrain+_20Percent.txt"
OUT = "logs/demo.log"
os.makedirs("logs", exist_ok=True)
src_ips = ["192.168.56.10","192.168.56.11","192.168.56.12","192.168.56.13"]

# remove existing file so controller can tail fresh stream (optional)
try:
    os.remove(OUT)
except:
    pass

print("[*] Streaming dataset into", OUT)
with open(IN, "r", errors="ignore") as fin:
    for i, line in enumerate(fin):
        line = line.strip()
        if not line:
            continue
        attack = line.split(",")[-1].strip().strip(".")
        src = random.choice(src_ips)
        entry = f"{i} SRC={src} ATTACK={attack}"
        with open(OUT, "a") as f:
            f.write(entry + "\n")
        print("[STREAM]", entry)
        time.sleep(0.2)   # slow down so controller shows live output
        if i >= 500:     # limit for demo; remove or increase if you want
            break
print("[*] Stream finished (demo limit reached).")
