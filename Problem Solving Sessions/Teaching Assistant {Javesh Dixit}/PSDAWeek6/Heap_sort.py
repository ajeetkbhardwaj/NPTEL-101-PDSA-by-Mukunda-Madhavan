
### Function checks the condition for max-heap for the given node 
### and also rearranges for that node.

def heapify(inp_seq, nodes, i):

	max_val_node = i
	lft_chld = 2*i + 1
	rgt_chld = 2*i + 2

	if lft_chld<nodes and inp_seq[max_val_node] < inp_seq[lft_chld]:

		max_val_node = lft_chld

	if rgt_chld<nodes and inp_seq[max_val_node] < inp_seq[rgt_chld]:

		max_val_node = rgt_chld

	if max_val_node != i:
		inp_seq[i], inp_seq[max_val_node] = inp_seq[max_val_node], inp_seq[i]

		heapify(inp_seq, nodes, max_val_node)


def heap_sort(inp_seq):
	nodes = len(inp_seq)
	#### Creating the max heap
	for i in range (nodes//2 -1, -1, -1):
		heapify(inp_seq, nodes, i)

	### replacing the root with ith element and 
	### again creating max heap with first i-1 elements
	for i in range (nodes-1, 0, -1):
		inp_seq[i], inp_seq[0] = inp_seq[0], inp_seq[i]
		heapify(inp_seq, i, 0)


def del_top_node(inp_seq):
	global nodes
	#### Creating the max heap
	for i in range (nodes//2 -1, -1, -1):
		heapify(inp_seq, nodes, i)

	last_elem = inp_seq[nodes-1]
	inp_seq[0] = last_elem
	inp_seq.pop(nodes-1)
	nodes=nodes-1
	for i in range (nodes//2 -1, -1, -1):
		heapify(inp_seq, nodes, i)

def insert_node(inp_seq, num):
	global nodes
	inp_seq.append(num)
	nodes = nodes+1
	for i in range (nodes//2 -1, -1, -1):
		heapify(inp_seq, nodes, i)


inp_seq = [3, 2, 12, 16, 2, 3, 23, 6, 12]
nodes = len(inp_seq)

for i in range (nodes//2 -1, -1, -1):
	heapify(inp_seq, nodes, i)

print('Creating heap bianary tree with given data', inp_seq)


inp_seq = [3, 2, 12, 16, 2, 3, 23, 6, 12]
nodes = len(inp_seq)

del_top_node(inp_seq)
print('Removing node of heap bianary tree with given data', inp_seq)



inp_seq = [3, 2, 12, 16, 2, 3, 23, 6, 12]
nodes = len(inp_seq)

heap_sort(inp_seq)

print('Sorting from max to min using heap sort', inp_seq)

insert_node(inp_seq, 56)
print('Adding node to heap bianary tree with given data', inp_seq)



# import random
# # inp_seq = random.sample(range(1, 10000000), 1000)
# nodes = len(inp_seq)
# print(inp_seq)
# print('\n\n\n')
# heap_sort(inp_seq)
# print(inp_seq)

# del_max(inp_seq)

# print('After Deletion', inp_seq)
