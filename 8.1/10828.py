import sys
n = int(input())
stack = []

for _ in range(n):
    commands = sys.stdin.readline().strip().split()
    val = 0

    if len(commands) == 2:
        val = commands[1]
    command = commands[0]

    if command == 'push':
        stack.append(val)

    elif command == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])

    elif command == 'size':
        print(len(stack))

    elif command == 'empty':
        if not stack:
            print(1)
        else:
            print(0)

    elif command == 'top':
        if not stack:
            print(-1)
        else:
            print(stack.pop())
