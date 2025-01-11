import tkinter as tk
from tkinter import ttk, messagebox

# Back-End Classes
class MagicBandSystem:
    def __init__(self):
        self.registered_bands = []
        self.parks = []
        self.band_counter = 0  # Counter for MagicBand IDs
        self.guest_counter = 0  # Counter for Guest IDs

    def generate_id(self, prefix, counter):
        """Generates a new ID with the given prefix and counter."""
        return f"{prefix}{counter:04d}"

    def register_band(self, band):
        self.registered_bands.append(band)

    def get_band_info(self, band_id):
        for band in self.registered_bands:
            if band.band_id == band_id:
                return band
        return None

    def register_new_guest(self, name, age):
        self.guest_counter += 1
        self.band_counter += 1

        guest_id = self.generate_id("G", self.guest_counter)
        band_id = self.generate_id("MB", self.band_counter)

        guest = Guest(guest_id, name, age)
        band = MagicBand(band_id, guest)
        guest.link_magic_band(band)

        self.register_band(band)
        return guest, band

    def purchase_park_tickets(self, band, park):
        band.purchase_park_ticket(park)

    def generate_usage_report(self):
        return "\n".join(f"Band {band.band_id}: {band.guest.name}" for band in self.registered_bands)


class MagicBand:
    def __init__(self, band_id, guest):
        self.band_id = band_id
        self.guest = guest
        self.current_location = None
        self.linked_tickets = []
        self.purchase_history = []

    def purchase_park_ticket(self, park):
        self.linked_tickets.append(park)

    def light_up(self, color):
        return f"Band lights up with {color} for {self.guest.name}"


class Guest:
    def __init__(self, guest_id, name, age):
        self.guest_id = guest_id
        self.name = name
        self.age = age
        self.magic_band = None

    def link_magic_band(self, band):
        self.magic_band = band


class Park:
    def __init__(self, park_name, latitude, longitude):
        self.park_name = park_name
        self.latitude = latitude
        self.longitude = longitude
        self.rides = []
        self.elements = []
        self.shops = []
        self.restaurants = []

    def add_ride(self, ride):
        self.rides.append(ride)

    def add_element(self, element):
        self.elements.append(element)

    def add_shop(self, shop):
        self.shops.append(shop)

    def add_restaurant(self, restaurant):
        self.restaurants.append(restaurant)

    def get_overview(self):
        return f"Park: {self.park_name}, Location: ({self.latitude}, {self.longitude})"


class Ride:
    def __init__(self, ride_name, height_requirement, capacity):
        self.ride_name = ride_name
        self.height_requirement = height_requirement
        self.capacity = capacity
        self.queue = []

    def add_to_queue(self, band):
        self.queue.append(band)

    def process_queue(self):
        if self.queue:
            self.queue.pop(0)

    def get_ride_info(self):
        return f"Ride: {self.ride_name}, Height Req: {self.height_requirement}, Capacity: {self.capacity}"


class Element:
    def __init__(self, element_id, name, interaction_type, location):
        self.element_id = element_id
        self.name = name
        self.interaction_type = interaction_type
        self.location = location
        self.interaction_log = []

    def interact(self, band):
        self.interaction_log.append(band.band_id)


class Restaurant(Element):
    def __init__(self, name, location):
        super().__init__(id(self), name, "Restaurant", location)
        self.menu = []

    def add_menu_item(self, item, price):
        self.menu.append((item, price))


class Store(Element):
    def __init__(self, name, location):
        super().__init__(id(self), name, "Store", location)
        self.items = []

    def add_item(self, item, price):
        self.items.append((item, price))


class Transaction:
    def __init__(self, transaction_id, band_id, amount, item_description, location):
        self.transaction_id = transaction_id
        self.band_id = band_id
        self.amount = amount
        self.item_description = item_description
        self.location = location

    def get_transaction_details(self):
        return f"Transaction {self.transaction_id}: {self.amount} for {self.item_description} at {self.location}"

import tkinter as tk
from tkinter import messagebox

