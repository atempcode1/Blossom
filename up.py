import mechanize
from  private import *

def huabanlogin(email,password):
    
    # Fire up a browser using mechanize
    br = mechanize.Browser()
    
    # Browse to the login page
    br.open('http://huaban.com/login/')
    
    # Enter the username and password into the login form
    isLoginForm = lambda l: l.action == "https://huaban.com/auth/" and l.method == "POST"
    
    try:
        br.select_form(predicate=isLoginForm)
    except:
        print("Unable to find login form.");
        exit(1);
    
    print br.form
    br.form.set_value(email, "email")
    br.form.set_value(password, "password")

    # Send the form
    response = br.submit()
    print response.read()

huabanlogin(email, password)    