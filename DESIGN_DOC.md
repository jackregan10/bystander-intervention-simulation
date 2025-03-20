# Design Document
## Authors: 
Jack Regan

### Design Features
* Utility Functions (UtilityFunctions Class)
  * Helper class for the main routine. Also communicates with WriteFile when math is needed for output
    statements.


* File Reading and Data Configuration (ReadFile Class)
  * Reads input file with data pertaining to simulation.


* File Writing and Data Output (WriteFile Class)
  * Writes csv with output data.


* Simulation (Model Class)
  * Contains main routine of simulation. Takes in parameters representing Agents in a data structure that
    contains their individual parameters and a count variable describing the number of iterations to
    be run.


* Driver (Driver Class)
  * Initializes all classes and translate information between file objects and model.

* Agent (Agent Class)
  * Holds state for all parameters of the agent

* Input Data (.csv)
  * The desired number of agents in a simulation (how many "people" are in an envrionemtn)
  * The desired number of times to run a rountine in order to generalize randomness (tentatively 1000)
  * Intervention Threshold, single routine (tentatively 50%)
  * Intervention Threshold, ammoratized rountines (tentatively 50%)
  * Min External Pressure
  * Max External Pressure
  * External Pressure Increment



