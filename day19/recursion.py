x=[1,2,3,[4,5,6,[3,4,5]]]
sum=0
for val in x:
    if isinstance(val,list):
        for i in val:
            if isinstance(i,list):
                for j in i:
                    sum+=j
            else:
                sum+=i
    else:
        sum+=val
print(sum)