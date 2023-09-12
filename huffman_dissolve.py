def count_frequency(pickup):
    check={}
    for element in pickup:
        if element in check:
            check[element]+=1
        else: check[element]=1
    del check[" "]
    total = 0;
    for key in check:
        total += check.get(key)
    count = dict(sorted(check.items(), key=lambda x: x[1]))
    for key, value in count.items():
        print(f"{key}: {value}/{total}")
    print("Total words:",total)

pickup=list("apple macintosh imac ipod Macbook Macbook pro ipad pro iphone ipod touch macbook air ipad mini apple watch")
count_frequency(pickup)