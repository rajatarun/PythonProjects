f = open('tarun1.txt','r');                                 #opening the file
data = f.readline()                                         #reading the first line in log
dnslist =[]; 
while data != '':
    data = data.strip()                                     #stripping the new line attribute
    dnslist.append(data.split())                            #splitting the data into array and adding it to an array
    data = f.readline(); 
dnslist.remove([]);                                         #removing the first sppace in array 
dnslist1 = dnslist;                                         #copying data into another array
for i in range (0,dnslist.__len__()): 
    dnslist[i][1] = dnslist[i][1].replace(':',' ');          #removing : in time data for calculation
    dnslist[i][1] = dnslist[i][1].replace('.',' ');          # removing . in time data for calculation

from datetime import datetime   
startTime = datetime.now()

import numpy as np                                          #importing numpy module     
b = [];
for i in range (0,len(dnslist)):                            #converting time attribute to seconds for calculation
    ran = dnslist[i][1].split();                            
    ran.pop();                                                      
    ran = int(ran[0])*3600+int(ran[1])*60+int(ran[2])
    b.append(ran);

#ranges = np.array(a);
listofdata = np.array(b);                                   # converting b to a numpy array
arr = [];
print(listofdata);
for i in range (0,len(listofdata)):                         # converting string data to int type
    arr.append(listofdata[i]);
diffarray = np.diff(arr,n=1);                               # differentiating the array values
values = [];
for i in range (0,len(diffarray)):                          # searching for values greater than 10000 change in time
    if(diffarray[i] > 10):
        values.append(i);
    else:
        continue;
#print(values);
finalindex = [];
for i in range (0,len(values)):                           # creating a final index if diff between indexes is less than 10 neglecting them   
        finalindex.append(values[i]+1);
#finalindex = values;

                                                         # appending final index to array
finalindex.append(len(dnslist)-1);
finalindex.reverse();
finalindex.append(0);                                       # appending starting index of array
finalindex.reverse();
#print(finalindex);

for i in range(0,len(finalindex)-1):                        # loop to analyze data and write into file
    temp = [];
    name= dnslist[finalindex[i]][6];
    name = name.replace('.','');
    
    name = name+('.report.txt');
    f1 = open(name,'w');                                # opening a file to write data
    time = dnslist[finalindex[i]][1];
    for j in range (finalindex[i],finalindex[i+1]-1):
        temp.append(dnslist[j][6]);
    print(temp[0],int(len(temp)/2));
    temp1 = [temp[0],':', int(len(temp)/2),time,'hhmmss.ms'];
    f1.write('\n');
    f1.write(str(temp1));
    for k in range(0, len(temp)-1):
        if (temp[k] == temp[k+1]):
            print(temp[k]);
            f1.write(temp[k]);
            f1.write('\n');
            
print(finalindex)
print(datetime.now()-startTime)

