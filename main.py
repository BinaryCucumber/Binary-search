import time
import timeit
from timeit import default_timer as timer

arr_1 = []
for i in range(1000000):
    arr_1.append(i)
object_1 = 564

ptr_start = 0
ptr_end = len(arr_1) - 1
start = timer()
while ptr_start <= ptr_end:
    ptr = (ptr_end + ptr_start) // 2
    if arr_1[ptr] == object_1:
        print(f"index: {ptr}, value: {arr_1[ptr]}")
        break
    elif arr_1[ptr] < object_1:
        ptr_start = ptr + 1
    else:
        ptr_end = ptr - 1
end = timer()
print(f"time: {end - start}")



