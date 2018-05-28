li = input("введите строку ")
m=""
for i in li:
    if i != "я":
        m+=(chr(ord(i) + 1))
    else:
        m+=" "
print(m)
