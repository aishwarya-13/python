# Get user email address
email = input('Enter your email: ').strip()
print(email)
# Slice out user name
username = email[:email.index('@')]
# Slice out domain name
domainname = email[email.index('@')+1:]
# Format message
output = "Your username is {} and domain name is {}".format(username, domainname)
# Display output message
print(output)


