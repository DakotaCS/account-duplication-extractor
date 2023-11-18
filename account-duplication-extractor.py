# import pandas
import pandas as pd

# Input SSO data and AOP data
user_info_df = pd.read_csv('user_info_accounts.csv')
emails_df = pd.read_csv('email_accounts.csv')

# Empty list to store matching data rows
output_rows = []

# List to store indices of matching rows in user_info_df
matched_indices = []

# Iterate through user_info_df rows
for index, user_info_row in user_info_df.iterrows():
    email_to_match = user_info_row['email']

    # Check if the email exists in emails_df
    matching_rows = emails_df[emails_df['email'] == email_to_match]

    # If there is a match, add it to the output list and record the index
    if not matching_rows.empty:
        output_rows.append(matching_rows)
        matched_indices.append(index)

# Create a DataFrame from the list of matching rows
output_df = pd.concat(output_rows)

# Save the output df to a csv
output_df.to_csv('output.csv', index=False)

# Remove the matched rows from user_info_df
user_info_df = user_info_df.drop(matched_indices)

# Save the modified user_info_df (without the matched rows) back to user_info.csv
user_info_df.to_csv('aop_user_accounts.csv', index=False)
