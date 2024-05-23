import re
import subprocess
from Robustness_under_action_uncertainty_syn import robustness_U_A_U_S
from Robustness_under_initial_uncertainty import Robustness_U_I_U_S
from Initial_state_opacity_syn import Initial_s_o_s
from Current_state_opacity_syn import current_s_o_s
from Shortest_path_syn import shortest_p_s
from Service_Level_Agreement_synthesis import Service_Level_Agreement_Synthesis
from Non_Interference_syn import Non_Interference_Synthesis
from Linearizability_synthesis import Linearizability_Syn
from Mutation_Testing import Mutation_Testing_Synthesis
from Side_Channel_Timing_Attacks import Side_Channel_Timing_Attacks_Synthesis
from Observational_Determinism_synthessis import Observational_Determinism_Syn
def synthesis_method(Formula, choice,dts_file_location,method):
    formula = Formula

    count_symbols_array = ["E_", "F_"]

    total_count = 0
    for symbol in count_symbols_array:
        total_count += formula.count(symbol)
    """
    switch = {
        1: "shortest_path",
        2: "Robustness under initial uncertainty",
        3: "Robustness under action uncertainty",
        4: "Initial-state opacity",
        5: "Current-state opacity",
    }
    """
    if choice == 1:
        shortest_p_s(Formula,total_count,dts_file_location,method)
    if choice == 2:
        Robustness_U_I_U_S(Formula,total_count,dts_file_location,method)
    if choice == 3:
        robustness_U_A_U_S(Formula,total_count,dts_file_location,method)
    if choice == 4:
        Initial_s_o_s(Formula,total_count,dts_file_location,method)
    if choice ==5:
        current_s_o_s(Formula,total_count,dts_file_location,method)
    if choice == 6:
        Service_Level_Agreement_Synthesis(Formula, total_count, dts_file_location, method)
    if choice == 7:
        Non_Interference_Synthesis(Formula, total_count, dts_file_location, method)
    if choice == 8:
        Linearizability_Syn(Formula, total_count, dts_file_location, method)
    if choice == 9:
        Mutation_Testing_Synthesis(Formula, total_count, dts_file_location, method)
    if choice == 10:
        Side_Channel_Timing_Attacks_Synthesis(Formula, total_count, dts_file_location, method)
    if choice == 11:
        Observational_Determinism_Syn(Formula, total_count, dts_file_location, method)


