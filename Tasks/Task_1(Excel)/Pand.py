# using Panda 

import pandas as pd

def read_data(file_name):
    return pd.read_excel(file_name)

def add_new_data(df):
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender: ")
    city = input("Enter City: ")

    new_data = {
        'Name': [name],
        'Age': [age],
        'Gender': [gender],
        'City': [city]
    }
    
    new_df = pd.DataFrame(new_data)
    return pd.concat([df, new_df], ignore_index=True)

def filter_data(df):
    age_filter = int(input("Enter the age filter: "))
    filtered_df = df[df['Age'] == age_filter]
    print("\nFiltered Data:")
    print(filtered_df)

# Read existing data from the Excel file into a DataFrame
df = read_data('Pand.xlsx')
print(df)

# Ask user if they want to add new data
add_new = input("Do you want to add new data? (yes/no): ")
if add_new.lower() == 'yes':
    df = add_new_data(df)
    df.to_excel('Pand.xlsx', index=False)
    print("New data has been added.")

# Ask user if they want to filter data
filter_data_option = input("Do you want to filter data? (yes/no): ")
if filter_data_option.lower() == 'yes':
    filter_data(df)