import random
import pandas as pd

from numpy import mean
from Agent import Agent

class Model:
    """
    A class to represent the simulation model for bystander intervention.

    Attributes
    agent_parameter : dictionary
        Dictionary containing parameters for the simulation.
    """
    def __init__(self, agent_parameter):
        self.iteration_count = 0
        self.intoxication_level = 0.0
        self.number_agents = int(agent_parameter["Agents"])
        self.number_simulations = int(agent_parameter["Simulations"])
        self.intoxication_level_increment = float(agent_parameter["Intoxication Level Increment"])
        self.loop_threshold = int(agent_parameter["Maximum Loop Iterations"])
        self.output_data = pd.DataFrame(
            {
                "Num Simulation": list(range(1, self.loop_threshold + 1)),
            }
        )

    def run_routine(self):
        """
        This method runs the routine of the model.
        """
        all_runs_data = []
        for _ in range(100):
            self.output_data = pd.DataFrame(
                {
                    "Num Simulation": list(range(1, self.loop_threshold + 1)),
                }
            )
            self.iteration_count = 0
            self.intoxication_level = 0.0
            for i in range(0, self.number_simulations):
                self.intoxication_level = self.intoxication_level_increment * i
                agent_list = []
                for k in range(0, self.number_agents):
                    agent_list.append(Agent())
                    agent_list[k].set_internal_pressure(
                            min(1.0, max(0.0, agent_list[k].get_internal_pressure() - self.intoxication_level))
                    )
                # Begin with first iteration of the simulation
                num_interventions = self.determine_agents_intervene(agent_list, i)
                self.print_output(agent_list, i)
                while num_interventions > 0 and self.iteration_count < self.loop_threshold:
                    self.iteration_count += 1
                    print(f"Running simulation: {self.iteration_count}")
                    # Calculate change in intoxication level
                    change = agent_list[k].get_internal_pressure() * (0.5 - num_interventions / self.number_agents) * 0.005
                    self.output_data.loc[self.iteration_count, f"{i} - Change"] = (change)
                    # Update intoxication level
                    self.intoxication_level = min(1.0, max(0.0, self.intoxication_level + change))
                    for k in range(0, self.number_agents):
                        agent_list[k].set_internal_pressure(
                            min(1.0, max(0.0, agent_list[k].get_internal_pressure() - self.intoxication_level))
                        )
                    # Determine if agents intervene
                    num_interventions = self.determine_agents_intervene(agent_list, i)
                    self.print_output(agent_list, i)
                self.output_data.loc[self.iteration_count, "---"] = (None)
                self.iteration_count = 0
            all_runs_data.append(self.output_data)
        averaged_data = pd.concat(all_runs_data).groupby(level = 0).mean()
        return averaged_data
    def determine_agents_intervene (self, agent_list, sim):
        """
        Determine if agents intervene.
        """
        num_interventions = 0
        for k in range(0, self.number_agents):
            if (
                agent_list[k].get_internal_pressure()
                >= random.random()
            ):
                num_interventions += 1
        self.output_data.loc[self.iteration_count, f"{sim} - Num Agents Intervene"] = (
            num_interventions
        )
        return num_interventions
    def print_output (self, agent_list, sim):
        """
        Updates the output data with the current simulation's 
        intoxication level and mean internal pressure.

        Parameters:
        agent_list (list): List of agent objects participating in the simulation.
        """
        self.output_data.loc[self.iteration_count, f"{sim} - Intoxication Level"] = (
            self.intoxication_level
        )
        self.output_data.loc[self.iteration_count, f"{sim} - Mean Internal Pressure"] = (
            mean([agent_list[k].get_internal_pressure() for k in range(0, self.number_agents)])
        )
        
