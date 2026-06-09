pat = input()

map = {
    "A" : "T",
    "T" : "A",
    "C" : "G",
    "G" : "C"
}

ans = ""
for i in (pat):
    ans += map[i]

print(ans[::-1])
