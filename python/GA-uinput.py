import random as r
import sys
import time
import math

def mkString(len):
    ret = ''
    for x in range(len):
        ret += chr(r.randint(20,128))
    return ret

def createMonkeys(len, len2):
    monkeys = []
    for x in range(len):
        monkeys.append(mkString(len2))
    return monkeys

def fitness(monkey, goal):
    numRight = 0
    for x in range(len(monkey)):
        if (monkey[x] == goal[x]):
            numRight += 1
    return float(numRight) / len(goal)

def createPool(monkeys, goal):
    matingPool = []
    rec = 0
    record = ''
    for monkey in monkeys:
        p = fitness(monkey, goal) * 100
        if (p>rec):
            rec = p
            record = monkey
        for x in range(int(p)):
            matingPool.append(monkey)
    matingPool.append(record)
    return matingPool

def crossover(A, B):
    monkey = ''
    midpoint = r.randint(0,len(A))
    for x in range(len(A)):
        if (x < midpoint):
            monkey += A[x]
        else:
            monkey += B[x]
    return monkey

def mutate(monkey, rate):
    ret = ''
    for x in range(len(monkey)):
        if(r.random() < rate):
            ret += mkString(1)
        else:
             ret += monkey[x]
    return ret

def help():
    print('Help View')
    print('execute as \t python3 GA-uinput.py <size> <mutationRate> <goal>')
    exit()

if(len(sys.argv) == 1):
    help()

if (sys.argv[1] == '-h' or sys.argv[1] == '-help' or sys.argv[1] == 'help' or sys.argv[1] == '/h' or sys.argv[1] == '/help' or sys.argv[1] == '?' or sys.argv[1] == '-?' or sys.argv[1] == '/?'):
    help()

size = int(sys.argv[1])
mutationRate = float(sys.argv[2])
record = ''
matingPool = []
gen = 0
goal = str(sys.argv[3])

#prin(t)formation
print('size \t '+str(size))
print('mutationRate \t '+str(mutationRate))
print('goal \t '+str(goal))

#pause
time.sleep(0.885)

#continue
start = time.time()

#init
monkeys = createMonkeys(size, len(goal))

#loop
while (record != goal):
    print(gen)
    gen += 1
    matingPool.clear();
    matingPool = createPool(monkeys, goal)
    record = matingPool[len(matingPool)-1]
    print(record)
    monkeys.clear()
    for x in range(size):
        A = matingPool[r.randint(0,len(matingPool)-2)]
        B = matingPool[r.randint(0,len(matingPool)-2)]
        monkey = crossover(A,B)
        monkey = mutate(monkey, mutationRate)
        monkeys.append(monkey)

end = time.time()

print('\nexecution time:')
print(str(math.floor((end - start)*100) / 100) + ' seconds')
