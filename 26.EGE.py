f=open('26-j1.txt')
data=int(f.readline())
d=[]
coin=0 #чтобы видеть.ОНА ЮЗЕЛЕСС
count=0
for i in range(data): #Пробегает по всем данным
    coin=data.readline()
    d.append(int(coin)) #записывает все данные
for x in range(data-1): #проходит по всем данным кроме предпослденго.
    for j in range(x+1,data) #берет следующее и доходит до конца.
        if d[x]+d[j]==100: #перебирает все значение и складывает,пока не соберется 100.Напримеь первое 17 и он ьудет перебирать,пока не найдет 83.
            count+=1 #записывает количество ящиков в count.
            d[j]=0 #.обнуляет,чтобы не суммировались
            d[x]=0 #.обнуляет,чтобы не суммировались
            print(count) #выовдим количество.
