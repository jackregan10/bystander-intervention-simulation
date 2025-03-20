import numpy as np
import pandas as pd

from Agent import Agent

class Model:
    
    def __init__ (self, agent_parameter):
        self.external_pressure = agent_parameter
        self.iterations = Utility.determine_iterations(agent_parameter)
        self.number_agents = agent_parameter["Agents"]
        self.intervention_threshold = agent_parameter["Intervention Threshold"]
        
    def run_routine(self):
        """
        This method runs the routine of the model.
        """
        output_data = pd.DataFrame({
            "Num Simulation": list(range(1, self.iterations))
        })
        ammoratized_num_interventions = 0
        for i in range(0, self.iterations):
            agent_list = []
            for j in range(0, self.number_agents):
                agent_tuple = []
                agent_tuple.append((Agent(), False))
                agent_list.append(agent_tuple)
            for k in range(0, self.number_agents):
                if agent_list[k][1] == False:
                    agent_list[k][0].set_internal_pressure(agent_list[k][0].get_internal_pressure() + self.external_pressure)
                if agent_list[k][0].get_internal_pressure() >= self.intervention_threshold:
                    agent_list[k][1] = True
                else:
                    agent_list[k][1] = False
            num_interventions = 0
            for l in range(0, self.number_agents):
                if agent_list[l][1] == True:
                    num_interventions += 1
            if num_interventions > self.number_agents / 2:
                ammoratized_num_interventions = 1
        output_data.loc[i, "Num Interventions"] = ammoratized_num_interventions
        