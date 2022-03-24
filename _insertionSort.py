
def _insertionsort_():
    a = [8,2,4,9,3,6]
    print(a)
    for i in range(0, n-1):
        temp = a[i]
        red = i-1
        while red>=0 & a[red]>temp:
            red=red-1
        a[red+1]=temp
    print(a)

if __name__ == "__main__":
   _insertionsort_()


