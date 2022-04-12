import heapq

# 타맥할 그래프와 시작 정즘을 인수로 전달받는다.
def dijkstra(graph, start, end):
    # 시작 점정에서 각 정점까지의 거리를 저장할 딕셔너리를 생성하고, 무한대(inf)로 초기화한다.
    distances = {vertex:[float('inf'), start] for vertex in graph}

    # 그래프의 시작 점정의 거리는 0으로 초기화 해준다
    distances[start] = [0, start]

    # 모든 정점이 저장될 큐를 생성
    queue = []

    # 그래프의 시작 정점과 시작 정점의 거리(0)를 최소힙에 넣어줌
    heapq.heappush(queue, [distances[start][0], start])

    while queue:
        # 큐에서 정점을 하나씩 꺼내 인접한 정점들의 가중치를 모두 확인하여 업데이트
        current_distance, current_vertex = heapq.heappop(queue)

        # 더 짧은 경로가 있다면 무시한다.
        if distances[current_vertex][0] < current_distance:
            continue

        for adjacent, weight in graph[current_vertex].items():
            distance = distances[current_vertex][0] + weight
            # 만약 시작 정점에서 인접 정점으로 바로가는 것 보다 현재 정점을 통해 가는것이 더 가까울 경우에는
            if distance < distances[adjacent][0]:
                # 거리를 업데이트 한다
                distances[adjacent] = [distance, current_vertex]
                heapq.heappush(queue, [distance, adjacent])
    
    path = end
    path_output = end + '->'
    while distances[path][1] != start:
        path_output += distances[path][1] + '->'
        path = distances[path][1]
    path_output += start
    print(path_output)
    return distances

mypgraph ={
    'A':{'B':8,'C':1,'D':2},
    'B':{},
    'C':{'B':5,'D':2},
    'D':{'E':3,'F':5},
    'E':{'F':1},
    'F':{'A':5}
}

print(dijkstra(mypgraph, 'A', 'F'))