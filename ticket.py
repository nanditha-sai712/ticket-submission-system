from datetime import datetime

def submit_ticket():
    print("=== Ticket Submission ===")
    
    # Collect user input
    name = input("Enter your name: ")
    issue = input("Describe your issue: ")

    # Generate timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create a ticket dictionary
    ticket = {
        "Name": name,
        "Issue": issue,
        "Time Submitted": timestamp
    }

    # Save ticket to a text file
    with open("tickets.txt", "a") as file:
        file.write("Ticket Submitted:\n")
        for key, value in ticket.items():
            file.write(f"{key}: {value}\n")
        file.write("-" * 30 + "\n")

    print("✅ Ticket successfully submitted!")

# Run the function
submit_ticket()
