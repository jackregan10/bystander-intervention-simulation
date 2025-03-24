from numpy import integer, mean
import random
import pandas as pd

import Utility
from Agent import Agent


class Model:

    def __init__(self, agent_parameter):
        self.number_agents = int(agent_parameter["Agents"])
        self.number_simulations = int(agent_parameter["Simulations"])
        self.intoxication_level = 0.1

    def run_routine(self):
        """
        This method runs the routine of the model.
        """
        output_data = pd.DataFrame(
            {
                "Num Simulation": list(range(1, self.number_simulations + 1)),
                "Num Agents Intervene": [0.0] * self.number_simulations,
                "Change": [0.0] * self.number_simulations,
                "Intoxication Level": [0.0] * self.number_simulations,
                "Mean Internal Pressure": [0.0] * self.number_simulations
            }
        )
        agent_list = []
        for j in range(0, self.number_agents):
            agent_tuple = [Agent(), False]
            agent_list.append(agent_tuple)
        for f in range(0, self.number_simulations):
            print(f"Running simulation: {f}")
            output_data.loc[f, "Mean Internal Pressure"] = (
                mean([agent_list[k][0].get_internal_pressure() for k in range(0, self.number_agents)])
            )
            for k in range(0, 10):
                for k in range(0, self.number_agents):
                    if (
                        agent_list[k][0].get_internal_pressure()
                        >= random.random()
                    ):
                        agent_list[k][1] = True
                    else:
                        agent_list[k][1] = False
            num_interventions = 0
            for l in range(0, self.number_agents):
                if agent_list[l][1] is True:
                    num_interventions += 1
            output_data.loc[f, "Num Agents Intervene"] = (
                num_interventions
            )
            change = agent_list[k][0].get_internal_pressure() * (0.5 - num_interventions / self.number_agents) * 0.01
            output_data.loc[f, "Change"] = (
                change
            )
            self.intoxication_level = min(1.0, max(0.0, self.intoxication_level + change))
            output_data.loc[f, "Intoxication Level"] = (
                self.intoxication_level
            )
            for k in range(0, self.number_agents):
                agent_list[k][0].set_internal_pressure(
                    min(1.0, max(0.0, agent_list[k][0].get_internal_pressure() - self.intoxication_level))
                )
        return output_data
