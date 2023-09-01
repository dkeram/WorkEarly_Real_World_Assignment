import os
import shutil
employee_list = ["Jasen_Kerluke", "Lazlo_Daniel", "Amparo_Schuster", "Tia_Kunde",  "Alana_Lueilwitz", 
                 "Tia_Mraz", "Lazlo_Metz", "Caroline_Pollich", "Aiyana_Weber", "Lazlo_Rolfson"]

#Task_1
def txt_creator(employee_list):
    for employee in employee_list:
        open(f"{employee}.txt", 'w+')
 
#Task_2
def frequent_first_names(employee_list):
    freq_first_names = {}
    new_employee_list = []
    
    for employee in employee_list:
        new_employee = employee.split('_')
        new_employee_list.append(new_employee[0])
    
    for employee in new_employee_list:
        counts = new_employee_list.count(employee)
        freq_first_names[employee] = counts
    
    sorted_freq_employee_fnames = dict(sorted(freq_first_names.items(), key=lambda x:x[1], reverse=True))
    most_freq_fnames = dict(list(sorted_freq_employee_fnames.items())[:5])
    
    print(most_freq_fnames)

#Task_3
def direction_creator_mover(employee_list):
    for employee in employee_list:
        first_letter = employee.split('_')[0][0].upper()
        folder_path = os.path.join(first_letter)
    
        if not os.path.exists(first_letter):
            os.makedirs(first_letter)
        
        original_file = f"{employee}.txt"
        destination_file = os.path.join(folder_path, f"{employee}.txt")
        shutil.move(original_file, destination_file)
    print("Files organized into folders.")
    
txt_creator(employee_list)
frequent_first_names(employee_list)
direction_creator_mover(employee_list)
