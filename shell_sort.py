def shellSort(a: list):
    h = 1
    n = len(a)

    # gap | knuth's sequency
    while h < n:
      h = h*3+1
      
    while h > 0:
      for i in range(h, n):
        c = a[i]
        j = i
        while j >= h and c < a[j - h]:
          a[j] = a[j - h]
          j = j - h
          a[j] = c
          
      h = int(h / 3)
