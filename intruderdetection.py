'''
Created on Nov 27, 2014

@author: rajatarun
'''
import os;
#from multiprocessing import Process;
#import time;
#def func1():
    #os.system("nmap -A -Pn 192.168.1.6 > nmap.txt");
#def func2(interface):
    #does something
    #os.system("chmod u+x test.sh")
    #os.system("./test.sh {} > test1.txt".format(interface))
def getip():                                                        # should call this function if we want to scan owt oun system
    os.system("route > route.txt");
    f1 = open("route.txt","rw");
    str1 = [line for line in f1 if line.__contains__('default')];
    str2 = str1[0];
    var = str2.split();
    print(var[7]);
    f1.flush();
    f1.close();
    os.system("ifconfig {} > ip.txt".format(var[7]));
    f1 = open("ip.txt","rw");
    str3 = [line for line in f1 if line.__contains__('Mask')];
    print(str3);
    str4 = str3[0].split();
    ipaddress = str4[1].replace('addr:','');
    return(ipaddress);
def checkforarp(ip):                                                #function for checking for a  arp scan
    f = open('intensescan.txt','r');
    ro = open('ARPfile.txt','w');
    count = 0;
    for line in f:
        if(line.__contains__('ARP') and line.__contains__(ip)):
            ro.write(line);
            count = count +1;

    ro.close();
    ro = open('ARPfile.txt','r');
    lista = [];
    for line in ro:
        if(line.__contains__('Request who-has {} tell'.format(ip))):
            string = line;
            string1 = string.split();
            index = string1.index(ip);
            lista.append(string1[index+2]);
    list1 = set(lista);
    if(count>1):
        print("a quick scan is made {}".format(list1));
    ro.close();
    f.close();
try:
    ip = raw_input("enter ip : ");                                  #taking user ip input to scan     
    checkforarp(ip);                                                #checking for arpscan
    f = open('intensescan.txt','r');                                #opening intensescan file
    f1 = open('sorted1.txt','w');                                   #opening sorted file as write mode
    for line in f:                                                  #loop to find in the list which has ip to be scanned  
        if line.__contains__(ip):
            f1.write(line);
    f1.close();                                                     #closing the files
    f.close();                                                      #closing the files
    f1 = open('sorted1.txt','r');                                   #opening sorted 1 in read mode
    seqnum = []; 
    for line in f1:                                                 #checking for seq word in the file and getting all the seq numbers 
        string = line;
        #print(string);
        string1 = string.split();
        if(string1.__contains__('seq')):
                indexvar = string1.index('seq');
                seqnum.append(string1[indexvar+1]);
    #print(seqnum);
    sorted1 = [];
    for a in seqnum:                                                 #sorting the seq numbers which are repeated more than 5 times
        if(seqnum.count(a) > 5 and sorted1.__contains__(a) == False):
            sorted1.append(a);
    #print(sorted1);
    ports = [];
    finports = [];
    ack = open('ack.txt','w');
    portsscanned = [];
    f2 = open('sorted1.txt','r');
    for i in sorted1:                                                    #checking for the ports which are scanned
        for line in f2:
            string = line;
            #print(string);
            string1 = string.split();
            if line.__contains__(i):
                indexvar = string1.index(i);
                ports.append(string1[indexvar-4].replace(ip,''));        #removing ip adress from the ip:port part
            var= i.replace(',','');
            var1 = "{},".format((int(var)+1));                           # checking for the acknowledgement number if replied will have ack number one more than seq number 
            if line.__contains__(var1): 
                string = line;
            #print(string);
                string1 = string.split();
                var2 = string1.index('Flags');
                if(string1[6].replace('[','').replace(']','').replace('.','').replace(',','') == 'S'): # checking if replied it replied with sync flag 
                    portsscanned.append((string1[2].replace(ip,'').replace('.','')));
                    ack.write(line);
            finports.append(ports);
    #print(finports);
    #print(string1[2]);
    #for i in range(len(finports)):
    #    print(finports[i]);   
    #    print(len(finports[i]));
    portsscanned1 = (i for i in portsscanned);
    f3 = open("portsscanned1.txt","w");
    a = [];
    for i in sorted(finports[0]):
        a.append(i.replace('.',''));
    a1 = [];
    for i in sorted(a):
        a1.append(i.replace(':',''));
    for i in a1:                                                         # checking for the known ports 
        if(i.isdigit() == True or i.isdigit() == False):
            f3.write(i);
            f3.write('\n');
    lengths = [];
    for i in finports:
        lengths.append(len(finports[0])); 
    
    if(max(lengths) > 900):                                              #printing the warning message if more than 900 ports are scanned it can be changed
        print("Warning your system is scanned ")
        print("ports that replied to the scan are {}".format(set(portsscanned1)));
        if (a1.__contains__('daytime') == True and portsscanned.__contains__('daytime')):
            print("attacker may get your os details make sure your daytime  port 13 is closed \n disable this service in etcinetd.conf")
            os.system("cat /etc/lsb-release");
        if (a1.__contains__('finger') == True and portsscanned.__contains__('finger')):
            print("attacker may find your system is up make sure finger port 79 is closed ");

except IndexError:                                                        # if there are no scanned ports it will throw a IndexError which is handled 
        fin = open("result1.txt","a");
        print("no error");
        fin.write("No Error \n");
        open('test1.txt', 'w').close();
        fin.close()
except TypeError:
        pass;
except ValueError:
        pass;    
except IOError:
    print("root access required");
#print(len(lengths));
#print(len(finports));
#print(len(sorted1));
#print(string1.__contains__(ip));
#print(string1);

