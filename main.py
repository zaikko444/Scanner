import socket, sys


while True:
    print('1 - PortScan' 
          ' 2 - Banner Grabbing'
    )

    escolha = int(input('Escolha: '))
    if escolha == 1:
        ip = str(input('Digite o ip: '))
        print('Vereficando...')
        for porta in range(1, 51680):
            meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            response = meusocket.connect_ex((ip, porta))
            if response == 0:
                print('[+] PORTA ABERTA:', porta)

        print('Scanner terminado')


    if escolha == 2:
        ip = str(input('Digite o ip: '))
        porta = int(input('Digite a porta: '))
        bannerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        response = bannerSocket.connect((ip, porta))
        banner = socket.recv(1024)
        print('Vereficando...')
        print(banner)