def quickSort(a: list, start: int, end: int):
    i = start
    j = end - 1
    pivot = a[int ((start + end)/2)]

    while i <= j:

      while a[i] < pivot and i < end: i += 1
      while a[j] > pivot and j > start: j -= 1

      if i < j:
        aux = a[i]
        a[i] = a[j]
        a[j] = aux
        
      if i <= j:
        i += 1
        j -= 1

    if j > start: quickSort(a, start, j+1)
    if i < end: quickSort(a, i, end)
