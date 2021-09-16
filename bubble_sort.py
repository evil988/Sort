def bubbleSort(a: list): 
    for i in range(a.__len__()):
      change = False
      for j in range(a.__len__()-1):
        if a[j] > a[j+1]:
          temp = a[j]
          a[j] = a[j+1]
          a[j+1] = temp
          change = True
      if not change:
        return
