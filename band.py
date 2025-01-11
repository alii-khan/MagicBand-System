# ---------------

class MagicBandSystem:
    def __init__(self):
        self.registered_bands = []  # List of MagicBand objects
        self.parks = []            # List of Park objects
        self.guests = []

    def register_band(self, band):
        self.registered_bands.append(band)
        print(f"MagicBand {band.band_id} registered.")

    def get_band_info(self, band_id):
        for band in self.registered_bands:
            if band.band_id == band_id:
                return band
        print("MagicBand not found.")
        return None
    
    def get_guest_info(self, guest_id):
        return next((guest for guest in self.guests if guest.guest_id == guest_id), None)
    
    def add_guest(self, guest):
        self.guests.append(guest)

    def generate_usage_report(self):
        report = {
            "total_bands": len(self.registered_bands),
            "total_parks": len(self.parks),
        }
        return report


class MagicBand:
    def __init__(self, band_id, guest, balance):
        self.band_id = band_id
        self.guest = guest  # Reference to Guest object
        self.balance = balance
        self.current_location = None
        self.linked_tickets = []
        self.purchase_history = []

    def load_balance(self, amount):
        self.balance += amount
        print(f"${amount} added to MagicBand {self.band_id}. New balance: ${self.balance}")

    def use_band(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"${amount} deducted from MagicBand {self.band_id}. Remaining balance: ${self.balance}")
        else:
            print("Insufficient balance.")

    def update_location(self, latitude, longitude):
        self.current_location = (latitude, longitude)
        print(f"MagicBand {self.band_id} location updated to {self.current_location}.")

    def light_up(self, color):
        print(f"MagicBand {self.band_id} lights up in {color}.")

    def interact_with_element(self, element_id):
        print(f"MagicBand {self.band_id} interacted with element {element_id}.")


class Guest:
    def __init__(self, guest_id, name, age):
        self.guest_id = guest_id
        self.name = name
        self.age = age
        self.magic_band = None
        self.preferences = []

    def link_magic_band(self, band):
        self.magic_band = band
        print(f"MagicBand {band.band_id} linked to guest {self.name}.")

    def update_preferences(self, preferences):
        self.preferences = preferences
        print(f"{self.name}'s preferences updated: {preferences}")

    def get_profile_summary(self):
        return {
            "Guest ID": self.guest_id,
            "Name": self.name,
            "Age": self.age,
            "Preferences": self.preferences,
            "MagicBand ID": self.magic_band.band_id if self.magic_band else None
        }


class Park:
    def __init__(self, park_name):
        self.park_name = park_name
        self.rides = []
        self.elements = []
        self.shops = []
        self.restaurants = []

    def add_ride(self, ride):
        self.rides.append(ride)
        print(f"Ride {ride.ride_name} added to {self.park_name}.")

    def add_element(self, element):
        self.elements.append(element)
        print(f"Element {element.name} added to {self.park_name}.")

    def get_overview(self):
        return {
            "Park Name": self.park_name,
            "Number of Rides": len(self.rides),
            "Number of Elements": len(self.elements),
            "Number of Shops": len(self.shops),
            "Number of Restaurants": len(self.restaurants)
        }


class Ride:
    def __init__(self, ride_name, height_requirement, capacity):
        self.ride_name = ride_name
        self.height_requirement = height_requirement
        self.capacity = capacity
        self.queue = []  # List of MagicBand objects in the queue

    def add_to_queue(self, band):
        self.queue.append(band)
        print(f"MagicBand {band.band_id} added to the queue for {self.ride_name}.")

    def process_queue(self):
        if len(self.queue) == 0:
            print(f"No guests in the queue for {self.ride_name}.")
            return
        
        group = self.queue[:self.capacity]
        self.queue = self.queue[self.capacity:]  # Remove processed guests from the queue

        print(f"The following MagicBands are riding {self.ride_name}: {[band.band_id for band in group]}")

    def get_ride_info(self):
        return {
            "Ride Name": self.ride_name,
            "Height Requirement": self.height_requirement,
            "Capacity": self.capacity,
            "Queue Length": len(self.queue)
        }


class Transaction:
    def __init__(self, transaction_id, band_id, amount, item_description, location):
        self.transaction_id = transaction_id
        self.band_id = band_id
        self.amount = amount
        self.item_description = item_description
        self.location = location

    def record_transaction(self, band):
        band.purchase_history.append(self)
        print(f"Transaction {self.transaction_id} recorded for MagicBand {band.band_id}.")

    def get_transaction_details(self):
        return {
            "Transaction ID": self.transaction_id,
            "Band ID": self.band_id,
            "Amount": self.amount,
            "Item Description": self.item_description,
            "Location": self.location
        }


