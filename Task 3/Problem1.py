text = input()

k = int(input())
d = int(input())

szText = len(text)

mxOcc = 0
for i in range (szText - k + 1):
    pat = text[i : i + k]
    occ = 0
    for j in range(szText - k + 1):
        subText = text[j : j + k]
        cnt = 0
        for id in range(k):
            if (pat[id] != subText[id]):
                cnt += 1
        if ( cnt <= d ) :
            occ += 1
    if ( occ >= mxOcc ):
        mxOcc = occ

patterns = []

for i in range (szText - k + 1):
    pat = text[i : i + k]
    occ = 0
    for j in range(szText - k + 1):
        subText = text[j : j + k]
        cnt = 0
        for id in range(k):
            if (pat[id] != subText[id]):
                cnt += 1
        if ( cnt <= d ) :
            occ += 1
    if ( occ >= mxOcc ):
        patterns.append(pat)


ans = list(set(patterns))

print(ans)

