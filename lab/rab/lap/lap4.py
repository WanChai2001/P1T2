class node:
    def __init__(self):
        self.data = None
        self.next = None
class stack():
    def __int__(self):
        self.first = None
    def push (self,data):
        new_node  = node()
        new_node.data = data
        new_node.next = self.first
        self.first = new_node
    def pop (self):
        if self.first == None :
            print("stack under flow")
            main()
            pop = self.first
            self.first =self.first.next
            pop.next = None
            print(" %s top stack was deleted"%pop.data)
            if self.first == None:
                print("stack under flow")
                main()
        def display(self):
            d = self.first
            if d.next == None:
                print("stack under flow")
            print("Data in stack")
            while d is not None:
                print("[ % ]"%d.data)
                d = d.next
ST = stack()
def main():
    while True:
        print("MENU")
        print("=======================")
        print("[1]  Push stack")
        print("[2]  Pop Stack")
        print("[3]  stop Program")
        print("========================")
        n = int(input("Select Number = "))
        if n == 1:
            print("Enter[0] Exit")
            while True:
                N = str(input("Enter you data = "))
                if N == '0':
                    print("Input Finish")
                    break
                ST.push(N)
            ST.display()
        if n == 2:
            ST.pop()
            ST.diaplay()
        if n == 3:
            print("End Program")
            exit()
main()



