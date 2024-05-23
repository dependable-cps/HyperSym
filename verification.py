from Robustness_under_initial_uncertainty_verification import Robustness_U_I_U_V
from Robustness_under_action_uncertainty_verification import robustness_U_A_U_V
from Shortest_path_verification import shortest_p_v
from Current_state_opacity_verification import current_s_o_v
#from Initial_s_o_v import Initial_s_o_verifi
from Initial_state_opacity_verification import Initial_s_o_v
from Service_Level_Agreement_Verification import Service_Level_Agreement_Verifi
from Non_Interference_Verification import Non_Interference_verifi
from Linearizability_Verifiaction import Linearizability_Verifi
from Mutation_Testing_Verification import Mutation_Testing_Verifi
from Side_Channel_Timing_Attacks_Verification import Side_Channel_Timing_Attacks_Verifi
from Observational_Determinism_Verification import Observational_Determinism_Verifi
def verification_method(Formula, choice,dts_file_location,method):
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
        6: "Non-Interference",
        7: "Linearizability",
        8: "Mutation Testing",
        9: "Side-Channel Timing Attacks",
        10: "Observational Determinism",
        11: "Service Level Agreement"
    }
    """
    if choice == 1:
        shortest_p_v(Formula,total_count,dts_file_location,method)
    if choice == 2:
        Robustness_U_I_U_V(Formula, total_count, dts_file_location, method)
    if choice == 3:
        robustness_U_A_U_V(Formula,total_count,dts_file_location,method)
    if choice == 4:
        Initial_s_o_v(Formula,total_count,dts_file_location,method)
    if choice ==5:
        current_s_o_v(Formula,total_count,dts_file_location,method)
    if choice ==6:
        Service_Level_Agreement_Verifi(Formula, total_count, dts_file_location, method)
    if choice==7:
        Non_Interference_verifi(Formula, total_count, dts_file_location, method)
    if choice==8:
        Linearizability_Verifi(Formula, total_count, dts_file_location, method)
    if choice == 9:
        Mutation_Testing_Verifi(Formula, total_count, dts_file_location, method)
    if choice==10:
        Side_Channel_Timing_Attacks_Verifi(Formula, total_count, dts_file_location, method)
    if choice==11:
        Observational_Determinism_Verifi(Formula, total_count, dts_file_location, method)

