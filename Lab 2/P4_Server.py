import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1030))
s.listen()

def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1

while True:
    connection, address = s.accept()
    try:
        n = connection.recv(2)
        n = struct.unpack("!H", n)[0]
        
        a = []
        
        for i in range(n):
            x = connection.recv(2)
            x = struct.unpack("!e", x)[0]
            a.append(round(x, 2))

        mergeSort(a)
        print(n)
        print(a)

    finally:
        connection.close()