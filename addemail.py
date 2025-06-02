import csv


def get_user_input():
    name = input("Enter name: ")
    email = input("Enter email: ")
    return name, email

# Function to write data to CSV file
def write_to_csv(name, email):
    with open('emails.csv', 'a', newline='') as csvfile:
        fieldnames = ['Name', 'Email']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write data to CSV file    
        writer.writerow({'Name': name, 'Email': email})


def search_receiver_name(csv_file, receiver_name ):
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['Name'] == receiver_name:
                return row['Email']
    return None

# Main program
if __name__ == "__main__":
    # Get user input
    name, email = get_user_input()

    # Write data to CSV file
    csv_file = 'emails.csv'
    write_to_csv(name, email)

    print("Data has been successfully added to the CSV file.")