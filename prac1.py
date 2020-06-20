def sort(l):
    for i, p in enumerate(l):
        if (p - 1) - i > 2:
            return "Too chaotic"
    else:
        swap = 0
        for i in range(len(l) - 1,0,-1):
            for j in range(i):
                if l[j] > l[j + 1]:
                    l[j],l[j + 1] = l[j + 1],l[j]
                    swap+=1
                else:
                    continue
        return swap

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().split()))
        sort(q)