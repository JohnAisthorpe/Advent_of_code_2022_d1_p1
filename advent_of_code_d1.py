#source: https://www.youtube.com/watch?v=xqilQUL_JDk

#getting data
with open('day_01.in') as file:
    data = [i for i in file.read().strip().split("\n")]

#traversing every string in out data
count = 0
max = 0
for item in data:
    if item == '':
        count = 0
    else:
        num = int(item)
        count += num

    if count > max:
        max = count
    

print(max)


