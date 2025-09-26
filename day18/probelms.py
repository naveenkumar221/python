list=["hello","welcome","something","hello","apple","apple"]
op={ }
for items in list:
    if items in op:
        op[items]+=1
    else:
        op[items]=1
print(op)


ex="BANANNA"
s={ }
for y in ex:
    if y in s:
        s[y]+=1
    else:
        s[y]=1
print(s)

