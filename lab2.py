import re
dic = {1:'один',2:'два',3:'три',4:'четыре',5:'пять',6:'шесть',7:'семь',8:'восемь',9:'девять'}
seq = open('txt1.txt','r').read()
print("Введите цифру")
k = input()
counter = 1
nums = re.findall(r'[-+]?\d+', seq)
for i in nums:
    if i[0] == k:
        if int(i) % 2 == 0:
            if counter == 5:
                for j in i:
                    print(dic.get(int(j)), end=' ')
                counter = 1
                print(end='\n')
            else:
                print(i)
                counter += 1