class Element:
    def __init__(self, element_id, name, interaction_type, location):
        self.element_id = element_id
        self.name = name
        self.interaction_type = interaction_type
        self.location = location
        self.interaction_log = []  # List of band_id for interactions

    def interact(self, band_id):
        self.interaction_log.append(band_id)
        print(f"MagicBand {band_id} interacted with {self.name}.")

    def get_interaction_summary(self):
        return {
            "Element ID": self.element_id,
            "Name": self.name,
            "Interactions": len(self.interaction_log),
            "Interaction Log": self.interaction_log
        }


import tkinter as tk
from tkinter import messagebox, simpledialog
import random

# class MagicBandUI:
#     def __init__(self, magic_band_system):
#         self.magic_band_system = magic_band_system
#         self.root = tk.Tk()
#         self.root.title("MagicBand Management System")
#         self.create_main_menu()

#     def create_main_menu(self):
#         """Create the main menu interface using grid layout."""
#         tk.Label(self.root, text="MagicBand Management System", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)

#         # Buttons for menu actions
#         tk.Button(self.root, text="Load Balance", command=self.load_balance_ui, width=20).grid(row=1, column=0, padx=10, pady=5)
#         tk.Button(self.root, text="Track Guest Location", command=self.track_guest_location_ui, width=20).grid(row=1, column=1, padx=10, pady=5)
#         tk.Button(self.root, text="View Ride Queue", command=self.view_ride_queue_ui, width=20).grid(row=2, column=0, padx=10, pady=5)
#         tk.Button(self.root, text="System Summary", command=self.show_system_summary, width=20).grid(row=2, column=1, padx=10, pady=5)
#         tk.Button(self.root, text="Exit", command=self.root.quit, width=20).grid(row=3, column=0, columnspan=2, pady=10)

#     def load_balance_ui(self):
#         """Interface for loading balance."""
#         window = tk.Toplevel(self.root)
#         window.title("Load Balance")

#         tk.Label(window, text="MagicBand ID:").grid(row=0, column=0, padx=5, pady=5)
#         band_id_entry = tk.Entry(window)
#         band_id_entry.grid(row=0, column=1, padx=5, pady=5)

#         tk.Label(window, text="Amount to Load:").grid(row=1, column=0, padx=5, pady=5)
#         amount_entry = tk.Entry(window)
#         amount_entry.grid(row=1, column=1, padx=5, pady=5)

#         def load_balance():
#             band_id = band_id_entry.get()
#             amount = amount_entry.get()
#             band = self.magic_band_system.get_band_info(band_id)
#             if not band:
#                 messagebox.showerror("Error", "Invalid MagicBand ID")
#                 return
#             try:
#                 amount = float(amount)
#                 band.load_balance(amount)
#                 messagebox.showinfo("Success", f"${amount:.2f} loaded to MagicBand {band_id}.")
#             except ValueError:
#                 messagebox.showerror("Error", "Invalid amount entered.")

#         tk.Button(window, text="Load", command=load_balance).grid(row=2, column=0, columnspan=2, pady=10)

#     def track_guest_location_ui(self):
#         """Interface for tracking guest location."""
#         window = tk.Toplevel(self.root)
#         window.title("Track Guest Location")

#         tk.Label(window, text="MagicBand ID:").grid(row=0, column=0, padx=5, pady=5)
#         band_id_entry = tk.Entry(window)
#         band_id_entry.grid(row=0, column=1, padx=5, pady=5)

#         def track_location():
#             band_id = band_id_entry.get()
#             band = self.magic_band_system.get_band_info(band_id)
#             if not band:
#                 messagebox.showerror("Error", "Invalid MagicBand ID")
#                 return
#             location = band.current_location
#             messagebox.showinfo("Location", f"MagicBand {band_id} is at location {location}.")

#         tk.Button(window, text="Track", command=track_location).grid(row=1, column=0, columnspan=2, pady=10)

#     def view_ride_queue_ui(self):
#         """Interface for viewing ride queues."""
#         window = tk.Toplevel(self.root)
#         window.title("View Ride Queue")

#         tk.Label(window, text="Ride Name:").grid(row=0, column=0, padx=5, pady=5)
#         ride_name_entry = tk.Entry(window)
#         ride_name_entry.grid(row=0, column=1, padx=5, pady=5)

