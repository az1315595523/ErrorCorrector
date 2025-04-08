from re import M


List = eval(input())
List1 = List.copy()
for i in List:
    Max = max(List)
    Min = min(List)
    if Max == max(List1):
        List1.remove(Max)
    elif Min == min(List1):
        List1.remove(Min)
    else:
        break
print(List1)
