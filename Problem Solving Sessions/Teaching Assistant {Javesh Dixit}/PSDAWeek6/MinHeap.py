def min_heapify(inp_seq, nodes, i):

    min_val_node = i
    lft_chld = 2*i + 1
    rgt_chld = 2*i + 2

    if lft_chld<nodes and inp_seq[min_val_node] > inp_seq[lft_chld]:

        min_val_node = lft_chld

    if rgt_chld<nodes and inp_seq[min_val_node] > inp_seq[rgt_chld]:

        min_val_node = rgt_chld

    if min_val_node != i:
        inp_seq[i], inp_seq[min_val_node] = inp_seq[min_val_node], inp_seq[i]

        min_heapify(inp_seq, nodes, min_val_node)


def min_heap_sort(inp_seq):
    global nodes 
    for i in range (nodes//2 -1, -1, -1):
        min_heapify(inp_seq, nodes, i)


    for i in range (nodes-1, 0, -1):
        inp_seq[0], inp_seq[i] = inp_seq[i], inp_seq[0]
        min_heapify(inp_seq, i, 0)

inp_seq = [3, 2, 12, 16, 2, 3, 23, 6, 12]
nodes = len(inp_seq)

for i in range (nodes//2 -1, -1, -1):
    min_heapify(inp_seq, nodes, i)

print('Creating heap bianary tree with given data', inp_seq)

min_heap_sort(inp_seq)
print('Sorting given data with heap sort', inp_seq)
