'''year=int(input())
yearAnimals={0:"Дракон",1:"Змея",2:"Лошадь",3:"Овца",
             4:"Обезьяна",5:"Петух",6:"Собака",7:"Свинья",
             8:"Крыса",9:"Бык",10:"Тигр",11:"Заяц"}
print(yearAnimals[(year-2000)%12]'''

'''ch=str(input())
if len(ch)==5:
    otv=ch[::-1]
else:
    otv=ch[0]+ch[5:0:-1]
print(int(otv))'''

'''ch=str(input())
ch=ch[::-1]
otv=ch[:3]
N=(len(ch)-1)//3

for i in range(1,N+1):
    otv+=','+ch[3*i:3*i+3]
if len(otv)<len(ch):
    otv+=','+ch[len(otv)-N:len(ch)]
print(otv[::-1])'''

'''kolvo=int(input())
minus=int(input())
ind=0
data=[i for i in range(1,kolvo+1)]
while len(data)>1:
    vyb=[data[i] for i in range(minus-1-ind,len(data),minus)]
    if len(vyb)>0 and len(vyb)<len(data):
        ind=len(data)-data.index(vyb[-1])-1
        data=[data[i] for i in range(len(data)) if not(data[i] in vyb)]
    elif len(vyb)==len(data):
        data=[data[-1]]
    else:
        data=[data[(minus-ind)%len(data)]]
print(data[0])'''

'''N=int(input())
k=[0,0,0,0]
for i in range(N):
    x,y=map(int,input().split())
    if x>0 and y>0:
        k[0]+=1
    elif x>0 and y<0:
        k[3]+=1
    elif x<0 and y>0:
        k[1]+=1
    elif x<0 and y<0:
        k[2]+=1
chet=['Первая','Вторая','Третья','Четвертая']
for i in range(4):
    print(f"{chet[i]} четверть:",k[i])'''

'''data=list(map(int,input().split()))
k=0
for i in range(1,len(data)):
    if data[i]>data[i-1]:
        k+=1
print(k)'''

'''data=list(map(str,input().split()))
N=len(data)//2
for i in range(N):
    data[i*2+1],data[i*2]=int(data[i*2]),int(data[i*2+1])
print(*data)'''

'''data=list(map(int,input().split()))
N=len(data)
data.reverse()
data+=[0]
data.reverse()
data[0]=data[-1]
print(*data[:N])'''

'''print(len(set(list(map(int,input().split())))))'''
'''data=list(map(int,input().split()))
k=1
for i in range(len(data)-1):
    if data[i]!=data[i+1]:
        k+=1
print(k)'''

'''N=int(input())
data=[]
for i in range(N):
    data.append(int(input()))
chislo=int(input())
data.sort()
ind=len(data)
for i in range(len(data)):
    if data[i]>chislo:
        ind=i-1
data=data[:ind+1]
fl=False
for i in range(len(data)):
    if chislo%data[i]==0 and chislo//data[i] in data[i+1:]:
        fl=True
        print('ДА')
if fl==False:
    print('НЕТ')
N=int(input())
data=[]
for i in range(N):
    data.append(int(input()))

fl=False
chislo=int(input())
for i in range(len(data)-1):
    for j in range(i+1,len(data)):
        if data[i]*data[j]==chislo:
            fl=True
            print('ДА')
            break
    if fl==True:
        break
if fl==False:
    print('НЕТ')'''

'''Tim=str(input())
Rus=str(input())
if Tim==Rus:
    print('ничья')
elif Tim=='ножницы' and Rus=='бумага' or Tim=='бумага' and Rus=='камень' \
        or Tim=='камень' and Rus=='ножницы':
    print('Тимур')
else:
    print('Руслан')'''

'''zn=['бумага','камень','ножницы','Спок','ящерица']
kl=['a','b','c','d','e']
sl={'a':'bd','b':'ce','c':'ae','d':'bc','e':'ad'}
Tim=str(input())
Rus=str(input())
for i in range(5):
    if Tim==zn[i]:
        Tim=kl[i]
    if Rus==zn[i]:
        Rus=kl[i]
if Rus==Tim:
    print('ничья')
elif Rus in sl[Tim]:
    print('Тимур')
else:
    print('Руслан')'''

'''data=str(input())
maxx=0
k=0
pre=''
for i in data:
    if i=='Р':
        if i==pre:
            k+=1
        else:
            maxx=max(maxx,k)
            k=1
    else:
        maxx=max(maxx,k)
        k=0
    pre=i
maxx=max(k,maxx)
print(maxx)'''

'''N=int(input())
nomera=[]
for i in range(1,N+1):
    s=str(input())
    q=len(s)
    for a in range(q):
        fl = False
        if s[a]=='a':
            for n in range(a+1,q):
                if fl == True:
                    break
                if s[n]=='n':
                    for t in range(n+1,q):
                        if fl == True:
                            break
                        if s[t]=='t':
                            for o in range(t+1,q):
                                if fl == True:
                                    break
                                if s[o]=='o':
                                    for z in range(o+1,q):
                                        if s[z]=='n':
                                            nomera.append(i)
                                            fl=True
                                            break
        if fl==True:
            break
print(*nomera)'''

'''slovo='роскомнадзор'
data=slovo+' запретил букву'
ind=[]
for i in slovo:
    ind.append(ord(i))
if max(ind)>ord('у'):
    print(chr(max(ind))+' '+chr(max(ind)))
elif max(ind)==ord('У'):
    print('у уу у')
else:
    print('уу у')
    
slovo=str(input())
data=slovo+' запретил букву '
for i in range(ord('а'),ord('я')+1):
    if chr(i) in data:
        print(data+chr(i))
        data=data.replace(chr(i),'')
        k=0
        for i in range(len(data)):
            if data[i]==' ':
                k+=1
            else:
                break
        data=data[k:]
        for i in range(1,10):
            data=data.replace(i*' ',' ')'''

print('Hello, git!')

