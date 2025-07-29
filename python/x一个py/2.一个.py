res = ["No"]*int(input())
for i in range(len(res)):
    msg = input()
    for j in range(len(msg)):
        res[i] = "Yes" if msg[:j+1]==msg[j::-1] and msg[j+1:]==msg[:j:-1] and len(msg[:j+1])>1 and len(msg[j+1:])>1 else ("No"if res[i]=="No" else "Yes")
for i in res:
    print(i)