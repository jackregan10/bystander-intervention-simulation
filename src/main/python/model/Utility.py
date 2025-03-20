def determine_iterations(agent_parameter):
    """
    This function determines the number of iterations of the model.
    """
    iterations = (agent_parameter["Maximum External Pressure"] - agent_parameter["Minimum External Pressure"]) / agent_parameter["Externam Pressure Increment"]
    return iterations