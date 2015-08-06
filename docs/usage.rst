========
Usage
========

To use Gmail check for two step verification in a project::

    import GmailTwoStepVerificationBug as g
    g.check_email(email,password)
    
Result::

    1) Two Step verification detected 
    
    This means we have detected two step verification on the email and if you try to login ,
    the user will we notified with the sms containing sign-in code.
    
    2) Incorrect Username or Password , Please provide correct username and password to test the account.
    
    This means the username or password supplied to the check_email() function is not valid . 
    
    3) Two step Verification not detected
    
    This means the user has not enabled the two step verification in his gmail account , the user will 
    not be notified by an sms containing sign-in code.   
