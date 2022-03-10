
import random
import socket
from datetime import datetime
import random

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
socket.bind(('', 14000));


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
   

def EVENODD(a) :
  x = a % 2
  if x == 0 :
    y = "Numri eshte cift"
    return y
  else :
    y = "Numri eshte tek"
    return y
        

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
def LOJA() : 
 arrayofnum=[]
 for i in range(5):
     num=random.randint(1,35)
     if num not in arrayofnum:
         arrayofnum.append(num)
         arrayofnum.sort()
 num=str(arrayofnum)
 num=num.replace('[','(').replace(']',')')

 return num


def function1(vargu,conn,addr):
    if(vargu[0]=='IP'):
        socket.sendto(str.encode("IP adresa e klientit eshte: " + addr[0]), addr);

    elif(vargu[0]=='NRPORTIT'):
       socket.sendto(str.encode("Klienti është duke përdorur portin " + str(addr[1])), addr);

    elif(vargu[0]=='NUMERO'):
        try:
            s=vargu[1];           
            count = 0;
            zanoret = set("aeiyou\u00EB");
            for letter in s:             
                if letter in zanoret:    
                    count += 1;
            consonate=len(s)-count; 
            socket.sendto(str.encode("Numri i zanoreve ne tekst eshte:" + str(count) + "\nNumri i bashktinglloreve ne tekst eshte:" + str(consonate)), addr);
  
        except IndexError:
           socket.sendto(str.encode("Shenoni nje fjali pas kerkeses ZANORE!"), addr);

    elif(vargu[0]=='TIME'):
        time=datetime.now().strftime('%Y-%m-%d %H:%M:%S');
        socket.sendto(str.encode(time), addr);

    elif(vargu[0]=='LOJA'):
        try:
            
            mesazhi = str(LOJA())
            socket.sendto(mesazhi.encode(),addr)
           
        except IndexError:
            socket.sendto(str.encode("Shenoni nje numer pas kerkeses FACTORIEL"), addr);
        except ValueError:
            socket.sendto(str.encode("Shenoni nje numer pas kerkeses FACTORIEL"), addr);
    elif(vargu[0]=='FACTORIEL'):
        try:
            
            mesazhi = str(FACTORIEL(int(vargu[1])))
            socket.sendto(mesazhi.encode(),addr)
           
        except IndexError:
            socket.sendto(str.encode("Shenoni nje numer pas kerkeses FACTORIEL"), addr);
        except ValueError:
            socket.sendto(str.encode("Shenoni nje numer pas kerkeses FACTORIEL"), addr);
    elif(vargu[0]=='PALINDROM'):
        try:
           
            mesazhi = str(PALINDROME(vargu[1]))
            socket.sendto(mesazhi.encode(),addr)

        except IndexError:
            socket.sendto(str.encode("Shenoni nje numer pas kerkeses FIBONACCI"), addr);
        except ValueError:
            socket.sendto(str.encode("Shenoni nje numer pas kerkeses FIBONACCI"), addr);

    elif(vargu[0]=='KONVERTO'):
        help="Mundesite :\nCMTOINCH  \nINCHTOCM \nKTOMILES \nMILESTOKM";
        
        try:
          
            mesazhi = str(CONVERT(vargu[1],int(vargu[2])))
            socket.sendto(mesazhi.encode(),addr)
        except IndexError:        
            socket.sendto(str.encode("Ju lutem shenoni cka deshironi te konvertoni pastaj shifren! \n" +help), addr);
        except ValueError:
            socket.sendto(str.encode("Ju lutem shenoni cka deshironi te konvertoni pastaj shifren!\n "+help), addr);
  #good
    elif(vargu[0]=='GCF'):
        
        try:
          
           mesazhi = str(computeGCF(int(vargu[1]),int(vargu[2])))
           socket.sendto(mesazhi.encode(),addr)
        except IndexError:
            socket.sendto(str.encode("Shenoni nje numer pas kerkeses FIBONACCI"), addr);
        except ValueError:
            socket.sendto(str.encode("Shenoni nje numer pas kerkeses FIBONACCI"), addr);
   #good

    elif(vargu[0]=='ANASJELLTAS'):
        try:
            mesazhi = str(REVERSE(str(vargu[1])))
            socket.sendto(mesazhi.encode(),addr)
        
        except IndexError:
            socket.sendto(str.encode("Shenoni nje numer pas kerkeses ANASJELLTAS"), addr);
        except ValueError:
            socket.sendto(str.encode("Shenoni nje numer pas kerkeses ANASJELLTAS"), addr);
  #good
    elif(vargu[0]=='EVENODD'):
        try:
            mesazhi = str(EVENODD(int(vargu[1])))
            socket.sendto(mesazhi.encode(),addr);
            
        except IndexError:
            socket.sendto(str.encode("Shenoni nje numer pas kerkeses PRIME!"),addr);
        except ValueError:
            socket.sendto(str.encode("Shenoni nje numer te plote pas kerkeses PRIME!"),addr)
  #good
    elif(vargu[0]=='SWAP'):
        try:
            mesazhi = str(SWAP(int(vargu[1]),int(vargu[2])))
            socket.sendto(mesazhi.encode(),addr); 
           
        except IndexError:
            socket.sendto(str.encode("Shenoni nje numer pas kerkeses PRIME!"),addr);
        except ValueError:
            socket.sendto(str.encode("Shenoni nje numer te plote pas kerkeses PRIME!"),addr)
    else:
        socket.sendto(str.encode("Shenoni njeren nga kerkesat!"), addr);

while True:
    kerkesa, addr = socket.recvfrom(1024);
    kerkesa = kerkesa.decode('utf-8');
    vargu= kerkesa.split();
    function1(vargu,socket,addr);
    

