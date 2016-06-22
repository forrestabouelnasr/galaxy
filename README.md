# galaxy simulator

This code will simulate a galaxy of stars interacting gravitationally. To run the galaxy simulator, use python to execute the file program1.py, like this:

python program1.py

To change what happens in the simulation, you can:

1. change the amount of simulation time between calculations, change the amount of simulation time between visualization frames, change the start/end times of the simulation, or change the number of stars, in program1.py lines 8-12
2. change the way the visualization works in visualization_methods.py . The parts dealing with the variables "camera" and "orientation" are experimental (and possibly broken)
3. modify the way that gravitational force is calculated in the file simulation_methods.py

TO DO: 

1.  add "Particle - In - Cell" (PIC) functionality or similar
    * Reduce the number of two-body interaction calculations from O(N^2).
2.  add variable time-step algorithms. the "dt" might vary over time and/or between objects
3.  add perspective 3D imagery. See:
    * http://www.dreamincode.net/forums/topic/239174-3d-perspective-projection/
    * http://stackoverflow.com/questions/23472048/projecting-3d-points-to-2d-plane
    * http://www.3dgep.com/understanding-the-view-matrix/#The_Camera_Transformation
    * https://en.wikipedia.org/wiki/Camera_matrix
    * https://en.wikipedia.org/wiki/3D_projection
