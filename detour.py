import math
 
def distance(p1, p2):
    #To calculate distance between two points, given their x and y coordinates
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
 
 
def shorter_route(pA, pB, pC, pD):
    #To find shorter route : A -> C -> D -> B or C -> A -> B -> D
    
    #The solution in this case is to start and end at the route that is longer and include the smaller route as a detour
    #This is because distance from start to end points remains constant, only the new path is the extra distance travelled
    
    detour_diff = distance(pA, pB) - distance(pC, pD)
    if detour_diff <= 0:
        route = 'C -> A -> B -> D'
    else:
        route = 'A -> C -> D -> B'
    
    return route