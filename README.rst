Communication pathways in tissues between cells of equal nuclear masses developed
##############
Author: Jakub Jankowski, Poznan University of Technology
+++++++++

**Theory**

* User provides the number of cells in the tissue, start and end points, and the mass to be assumed by the path between the given points.
* Then program creates a graph representing the tissue, where the boundary neighborhood is additionally implemented, meaning - closing the system into a torus so that each vertex (cell) has 6 neighbors.
* Program losuje masę dla wszystkich wierzchołków zgodnie z rozkładem Gaussa, z wyjątkiem dwóch podanych przez użytkownika(początkowego i końcowego).
* Program randomizes the mass for all vertices according to the Gaussian distribution, except for two specified by the user (initial and final)
* An adjacency list is created. On its basis, the program creates a path from the starting point, where in each subsequent iteration the value of all vertices is changed, except for those that are in the path and have the same mass as the one given by the user.

.. image:: https://cdn.discordapp.com/attachments/885201652305494020/1135498024836145192/hipoteza.png
*problem visualization*


++++++++++
Example solution
++++++++++

**Graph representation of cells connection**

* A hexagonal mesh is created with each vertex representing one cell.
* Each vertex. which is not on the edge of the grid has 6 neighbors.
* Next, we create a torus closing the entire system, so that each vertex has exactly 6 neighbors.

.. image:: https://cdn.discordapp.com/attachments/885201652305494020/1135498045556011010/torus.png
*solution visualization*

.. image:: https://cdn.discordapp.com/attachments/885201652305494020/1135498057488814130/torus2.png
*app wisualization screenshot*
