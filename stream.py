import socket
from threading import Thread
from time import sleep
import pygame


def image_display(conn):
    while True:
        with open('img.png', 'wb+') as file:
            data = conn.recv(1024)
            print(len(data))
            if len(data) != 1024:
                print(data)
                sleep(10000)
            file.write(data)
    sleep(1000000000)
    pygame.init()
    display_surface = pygame.display.set_mode((720, 480))
    pygame.display.set_caption('Image')
    image = pygame.image.load(data)
    while True:
        display_surface.fill((0, 0, 0))
        display_surface.blit(image, (0, 0))
        pygame.display.update()
        sleep(1)


def clientloop(conn, addr):
    print(f"Connected to {addr}")
    command_thread = Thread(target=image_display, args=(conn, ))
    command_thread.start()

    #conn.sendall(data)


client_threads = []
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('127.0.0.1', 55555))
    s.listen()
    while True:
        conn, addr = s.accept()
        client_threads.append(Thread(target=clientloop, args=(conn, addr)))
        client_threads[-1].start()
