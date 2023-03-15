class CircularQueue(object):
    def __init__(self,limit = 7):
        self.front = None
        self.rear = None
        self.limit = limit
        self.queue = []
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
    def isEmpty(self):
        return self.queue == []
    def isFull(self):
        return len(self.queue) == self.limit
    def enqueue(self,data):
        if self.isFull():
            print("Queue is Overflow")
            print("Unsuccessfull")
        elif self.isEmpty():
            self.front = self.rear = 0
            self.queue.append(data)
            print("Successfull")
        else:
            self.rear += 1
            self.queue.append(data)
            print("Successfull")
    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            print("Unsuccessfull")
        else:
            self.front += 1
            print("Successfull")
            return self.queue.pop(0)

if __name__ == '__main__':
    stack = CircularQueue(7)
    while (1):
        print("MENU")
        print("\t[1] :  push")
        print("\t[2] :  pop")
        print("\t[3] :  Stop program")
        ch = input("กรุณาเลือกคำสั่ง ==> ")
        if ch == '1':
            stack.enqueue(input("กรุณาป้อนหมายเลขหรือตัวอักษรที่ต้องการ = "))
            print(" [ %s ] "%stack)
        if ch == '2':
            stack.dequeue()
            print(" [ %s ] "%stack)
        if ch == '3':
            print("โปรแกรมสิ้นสุดการทำงาน")
            exit()


