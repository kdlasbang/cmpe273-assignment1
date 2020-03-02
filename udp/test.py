upload=[]
output=[]
with open("upload.txt","r") as f:
    db=f.read().splitlines()

for line in db:
    words=line.split(':')
    upload.append(words[1])


with open("data.txt","r") as f1:
    db1=f1.read().splitlines()
for line1 in db1:
    output.append(line1)

if len(output)!=len(upload):
    print("len wrong")

for i in range(len(output)):
    if output[i]!=upload[i]:
        print("data wrong---i: ",i)

print("got through")
