#Calculate the amplitude ratio

import numpy as np

def calculate_ratio(amp_a, amp_b) : 
    ratio = amp_a - amp_b
    return ratio

def ratio_only_assignment(IDs, Data_aud, Data_label, hop_length) : 

    USVs = {}
    USV_meds = {}
    ratio_set = {}
    assign_set = {}
    amplitude = {}

    for ID_1 in IDs : 
        assign_set[ID_1] = []
        for label in Data_label[ID_1] : 
            onset_idx = label[0] // hop_length
            offset_idx = label[1] // hop_length
            
            for ID_2 in IDs : 
                amplitude[ID_2] = Data_aud[ID_2]["amplitude"]
                USVs[ID_2] = amplitude[ID_2][:, onset_idx:offset_idx]
                USV_meds[ID_2] = np.median(USVs[ID_2])

                ratio = 0
                max_amp = max(USV_meds.values())

                winners = [
                    ID for ID, amp in USV_meds.items()
                    if amp == max_amp
                ]

                if len(winners) == 1:
                    assign = winners[0]
                else:
                    assign = "unassigned"

                assign_set[ID_1].append(assign)

                Data_aud[ID_1]["label_assign"] = assign_set[ID_1]
        
    return Data_aud
                

        

