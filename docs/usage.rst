========
Usage
========

To use Gmail check for two step verification in a project::

    import GmailTwoStepVerificationBug as g
    g.check_email(email,password)
    
Result

    Two Step verification detected 
    This means we have detected two step verification on the email and if you try to login , the user will we notified with the sms containing sign-in code
    
