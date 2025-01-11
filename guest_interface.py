import tkinter as tk
from tkinter import ttk, messagebox
from main import *

class GuestInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Disney Guest Interface")
        self.root.geometry("800x600")
        self.setup_main_screen()

    def setup_main_screen(self):
        tk.Label(self.root, text="Disney Guest Interface", font=("Helvetica", 18)).pack(pady=20)
        tk.Button(self.root, text="Login with Magic Band", command=self.show_login, height=2, width=20).pack(pady=10)

    def show_login(self):
        login_window = tk.Toplevel(self.root)
        login_window.title("Guest Login")
        login_window.geometry("400x300")

        tk.Label(login_window, text="Enter Magic Band ID:").pack(pady=10)
        band_id_entry = tk.Entry(login_window)
        band_id_entry.pack()

        def validate_band():
            try:
                band_id = int(band_id_entry.get())
                for band in magic_band_system.registered_bands:
                    if band.band_id == band_id:
                        login_window.destroy()
                        self.show_guest_dashboard(band)
                        return
                tk.Label(login_window, text="Invalid Band ID", fg="red").pack()
            except ValueError:
                tk.Label(login_window, text="Please enter a valid number", fg="red").pack()

        tk.Button(login_window, text="Login", command=validate_band).pack(pady=10)

    def purchase_tickets(self, band):
        ticket_window = tk.Toplevel(self.root)
        ticket_window.title("Purchase Park Tickets")
        ticket_window.geometry("500x600")

        tk.Label(ticket_window, text="Purchase Park Tickets", font=("Helvetica", 16, "bold")).pack(pady=10)
        
        # Create a frame for the park selection
        selection_frame = ttk.Frame(ticket_window)
        selection_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Variables to store checkbox states
        park_vars = {}
        
        # Create checkboxes for each park
        for park in disney_parks:
            var = tk.BooleanVar()
            park_vars[park] = var
            
            # Check if guest already has ticket for this park
            if park.park_name in band.linked_tickets:
                ttk.Checkbutton(selection_frame, 
                               text=f"{park.park_name} (Already Purchased)", 
                               variable=var,
                               state='disabled').pack(pady=5, anchor='w')
            else:
                ttk.Checkbutton(selection_frame, 
                               text=f"{park.park_name} - $99.99", 
                               variable=var).pack(pady=5, anchor='w')

        def process_purchase():
            selected_parks = [park for park in disney_parks if park_vars[park].get()]
            
            if not selected_parks:
                messagebox.showwarning("No Selection", "Please select at least one park.")
                return
                
            total_cost = len(selected_parks) * 99.99  # Price per ticket
            
            # Confirm purchase
            confirm = messagebox.askyesno("Confirm Purchase", 
                                        f"Total cost for {len(selected_parks)} tickets: ${total_cost:.2f}\n\nProceed with purchase?")
            
            if confirm:
                # Process the purchase for each selected park
                for park in selected_parks:
                    magic_band_system.purchase_park_tickets(band, park)
                
                messagebox.showinfo("Success", "Tickets purchased successfully!")
                ticket_window.destroy()
                
                # Refresh the dashboard to show new tickets
                self.show_guest_dashboard(band)

        # Add a purchase button
        ttk.Button(ticket_window, 
                   text="Purchase Selected Tickets",
                   command=process_purchase).pack(pady=20)

        # Add a cancel button
        ttk.Button(ticket_window, 
                   text="Cancel",
                   command=ticket_window.destroy).pack(pady=10)

    def show_guest_dashboard(self, band):
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # Create dashboard
        tk.Label(self.root, text=f"Welcome, {band.guest.name}!", font=("Helvetica", 18)).pack(pady=20)

        # Add Purchase Tickets button at the top
        tk.Button(
            self.root,
            text="Purchase Tickets",
            command=lambda: self.purchase_tickets(band),
            width=20,
            height=2
        ).pack(pady=10)

        # Create notebook for tabbed interface
        notebook = ttk.Notebook(self.root)
        notebook.pack(pady=10, expand=True, fill="both")

        # Park Information Tab
        park_frame = ttk.Frame(notebook)
        notebook.add(park_frame, text="Park Information")
        
        for park in disney_parks:
            park_label = tk.Label(park_frame, text=f"\n{park.park_name}", font=("Helvetica", 14, "bold"))
            park_label.pack(pady=5)
            
            rides_text = "Rides:\n" + "\n".join([f"- {ride.ride_name}" for ride in park.rides])
            tk.Label(park_frame, text=rides_text, justify="left").pack(pady=5)
            
            restaurants_text = "Restaurants:\n" + "\n".join([f"- {rest.name}" for rest in park.restaurants])
            tk.Label(park_frame, text=restaurants_text, justify="left").pack(pady=5)

        # Magic Band History Tab
        history_frame = ttk.Frame(notebook)
        notebook.add(history_frame, text="Band History")
        
        history_label = tk.Label(history_frame, text="Your Activity History:", font=("Helvetica", 14))
        history_label.pack(pady=10)
        
        history_text = "\n".join([f"- {activity}" for activity in band.useage_history])
        tk.Label(history_frame, text=history_text, justify="left").pack(pady=10)

        # Current Location Tab
        location_frame = ttk.Frame(notebook)
        notebook.add(location_frame, text="Current Location")
        
        location_text = f"Current Location: {band.current_location if band.current_location else 'Not in park'}"
        tk.Label(location_frame, text=location_text, font=("Helvetica", 14)).pack(pady=20)

        # Ticket Information Tab
        ticket_frame = ttk.Frame(notebook)
        notebook.add(ticket_frame, text="Tickets")
        
        if band.linked_tickets:
            ticket_text = "Your Park Tickets:\n" + "\n".join([f"- {ticket}" for ticket in band.linked_tickets])
        else:
            ticket_text = "No tickets purchased yet."
        
        tk.Label(ticket_frame, text=ticket_text, font=("Helvetica", 12)).pack(pady=20)

        # Add logout button at bottom
        tk.Button(
            self.root, 
            text="Logout", 
            command=lambda: [self.root.destroy(), main_screen()], 
            width=20, 
            height=2
        ).pack(pady=10)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = GuestInterface()
    app.run()