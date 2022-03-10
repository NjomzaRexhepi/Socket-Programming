
import socket
import sys
from _thread import *
from datetime import datetime
import random


hostName = ''
serverPort = 14000;
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
ThreadCount=0;
try:
    serverSocket.bind((hostName, serverPort));
except socket.error as e:
    print(str(e));

print('Serveri TCP u startua ne :'+str(serverPort));
serverSocket.listen(5);
print('Serveri eshte duke pritur kerkesa!');

#funksioni per llogaritjen e GCF
def PALINDROME(f):
    if (f == f[:: - 1]):
        x = "Po, teksti juaj eshte POLINDROM"
    else:
        x = "Jo, teksti  juaj nuk eshte POLINDROM"
    y = str(x)
    return y

def REVERSE(a):
    fjala = ""
    for i in a:
	    fjala = i + fjala
    return fjala



def computeGCF(x, y): 
  
    if x > y: 
        z = y 
    else: 
        z = x 
    for i in range(1, z+1): 
        if((x % i == 0) and (y % i == 0)): 
            gcd = i 
    an = "The result : " + str(gcd)+"\n"  
    return an 

def konvertimi(s,n): 
    if(s=="CMTOINCH"):
        return (n / 2.54);
    elif(s=="INCHTOCM"):
        
        return (2.54 * n);
    elif(s=="KTOMILES"):
      
        return (n * 0.62137);
    elif(s=="MILESTOKM"):
        return (n / 0.62137);
   

def EVENODD(n):
    x=True;
    for x in range(2,n):
        if n%x ==0:
            x=False;
            return x;
    return x;
        

def FACTORIEL(n):
    if n == 1:
        return 1
    else:
        return n * FACTORIEL(n - 1)

def SWAP(a, b):
    x = a
    a = b
    b = x
    y = 'Vlera e parametrit te pare pas shkembimit eshte: {}'.format(a)
    z = 'Vlera e parametrit te dyte pas shkembimit eshte: {}'.format(b)
    return y, z


#funksiooni per kerkesa
def functionHandle(varg,conn,addr):
    if(varg[0]=='IP'):
        conn.send(str.encode("IP e klientit është:"+addr[0]));

    elif(varg[0]=='NRPORTIT'):
       conn.send(str.encode("Klienti është në portin "+str(addr[1])));

    elif(varg[0]=='NUMERO'):
        try:
            s="";
            s=s.join(varg[1:]);          
            count = 0;
            consonate=0;
            zanoret = set("aeiouy\u00EB");
            for letter in s:             
                if letter in zanoret:    
                    count += 1;
            consonate=len(s)-count;    
            conn.send(str.encode("Teksti i shtypur ka "+ str(count) +" zanore, numri i bashketinglloreve eshte " +str(consonate)+"\n"));
        except IndexError:
            conn.send(str.encode("Shenoni nje fjali pas funksionit!"));
   
    elif(varg[0]=='KOHA'):
        time=datetime.now().strftime('%Y-%m-%d %H:%M:%S');
        conn.send(str.encode(time));
    elif(varg[0]=='LOJA'):
        srand= [];
        for x in range(5):
            rand= random.randint(1,35); 
            if rand not in srand:
                srand.append(rand);
                srand.sort()
            rand=str(srand)
            rand=rand.replace('[','(').replace(']',')')
        conn.send(str.encode(rand));
    elif(varg[0]=='FACTORIEL'):
        try:
            n=FACTORIEL(int(varg[1]));
            conn.send(str.encode(str(n)));
        except IndexError:
            conn.send(str.encode("Ju lutem shenoni nje shifer pas thirrjes se metodes FACTORIEL")); 
        except ValueError:
            conn.send(str.encode("Ju lutem shenoni nje shifer pas thirrjes se metodes FIBONACCI"));

    elif(varg[0]=='SWAP'):
        try:
            mesazhi = str(SWAP(int(varg[1]), int(varg[2])))
            conn.send(str.encode(str(mesazhi))); 
        except IndexError:
            conn.send(str.encode("Ju lutem shenoni dy shifera pas thirrjes se metodes SWAP")); 
        except ValueError:
            conn.send(str.encode("Ju lutem shenoni dy shifera pas thirrjes se metodes SWAP"));

    elif(varg[0]=='KONVERTO'):
        help="Mundesite:\nCMTOINCH  \nINCHTOCM \nKTOMILES \nMILESTOKM";

        try:
            s=varg[1];
            n=float(varg[2]);
            conn.send(str.encode(str(konvertimi(s,n))));
        except IndexError:
            conn.send(str.encode("Ju lutem shenoni ne cilin parameter deshironi te konvertoni pastaj numrin! \n"+help));
        except ValueError:
            conn.send(str.encode("Ju lutem shenoni ne cilin parameter deshironi te konvertoni pastaj numrin! \n" +help));


    elif(varg[0]=='GCF'):
        
        try:
           x=int(varg[1]);
           y=int(varg[2]);
           conn.send(str.encode(str(computeGCF(x, y))));
        except IndexError:
            conn.send(str.encode("Ju lutem shenoni nje shifer pas thirrjes se metodes GCF")); 
        except ValueError:
            conn.send(str.encode("Ju lutem shenoni nje shifer pas thirrjes se metodes  GCF"));

    elif(varg[0]=='ANASJELLTAS'):
        try:
           a=varg[1];
         
           conn.send(str.encode(str(REVERSE(a))));
        except IndexError:
            conn.send(str.encode("Ju lutem shenoni nje string pas thirrjes se metodes ANASJELLTAS")); 
        except ValueError:
            conn.send(str.encode("Ju lutem shenoni nje shifer pas thirrjes se metodes ANASJELLTAS"));

    elif(varg[0]=='PALINDROM'):
        try:
           f=varg[1];
         
           conn.send(str.encode(str(PALINDROME(f))));
        except IndexError:
            conn.send(str.encode("Ju lutem shenoni nje string pas thirrjes se metodes PALINDROME")); 
        except ValueError:
            conn.send(str.encode("Ju lutem shenoni nje shifer pas thirrjes se metodes PALINDROME"));
  
 
    elif(varg[0]=='EVENODD'):
        try:
            n = int(varg[1]);
            if EVENODD(n):
                conn.send(str.encode("Numri " + str(n) + " eshte numer i thjeshte!"));
            else:
                conn.send(str.encode("Numri " + str(n) + " nuk eshte numer i thjeshte!"));
        except IndexError:
            conn.send(str.encode("Shenoni nje numer pas thirrjes se metodes EVENODD!"));
        except ValueError:
            conn.send(str.encode("Shenoni nje numer te plote pas thirrjes se metodes EVENODD!"));

    else:
        conn.send(str.encode("Nuk ekziston kjo metode, ju lutem shenoni njerat nga kerkesat ne listen e shfaqur!"));
    
def clientConnection_thread(conn,addr):
    while True:
        try:
            data=conn.recv(1024);
            kerkesa = data.decode('utf-8');
            varg = kerkesa.split();
            try:
                functionHandle(varg,conn,addr);
            except IndexError:
                conn.send(str.encode("Kerkesa nuk mund te procesohet me tutje!"))
        except OSError:
            conn.close();
    conn.close();


while True: 
    # accept connections from outside
    connectionSocket, addr = serverSocket.accept();
    print('Klienti u lidh ne serverin %s me port %s' % addr);
    start_new_thread(clientConnection_thread,(connectionSocket,addr,));
    ThreadCount += 1

    print('\n Numri i klientit: ' + str(ThreadCount)+'\n')







