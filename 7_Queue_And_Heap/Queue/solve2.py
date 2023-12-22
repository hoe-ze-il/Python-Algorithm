from queue import Queue

def solve(cmd, queue):
    if cmd[0] == "enqueue":
        print(queue.enqueue(cmd[1]))
    elif cmd[0] == "dequeue":
        print("Oops!" if queue.empty() else queue.dequeue())
    elif cmd[0] == "peek":
       print("None!" if queue.empty() else queue.peek())
    elif cmd[0] == "size":
        print(queue.size())
    elif cmd[0] == "empty":
        print(queue.empty())
        
N = int(input())
queue = Queue()
for _ in range(N):
    cmd = input().split()
    solve(cmd, queue)