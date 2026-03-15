# fake_service.py
import socket, sys

PORT = 2222
if len(sys.argv) > 1:
    try:
        PORT = int(sys.argv[1])
    except:
        pass

HOST = "0.0.0.0"
banner = b"SSH-2.0-FakeSSH_1.0\r\n"

print(f"[+] Fake SSH service starting on port {PORT} ... (CTRL+C to stop)")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"[CONN] From {addr}")
            try:
                conn.sendall(banner)
            except:
                pass
