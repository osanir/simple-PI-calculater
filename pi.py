pie = 0.0
step = int(input("Enter the number of steps: "))
k = 0
while k <= step:
    if k % 2 == 0:
        pie += 1 / (2*k+1)
    else:
        pie -= 1 / (2*k+1)
    k += 1
    print("Pi: ",4*pie)