class MagicBandUI:
    def __init__(self, root, system):
        self.root = root
        self.system = system

        self.root.title("MagicBand System")
        self.root.geometry("600x400")

        # Main Frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Create the Main Menu
        self.create_main_menu()

    def create_main_menu(self):
        """Creates the main menu with buttons for each feature."""
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        tk.Label(self.main_frame, text="MagicBand System", font=("Arial", 20)).pack(pady=10)

        # Menu Buttons
        menu_buttons = [
            ("Register Guest", self.show_register_guest_ui),
            ("Purchase Park Ticket", self.show_purchase_ticket_ui),
            ("Transactions", self.show_transaction_ui),
            ("Manage Rides", self.show_ride_ui),
            ("Track Guest Location", self.show_track_guest_ui),
        ]

        for text, command in menu_buttons:
            tk.Button(self.main_frame, text=text, command=command, width=25).pack(pady=5)

    def show_register_guest_ui(self):
        """UI for registering a guest."""
        self.switch_frame()
        tk.Label(self.main_frame, text="Register Guest", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.main_frame, text="Name:").pack()
        name_entry = tk.Entry(self.main_frame)
        name_entry.pack()

        tk.Label(self.main_frame, text="Age:").pack()
        age_entry = tk.Entry(self.main_frame)
        age_entry.pack()

        def register_guest():
            name = name_entry.get()
            age = age_entry.get()
            if not name or not age.isdigit():
                messagebox.showerror("Error", "Invalid input!")
                return
            guest, band = self.system.register_new_guest(name, int(age))
            messagebox.showinfo(
                "Success",
                f"Registered Guest: {guest.name}\nGuest ID: {guest.guest_id}\nBand ID: {band.band_id}",
            )
            self.create_main_menu()

        tk.Button(self.main_frame, text="Register", command=register_guest).pack(pady=10)
        tk.Button(self.main_frame, text="Back to Menu", command=self.create_main_menu).pack(pady=5)

    def show_purchase_ticket_ui(self):
        """UI for purchasing park tickets."""
        self.switch_frame()
        tk.Label(self.main_frame, text="Purchase Park Ticket", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.main_frame, text="Band ID (e.g., MB1234):").pack()
        band_id_entry = tk.Entry(self.main_frame)
        band_id_entry.pack()

        tk.Label(self.main_frame, text="Park Name:").pack()
        park_entry = tk.Entry(self.main_frame)
        park_entry.pack()

        def purchase_ticket():
            band_id = band_id_entry.get()
            park_name = park_entry.get()
            if not band_id.startswith("MB") or not park_name:
                messagebox.showerror("Error", "Invalid input!")
                return
            band = self.system.get_band_info(band_id)
            if not band:
                messagebox.showerror("Error", "Band not found!")
                return
            park = next((p for p in self.system.parks if p.park_name == park_name), None)
            if not park:
                messagebox.showerror("Error", "Park not found!")
                return
            self.system.purchase_park_tickets(band, park)
            messagebox.showinfo("Success", f"Ticket purchased for {park_name}")
            self.create_main_menu()

        tk.Button(self.main_frame, text="Purchase", command=purchase_ticket).pack(pady=10)
        tk.Button(self.main_frame, text="Back to Menu", command=self.create_main_menu).pack(pady=5)

    def show_transaction_ui(self):
        """UI for handling transactions (hotel booking, food, shopping)."""
        self.switch_frame()
        tk.Label(self.main_frame, text="Transactions", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.main_frame, text="Band ID (e.g., MB1234):").pack()
        band_id_entry = tk.Entry(self.main_frame)
        band_id_entry.pack()

        def create_transaction(type_):
            band_id = band_id_entry.get()
            if not band_id.startswith("MB"):
                messagebox.showerror("Error", "Invalid Band ID!")
                return
            band = self.system.get_band_info(band_id)
            if not band:
                messagebox.showerror("Error", "Band not found!")
                return
            if type_ == "hotel":
                messagebox.showinfo("Hotel", f"Hotel booked for Band ID {band_id}")
            elif type_ == "food":
                messagebox.showinfo("Food", f"Food purchased for Band ID {band_id}")
            elif type_ == "item":
                messagebox.showinfo("Store", f"Item purchased for Band ID {band_id}")
            self.create_main_menu()

        tk.Button(self.main_frame, text="Book Hotel", command=lambda: create_transaction("hotel")).pack(pady=5)
        tk.Button(self.main_frame, text="Buy Food", command=lambda: create_transaction("food")).pack(pady=5)
        tk.Button(self.main_frame, text="Buy Item", command=lambda: create_transaction("item")).pack(pady=5)
        tk.Button(self.main_frame, text="Back to Menu", command=self.create_main_menu).pack(pady=10)

    def show_ride_ui(self):
        """UI for managing rides (view/add to queue)."""
        self.switch_frame()
        tk.Label(self.main_frame, text="Manage Rides", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.main_frame, text="Ride Name:").pack()
        ride_entry = tk.Entry(self.main_frame)
        ride_entry.pack()

        tk.Label(self.main_frame, text="Band ID (e.g., MB1234):").pack()
        band_id_entry = tk.Entry(self.main_frame)
        band_id_entry.pack()

        def view_queue():
            ride_name = ride_entry.get()
            ride = next((r for p in self.system.parks for r in p.rides if r.ride_name == ride_name), None)
            if ride:
                queue = ", ".join(str(b.band_id) for b in ride.queue)
                messagebox.showinfo("Ride Queue", f"Queue for {ride_name}: {queue}")
            else:
                messagebox.showerror("Error", "Ride not found!")

        def add_to_queue():
            ride_name = ride_entry.get()
            band_id = band_id_entry.get()
            if not band_id.startswith("MB") or not ride_name:
                messagebox.showerror("Error", "Invalid input!")
                return
            band = self.system.get_band_info(band_id)
            ride = next((r for p in self.system.parks for r in p.rides if r.ride_name == ride_name), None)
            if band and ride:
                ride.add_to_queue(band)
                messagebox.showinfo("Success", f"Added Band ID {band_id} to {ride_name}")
            else:
                messagebox.showerror("Error", "Band or Ride not found!")

        tk.Button(self.main_frame, text="View Ride Queue", command=view_queue).pack(pady=5)
        tk.Button(self.main_frame, text="Add to Ride Queue", command=add_to_queue).pack(pady=5)
        tk.Button(self.main_frame, text="Back to Menu", command=self.create_main_menu).pack(pady=10)

    def show_track_guest_ui(self):
        """UI for tracking guest locations."""
        self.switch_frame()
        tk.Label(self.main_frame, text="Track Guest Location", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.main_frame, text="Band ID (e.g., MB1234):").pack()
        band_id_entry = tk.Entry(self.main_frame)
        band_id_entry.pack()

        def track_location():
            band_id = band_id_entry.get()
            if not band_id.startswith("MB"):
                messagebox.showerror("Error", "Invalid Band ID!")
                return
            band = self.system.get_band_info(band_id)
            if band:
                location = band.current_location or "Unknown"
                messagebox.showinfo("Guest Location", f"Location for Band ID {band_id}: {location}")
            else:
                messagebox.showerror("Error", "Band not found!")

        tk.Button(self.main_frame, text="Track Location", command=track_location).pack(pady=5)
        tk.Button(self.main_frame, text="Back to Menu", command=self.create_main_menu).pack(pady=10)

    def switch_frame(self):
        """Clears the current frame to switch to a new view."""
        for widget in self.main_frame.winfo_children():
            widget.destroy()

# System Initialization
magic_band_system = MagicBandSystem()

# Adding parks for testing
magic_band_system.parks.append(Park("Adventure Land", 28.3852, -81.5639))
magic_band_system.parks.append(Park("Fantasy World", 28.3747, -81.5494))

# Adding sample restaurants and stores
restaurant1 = Restaurant("Cosmic Cafe", "Adventure Land")
restaurant1.add_menu_item("Burger", 9.99)
restaurant1.add_menu_item("Pizza", 12.99)
magic_band_system.parks[0].add_restaurant(restaurant1)

store1 = Store("Galactic Goods", "Fantasy World")
store1.add_item("Plush Toy", 19.99)
store1.add_item("T-Shirt", 24.99)
magic_band_system.parks[1].add_shop(store1)

# Start the UI
root = tk.Tk()
app = MagicBandUI(root, magic_band_system)
root.mainloop()
