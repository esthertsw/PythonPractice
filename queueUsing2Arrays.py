class Queue:
    def __init__(self):
        self.queue = []
        self.size = -1
    def enqueue(self, x):
        if (x!=0 and abs(x)<=1000000000):
            self.queue.append(x)
            self.size += 1
    def dequeue(self):
        if (self.size>=0):
            del self.queue[0]
    def printQueue(self):
        if (self.size>=0): 
            print(self.queue[0])
        else:
            print("None")

aQueue = Queue()
queryCount = input()
queryCount = int(queryCount)
queryArray = []
for i in range (0, queryCount):
    queryArray = [int(x) for x in input().split()]
    while(queryArray[0] !=1 and queryArray[0] != 2 and queryArray[0] !=3):
        del queryArray[0]
        queryArray = [int(x) for x in input().split()]
    if queryArray[0] == 1:
        aQueue.enqueue(int(queryArray[1]))
        del queryArray[1]
    elif queryArray[0] == 2:
        aQueue.dequeue()
    elif queryArray[0] == 3:
        aQueue.printQueue()
    del queryArray[0]