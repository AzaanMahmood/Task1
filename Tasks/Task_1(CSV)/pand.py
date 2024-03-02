import pandas as pd

def read_data():
    return pd.read_csv('pand.csv')

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
    df = pd.concat([df, new_df], ignore_index=True)
    df.to_csv('pand.csv', index=False)
    return df

def filter_data(df):
    age_filter = int(input("Enter the age filter: "))
    filtered_df = df[df['Age'] == age_filter]
    print("\nFiltered Data:")
    print(filtered_df)

df = read_data()
print(df)

add_new = input("Do you want to add new data? (yes/no): ")
if add_new.lower() == 'yes':
    df = add_new_data(df)
    print("New data has been added.")

filter_data_option = input("Do you want to filter data? (yes/no): ")
if filter_data_option.lower() == 'yes':
    filter_data(df)
