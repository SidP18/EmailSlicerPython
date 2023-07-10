# collect emails from the user
# split the email using the @ symbol, the first part as the user name, the second is the domain
# then we will split the domain using the . symbol
# ie whatsup@gmail.com turns into whatsup gmail com separately

def main():
    print("Welcome to the email slicer!")
    print("")

    email_input = input("Please enter your email address: ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)


while True:
    main()

