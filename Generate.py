import random
import time

timestart = time.time() 
vertix = int()
array = int()
C1 = list()
temp = list()
checked = list()
# Cg = list([],[],[],[],[],[],[],[],[],[],[],[],[],[])
nCg = int()
n2 = int()
x = int()
tim = True
Graph_Matrix = list([[],[],[],[],[],[],[],[],[],[]]) # Here we put 10 arrays/matricies as a representation for the 10 verticies
c_graphs = list()
def generate():
    global tim
    while tim: 
        global Graph_Matrix

        #Now we have the list of matrices which is empty, we need to fill each with 10 
        # different random numbers between 1 and zero (0), because we can 't have a number more than that 
        # as long as we are generating a simple undirected graph with no loops or multible edges.

        array_numb = int(0)
        vert_numb = int(0)
        for i in range(100):
            if vert_numb == array_numb:
                Graph_Matrix[array_numb].append(0)
            else:
                Graph_Matrix[array_numb].append(random.randint(0, 1))
            vert_numb += 1
            if vert_numb == 10 :
                vert_numb = int(0)
                array_numb += 1
            if array_numb == 10:
                break

        n1 = int(-1)
        n2 = int()

        for array in range (10):
            n2 = 0 
            n1 += 1
            for vertix in range(10):
                if Graph_Matrix[n1][n2] == 0 and Graph_Matrix[n2][n1] == 1:
                    Graph_Matrix[n1][n2] = 1
                    n2 += 1
                elif Graph_Matrix[n1][n2] == 1 and Graph_Matrix[n2][n1] == 0:
                    Graph_Matrix[n2][n1] = 1
                    n2 += 1
                else:
                    n2 += 1
                    pass

            

        print (f"The Adjecency martix of our randomly generated graph is as the following")    
        for i in Graph_Matrix: 
            print (i)    

        # Graph_Matrix = [[0, 0, 1, 1, 0], [0, 0, 1, 1, 0], [1, 1, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        # Graph_Matrix = [[0, 0, 0, 1, 0], [0, 0, 1, 0, 1], [0, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        # Graph_Matrix = [[0, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 1, 0], [0,0,1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        # for i in Graph_Matrix: 
        #     print (i)  

        

        def other_components():
            global array, vertix, C1, checked, temp, x

            
            for num in range(10):
                try:
                    if C1[-1] != "sep" :
                        C1.append("sep")
                except BaseException:
                    C1.append("sep")
                if x in checked and x < 9:
                    x+=1
                elif x not in checked and x < 9:
                    array = x 
                    C1.append(array)
                    checked.append(x)
                    first_component(array)
                    x += 1
                elif x == 9 and x not in checked:
                    array = x 
                    C1.append(array)
                    first_component(array)
                    break
                elif x == 9 and x in checked: 
                    break
            


        def first_component(line):
            global array, vertix, C1, checked, temp, n2, tim

            loop = True

            while loop == True:
                
                vertix = 0
                for i in Graph_Matrix[line]:
                    
                    if i == 0: 
                        vertix += 1
                        pass
                    elif i == 1 and vertix < 9 and vertix not in checked and vertix != C1[-2]:
                        if Graph_Matrix[vertix][C1[-1]] == 1:
                            C1.append(vertix)
                        temp.append(vertix)
                        vertix += 1
                    elif i == 1 and vertix < 9 and (vertix in checked or vertix == C1[-2]):
                        # C1.append(vertix)
                        vertix += 1
                    elif i == 1 and vertix == 9 and vertix not in checked and vertix != C1[-2]:
                        C1.append(vertix)
                        temp.append(vertix)
                        # checked.append(line)
                    elif i == 1 and vertix == 9 and (vertix in checked or vertix == C1[-2]) :
                            # checked.append(temp[0])
                            # del temp[0]
                            pass
                    elif i == 0 and vertix == 9 and vertix in checked:
                        # checked.append(line)
                        pass
            
                if temp == []:
                    loop = False
                else:
                    pass
                
                for i1 in range(len(temp)):
                    vertix = 0
                    for num in Graph_Matrix[temp[0]]:
                        if num == 0 and vertix < 9: 
                            vertix += 1
                            pass
                        elif num == 1 and vertix < 9 and vertix != C1[-2] and vertix not in checked:
                            if vertix not in checked:
                                if vertix not in temp:
                                    temp.append(vertix)
                            if vertix != C1[-1] and temp[0] == C1[-1]:
                                C1.append(vertix)
                            elif vertix != C1[-1] and temp[0] != C1[-1] and temp[0] != C1[-2]:
                                C1.append(temp[0])
                                C1.append(vertix)
                            vertix += 1
                        elif num == 1 and vertix < 9 and (vertix in checked or vertix == C1[-2]) :
                            # C1.append(vertix)
                            vertix += 1
                            # if vertix not in checked:
                            #     checked.append(vertix)
                            # del temp[i1]
                        elif num == 1 and vertix == 9 and (vertix in checked or vertix == C1[-2]) :
                            checked.append(temp[0])
                            del temp[0]
                            n2 = True
                        elif (num == 1  and vertix == 9) and (vertix != C1[-2] and vertix not in checked):
                            if vertix not in C1:
                                temp.append(vertix)
                            if vertix != C1[-1] and temp[0] == C1[-1] :
                                C1.append(vertix)
                            elif vertix != C1[-1] and temp[0] != C1[-1] and temp[0] != C1[-2]:
                                C1.append(temp[0])
                                C1.append(vertix)
                                
                            checked.append(temp[0])
                            del temp[0]
                            n2 = True
                        elif (num == 0 ) and (vertix == 9):
                            checked.append(temp[0])
                            del temp[0]
                            n2 = True
                    
                        # if vertix == 4 and n2 == True:
                        #     try:
                        #         if temp[0] not in checked:
                        #             checked.append(temp[0])
                        #     except BaseException:
                        #         pass
                            
                        #     try:
                        #         del temp[0]
                        #     except BaseException:
                        #         pass
                        #     n2 = False
                                
                            
                        if temp == []:
                            loop = False
                            other_components()
                        else:
                            
                            if 1 in checked and 2 in checked and 3 in checked and 4 in checked and 5 in checked and 6 in checked and 7 in checked and 8 in checked and 9 in checked and 0 in checked:
                                loop = False
                                other_components()
                                break
                            pass
                    


        other_components()
        global c_graphs
        # print(C1)
        # print(checked)
        # print(temp)

        c_graphs = list()
        n1 = int()
        n2 = int()
        n3 = int()
        l = True
        component_num = int()
        temp_list = list()
        del C1[0]


        for g in C1:
            l = True
            count = int()
            if g != 'sep':
                temp_list.append(g)
            else:
                while l == True :
                    for i in temp_list:
                        n2 = int()
                        
                        if Graph_Matrix[i][temp_list[n2+1]] == 1 and Graph_Matrix[temp_list[n2+1]][i] == 1:
                            count +=1
                            if count == len(temp_list)-1:
                                l = False
                                break
                            else:
                                n2+=1
                                pass
                        elif Graph_Matrix[i][temp_list[n2+1]] != 1 or Graph_Matrix[temp_list[n2+1]][i] != 1:
                            n2 = int()
                            temp_list.remove(i)
                            for t in range(len(temp_list)+1):
                                if time.time()- timestart > 3:
                                    break
                                temp_list.insert(t, i)
                                if Graph_Matrix[i][temp_list[n2+1]] == 1 and Graph_Matrix[temp_list[n2+1]][i] == 1:
                                    n2+=1
                                    break
                                elif Graph_Matrix[i][temp_list[n2+1]] != 1 or Graph_Matrix[temp_list[n2+1]][i] != 1:
                                    n2+=1
                                    pass
                        if n2 >= len(temp_list)-1:
                            l = False
                            break
                component_num += 1
                # print(f"The component number {component_num} is : {temp_list}")
                c_graphs.append(temp_list)
                temp_list = list()
                print(f"We have {component_num} components/connected graphs in our main graph and they are as the following: ")
                g_num = int()
                for k in c_graphs:
                    g_num += 1
                    print(f"The component number {g_num} is : {k}")
                    tim = False
                if time.time()- timestart > 3:
                    print("Something wrong happend with the graph, please rerun the programme")


    ########################################


generate()


