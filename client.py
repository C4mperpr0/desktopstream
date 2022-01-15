import mss
from time import sleep
from PIL import Image
import socket
from datetime import datetime
from io import BytesIO

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('127.0.0.1', 55555))

    with mss.mss() as sct:
        #sct.compression_level = 6
        monitor = sct.monitors[1]
        while True:
            sct_img = sct.grab(monitor)

            # Generate the PNG
            png = mss.tools.to_png(sct_img.rgb, sct_img.size)
            img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
            img = img.resize((720, 480))
            raw_img = BytesIO()
            img.save(raw_img, 'png')
            s.sendall(raw_img.getvalue())
            print(len(raw_img.getvalue()))
            print("sent")
            sleep(1000000)

