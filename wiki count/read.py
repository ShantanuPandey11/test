l=[]
k=[]
no_of_words = 0
no_of_letters = 0
data = open('bihar.txt','r',encoding="utf8")

for word in data:
    if word == '\n':
        pass
    else:
        s = word.split()
        l.append(s)
data.close()

for i in l:
    for j in i:
        s = str(j)
        k.append(s)
        
for i in k:
    no_of_letters = len(i) + no_of_letters

no_of_words = len(k)
print("The Number Of words In bihar.txt : " ,no_of_words)



print("The Number Of letters In bihar.txt : ", no_of_letters)