#         def view_queue():
#             ride_name = ride_name_entry.get()
#             ride = next((r for r in self.magic_band_system.parks[0].rides if r.ride_name == ride_name), None)
#             if not ride:
#                 messagebox.showerror("Error", "Invalid Ride Name")
#                 return
#             queue = [band.band_id for band in ride.queue]
#             messagebox.showinfo("Ride Queue", f"Queue for {ride_name}: {', '.join(queue) if queue else 'No one in queue.'}")

#         tk.Button(window, text="View Queue", command=view_queue).grid(row=1, column=0, columnspan=2, pady=10)

#     def show_system_summary(self):
#         """Display system usage summary."""
#         summary = self.magic_band_system.generate_usage_report()
#         messagebox.showinfo("System Summary", summary)

#     def run(self):
#         """Run the tkinter main loop."""
#         self.root.mainloop()


# class MagicBandUI:
#     def __init__(self, magic_band_system):
#         self.magic_band_system = magic_band_system

#     def display_menu(self):
#         print("Welcome to the MagicBand Management System!")
#         print("1. Load Balance")
#         print("2. Track Guest Location")
#         print("3. View MagicBand Details")
#         print("4. System Summary")
#         print("5. Exit")

#     def handle_input(self, option):
#         if option == 1:
#             band_id = input("Enter MagicBand ID: ")
#             amount = float(input("Enter amount to load: "))
#             band = self.magic_band_system.get_band_info(band_id)
#             if band:
#                 band.load_balance(amount)
#         elif option == 2:
#             band_id = input("Enter MagicBand ID: ")
#             band = self.magic_band_system.get_band_info(band_id)
#             if band:
#                 print(f"Current location for MagicBand {band_id}: {band.current_location}")
#         elif option == 3:
#             band_id = input("Enter MagicBand ID: ")
#             band = self.magic_band_system.get_band_info(band_id)
#             if band:
#                 print(f"Details for MagicBand {band_id}:")
#                 print(band.__dict__)
#         elif option == 4:
#             summary = self.magic_band_system.generate_usage_report()
#             print("System Summary:")
#             print(summary)
#         elif option == 5:
#             print("Goodbye!")
#         else:
#             print("Invalid option.")

# magicbandsystem = MagicBandSystem()
# magicband = MagicBand()
# guest = Guest()
# park = Park()
# ride = Ride()
# transaction = Transaction()
# element = Element()
# magicbandui = MagicBandUI()


# Step 1: Import Necessary Classes (Assume already defined)
# from magic_band_system import MagicBandSystem, MagicBand, Guest, Park, Ride, MagicBandUI

# Step 2: Create the MagicBandSystem
# magic_band_system = MagicBandSystem()

# # Step 3: Add Parks
# disneyland = Park(park_name="Disneyland")
# magic_kingdom = Park(park_name="Magic Kingdom")

# magic_band_system.parks.extend([disneyland, magic_kingdom])

# # Step 4: Add Rides to Parks
# space_mountain = Ride(ride_name="Space Mountain", height_requirement=120, capacity=10)
# pirates_of_caribbean = Ride(ride_name="Pirates of the Caribbean", height_requirement=100, capacity=15)

# disneyland.add_ride(space_mountain)
# disneyland.add_ride(pirates_of_caribbean)

# # Step 5: Create Guests and MagicBands
# guest_1 = Guest(guest_id="G001", name="Alice", age=25)
# guest_2 = Guest(guest_id="G002", name="Bob", age=30)

# magic_band_1 = MagicBand(band_id="MB001", guest=guest_1, balance=100.0)
# magic_band_2 = MagicBand(band_id="MB002", guest=guest_2, balance=50.0)

# guest_1.link_magic_band(magic_band_1)
# guest_2.link_magic_band(magic_band_2)

# magic_band_system.register_band(magic_band_1)
# magic_band_system.register_band(magic_band_2)

# # Step 6: Assign MagicBands to Guests
# guest_1.update_preferences(["Space Mountain", "Vegetarian Food"])
# guest_2.update_preferences(["Pirates of the Caribbean", "Non-Vegetarian Food"])

# # Step 7: UI Setup and Launch
# ui = MagicBandUI(magic_band_system)
# ui.run()

