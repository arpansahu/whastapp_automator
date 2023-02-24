import os

import pandas as pd

final_name_array = []
final_mob_no_array = []
member_count = 1
for file in os.listdir('/Users/arpansahu/projects/whastapp_automator/Contacts Sheet'):
    print(file)

    excel_data = pd.read_excel('/Users/arpansahu/projects/whastapp_automator/Contacts Sheet/' + file)

    saved_name_arr = excel_data['Saved Name']
    mob_no_arr = excel_data['WhatsApp Number(with country code)']
    for count in range(1, len(saved_name_arr) + 1):
        try:
            contact_name = saved_name_arr[count]
            mob_no = mob_no_arr[count]

            if '+' in contact_name:
                final_name_array.append(f'MCH MEMBER {member_count}')
                final_mob_no_array.append(mob_no)
                member_count += 1
        except Exception as e:
            print(e)

dict = {'First Name': final_name_array, 'Mobile Phone': final_mob_no_array}

df = pd.DataFrame(dict)

df.to_csv('file1.csv')
