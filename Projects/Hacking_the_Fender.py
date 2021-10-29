import csv
import json

# We need to create a list of users whose passwords have been compromised, create a new list and save it to the variable compromised_users.
compromised_users = []


# Next we’ll need you to open up the file itself. Store it in a file object called password_file. 
# Create a for loop and save each row of the CSV into the temporary variable password_row.
# Inside your for loop, print out password_row['Username']. This is the username of the person whose password was compromised.
with open('passwords.csv') as password_file:
  password_csv = csv.DictReader(password_file)
  for password_row in password_csv:
    compromised_users.append(password_row['Username'])

print(compromised_users)

# Start a new with block, opening a file called compromised_users.txt. Open this file in write-mode, saving the file object as compromised_user_file.
with open('compromised_users.txt', 'w') as compromised_user_file:
  for users in compromised_users:
    compromised_user_file.write(users)

# Open a new JSON file in write-mode called boss_message.json. Save the file object to the variable boss_message.
# Create a Python dictionary object within your with statement that relays a boss message. Call this boss_message_dict.
# Give it a "recipient" key with a value "The Boss".
# Also give it a "message" key with the value "Mission Success".
# Write out boss_message_dict to boss_message using json.dump()
with open('boss_message.json', 'w') as boss_message:
  boss_message_dict = {
    "recipient": "The Boss",
    "message": "Mission Success"
  }
  json.dump(boss_message_dict, boss_message)

# Create a new with block and open "new_passwords.csv" in write-mode. Save the file object to a variable called new_passwords_obj.
# Write slash_null_sig to new_passwords_obj. Now we have the file to replace passwords.csv with!
with open('new_passwords.csv', 'w') as new_passwords_obj:
  slash_null_sig = """
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""
  new_passwords_obj.write(slash_null_sig)