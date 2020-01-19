"""Scaffold Topology Correlation Modeling
A Polaris Research Assignment for Natalia Patritti-Cram


In this assignment, we will explore the properties of a randomly generated DNA scaffold. To represent the scaffold in our program, we will
generate a random 3D-polygon in which the sides are allowed to overlap, which we will show in a plot.
The goal of the modeling is to produce a distribution of the correlation between the vertices of the polygon.
If there is time, we will construct a model which adds a constrained section of the polygon and get the correlation function for that."""




def make_scaffold(int perimeter)
    """ Input: perimeter (integer)
        output: scaffold (1D array)"""

    
    """We are going to make our scaffold by starting with a small square on a 3D-grid, represented by an array of vertices. Each vertex is assumed
    to be connected to its neighbors in the array.
    Then we will create the scaffold by randomly expanding the perimeter until the scaffold is large enough"""
    scaffold = [(0,0,0), (1,0,0), (1,1,0), (0,1,0)]
    current_perimeter =
    
    """The minimum perimeter is 4, and we are going to run into problems if the perimeter submitted is an odd number, so you should throw an error
    if either of these is a problem"""

    if perimeter ...
        print('The perimeter must be an even integer greater than 4...')
        
            """decide what to do here"""       
    
    """Now it is time to start expanding the scaffold. To do this we need to add perimeter until the total is reached
which means adding elements to the array. Continue by writing the expand_scaffold function below"""
    if current_perimeter < perimeter
        scaffold = expand_scaffold (scaffold)
        current_perimeter = 

def expand_scaffold (scaffold)
    """ Input: scaffold (1D array)
        Output: expanded_scaffold (1D array)

        To expand the scaffold, we need to pick an edge to expand it on and a direction to expand it in.
        Try drawing out this process on graph paper before coding it."""
    random_vertex_1 =
    random_vertex_2 =
    possible_directions = [(1,0,0), (0,1,0), (0,0,1), (-1,0,0), (0,-1,0), (0,0,-1)]
    """Then we need to insert two new vertices into the array in the direction we chose and in the right order"""
    expanded_scaffold = insert(...)
    return expanded_scaffold






""" Next we need a function that calculates the distance between each point and every other point in the scaffold.
The intput will be the scaffold and the output"""
def calculate_distances (scaffold)

    """ To do this, we're going to iterate (for loop) over the scaffold"""
    
    
