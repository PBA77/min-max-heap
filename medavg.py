from minmaxheap import MinMaxHeap

count = sum = 0

medianHeap = MinMaxHeap()

while True:
    x = input()
    if x == "a":
        if count > 0: print(sum / count)
        else: print(None)
    elif x == "m":
        print(medianHeap.getMedian())
    else:
        num = int(x)
        sum += num
        count += 1
        medianHeap.put(num)
