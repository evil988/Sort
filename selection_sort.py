def selectionSort(a: list):
  for i in range(a.__len__()):
    min = i
    for j in range(i+1, a.__len__()):
      if a[j] < a[min]:
        min = j
    temp = a[min]
    a[min] = a[i]
    a[i] = temp
  