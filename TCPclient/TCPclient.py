import socket
import sys 
import select

#localhost, 14000;
serverName = input("Shenoni emrin e serverit:");
PortNumber = input("Shenoni portin:");
serverPort = int(PortNumber);
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
s.connect((serverName,serverPort));



while True:

    clientRequest=input("\nZgjedhni njeren nga kerkesat: \n1.IP\n2.NRPORTIT\n 3.NUMERO\n 4.ANASJELLTAS\n 5.PALINDROM\n 6.KOHA\n 7.LOJA\n 8.GCF\n"+
              " KONVERTO\n SWAP\n FACTORIEL\n EVENODD\n" +
              "Komanda 0 per ta mbyllyr programin\n "+
              "Komanda 1 per te ndryshuar serverin!\n Shtypni kerkesen: ");
    clientRequest=clientRequest.strip(); 
    if len(clientRequest) > 128:
        print("Nuk mund te pranoje serveri kerkese me shume se 128 karaktere!");
        continue;
    if not clientRequest:
        print("Shenoni nje kerkese!");
        continue;
    if clientRequest=="1":
       
        print("\n New Connection ")
        serverName = input(" Emrin e serverit: ") 
        PortNumber = input(" Portin: ")
        serverPort = int(PortNumber)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((serverName,serverPort))
        print("\n")
    if clientRequest == "0":
        s.close();
        break;
  


    s.sendall(str.encode(clientRequest));
    data = s.recv(1024);
    data = data.decode('utf-8');
    print(data);

