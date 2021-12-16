from Generate import generate, Graph_Matrix, c_graphs

x = int()
circ_num = int()
test_graph = list()
circuits = list()
euler_c = bool()

def euler():
    global x, test_graph, circuits, circ_num, euler_c
    for array in Graph_Matrix:
        for i in array:
            x += i
        if x % 2:
            x = int()
            euler_c = True
            pass
        else:
            euler_c = False
            print("The Main graph doesn't have an euler circuit as one or more of the verticies has an odd degree...")
            break

    if euler_c == True:
        for graph in c_graphs: 
            for vertix in graph:
                if vertix not in test_graph:
                    test_graph.append(vertix)
                test_graph.append(test_graph[0])
                circuits.append(test_graph)

        print(f" We have {circ_num} Euler's circuits in the main graph, and they are as the following: ")
        y = int()
        for circ in circuits:
            y += 1
            print(f"The circuit number {y} is : {circ}")
