import heapq

queue = list()
graph_data = [[2,'A'],[5,'B'],[3,'C']]

# for edge in graph_data:
#     heapq.heappush(queue, edge)

# for index in range(len(queue)):
#     print(heapq.heappop(queue))

heapq.heapify(graph_data)

for index in range(len(graph_data)):
    print(heapq.heappop(graph_data))
    