import pandas as pd

# Define the DataFrame with the appropriate columns, including Balance
df = pd.DataFrame(columns=['Name', 'Email', 'Password', 'Balance'])

# Specify the filename
filename = 'user_credentials.xlsx'

# Use the ExcelWriter to save the DataFrame to an Excel file
with pd.ExcelWriter(filename, engine='openpyxl') as writer:
    df.to_excel(writer, index=False, sheet_name='Users')

print(f'Excel file "{filename}" has been created with a "Users" sheet.')
