"""Scaffold Topology Correlation Modeling
A Polaris Research Assignment for Natalia Patritti-Cram


In this assignment, we will explore the properties of a randomly generated DNA scaffold. To represent the scaffold in our program, we will
generate a random 3D-polygon in which the sides are allowed to overlap, which we will show in a plot.
The goal of the modeling is to produce a distribution of the correlation between the vertices of the polygon.
If there is time, we will construct a model which adds a constrained section of the polygon and get the correlation function for that.

You can peruse the main function below, which will lay out the steps and then we'll program it in pieces."""

from matplotlib import pyplot as plt
import numpy as np
import math


def main()

perimeter =4 "default value"

scaffold = make_scaffold(perimeter)

{distances_array, counts_array} = calculate_correlation(scaffold)

plt.plot(distances_array, counts_array)

plt.xlabel("Distance")
plt.ylabel("Correlation")
plt.title('Correlation between points on random scaffold')
plt.show()


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
    while current_perimeter < perimeter
        scaffold = expand_scaffold (scaffold)
        current_perimeter = """how do you calculate perimeter from the scaffold object?"""
    return scaffold

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
The intput will be the scaffold and the point we want to calculate distances from (index) and the output is an array of distances to other points"""
def calculate_distances (scaffold, index)
    start = scaffold(index);
    """ To do this, we're going to iterate (for loop) over the scaffold"""
    scaffold_distances = []
    for i in scaffold
        endpoint = scaffold(i)
        """ we have the coordinates for both our points now, start and endpoint"""
        distance = """pythagorean theorem goes here"""
        scaffold_distances(i) = distance;
    end
    return scaffold_distances


    """ Now we're ready to write the function that calculates the correlation. We'll use the distances from each point to each other point to make the
spacial correlation distribution """
def calculate_correlation(scaffold)

    """Step one is that we need to apply calculate_distances to every point in the scaffold. This will give us a long array of distances between points."""
    distances_array = []
    for i in scaffold
        distances_array.extend( calculate_distances(scaffold, i) ) """the extend function will add our new array to the end of the old one"""
    end

    """Now we need to take those distances and sort them so we can make a plot with "distance" on the x-axis, turns out we can use the built-in method"""
    distances_array.sort()

    """This is the x-axis information of what we want to plot. At each of these points, we need to increase the count on our "histogram" by 1.
    We also need to handle duplicates; for example if we have 3 points which are all 4 units away: [4,4,4], we're going to want to condense those
    and just increase the count by 3 at x=4. At the end we should have an array of distances [distance 1, distance 2...] and an array of counts
    [number of points at distance 1, number of points at distance 2,...]"""
    counts_array = []
    last_count = 0
    for i in range(len(distances_array))
        if last_count = ??
            """if the last count is the same as this one, then we need to _continue_"""
            continue
        else
        
        """add to the count array"""
        counts_array.append(i)
        last_count = distances_array(i)
    end
    """Okay now we have our two arrays, counts_array (aka the y axis) and distances_array (x axis). Lets quickly normalize (scale values between 0 and 1)
the counts_array"""
    counts_array = counts_array / """put the maximum value of the counts_array here"""
    return {distances_array, counts_array}
