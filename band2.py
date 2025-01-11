import tkinter as tk
from tkinter import messagebox, ttk

# -------------------- Dummy Classes --------------------
class MagicBandSystem:
    def __init__(self):
        self.registered_bands = []
        self.guests = []
        self.transactions = []
        self.parks = ["Magic Kingdom", "EPCOT", "Animal Kingdom", "Hollywood Studios"]
        self.rides = [
            {"ride_name": "Space Mountain", "queue": []},
            {"ride_name": "Splash Mountain", "queue": []},
            {"ride_name": "Test Track", "queue": []},
            {"ride_name": "Expedition Everest", "queue": []}
        ]
        self.hotel_rooms = set()
        self.shop = Shop("Disney Store", "Mickey Mouse Plush Toy", 20)
        self.restaurant = Restaurant("Disney Diner", "Cheeseburger Combo", 15)

    def register_new_guest(self, guest):
        self.guests.append(guest)

    def purchase_park_tickets(self, magic_band, park_name):
        magic_band.linked_tickets.append(park_name)

    def add_to_ride_queue(self, ride_name, band_id):
        for ride in self.rides:
            if ride["ride_name"] == ride_name:
                ride["queue"].append(band_id)

    def get_ride_queues(self):
        return self.rides
    
    def book_hotel_room(self, guest):
        room_number = len(self.hotel_rooms) + 101
        self.hotel_rooms.add(room_number)
        return room_number

class MagicBand:
    def __init__(self, band_id, guest):
        self.band_id = band_id
        self.guest = guest
        self.balance = 0
        self.linked_tickets = []
        self.credit_card_details = None
        self.purchase_history = []
        self.current_location = "Unknown"

    def add_credit_card(self, card_details):
        self.credit_card_details = card_details

    def update_location(self, location):
        self.current_location = location

    def record_transaction(self, amount, description, location):
        self.purchase_history.append((amount, description, location))

class Guest:
    def __init__(self, guest_id, name, age):
        self.guest_id = guest_id
        self.name = name
        self.age = age
        self.magic_band = None
        
# --------------------------------------------------
# Alterable classes
# (Might need to create manual instantiations)
        
class Shop:
    def __init__(self, name, item_name, price):
        self.name = name
        self.item_name = item_name
        self.price = price

class Restaurant:
    def __init__(self, name, food_item, price):
        self.name = name
        self.food_item = food_item
        self.price = price

