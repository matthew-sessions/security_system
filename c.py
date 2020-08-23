import socket


def Main():

    host = "67.170.120.133"  # client ip
    port = 4000

    server = ("104.140.79.132", 4000)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    message = input("-> ")
    while message != "q":
        s.sendto(message.encode("utf-8"), server)
        data, addr = s.recvfrom(1024)
        data = data.decode("utf-8")
        print("Received from server: " + data)
        message = input("-> ")
    s.close()


if __name__ == "__main__":
    Main()
