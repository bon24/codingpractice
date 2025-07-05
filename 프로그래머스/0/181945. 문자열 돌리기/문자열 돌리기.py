str = input()
lang=[]
for i in range(len(str)):
    lang.append(str[i:i+1])
for i in range(len(lang)):
    print(lang[i])