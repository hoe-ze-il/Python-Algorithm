# def solve(cmd, queue):
#     if cmd[0] == "push_front":
#         queue.append(cmd[1])
#     elif cmd[0] == "push_back":
#         queue.insert(0, cmd[1])
#     elif cmd[0] == "pop_front":
#         print("Oops!" if len(queue) == 0 else queue.pop(-1))
#     elif cmd[0] == "pop_back":
#         print("Oops!" if len(queue) == 0 else queue.pop(0))
#     elif cmd[0] == "peek_front":
#         print("None!" if len(queue) == 0 else queue[-1])
#     elif cmd[0] == "peek_back":
#         print("None!" if len(queue) == 0 else queue[0])

from collections import deque

def solve(cmd, queue: deque):
    if cmd[0] == "push_front":
        queue.append(cmd[1])
    elif cmd[0] == "push_back":
        queue.appendleft(0, cmd[1])
    elif cmd[0] == "pop_front":
        print("Oops!" if len(queue) == 0 else queue.pop())
    elif cmd[0] == "pop_back":
        print("Oops!" if len(queue) == 0 else queue.popleft())
    elif cmd[0] == "peek_front":
        print("None!" if len(queue) == 0 else queue[-1])
    elif cmd[0] == "peek_back":
        print("None!" if len(queue) == 0 else queue[0])

N = int(input())
queue = deque()
for _ in range(N):
    cmd = input().split()
    solve(cmd, queue)