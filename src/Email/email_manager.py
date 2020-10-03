# stolen code from 'kiteco/python-youtube-code' 

import logging
try:
    import smtplib 
except:
    # TODO: Report error
    pass

logger = logging.getLogger(__name__)

class email():
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.port = None
        self.server = None

    def setupEmailServer(self, port):
        """
        Setup email server.
        """
        self.port = port
        return 

    def sendEmail(self, message, subject):
        """
        Send given email
        """
        return 

# # email constraints
# sender = "..."    
# recipient = "..."       
# subject = "Sick Day"   
# message = "Hi Team,\n\nSorry, but I can't make it into work today."

# # creates SMTP session 
# mailServer = smtplib.SMTP("smtp.gmail.com", 587) 
  
# # start TLS for security 
# mailServer.starttls() 
  
# # authentication 
# mailServer.login(sender, password) 
# print("Email login successfull")
  
# # sending the mail 
# mailServer.sendmail(sender, recipient, message)
# print("Email send successfull")
 
# # terminating the session 
# mailServer.quit() 

# # success message
# print("\nSuccessfully sent a sick-day email to", recipient, "since the travel time was too long")