# gpssGUI
This GPSS Simulation Tool proposes an open-source version of the well-known discrete event simulator

It has the following functionalities:

1. Open GPSS file - a file dialogue is opened and the user should choose a .gps file.
The file is then loaded into the GPSS model editor (left part of the main screen);

2. Edit and/or correct the model directly in the GPSS model editor;

3. Save to file - saves the model to a model.gps file in the same folder as the GPSS Simulation Tool;

4. Start GPSS Simulation - Saves the model from the editor to a model.gps file and run the simulation;
 
The simulator uses the gpss.py module (A Python implementation of IBM’s General Purpose Simulation System).

For more information: https://github.com/martendo/gpss.py
Basic syntax and its peculiarity are online available at:
https://github.com/martendo/gpss.py/blob/master/docs/syntax.md
