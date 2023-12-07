f = open("puzzle", "r").read().strip().split("\n")
times = [int(x) for x in f[0].split(":")[1].strip().split(" ") if x]
dists = [int(x) for x in f[1].split(":")[1].strip().split(" ") if x]
t = int("".join(str(c) for c in times))
dist = int("".join(str(c) for c in dists))

start = 0
end = t
while True:
    temp = start * (t - start)
    if temp > dist:
        break
    start += 1

while True:
    temp = end * (t - end)
    if temp > dist:
        break
    end -= 1


prod = 1
j = 0
for time in times:
    counter = 0
    for i in range(time+1):
        if i * (time - i) > dists[j]:
            counter += 1
    j += 1
    prod *= counter

print("part 1: ", prod)
print("part 2: ", end - start + 1)
