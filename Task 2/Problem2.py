text = input()
k = int(input())

txt_sz = len(text)

mxOcc = 0
for i in range(txt_sz - k + 1):
    pat = text[i : i + k]
    occ = 0
    for j in range(txt_sz - k + 1) : 
        if text[j : j + k] == pat :
            occ += 1
    if ( occ >= mxOcc ) :
        mxOcc = occ

patterns = []
for i in range(txt_sz - k + 1):
    pat = text[i : i + k]
    occ = 0
    for j in range(txt_sz - k + 1) : 
        if text[j : j + k] == pat :
            occ += 1
    if ( occ == mxOcc ) :
        patterns.append(pat)

ans = list(set(patterns))
print(ans)
