from operator import index
import sys
sys.stdin = open("피자굽기_input.txt")

class Queue():
    def __init__ (self, leng): # 리스트로 큐를 만들어요.
        self.datas = [None] * leng
        self.leng = leng
        self.front = 0
        self.rear = 0

    def __len__(self):
        return(self.rear - self.front + self.leng) % self.leng


    def enqueue(self, data): # 맨 마지막 자리 뒤에 추가
        global rear
        if self.isFull():
            print("Queue is Full")
        else:
            
            self.rear = (self.rear + 1) % self.leng
            self.datas[self.rear] = data
            

    def dequeue(self): # 맨 앞자리 제거
        global front
        if self.isEmpty():
            print("Queue is Empty")
        else:
            self.front = (self.front + 1) % self.leng
            return self.datas[self.front]

    def isEmpty(self): # 비어있으면 트루 반환
        return self.front == self.rear

    def isFull(self): # 가득 찼으면 트루 반환
        # 맨 끝의 뒤에 시작이 위치해야함.
        # 원형이니까 큐 길이로 나누고 나머지가 시작 위치랑 같은지 보기
        return (self.rear+1) % self.leng == self.front 
    
    def peek(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            return self.datas[(self.front + 1) % self.leng]
    
    def print(self):
        out= []
        if self.front < self.rear:
            out = self.datas[self.front+1:self.rear+1]
        else:
            out = self.datas[self.front+1:self.leng] + self.datas[0:self.rear+1]
        print("[f=%s, r=%d] => "%(self.front, self.rear), out)



testcase = int(input())

for test_num in range(1, testcase+1):

    circle_cnt, pizza_cnt = map(int, input().split())
    piz = list(map(int, input().split()))
    pizzas = Queue(circle_cnt+1)


    p = 0
    while not pizzas.isFull():
        pizzas.enqueue([piz[p], p])
        p += 1
    # pizzas.print()
    # print(pizzas.datas)

    turn = circle_cnt
    out_pizza = 0

    # for _ in range(15):
    while 1:
        # print(f'turn : {turn//circle_cnt}')

        # 0인 피자 들어가면
        
        # 도착했을 때 치즈 양을 반으로 줄임
        if pizzas.peek() != 0:
            # 반으로 줄였을 때 0이 되면 바로 뺌
            if pizzas.peek()[0]//2 == 0:
                pizzas.dequeue()
                out_pizza+=1
                if p == pizza_cnt: # 더 넣을 피자가 없으면
                    if len(pizzas) == 1: # 완전 끝이면
                        break
                    # else:
                    #     pizzas.enqueue([-1) # , p]더미피자 넣어줌 회전용
                else:
                    pizzas.enqueue([piz[p], p])
                    p+=1
            else: # 반으로 줄여도 0이 아니면
                # print(pizzas.peek())
                half = pizzas.peek()[0] // 2
                imp = pizzas.peek()[1]
                pizzas.dequeue()
                pizzas.enqueue([half, imp])
        # pizzas.print()

    print(f'#{test_num} {pizzas.peek()[1]+1}')