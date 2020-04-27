# /**
#  * @author Kotoz
#  * @email mohamed.t.elshetry@mail.com
#  * @create date 2020-04-24 07:23:29
#  * @modify date 2020-04-24 07:23:29
#  * @desc [description]
#  */
def max_heapfy(A, i):
    left_child = (2*i) +1
    right_child = (2*i) + 2

    if left_child < len(A) and A[left_child] > A[i]  :
        largest = left_child
    else:
        largest = i

    if right_child < len(A) and A[right_child] > A[largest] :
        largest = right_child

    if largest != i:
        temp = A[i]
        A[i] = A[largest]  
        A[largest] = temp
        max_heapfy(A, largest)

def build_max_heap(A):
    heap_size = len(A)
    for i in range((heap_size//2) , -1, -1):
        max_heapfy(A, i)

def heap_sort(A):
    build_max_heap(A)
    for i in range(len(A)-1, -1, -1):
        
        temp = A[len(A)-1]
        A[len(A)-1] = A[i]
        A[i] = temp 

        A = A[:-1]
        max_heapfy(A, i)

a = [1, 3, 0, 5, 2, 4 , 6, 4, 7]
heap_sort(a)
print(a)
     


