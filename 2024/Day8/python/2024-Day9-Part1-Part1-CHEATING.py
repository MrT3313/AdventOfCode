import os
import sys
import time

start_time = time.time()

def findSlope(antA,antB):
    x1, y1 = antA
    x2, y2 = antB

    return abs((y2 - y1)),abs((x2 - x1))

def setAntinode(antA,antB):
    rise,run=findSlope(antA,antB)
    x1, y1 = antA
    x2, y2 = antB

    if x1>x2:
        x1=x1+run
        x2=x2-run
    elif x1<x2:
        x1=x1-run
        x2=x2+run
    
    if y1<y2:
        y1=y1-rise
        y2=y2+rise

    return str(x1)+","+str(y1), str(x2)+","+str(y2)

def setAntinodePart2(antA,antB, xLimit, yLimit):
    rise,run=findSlope(antA,antB)
    x1, y1 = antA
    x2, y2 = antB

    antinodes=[str(x1)+","+str(y1),str(x2)+","+str(y2)]
    
    inBounds1,inBounds2=True,True
    while inBounds1 or inBounds2:
        if x1>x2:
            x1+=run
            x2-=run
        elif x1<x2:
            x1-=run
            x2+=run
        
        if y1<y2:
            y1-=rise
            y2+=rise
        
        if x1<0 or x1>xLimit or y1<0 or y1>yLimit:
            inBounds1=False
        else:
            antinodes.append(str(x1)+","+str(y1))
        
        if x2<0 or x2>xLimit or y2<0 or y2>yLimit:
            inBounds2=False
        else:
            antinodes.append(str(x2)+","+str(y2))


    return antinodes

part1=0
part2=0
antennaMap=[]
totalMap=[]
frequencies=set()
antinodeList=set()
antinodeList2=set()

with open(os.path.join(os.path.dirname(sys.argv[0]), "../input.txt"),"r") as file:
# with open(os.path.join(os.path.dirname(sys.argv[0]), "../test_input.txt"),"r") as file:
    for y,line in enumerate(file):
        eachChar=[]
        for x,char in enumerate(line):
            if char !='\n': eachChar.append(char)
            if char != "." and char !='\n':
                frequencies.add(str(char))
                antennaMap.append([char,[x,y]])
        totalMap.append(eachChar)

for f in frequencies:
    antennas=[]
    for a in antennaMap:
        if a[0]==f:
            antennas.append(a[1])

    for i,antA in enumerate(antennas):
        for b in range(i+1,len(antennas)):
            antinodeA,antinodeB=setAntinode(antA,antennas[b])
            antinodeList.add(antinodeA)
            antinodeList.add(antinodeB)

# part2
for f in frequencies:
    antennas=[]
    for a in antennaMap:
        if a[0]==f:
            antennas.append(a[1])

    for i,antA in enumerate(antennas):
        for b in range(i+1,len(antennas)):
            antinodes=setAntinodePart2(antA,antennas[b],len(totalMap[0]),len(totalMap))
            for antis in antinodes:
                antinodeList2.add(antis)

for a in antinodeList:
    crd=a.split(',')
    x,y=int(crd[0]),int(crd[1])

    if x<0 or x>=len(totalMap[0]) or y<0 or y>=len(totalMap): continue
    else:
        part1+=1
        totalMap[y][x]="#"

# print("\n\n MAP FOR PART ONE \n\n")
# for t in totalMap: print(''.join(t))

for a in antinodeList2:
    crd=a.split(',')
    x,y=int(crd[0]),int(crd[1])

    if x<0 or x>=len(totalMap[0]) or y<0 or y>=len(totalMap): continue
    else:
        part2+=1
        totalMap[y][x]="#"

# print("\n\n MAP FOR PART two \n\n")
# for t in totalMap: print(''.join(t))

print("\n\nPart 1:",part1, "   |   Part 2:",part2)
print("Total elapsed time: %.2f MS" % ((time.time()-start_time)*1000))