import time
import socket
#localhost,14000
clientUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
clientUDP.settimeout(1.0);
serverName = input("Emrin e serverit? :");
portNumber = input("Portin? :");
serverPort = int(portNumber);
#bind() the socket in the client because UDP is connectionless
bindUDP = (serverName, serverPort); 

while True:
    clientRequest=input("\nZgjedhni njeren nga kerkesat: \n1.IP\n2.NRPORTIT\n 3.NUMERO\n 4.ANASJELLTAS\n 5.PALINDROM\n 6.KOHA\n 7.LOJA\n 8.GCF\n"+
              " KONVERTO\n SWAP\n FACTORIEL\n EVENODD\n" +
              "Shtypni 0 per ta mbyllyr programin\n "+
              "Shtypni 1 per te ndryshuar serverin: ");
    if not clientRequest:
        print("Shenoni njeren nga kerkesat!");
        continue;
    if clientRequest=="1":       
        
        print("\n Lidhja e re \n ")
        clientUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        clientUDP.settimeout(1.0)
        serverName = input(" Emrin e serverit? : ")
        portNumber = input("Portin? : ")
        serverPort = int(Port)
        bindUDP  = (serverName, serverPort)
        print("\n")
    clientUDP.sendto(clientRequest.encode(), bindUDP )

    if clientRequest == "0":
        clientUDP.close();
        break;
    clientUDP.sendto(clientRequest.encode(),bindUDP); 
    try:
        data, server = clientUDP.recvfrom(1024);
        data = data.decode('utf-8');
        print(data);
    except socket.timeout:
        print('Perfundoje koha e caktuar!');
    finally:
        print("...")

