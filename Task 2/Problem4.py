pat = input()
str = input()

pat_sz = len(pat)
for i in range (len(str) - pat_sz + 1) : 
    if str[i : i + pat_sz] == pat :
        print(i)

