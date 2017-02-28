'''
COMP3121 Assignment 1 Question2
Feb 15, 2017
Student Name: MA Mingyu
Student ID: 14110562D
'''

import networkx as nx
import math    #log function
import numpy as np #round function for truncating numbers to 2 decimal places
   
def in_out_degree(G,n):
   in_degree = G.in_degree(n)       #use networkx function to get in_degree directly
   out_degree = G.out_degree(n)     #use networkx function to get out_degree directly
   return [in_degree, out_degree]   #a list of in-degree and out-degree of node n, excluding loops


def closenessCentrality(G, n):
   result = 0                       #set initial result value
   for node in list(G.node):        #loop all other nodes in the graph
      if node != n :                #if the node is not itself
         if nx.has_path(G, n, node) == True: #make sure there are path between two nodes to avoid error
            d = nx.shortest_path_length(G, n, node) #use shortest_path_length function to get shortest path length
            result += 1/d           #calculate the result
   return round(result,2) #the closeness centrality of N in G (rounded to 2 decimal places)
         
def recommendNewFriends(G,n,k):
   topList = {}                     #define topList as a dictionary
   for node in list(G.node):        #loop all other nodes in the graph
      if node != n:                    #verify the node is not itself
         score = 0
         successors = G.successors(n)  #get all successors of original node
         predecessors = G.predecessors(node) #get all predecessors of loop node
         try:
            successors.remove(n)       #use two try to make sure the successors
         except:                       # and predecessors don't include original
            pass                       # node and loop node
          try:
            predecessors.remove(node)
         except:
            pass
         for common_neighbor in set(successors).intersection(predecessors): #loop all common friends between two nodes
            score += 1/math.log10(G.out_degree(common_neighbor)+1)    #calculate the score
         if score != 0 :
            topList[node] = round(score,2)
   topListSorted = sorted(topList.items(), key = lambda d: (-d[1], d[0]))  #sort twice to the dictionary
   return topListSorted[0:k] #a list of top k friend with their score for recommendation


#create the sample graph with sample test cases
def main():
   G = nx.DiGraph()
   G.add_edges_from([("A", "C"),("A", "D"), ("A", "D"),("B", "B"), 
            ("B", "A"), ("D", "B"), ("D", "E"),("C", "E"),("D", "F"),("E", "F")])
   print ("Number of nodes: %d, Number of edges: %d" %(len(G.nodes()),len(G.edges())))

   #test of closeness centrality function
   print ('\ncloseness centrality of A is ', closenessCentrality(G, "A"))
   print ('closeness centrality of D is ', closenessCentrality(G, "D"))
   print ('closeness centrality of E is ', closenessCentrality(G, "E"))
   print ('closeness centrality of F is ', closenessCentrality(G, "F"))

   #test of friend recommendation function
   print ('\nThe top 3 friends recommended to A: ', recommendNewFriends(G,'A', 3))
   print ('The top 2 friends recommended to A: ', recommendNewFriends(G,'A', 2))
   print ('The top 3 friends recommended to B: ', recommendNewFriends(G,'B', 3))
   print ('The top 3 friends recommended to F: ', recommendNewFriends(G,'F', 3)) 


if __name__ == "__main__":
   main()
   
