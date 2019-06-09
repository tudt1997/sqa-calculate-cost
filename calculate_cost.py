import pandas as pd
import numpy as np

table = pd.read_csv('table.csv')
print(table)

previous_faults = 0
total_cost = 0
result = np.empty((0, 2))

for index, row in table.iterrows():
    faults, cost_per_fault, detection_rate = row
    
    detected_faults = (previous_faults + faults) * detection_rate
    cost = detected_faults * cost_per_fault
    result = np.append(result, np.array([[detected_faults, cost]]), axis=0)
    
    previous_faults = previous_faults + faults - detected_faults

    total_cost += cost

result_table = pd.DataFrame(result, columns=['detect', 'cost'])
print(result_table)
print('Total cost: {}'.format(total_cost))