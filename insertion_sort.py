def insertionSort(a: list):
  for x in range(1, a.__len__()):
    j = x
    value = a[x]
    while(j>0 and a[j-1] > value):
      a[j] = a[j-1]
      j -= 1
    a[j] = value
