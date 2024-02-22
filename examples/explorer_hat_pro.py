import time

from cap1xxx import Cap1208

captouch = Cap1208()

captouch.start_watching()

while True:
    status = captouch.get_input_status()
    print(status)
    time.sleep(1.0)