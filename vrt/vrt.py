lines=open('president.vrt').readlines()
length=len(lines)
i=0
while i<length:
    i+=1
    if lines[i][:2]=='<s':
        i+=1
        while lines[i][:4] != '</s>':
            print lines[i].split()[0],
            i+=1
        print
