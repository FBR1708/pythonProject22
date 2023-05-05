# l1 = [2,4,3]
# l2 = [5,6,4]
# k=l1[::-1]
# k1=l2[::-1]
# l=''
# l1=''
# for i in k:
#     l += ''.join(str(i))
# for j in k1:
#     l1 += ''.join(str(j))
# j=int(l)+int(l1)
# p=[]
# for m in str(j):
#     p.append(int(m))
# print(p[::-1])


# from collections import Counter
# s = "abacbc"
# l=(i[1] for i in Counter(s).items())
# k=set(l)
# if len(k)==1:
#     print(True)
# else:
#     print(False)


# from collections import Counter
# s = [3,2,3,2,2,2]
# l=(i[1] for i in Counter(s).items())
# k=set(l)
# for i in k:
#     if i%2==0:
#         print(True)
#     else:
#         print(False)


# x=-123
# x=str(x)
# if x>'0':
#     k=reversed(x)
#     l=''
#     for i in k:
#         l+=''.join(i)
# elif x<'0':
#     b=list(x)
#     k1=b.pop(0)
#     m=reversed(b)
#     l1=''
#     for j in b:
#      l1+=''.join(j)
#      print(l1)


# from threading import Thread
# import time
#
#
# def task(n):
#     time.sleep(4)
#     print(f'Task {n} bajarildi')
#
#
# start = time.time()
#
# oqimlar = []
# for i in range(10):
#     oqimlar.append(Thread(target=task, args=(i,), daemon=True))
#
# for oqim in oqimlar:
#     oqim.start()
#
# time.sleep(6)
#
# for oqim in oqimlar:
#     oqim.join()
#
# end = time.time()
# print(int(end - start), '- seconds')


import json, httpx, time
start=time.time()
import yaml
url = 'https://jsonplaceholder.typicode.com/photos'
response = httpx.get(url)
if response.status_code == 200:
    data = response.json()
    with open('photos1.json', 'w') as f:
        json.dump(data, f, indent=2)
    with open('photos.json', 'w') as f:
        json.dump(data, f, indent=2)
    with open("photos1.yaml", 'w') as f:
        yaml.dump(data, f, indent=2)
    with open("photos.yaml", 'w') as f:
        yaml.dump(data, f, indent=2)
end=time.time()
print(int(end-start))