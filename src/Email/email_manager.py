# stolen code from 'kiteco/python-youtube-code' 

import smtplib 

# API key
api_file = open("api-key.txt", "r")
api_key = api_file.readline()
api_file.close()

# email constraints
sender = "..."    
recipient = "..."       
subject = "Sick Day"   
message = "Hi Team,\n\nSorry, but I can't make it into work today."

# get sender password
password_file = open("password.txt", "r")
password = password_file.readline()
password_file.close()

# creates SMTP session 
mailServer = smtplib.SMTP("smtp.gmail.com", 587) 
  
# start TLS for security 
mailServer.starttls() 
  
# authentication 
mailServer.login(sender, password) 
print("Email login successfull")
  
# sending the mail 
mailServer.sendmail(sender, recipient, message)
print("Email send successfull")
 
# terminating the session 
mailServer.quit() 

# success message
print("\nSuccessfully sent a sick-day email to", recipient, "since the travel time was too long")