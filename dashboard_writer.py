# dashboard_writer.py
import time, os

LOG = "logs/demo.log"
OUT = "dashboard.html"

print("[*] Dashboard writer running - ensuring dashboard.html exists (it will be updated by static HTML fetch).")
# This script just ensures logs exist; if you want continuous writes to demo.log, use stream_kdd.py
# The dashboard HTML fetches logs/demo.log directly; no extra server-side work is required.
while True:
    # simply touch files so they exist
    if not os.path.exists(LOG):
        os.makedirs(os.path.dirname(LOG), exist_ok=True)
        open(LOG, "a").close()
    # update timestamp on dashboard.html if exists so browser reloads may detect change (not required)
    time.sleep(2)
