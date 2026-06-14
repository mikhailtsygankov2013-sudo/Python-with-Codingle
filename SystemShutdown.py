def shutdown():
    """
    Function to handle system shutdown with user confirmation.
    Checks user input and displays appropriate messages.
    """
    print("Do you want to shutdown the system? (Yes/No)")
    user_input = input("Enter your choice: ").strip()
    
    if user_input.lower() == "yes":
        print("Shutting down...")
    elif user_input.lower() == "no":
        print("Abort shutdown")
    else:
        print("Sorry.")

shutdown()