# -------------------- Tkinter UI --------------------
class MagicBandUIApp:
    def __init__(self, system):
        self.system = system
        self.root = tk.Tk()
        self.root.title("Disney Guest Portal")
        self.root.geometry("500x500")
        self.create_main_menu()

    def create_main_menu(self):
        tk.Label(self.root, text="Disney Guest Portal", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=20)

        # Buttons for Main Menu Categories
        categories = [
            ("Register New Guest", self.register_guest_menu),
            ("Purchase Park Tickets", self.purchase_tickets_menu),
            ("Add Credit Card / Payments", self.add_payment_menu),
            ("Find Guest Location", self.track_location_menu),
            ("View Ride Queue", self.view_ride_queue),
            ("View Transaction History", self.view_transaction_history),
            ("Exit", self.root.quit)
        ]

        for i, (label, command) in enumerate(categories):
            tk.Button(self.root, text=label, command=command, width=30).grid(row=i + 1, column=0, pady=10)

        self.root.columnconfigure(0, weight=1)

    # -------------------- Guest Management --------------------
    def register_guest_menu(self):
        window = tk.Toplevel(self.root)
        window.title("Register New Guest")
        window.geometry("300x200")

        tk.Label(window, text="Guest Name:").grid(row=0, column=0)
        name_entry = tk.Entry(window)
        name_entry.grid(row=0, column=1)

        tk.Label(window, text="Guest Age:").grid(row=1, column=0)
        age_entry = tk.Entry(window)
        age_entry.grid(row=1, column=1)

        def register_guest():
            name = name_entry.get()
            age = age_entry.get()
            if not name or not age.isdigit():
                messagebox.showerror("Error", "Invalid name or age!")
                return
            guest_id = f"G{len(self.system.guests) + 1}"
            new_guest = Guest(guest_id, name, int(age))
            magic_band = MagicBand(f"MB{len(self.system.registered_bands) + 1}", new_guest)
            new_guest.magic_band = magic_band
            self.system.register_new_guest(new_guest)
            self.system.registered_bands.append(magic_band)
            messagebox.showinfo("Success", f"Guest '{name}' registered with MagicBand ID '{magic_band.band_id}'.")

        tk.Button(window, text="Register", command=register_guest).grid(row=2, column=0, columnspan=2, pady=10)

    # -------------------- Park Tickets --------------------
    def purchase_tickets_menu(self):
        window = tk.Toplevel(self.root)
        window.title("Purchase Park Tickets")
        window.geometry("300x200")

        tk.Label(window, text="MagicBand ID:").grid(row=0, column=0)
        band_entry = tk.Entry(window)
        band_entry.grid(row=0, column=1)

        tk.Label(window, text="Select Park:").grid(row=1, column=0)
        park_combobox = ttk.Combobox(window, values=self.system.parks)
        park_combobox.grid(row=1, column=1)

        def purchase_tickets():
            band_id = band_entry.get()
            park_name = park_combobox.get()
            band = next((b for b in self.system.registered_bands if b.band_id == band_id), None)
            if band and park_name:
                self.system.purchase_park_tickets(band, park_name)
                messagebox.showinfo("Success", f"Ticket to '{park_name}' added to MagicBand {band_id}.")
            else:
                messagebox.showerror("Error", "Invalid MagicBand ID or Park Name!")

        tk.Button(window, text="Purchase Ticket", command=purchase_tickets).grid(row=2, column=0, columnspan=2, pady=10)

    # -------------------- View Ride Queue --------------------
    def view_ride_queue(self):
        window = tk.Toplevel(self.root)
        window.title("Ride Queue")
        window.geometry("400x300")

        ride_text = ""
        for ride in self.system.get_ride_queues():
            queue = ", ".join(ride["queue"]) if ride["queue"] else "Empty"
            ride_text += f"{ride['ride_name']} - Queue: {queue}\n"

        tk.Label(window, text="Current Ride Queues:", font=("Arial", 12)).pack(pady=10)
        tk.Label(window, text=ride_text, justify="left").pack()

    # -------------------- View Transaction History --------------------
    def view_transaction_history(self):
        window = tk.Toplevel(self.root)
        window.title("Transaction History")
        window.geometry("400x300")

        tk.Label(window, text="MagicBand ID:").pack()
        band_entry = tk.Entry(window)
        band_entry.pack()

        def show_transactions():
            band_id = band_entry.get()
            band = next((b for b in self.system.registered_bands if b.band_id == band_id), None)
            if band:
                transactions = "\n".join([f"${t['amount']} - {t['description']} ({t['location']})" for t in band.purchase_history])
                transactions = transactions if transactions else "No transactions found."
                tk.Label(window, text=transactions, justify="left").pack()
            else:
                messagebox.showerror("Error", "Invalid MagicBand ID!")

        tk.Button(window, text="Show Transactions", command=show_transactions).pack(pady=10)

    def add_payment_menu(self):
            window = tk.Toplevel(self.root)
            window.title("Add Credit Card")
            window.geometry("300x200")

            tk.Label(window, text="MagicBand ID:").grid(row=0, column=0)
            band_entry = tk.Entry(window)
            band_entry.grid(row=0, column=1)

            tk.Label(window, text="Credit Card #:").grid(row=1, column=0)
            card_entry = tk.Entry(window)
            card_entry.grid(row=1, column=1)

            def add_payment():
                band_id = band_entry.get()
                card_number = card_entry.get()
                band = next((b for b in self.system.registered_bands if b.band_id == band_id), None)
                if band and card_number:
                    band.add_credit_card(card_number)
                    messagebox.showinfo("Success", "Credit Card added successfully!")
                else:
                    messagebox.showerror("Error", "Invalid MagicBand ID or Card Number!")

            tk.Button(window, text="Add Card", command=add_payment).grid(row=2, column=0, columnspan=2, pady=10)


    def track_location_menu(self):
        window = tk.Toplevel(self.root)
        window.title("Track Guest Location")
        window.geometry("300x150")

        tk.Label(window, text="MagicBand ID:").grid(row=0, column=0)
        band_entry = tk.Entry(window)
        band_entry.grid(row=0, column=1)

        def track_location():
            band_id = band_entry.get()
            band = next((b for b in self.system.registered_bands if b.band_id == band_id), None)
            if band:
                messagebox.showinfo("Location", f"Current Location: {band.current_location}")
            else:
                messagebox.showerror("Error", "Invalid MagicBand ID!")

        tk.Button(window, text="Track", command=track_location).grid(row=1, column=0, columnspan=2, pady=10)
        
    # -------------------- Food Purchase --------------------
    def purchase_food_menu(self):
        self.purchase_item_or_food(self.system.restaurant, "Food")

    # -------------------- Item Purchase --------------------
    def purchase_item_menu(self):
        self.purchase_item_or_food(self.system.shop, "Item")

    def purchase_item_or_food(self, location, item_type):
        window = tk.Toplevel(self.root)
        window.title(f"Purchase {item_type}")
        window.geometry("300x200")

        tk.Label(window, text="MagicBand ID:").grid(row=0, column=0)
        band_entry = tk.Entry(window)
        band_entry.grid(row=0, column=1)

        tk.Label(window, text=f"{item_type} Available: {location.item_name} - ${location.price}").grid(row=1, column=0, columnspan=2)

        def make_purchase():
            band_id = band_entry.get()
            band = next((b for b in self.system.registered_bands if b.band_id == band_id), None)
            if band:
                band.record_transaction(location.price, f"{item_type}: {location.item_name}", location.name)
                messagebox.showinfo("Success", f"Purchased {location.item_name} for ${location.price}!")
            else:
                messagebox.showerror("Error", "Invalid MagicBand ID!")

        tk.Button(window, text="Purchase", command=make_purchase).grid(row=2, column=0, columnspan=2, pady=10)

    # -------------------- Book Hotel Room --------------------
    def book_hotel_room_menu(self):
        window = tk.Toplevel(self.root)
        window.title("Book Hotel Room")
        window.geometry("300x150")

        tk.Label(window, text="MagicBand ID:").grid(row=0, column=0)
        band_entry = tk.Entry(window)
        band_entry.grid(row=0, column=1)

        def book_room():
            band_id = band_entry.get()
            guest = next((g for g in self.system.guests if g.magic_band.band_id == band_id), None)
            if guest:
                room_number = self.system.book_hotel_room(guest)
                messagebox.showinfo("Success", f"Room {room_number} booked for {guest.name}!")
            else:
                messagebox.showerror("Error", "Invalid MagicBand ID!")

        tk.Button(window, text="Book Room", command=book_room).grid(row=1, column=0, columnspan=2, pady=10)

    def run(self):
        self.root.mainloop()

# -------------------- Main Program --------------------
if __name__ == "__main__":
    system = MagicBandSystem()
    app = MagicBandUIApp(system)
    app.run()