class MagicBandUI:
    def __init__(self, magic_band_system):
        self.system = magic_band_system
        self.root = tk.Tk()
        self.root.title("MagicBand Management System")
        self.root.geometry("400x400")  # Set window size
        self.create_main_menu()

    def create_main_menu(self):
        """Main menu with categorized options."""
        tk.Label(self.root, text="MagicBand Management System", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)

        categories = [
            ("Manage Guests", self.manage_guests),
            ("Manage MagicBands", self.manage_bands),
            ("System Summary", self.show_system_summary),
            ("Exit", self.root.quit)
        ]

        # Center buttons in the grid
        for i, (label, command) in enumerate(categories):
            tk.Button(self.root, text=label, command=command, width=25).grid(row=i + 1, column=0, padx=20, pady=10, sticky="nsew")

        # Adjust column weight to center content
        self.root.columnconfigure(0, weight=1)

    # --------------------------- Category 1: Manage Guests ---------------------------

    def manage_guests(self):
        window = tk.Toplevel(self.root)
        window.title("Manage Guests")
        window.geometry("400x200")

        tk.Label(window, text="Manage Guests", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=10)

        tk.Button(window, text="Add New Guest", command=self.add_guest, width=25).grid(row=1, column=0, pady=5)
        tk.Button(window, text="View Guest Info", command=self.view_guest_info, width=25).grid(row=2, column=0, pady=5)

        window.columnconfigure(0, weight=1)

    def add_guest(self):
        name = simpledialog.askstring("Add Guest", "Enter Guest Name:")
        if not name:
            return
        try:
            age = int(simpledialog.askstring("Add Guest", "Enter Guest Age:"))
            guest_id = f"G{random.randint(1000, 9999)}"
            new_guest = Guest(guest_id, name, age)
            self.system.add_guest(new_guest)
            messagebox.showinfo("Success", f"Guest '{name}' added with ID {guest_id}.")
        except ValueError:
            messagebox.showerror("Error", "Invalid age entered.")

    def view_guest_info(self):
        guest_id = simpledialog.askstring("View Guest", "Enter Guest ID:")
        guest = self.system.get_guest_info(guest_id)
        if guest:
            info = f"Guest ID: {guest.guest_id}\nName: {guest.name}\nAge: {guest.age}"
            messagebox.showinfo("Guest Info", info)
        else:
            messagebox.showerror("Error", "Guest not found.")

    # --------------------------- Category 2: Manage MagicBands ---------------------------

    def manage_bands(self):
        window = tk.Toplevel(self.root)
        window.title("Manage MagicBands")
        window.geometry("400x250")

        tk.Label(window, text="Manage MagicBands", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=10)

        tk.Button(window, text="Create MagicBand", command=self.create_magic_band, width=25).grid(row=1, column=0, pady=5)
        tk.Button(window, text="Load Balance", command=self.load_balance, width=25).grid(row=2, column=0, pady=5)
        tk.Button(window, text="Track Location", command=self.track_location, width=25).grid(row=3, column=0, pady=5)

        window.columnconfigure(0, weight=1)

    def create_magic_band(self):
        guest_id = simpledialog.askstring("Create MagicBand", "Enter Guest ID:")
        guest = self.system.get_guest_info(guest_id)
        if guest:
            band_id = f"MB{random.randint(1000, 9999)}"
            magic_band = MagicBand(band_id, guest)
            guest.magic_band = magic_band
            self.system.register_band(magic_band)
            messagebox.showinfo("Success", f"MagicBand '{band_id}' created for Guest '{guest.name}'.")
        else:
            messagebox.showerror("Error", "Guest not found.")

    def load_balance(self):
        band_id = simpledialog.askstring("Load Balance", "Enter MagicBand ID:")
        band = self.system.get_band_info(band_id)
        if band:
            try:
                amount = float(simpledialog.askstring("Load Balance", "Enter amount to load:"))
                band.load_balance(amount)
                messagebox.showinfo("Success", f"${amount:.2f} loaded to MagicBand {band_id}.")
            except ValueError:
                messagebox.showerror("Error", "Invalid amount entered.")
        else:
            messagebox.showerror("Error", "MagicBand not found.")

    def track_location(self):
        band_id = simpledialog.askstring("Track Location", "Enter MagicBand ID:")
        band = self.system.get_band_info(band_id)
        if band:
            messagebox.showinfo("Location", f"MagicBand {band_id} is at location: {band.current_location}.")
        else:
            messagebox.showerror("Error", "MagicBand not found.")

    # --------------------------- Category 3: System Summary ---------------------------

    def show_system_summary(self):
        summary = f"Total Guests: {len(self.system.guests)}\nTotal MagicBands: {len(self.system.registered_bands)}"
        messagebox.showinfo("System Summary", summary)

    def run(self):
        self.root.mainloop()

# --------------------------- Main Program ---------------------------
if __name__ == "__main__":
    system = MagicBandSystem()
    app = MagicBandUI(system)
    app.run()