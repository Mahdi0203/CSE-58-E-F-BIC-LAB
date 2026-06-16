kmers = input()
str = input()

d = int(input())

szPat = len(kmers)
szStr = len(str)

for i in range (0, szStr) :
    cnt = 0
    idx = i
    for j in range(0, szPat, 1):
        if ( kmers[j] != str[idx]) :
            cnt += 1
        idx += 1
    if ( cnt <= d ) :
        print(i)
