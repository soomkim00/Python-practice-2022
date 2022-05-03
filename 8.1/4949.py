while True:
    stk = []
    brackets = ['(', ')', '[', ']']
    st = input()

    if st == '.':
        break
    for s in st:
        if s in brackets:
            stk.appends(s)
        if stk[-2:] == brackets[:2] or stk[-2:] == brackets[2:]:
            stk.pop()
            stk.pop()
    if len(stk) == 0:
        print('yes')
    else:
        print('no')
