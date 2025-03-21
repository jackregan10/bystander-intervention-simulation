import pandas as pd

import Utility
from Agent import Agent


class Model:

    def __init__(self, agent_parameter):
        self.external_pressure = agent_parameter
        self.iterations = agent_parameter["Runs"]
        self.number_agents = agent_parameter["Agents"]
        self.number_simulations = Utility.determine_simulations(agent_parameter)
        self.intervention_threshold = agent_parameter["Intervention Threshold"]

    def run_routine(self):
        """
        This method runs the routine of the model.
        """
        output_data = pd.DataFrame(
            {
                "Num Simulation": list(range(1, self.iterations)),
                "Num Routine Iteractions": [self.iterations] * self.number_simulations,
            }
        )
        ammoratized_num_interventions = 0
        for f in range(0, self.number_simulations):
            for i in range(0, self.iterations):
                agent_list = []
                for j in range(0, self.number_agents):
                    agent_tuple = []
                    agent_tuple.append((Agent(), False))
                    agent_list.append(agent_tuple)
                for k in range(0, self.number_agents):
                    if agent_list[k][1] == False:
                        agent_list[k][0].set_internal_pressure(
                            agent_list[k][0].get_internal_pressure()
                            + self.external_pressure
                        )
                    if (
                        agent_list[k][0].get_internal_pressure()
                        >= self.intervention_threshold
                    ):
                        agent_list[k][1] = True
                    else:
                        agent_list[k][1] = False
                num_interventions = 0
                for l in range(0, self.number_agents):
                    if agent_list[l][1] == True:
                        num_interventions += 1
                if num_interventions > self.number_agents / 2:
                    ammoratized_num_interventions = 1
            output_data.loc[f, "Num Routine Iteractions"] = (
                ammoratized_num_interventions
            )
        return output_data
