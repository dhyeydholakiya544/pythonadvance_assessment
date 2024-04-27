# Import necessary modules
import pharmacy_management_system as pms  # Import module for pharmacy management system

def display_menu(role):
    """Display the menu based on user role."""
    if role == "admin":
        print("Admin Menu:")
        print("1. Register")
        print("2. Login")
        print("3. View All Managers")
        print("4. View All Medicines")
        print("5. Exit")
    elif role == "manager":
        print("Pharmacy Manager Menu:")
        print("1. Register")
        print("2. Login")
        print("3. Add Medicine")
        print("4. View Medicine")
        print("5. Delete Medicine")
        print("6. Exit")
    else:
        print("Invalid role")

def main():
    # Initialize the pharmacy management system
    pms.initialize()

    while True:
        role = input("Are you an Admin or Pharmacy Manager? (admin/manager): ").lower()

        if role == "admin":
            admin = pms.Admin()
            while True:
                display_menu("admin")
                choice = input("Enter your choice: ")

                if choice == "1":
                    admin.register()
                elif choice == "2":
                    admin.login()
                elif choice == "3":
                    admin.view_all_managers()
                elif choice == "4":
                    admin.view_all_medicines()
                elif choice == "5":
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif role == "manager":
            manager = pms.PharmacyManager()
            while True:
                display_menu("manager")
                choice = input("Enter your choice: ")

                if choice == "1":
                    manager.register()
                elif choice == "2":
                    manager.login()
                elif choice == "3":
                    manager.add_medicine()
                elif choice == "4":
                    manager.view_medicine()
                elif choice == "5":
                    manager.delete_medicine()
                elif choice == "6":
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice. Please try again.")

        else:
            print("Invalid role. Please try again.")

if __name__ == "__main__":
    main()
