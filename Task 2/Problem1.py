text = input()
patern = input()

pat_sz = len(patern)

cnt = 0
for i in range (len(text) - pat_sz + 1):
    if text[i : i + pat_sz] == patern:
        cnt += 1
        
print(cnt)
