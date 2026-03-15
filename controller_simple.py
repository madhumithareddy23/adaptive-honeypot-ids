# controller_simple.py
import time, os

log_path = "logs/demo.log"
counts = {}
last_size = 0

print("Adaptive controller started - watching", log_path)

while True:
    if not os.path.exists(log_path):
        time.sleep(1)
        continue

    with open(log_path, "r") as log_file:
        log_file.seek(last_size)
        lines = log_file.readlines()
        if lines:
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                # parse SRC
                src = None
                if "SRC=" in line:
                    try:
                        src = line.split("SRC=")[1].split()[0]
                    except:
                        src = None
                # parse ATTACK label if present
                attack = None
                if "ATTACK=" in line:
                    try:
                        attack = line.split("ATTACK=")[1].split()[0]
                    except:
                        attack = None

                if src:
                    counts[src] = counts.get(src, 0) + 1
                    print(f"[LOG] {line}")
                    print(f"[INFO] Events from {src} = {counts[src]}")
                    # example rule: 3 events from same IP -> adaptive action
                    if counts[src] >= 3:
                        print(f"[ACTION] Trigger adaptive response for {src} (e.g., spawn fake SSH on port 2222)")
                        with open("logs/actions.log", "a") as action_file:
                            action_file.write(f"ACTION: {src} triggered adaptive response at {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                    if counts[src] >= 5:
                        print(f"[BLOCK] Simulated firewall block for {src}")
                        with open("logs/actions.log", "a") as action_file:
                            action_file.write(f"BLOCK: {src} simulated firewall block at {time.strftime('%Y-%m-%d %H:%M:%S')}\n")

                        # reset counter for demo
                        counts[src] = 0
                else:
                    print("[LOG] (unparsed) ", line)
            # update last_size **inside the file's with block**
            last_size = log_file.tell()
    time.sleep(1)

