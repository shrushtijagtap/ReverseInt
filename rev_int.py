def func(str):
    for i in str:
        if i>=65 and i<=90:
            return 0
    n=len(str)

    result=0
    multiplier=1
    for i in str:
        i=int(i)
        result+=i*multiplier
        multiplier=multiplier*10
    return result

print(func('1509'))
i='a'
i=int(i)
print(i)

