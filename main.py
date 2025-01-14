# -----------------------------------------------
# Created By: Ali Khan (& Mr. Alexander's Class)
# Date: January 9-16, 2025
# DisneyWorld MagicBandSystem Culminating 
# -----------------------------------------------

from model_classes import *

# USE CASE:
# ------------------------------------
# Part 1 - Creation of Disney World Environment

# Create Parks
animal_kingdom_park = Park("Animal Kingdom")
magic_kingdom_park = Park("Magic Kingdom")
epcot_park = Park("Epcot")
hollywood_studios_park = Park("Hollywood Studios")

# Animal Kingdom Rides
ride_ak1 = Ride("Bug's Life", 48, 250)
animal_kingdom_park.add_ride(ride_ak1)

ride_ak2 = Ride("Expedition Everest", 44, 100)
animal_kingdom_park.add_ride(ride_ak2)

ride_ak3 = Ride("Kilimanjaro Safaris", 40, 300)
animal_kingdom_park.add_ride(ride_ak3)

# Animal Kingdom Restaurants
restaurant_ak1 = Restaurant("Pizzafari")
restaurant_ak1.add_dish("Noodles", 3.99)
restaurant_ak1.add_dish("Pizza Slice", 5.49)
animal_kingdom_park.add_restaurant(restaurant_ak1)

restaurant_ak2 = Restaurant("Rainforest Cafe")
restaurant_ak2.add_dish("Burgers", 9.99)
restaurant_ak2.add_dish("Chicken Wings", 7.99)
animal_kingdom_park.add_restaurant(restaurant_ak2)

restaurant_ak3 = Restaurant("Tiffins")
restaurant_ak3.add_dish("Grilled Salmon", 14.99)
restaurant_ak3.add_dish("Mac and Cheese", 8.99)
animal_kingdom_park.add_restaurant(restaurant_ak3)

# Animal Kingdom Shops
shop_ak1 = Shop("Trader Sam's")
shop_ak1.add_item("Stitch Plushie", 24.99)
shop_ak1.add_item("Animal Kingdom Mug", 14.99)
animal_kingdom_park.add_shops(shop_ak1)

shop_ak2 = Shop("Island Mercantile")
shop_ak2.add_item("Safari Hat", 19.99)
shop_ak2.add_item("Water Bottle", 12.99)
animal_kingdom_park.add_shops(shop_ak2)

shop_ak3 = Shop("Zuri's Sweets Shop")
shop_ak3.add_item("Candy Apple", 5.99)
shop_ak3.add_item("Chocolate Bar", 3.99)
animal_kingdom_park.add_shops(shop_ak3)

# Animal Kingdom Elements
element_ak1 = Element("Timon and Pumba Statue", "Golden Statue")
animal_kingdom_park.add_elements(element_ak1)

element_ak2 = Element("Tree of Life", "Iconic Structure")
animal_kingdom_park.add_elements(element_ak2)

element_ak3 = Element("Pandora Floating Rocks", "Proximity Attraction")
animal_kingdom_park.add_elements(element_ak3)

# Magic Kingdom Rides
ride_mk1 = Ride("Space Mountain", 48, 200)
magic_kingdom_park.add_ride(ride_mk1)

ride_mk2 = Ride("It's a Small World", 0, 300)
magic_kingdom_park.add_ride(ride_mk2)

ride_mk3 = Ride("Big Thunder Mountain Railroad", 42, 180)
magic_kingdom_park.add_ride(ride_mk3)

# Magic Kingdom Restaurants
restaurant_mk1 = Restaurant("Cinderella's Royal Table")
restaurant_mk1.add_dish("Roast Chicken", 16.99)
restaurant_mk1.add_dish("Mashed Potatoes", 4.99)
magic_kingdom_park.add_restaurant(restaurant_mk1)

restaurant_mk2 = Restaurant("Be Our Guest")
restaurant_mk2.add_dish("Steak", 19.99)
restaurant_mk2.add_dish("Pasta Alfredo", 11.99)
magic_kingdom_park.add_restaurant(restaurant_mk2)

restaurant_mk3 = Restaurant("Liberty Tree Tavern")
restaurant_mk3.add_dish("Turkey Leg", 14.99)
restaurant_mk3.add_dish("Apple Pie", 6.99)
magic_kingdom_park.add_restaurant(restaurant_mk3)

# Magic Kingdom Shops
shop_mk1 = Shop("Emporium")
shop_mk1.add_item("Mickey Ears", 19.99)
shop_mk1.add_item("Cinderella Figurine", 29.99)
magic_kingdom_park.add_shops(shop_mk1)

shop_mk2 = Shop("Big Top Souvenirs")
shop_mk2.add_item("Popcorn Bucket", 12.99)
shop_mk2.add_item("Plush Minnie Mouse", 24.99)
magic_kingdom_park.add_shops(shop_mk2)

shop_mk3 = Shop("Star Traders")
shop_mk3.add_item("Star Wars Mug", 16.99)
shop_mk3.add_item("Galaxy T-Shirt", 19.99)
magic_kingdom_park.add_shops(shop_mk3)

# Magic Kingdom Elements
element_mk1 = Element("Cinderella's Castle", "Iconic Structure")
magic_kingdom_park.add_elements(element_mk1)

element_mk2 = Element("Partners Statue", "Golden Statue")
magic_kingdom_park.add_elements(element_mk2)

element_mk3 = Element("Seven Dwarfs Mine Entrance", "Interactive Exhibit")
magic_kingdom_park.add_elements(element_mk3)

# Epcot Rides
ride_ep1 = Ride("Soarin'", 40, 200)
epcot_park.add_ride(ride_ep1)

ride_ep2 = Ride("Test Track", 40, 150)
epcot_park.add_ride(ride_ep2)

ride_ep3 = Ride("Spaceship Earth", 0, 300)
epcot_park.add_ride(ride_ep3)

# Epcot Restaurants
restaurant_ep1 = Restaurant("Coral Reef Restaurant")
restaurant_ep1.add_dish("Lobster Tail", 24.99)
restaurant_ep1.add_dish("Caesar Salad", 12.99)
epcot_park.add_restaurant(restaurant_ep1)

restaurant_ep2 = Restaurant("Le Cellier Steakhouse")
restaurant_ep2.add_dish("Filet Mignon", 36.99)
restaurant_ep2.add_dish("Poutine", 10.99)
epcot_park.add_restaurant(restaurant_ep2)

restaurant_ep3 = Restaurant("Garden Grill Restaurant")
restaurant_ep3.add_dish("BBQ Ribs", 19.99)
restaurant_ep3.add_dish("Grilled Vegetables", 14.99)
epcot_park.add_restaurant(restaurant_ep3)

# Epcot Shops
shop_ep1 = Shop("Mouse Gear")
shop_ep1.add_item("Epcot Globe Figurine", 29.99)
shop_ep1.add_item("Disney Pins", 9.99)
epcot_park.add_shops(shop_ep1)

shop_ep2 = Shop("World Traveler")
shop_ep2.add_item("Epcot T-Shirt", 19.99)
shop_ep2.add_item("Minnie Ears", 24.99)
epcot_park.add_shops(shop_ep2)

shop_ep3 = Shop("The Art of Disney")
shop_ep3.add_item("Disney Artwork", 99.99)
shop_ep3.add_item("Sketchbook Journal", 14.99)
epcot_park.add_shops(shop_ep3)

# Epcot Elements
element_ep1 = Element("Spaceship Earth Structure", "Iconic Structure")
epcot_park.add_elements(element_ep1)

element_ep2 = Element("Fountain of Nations", "Proximity Attraction")
epcot_park.add_elements(element_ep2)

element_ep3 = Element("Living with the Land Exhibit", "Interactive Exhibit")
epcot_park.add_elements(element_ep3)

# Hollywood Studios Rides
ride_hs1 = Ride("Tower of Terror", 40, 150)
hollywood_studios_park.add_ride(ride_hs1)

ride_hs2 = Ride("Rock 'n' Roller Coaster", 48, 120)
hollywood_studios_park.add_ride(ride_hs2)

ride_hs3 = Ride("Star Tours", 40, 180)
hollywood_studios_park.add_ride(ride_hs3)

# Hollywood Studios Restaurants
restaurant_hs1 = Restaurant("50's Prime Time Café")
restaurant_hs1.add_dish("Fried Chicken", 16.99)
restaurant_hs1.add_dish("Pot Roast", 18.99)
hollywood_studios_park.add_restaurant(restaurant_hs1)

restaurant_hs2 = Restaurant("Hollywood & Vine")
restaurant_hs2.add_dish("Seafood Platter", 29.99)
restaurant_hs2.add_dish("Spaghetti & Meatballs", 19.99)
hollywood_studios_park.add_restaurant(restaurant_hs2)

restaurant_hs3 = Restaurant("Woody's Lunch Box")
restaurant_hs3.add_dish("Grilled Cheese", 8.99)
restaurant_hs3.add_dish("Tachos", 9.99)
hollywood_studios_park.add_restaurant(restaurant_hs3)

# Hollywood Studios Shops
shop_hs1 = Shop("Tatooine Traders")
shop_hs1.add_item("Lightsaber", 49.99)
shop_hs1.add_item("Star Wars T-Shirt", 24.99)
hollywood_studios_park.add_shops(shop_hs1)

shop_hs2 = Shop("Mickey's of Hollywood")
shop_hs2.add_item("Hollywood Studios Mug", 14.99)
shop_hs2.add_item("Disney Collectible Keychain", 7.99)
hollywood_studios_park.add_shops(shop_hs2)

shop_hs3 = Shop("Keystone Clothiers")
shop_hs3.add_item("Disney Sweatshirt", 34.99)
shop_hs3.add_item("Mickey Mouse Watch", 44.99)
hollywood_studios_park.add_shops(shop_hs3)

# Hollywood Studios Elements
element_hs1 = Element("Hollywood Tower Hotel Sign", "Golden Statue")
hollywood_studios_park.add_elements(element_hs1)

element_hs2 = Element("Millennium Falcon", "Iconic Structure")
hollywood_studios_park.add_elements(element_hs2)

element_hs3 = Element("Toy Story Land Entrance", "Interactive Exhibit")
hollywood_studios_park.add_elements(element_hs3)

# Initialize Magic Band System

disney_parks = [animal_kingdom_park, magic_kingdom_park, epcot_park, hollywood_studios_park]

magic_band_system = MagicBandSystem(disney_parks)
print(magic_band_system)

# Part 2 - SIMULATION

# Guests deciding to go to Disney world (Create six guests.)
guest_1_ca = Guest("Christopher Alexander", 47)
guest_2_ra = Guest("Ruby Alexander", 9)
guest_3_aa = Guest("Annie Alexander", 6)
guest_4_jt = Guest("Joey Tribiani", 35)
guest_5_mb = Guest("Monica Bing", 28)
guest_6_rg = Guest("Ross Geller", 32)

# Three Guests purchase their own Magic Band"
magic_band_1 = MagicBand(guest_1_ca)
magic_band_2 = MagicBand(guest_2_ra)
magic_band_3 = MagicBand(guest_3_aa)

# --------------------------------------
# SIMULATION EDIT: ALI KHAN 01/12/25
# Links MagicBand to Guest (Guest Info)
guest_1_ca.link_magic_band(magic_band_1)
guest_2_ra.link_magic_band(magic_band_2)
guest_3_aa.link_magic_band(magic_band_3)
# --------------------------------------

# Magic bands are registered in the disney system
magic_band_system.register_band(magic_band_1)
magic_band_system.register_band(magic_band_2)
magic_band_system.register_band(magic_band_3)

# Guests purchase tickets for parks
magic_band_system.purchase_park_tickets(magic_band_1, animal_kingdom_park)
magic_band_system.purchase_park_tickets(magic_band_2, animal_kingdom_park)
magic_band_system.purchase_park_tickets(magic_band_3, animal_kingdom_park)
magic_band_system.purchase_park_tickets(magic_band_1, epcot_park)
magic_band_system.purchase_park_tickets(magic_band_2, epcot_park)
magic_band_system.purchase_park_tickets(magic_band_3, epcot_park)

# Guests enter the Animal Kingdom Park
magic_band_1.use_band_for_park_entry(animal_kingdom_park)
magic_band_2.use_band_for_park_entry(animal_kingdom_park)
magic_band_3.use_band_for_park_entry(animal_kingdom_park)

# Guests get in line for and complete rides
magic_band_1.use_band_for_ride(ride_ak1)  # Christopher on Bug's Life
ride_ak1.complete_ride(magic_band_1)

magic_band_2.use_band_for_ride(ride_ak2)  # Ruby on Expedition Everest
ride_ak2.complete_ride(magic_band_2)

magic_band_3.use_band_for_ride(ride_ak3)  # Annie on Kilimanjaro Safaris
ride_ak3.complete_ride(magic_band_3)

magic_band_2.use_band_for_ride(ride_ak3)  # Ruby on Kilimanjaro
ride_ak3.complete_ride(magic_band_2)

magic_band_1.use_band_for_ride(ride_ak3)  # Christopher on Kilimanjaro
ride_ak3.complete_ride(magic_band_1)

# Guests purchase food at restaurants
magic_band_1.use_band_in_restaurant(restaurant_ak1, 10.99, "Noodles")  # Christopher at Pizzafari
magic_band_2.use_band_in_restaurant(restaurant_ak2, 14.99, "Burgers")  # Ruby at Rainforest Cafe
magic_band_3.use_band_in_restaurant(restaurant_ak3, 15.99, "Grilled Salmon")  # Annie at Tiffins

# Guests purchase merchandise at shops
magic_band_1.use_band_in_shop(shop_ak1, 29.99, "Stitch Plushie")  # Christopher at Trader Sam's
magic_band_2.use_band_in_shop(shop_ak2, 19.99, "Safari Hat")  # Ruby at Island Mercantile
magic_band_3.use_band_in_shop(shop_ak3, 5.99, "Candy Apple")  # Annie at Zuri's Sweets Shop

# Guests interact with park elements
magic_band_1.use_band_in_element(element_ak1)  # Christopher interacts with Timon and Pumba Statue
magic_band_2.use_band_in_element(element_ak2)  # Ruby interacts with Tree of Life
magic_band_3.use_band_in_element(element_ak3)  # Annie interacts with Pandora Floating Rocks

guests = [guest_1_ca, guest_2_ra, guest_3_aa, guest_4_jt, guest_5_mb, guest_6_rg]

# ------------------------------------------------------------------------------------------------

import tkinter as tk
# from tkinter import ttk # This is just the themed window set
from tkinter import PhotoImage


# I didn't want to manually load a photo in every function/method: 
#   Created an external function that I can simply call
# Parameters are:
#   1. Window to put logo on
#   2. Image path (Different images in this case is referring to different sizes)

def load_logo_image(window, file):
    logo_image = PhotoImage(file=file)
    logo_label = tk.Label(window, image=logo_image)
    logo_label.image = logo_image  # Keep a reference to prevent garbage collection
    logo_label.pack(anchor="n", padx=10, pady=5)

# Main Application Window
def main_screen():
    
    # Create Window
    root = tk.Tk()
    root.title("Disney System Interface") # Window Title
    root.geometry("800x600") # Size of Window

    def open_employee_interface():
        
        password_window = tk.Toplevel(root)
        
        # Toplevel is something we haven't covered, but makes sense. This is crucial because
        # it is used to create a window on top of other windows
        # Learnt and Obtained Understanding from: https://www.geeksforgeeks.org/python-tkinter-toplevel-widget/
        
        password_window.title("Employee Login") # Title for Overlapped Window
        password_window.geometry("300x200") # Size of Window

        load_logo_image(password_window, "logo3.png")
        tk.Label(password_window, text="Enter Password").pack(pady=10) # Asks user to enter password
        password_entry = tk.Entry(password_window, show="*") # When typing, entry is censored by asterisks!
        password_entry.pack()

        def validate_password():
            if password_entry.get() == "123": # Checks to see if Employee's password is correct.
                password_window.destroy() # This is just going to collapse the widgets!
                employee_interface() # If password is correct, redirects you to the Employee UI!
            else:
                tk.Label(password_window, text="Incorrect Password", fg="red").pack()
                # (I know it's unnecessary to expect invalid entries, but this helps me when testing code)
                # You can also use Tkinter messagebox for an Error window to come up. That is also very simple
                # However, I wanted to implement code that we have taken up in class to show understanding.

        tk.Button(password_window, text="Login", command=lambda: validate_password()).pack(pady=10) # Login Button
        
    def open_guest_interface():
        
        id_window = tk.Toplevel(root)
        
        # Toplevel is something we haven't covered, but makes sense. This is crucial because
        # it is used to create a window on top of other windows
        # Learnt and Obtained Understanding from: https://www.geeksforgeeks.org/python-tkinter-toplevel-widget/
        
        id_window.title("Guest Login") # Title for Overlapped Window
        id_window.geometry("300x200") # Size of Window

        load_logo_image(id_window, "logo3.png")
        tk.Label(id_window, text="Enter Guest ID").pack(pady=10) # Asks user to enter password
        guest_id_entry = tk.Entry(id_window) # When typing, entry is censored by asterisks!
        guest_id_entry.pack()

        def validate_entry():
            guest_id = guest_id_entry.get()
            for guest in guests:
                if guest.guest_id == guest_id: # Checks to See if Guest Exists!
                    id_window.destroy() # This is just going to collapse the widgets!
                    guest_interface() # If password is correct, redirects you to the Employee UI!
                else:
                    tk.Label(id_window, text="Invalid Identification", fg="red").pack()
                # (I know it's unnecessary to expect invalid entries, but this helps me when testing code)
                # You can also use Tkinter messagebox for an Error window to come up. That is also very simple
                # However, I wanted to implement code that we have taken up in class to show understanding.

        tk.Button(id_window, text="Login", command=lambda: validate_entry()).pack(pady=10) # Login Button


    # Buttons for the Main Window
    
    load_logo_image(root, "logo.png") # Add logo image
    
    tk.Label(root, text="Welcome to the Disney System", font=("Helvetica", 18)).pack(pady=20)
    tk.Button(root, text="Employee Login", command=lambda: open_employee_interface(), height=2, width=20).pack(pady=10)
    tk.Button(root, text="Guest Login", command=lambda: open_guest_interface(), height=2, width=20).pack(pady=10)  # Placeholder

    root.mainloop()

# Employee Interface
def employee_interface():
    
    # Create Employee UI Window
    emp_root = tk.Toplevel()
    emp_root.title("Disney Employee Interface") # Window Name
    emp_root.geometry("1000x700") # Window Size

    def show_park_overview():
        park_window = tk.Toplevel(emp_root)
        # Again, Toplevel will open an overlapping window!
        park_window.title("Park Overview") # Name of Overlapping Window
        park_window.geometry("800x600") # Window Size

        load_logo_image(park_window, "logo.png") # Add logo image
        tk.Label(park_window, text="Select a Park to View Details", font=("Helvetica", 14)).pack(pady=10) # Label on Overlapping Window

        def show_park_details(park):
            detail_window = tk.Toplevel(park_window)
            # Again, Toplevel will open an overlapping window, but now, on an overlapping window!
            detail_window.title(f"{park.park_name} Details") # Name of Double Overlapping Window
            detail_window.geometry("800x600")
            
            # Gather the Required Information to Show on Window
            # In each line, there a for loop, iterating through all rides, restaurants, shops, and elements (RESPECTIVELY)
            details = f"Rides: \n" + "\n".join([ride.ride_name for ride in park.rides]) + "\n\n" \
                      f"Restaurants: \n" + "\n".join([rest.name for rest in park.restaurants]) + "\n\n" \
                      f"Shops: \n" + "\n".join([shop.name for shop in park.shops]) + "\n\n" \
                      f"Elements: \n" + "\n".join([element.name for element in park.elements])

            # In a single label, show all details!
            load_logo_image(detail_window, "logo.png") # Add logo image
            tk.Label(detail_window, text=details, justify="center", font=("Helvetica", 12)).pack(pady=20, padx=20)

        # Rather than individually creating all overlapping windows for the parks, make a simple for loop!
        for park in disney_parks:
            tk.Button(park_window, text=park.park_name, command=lambda p=park: show_park_details(p)).pack(pady=10)
        # In the command=lambda, you're stating p=park and sending it in as a parameter for the command

    def show_magic_band_management():
        band_window = tk.Toplevel(emp_root)
        # Again, Toplevel will open an overlapping window!
        band_window.title("Magic Band Management") # Overlapping Window Name
        band_window.geometry("800x600") # Overlapping Window Size

        load_logo_image(band_window, "logo.png") # Add logo image
        tk.Label(band_window, text="Magic Band Management", font=("Helvetica", 14)).pack(pady=10)

        def create_new_guest():
            create_guest_window = tk.Toplevel(band_window)
            # Again, Toplevel will open an overlapping window, but now, on another overlapping window!
            create_guest_window.title("Create New Guest") # Double Overlapping Window Name
            create_guest_window.geometry("400x300") # Double Overlapping Window Size

            load_logo_image(create_guest_window, "logo2.png") # Add logo image
            tk.Label(create_guest_window, text="Enter Guest Name").pack(pady=5)
            guest_name_entry = tk.Entry(create_guest_window) # Asks for Guest Name
            guest_name_entry.pack(pady=5)

            tk.Label(create_guest_window, text="Enter Guest Age").pack(pady=5)
            guest_age_entry = tk.Entry(create_guest_window) # Asks for Guest Age
            guest_age_entry.pack(pady=5)

            def add_guest():
                name = guest_name_entry.get()
                age = int(guest_age_entry.get())
                new_guest = Guest(name, age) # Creates New Guest Object
                guests.append(new_guest) # Adds to list of Guests so Guest ID can be used!
                tk.Label(create_guest_window, text=f"Guest created with ID: {new_guest.guest_id}", fg="green").pack(pady=5)

            tk.Button(create_guest_window, text="Create Guest", command=lambda: add_guest()).pack(pady=10)

        def provide_new_band():
            new_band_window = tk.Toplevel(band_window)
            # Again, Toplevel will open an overlapping window, but now, on another overlapping window!
            new_band_window.title("Provide New Magic Band") # Double Overlapping Window Name
            new_band_window.geometry("400x370") # Double Overlapping Window Size

            load_logo_image(new_band_window, "logo2.png") # Add logo image
            tk.Label(new_band_window, text="Enter Guest ID").pack(pady=5)
            guest_id_entry = tk.Entry(new_band_window) # Asks user for Guest ID
            guest_id_entry.pack(pady=5)

            def create_band():
                guest_id = guest_id_entry.get()
                for guest in guests:
                    if guest.guest_id == guest_id: # Checks to See if Guest Exists!
                        new_band = MagicBand(guest) # If so, creates object!
                        guest.link_magic_band(new_band)
                        tk.Label(new_band_window, text=f"Magic Band {new_band.band_id} created for and linked to {guest.name}", fg="green").pack(pady=5)

                        # Sub-option to register the new band
                        def register_band():
                            magic_band_system.register_band(new_band)
                            tk.Label(new_band_window, text=f"Band {new_band.band_id} registered successfully", fg="green").pack(pady=5)

                        tk.Label(new_band_window, text="This band must be registered into the system!", fg="blue").pack(pady=10)
                        # In order for this MagicBand to be used, it must be put into magic_band_system.registered_bands!
                        tk.Button(new_band_window, text="Register This Band", command=lambda: register_band()).pack(pady=10)
                        return

                # Error message, helps me when testing. (Still avoiding messagebox in Employee UI)
                tk.Label(new_band_window, text="Guest not found", fg="red").pack(pady=5)

            tk.Button(new_band_window, text="Create Band", command=lambda: create_band()).pack(pady=10)

        def view_guest_details():
            guest_window = tk.Toplevel(band_window)
            # Again, Toplevel will open an overlapping window!
            guest_window.title("View Guest Details") # Overlapping Window Name
            guest_window.geometry("400x300") # Overlapping Window Size

            load_logo_image(guest_window, "logo2.png") # Add logo image
            tk.Label(guest_window, text="Enter Guest ID").pack(pady=5)
            guest_id_entry = tk.Entry(guest_window) # Asks for Guest ID
            guest_id_entry.pack(pady=5)
            
            tk.Button(guest_window, text="View Details", command=lambda: display_details()).pack(pady=10)
            info_label = tk.Label(guest_window, text="")
            info_label.pack(pady=10)

            def display_details():
                guest_id = guest_id_entry.get()
                for guest in guests:
                    if guest.guest_id == guest_id: # Checks if the Guest Exists
                        details = f"Name: {guest.name}\nGuest ID: {guest.guest_id}\nMagic Band: {guest.magic_band.band_id if guest.magic_band else 'None'}"
                        info_label.config(text=details)  # Update the existing label with new guest details
                        return
                
                # Error message, helps me when testing. (Still avoiding messagebox in Employee UI)
                tk.Label(guest_window, text="Guest not found", fg="red").pack(pady=5)

        def find_location():
            location_window = tk.Toplevel(band_window)
            # Again, Toplevel will open an overlapping window!
            location_window.title("Find Band/Guest Location") # Overlapping Window Name
            location_window.geometry("400x300") # Overlapping Window Size

            load_logo_image(location_window, "logo2.png") # Add logo image
            tk.Label(location_window, text="Enter Magic Band ID").pack(pady=5)
            band_id_entry = tk.Entry(location_window) # Asks user for MagicBand ID
            band_id_entry.pack(pady=5)

            def display_location():
                band_id = int(band_id_entry.get())
                for band in magic_band_system.registered_bands:
                    if band.band_id == band_id: # Checks If the MagicBand is Registered
                        location = band.current_location if band.current_location else "Location not available"
                        # Checks if the Band has a Location!
                        tk.Label(location_window, text=f"Current Location: {location}").pack(pady=10)
                        return
                    
                # Error message, helps me when testing. (Still avoiding messagebox in Employee UI)
                tk.Label(location_window, text="Band not found", fg="red").pack(pady=5)

            tk.Button(location_window, text="Find Location", command=lambda: display_location()).pack(pady=10)

        def add_park_ticket():
            ticket_window = tk.Toplevel(band_window)
            # Again, Toplevel will open an overlapping window!
            ticket_window.title("Add Park Ticket") # Overlapping Window Name
            ticket_window.geometry("400x300") # Overlapping Window Size

            load_logo_image(ticket_window, "logo2.png") # Add logo image
            tk.Label(ticket_window, text="Enter Magic Band ID").pack(pady=5)
            band_id_entry = tk.Entry(ticket_window) # Asks user for MagicBand ID
            band_id_entry.pack(pady=5)

            tk.Label(ticket_window, text="Enter Park Name").pack(pady=5)
            park_name_entry = tk.Entry(ticket_window) # Asks user for Desired Park Name
            park_name_entry.pack(pady=5)

            def purchase_ticket():
                band_id = int(band_id_entry.get())
                park_name = park_name_entry.get()
                for band in magic_band_system.registered_bands:
                    if band.band_id == band_id: # Checks if the MagicBand is Registered
                        for park in disney_parks: 
                            if park.park_name == park_name: # Checks the name of Park
                                magic_band_system.purchase_park_tickets(band, park)
                                tk.Label(ticket_window, text="Ticket Added Successfully", fg="green").pack(pady=5)
                                return
                            
                # Error message, helps me when testing. (Still avoiding messagebox in Employee UI)
                tk.Label(ticket_window, text="Invalid Band or Park", fg="red").pack(pady=5)

            tk.Button(ticket_window, text="Add Ticket", command=lambda: purchase_ticket()).pack(pady=10)

        # Create Buttons for MagicBand Management
        
        tk.Button(band_window, text="Create New Guest", command=lambda: create_new_guest()).pack(pady=5)
        tk.Button(band_window, text="Provide New Band", command=lambda: provide_new_band()).pack(pady=5)
        tk.Button(band_window, text="View Guest Details", command=lambda: view_guest_details()).pack(pady=5)
        tk.Button(band_window, text="Find Band/Guest Location", command=lambda: find_location()).pack(pady=5)
        tk.Button(band_window, text="Add Park Ticket", command=lambda: add_park_ticket()).pack(pady=5)

    def show_ride_management():
        ride_window = tk.Toplevel(emp_root)
        # Again, Toplevel will open an overlapping window!
        ride_window.title("Ride Management") # Overlapping Window Name
        ride_window.geometry("800x600") # Overlapping Window Size

        load_logo_image(ride_window, "logo.png") # Add logo image
        tk.Label(ride_window, text="Select a Park to View Ride Info", font=("Helvetica", 14)).pack(pady=10)

        def show_ride_details(park):
            ride_detail_window = tk.Toplevel(ride_window)
            # Again, Toplevel will open an overlapping window, but again, on an overlapping window!
            ride_detail_window.title(f"{park.park_name} Rides") # Double Overlapping Window Name
            ride_detail_window.geometry("800x700") # Double Overlapping Window Size

            load_logo_image(ride_detail_window, "logo.png") # Add logo image

            # Create a simple for loop for each ride at a park instead of doing it individually
            for ride in park.rides:
                tk.Button(ride_detail_window, text=ride.ride_name, command=lambda r=ride: tk.Label(ride_detail_window, text=r.get_ride_info(), justify="left", font=("Helvetica", 10)).pack(pady=5)).pack(pady=5)
                # Here, the command isn't a function or method. It is itself a Label being packed onto the window!
                # Rephrase: This button is packed on the screen. When clicked, it packs a label!

        # Create a simple for loop for each park instead of doing it individually.
        # (This loop contains the for loop above because the command in button below calls the for loop)
        for park in disney_parks:
            tk.Button(ride_window, text=park.park_name, command=lambda p=park: show_ride_details(p)).pack(pady=5)

    def show_restaurant_management():
        restaurant_window = tk.Toplevel(emp_root)
        # Again, Toplevel will open an overlapping window!
        restaurant_window.title("Restaurant Management") # Overlapping Window Name
        restaurant_window.geometry("800x600") # Overlapping Window Size

        load_logo_image(restaurant_window, "logo.png") # Add logo image
        tk.Label(restaurant_window, text="Select a Park to View Restaurants", font=("Helvetica", 14)).pack(pady=10)

        def show_restaurant_details(park):
            rest_detail_window = tk.Toplevel(restaurant_window)
            # Again, Toplevel will open an overlapping window, but again, on an overlapping window!
            rest_detail_window.title(f"{park.park_name} Restaurants") # Double Overlapping Window Name
            rest_detail_window.geometry("800x600") # Double Overlapping Window Size
            
            load_logo_image(rest_detail_window, "logo.png") # Add logo image
            
            # Create a simple for loop for each restaurant at a park instead of doing it individually.
            for restaurant in park.restaurants:
                
                def add_dish_window(restaurant=restaurant):
                    add_dish_win = tk.Toplevel(rest_detail_window)
                    # Again, Toplevel will open an overlapping window, but now, on a DOUBLE overlapping window
                    add_dish_win.title("Add Dish") # Triple Overlapping Window Name
                    add_dish_win.geometry("400x320") # Triple Overlapping Window Size

                    load_logo_image(add_dish_win, "logo2.png") # Add logo image
                    tk.Label(add_dish_win, text="Enter Dish Name").pack(pady=5)
                    dish_name_entry = tk.Entry(add_dish_win) # Asks user for Name of Dish
                    dish_name_entry.pack(pady=5)

                    tk.Label(add_dish_win, text="Enter Price").pack(pady=5)
                    price_entry = tk.Entry(add_dish_win) # Asks user for Price of Dish
                    price_entry.pack(pady=5)

                    def add_dish():
                        dish_name = dish_name_entry.get()
                        price = price_entry.get()
                        restaurant.add_dish(dish_name, price) # Dish is created based on input of user
                        tk.Label(add_dish_win, text="Dish Added Successfully", fg="green").pack(pady=5)
                        tk.Label(add_dish_win, text="Reload Restaurant Window To See Updated Menu!", fg="purple").pack(pady=5)

                    tk.Button(add_dish_win, text="Add Dish", command=lambda: add_dish()).pack(pady=10) # Button to add dish

                def show_restaurant_info(restaurant=restaurant):
                    info_window = tk.Toplevel(rest_detail_window) # Overlapping Window
                    info_window.title(f"{restaurant.name} Info") # Overlapping Window Name
                    info_window.geometry("800x600") # Overlapping Window Size
                    
                    load_logo_image(info_window, "logo.png") # Add logo image
                    tk.Label(info_window, text=restaurant.get_restaurant_info(), justify="center", font=("Helvetica", 12)).pack(pady=10)
                    tk.Button(info_window, text="Add Dish", command=lambda: add_dish_window(restaurant)).pack(pady=10)

                tk.Button(rest_detail_window, text=restaurant.name, command=lambda r=restaurant:show_restaurant_info(r)).pack(pady=5)

        for park in disney_parks:
            tk.Button(restaurant_window, text=park.park_name, command=lambda p=park: show_restaurant_details(p)).pack(pady=10)

    def show_shop_management():
        shop_window = tk.Toplevel(emp_root)
        # Again, Toplevel will open an overlapping window!
        shop_window.title("Shop Management") # Overlapping Window Name
        shop_window.geometry("800x600") # Overlapping Window Size

        load_logo_image(shop_window, "logo.png") # Add logo image
        tk.Label(shop_window, text="Select a Park to View Shops", font=("Helvetica", 14)).pack(pady=10)

        def show_shop_details(park):
            shop_detail_window = tk.Toplevel(shop_window)
            # Again, Toplevel will open an overlapping window, but again, on an overlapping window!
            shop_detail_window.title(f"{park.park_name} Shops") # Double Overlapping Window Name
            shop_detail_window.geometry("800x600") # Double Overlapping Window Size

            load_logo_image(shop_detail_window, "logo.png") # Add logo image
            # Create a simple for loop for each shop at a park instead of doing it individually.
            for shop in park.shops:
                def add_item_window(shop=shop):
                    add_item_win = tk.Toplevel(shop_detail_window) 
                    # Again, Toplevel will open an overlapping window, but now, on a DOUBLE overlapping window
                    add_item_win.title("Add Item") # Triple Overlapping Window Name
                    add_item_win.geometry("400x320") # Triple Overlapping Window Size

                    load_logo_image(add_item_win, "logo2.png") # Add logo image
                    tk.Label(add_item_win, text="Enter Item Name").pack(pady=5)
                    item_name_entry = tk.Entry(add_item_win) # Asks user for Name of Item
                    item_name_entry.pack(pady=5)

                    tk.Label(add_item_win, text="Enter Price").pack(pady=5)
                    price_entry = tk.Entry(add_item_win) # Asks user for Price of Item
                    price_entry.pack(pady=5)

                    def add_item():
                        item_name = item_name_entry.get()
                        price = round(float(price_entry.get()), 2)
                        shop.add_item(item_name, price) # Creates Item based on User Input
                        tk.Label(add_item_win, text="Item Added Successfully", fg="green").pack(pady=5)
                        tk.Label(add_item_win, text="Reload Restaurant Window To See Updated Inventory!", fg="purple").pack(pady=5)

                    tk.Button(add_item_win, text="Add Item", command=lambda: add_item()).pack(pady=10) # Button to add Item

                def show_shop_info(shop=shop):
                    info_window = tk.Toplevel(shop_detail_window) # Overlapping Window
                    info_window.title(f"{shop.name} Info") # Overlapping Window Name
                    info_window.geometry("800x600") # Overlapping Window Size
                    
                    load_logo_image(info_window, "logo.png") # Add logo image
                    tk.Label(info_window, text=shop.get_shop_info(), justify="center", font=("Helvetica", 12)).pack(pady=10)
                    tk.Button(info_window, text="Add Item", command=lambda: add_item_window(shop)).pack(pady=10)

                tk.Button(shop_detail_window, text=shop.name, command=lambda s=shop: show_shop_info(s)).pack(pady=5)

        # Create a simple loop for each park instead of doing it individually
        # (This loop contains the for loop above because the command in button below calls the for loop)
        for park in disney_parks:
            tk.Button(shop_window, text=park.park_name, command=lambda p=park: show_shop_details(p)).pack(pady=10)


    def show_element_management():
        element_window = tk.Toplevel(emp_root)
        # Again, Toplevel will open an overlapping window!
        element_window.title("Park Elements") # Overlapping Window Name
        element_window.geometry("800x600") # Overlapping Window Size

        load_logo_image(element_window, "logo.png") # Add logo image
        tk.Label(element_window, text="Select a Park to View Elements", font=("Helvetica", 14)).pack(pady=10)

        def show_element_details(park):
            element_detail_window = tk.Toplevel(element_window)
            # Again, Toplevel will open an overlapping window, but again, on an overlapping window!
            element_detail_window.title(f"{park.park_name} Elements") # Double Overlapping Window Name
            element_detail_window.geometry("800x600") # Double Overlapping Window Size

            load_logo_image(element_detail_window, "logo.png") # Add logo image
        
            # Gather the Required Information to Display on Screen
            # Simple for loop iterating through element names in a park (from parameter)
            details = "\n\n\n\n".join([elem.name for elem in park.elements])
            
            # Display Details in a Single Label
            tk.Label(element_detail_window, text=details, justify="center", font=("Helvetica", 12)).pack(pady=20)

        # Create a simple for loop for each park instead of making each button individually
        for park in disney_parks:
            tk.Button(element_window, text=park.park_name, command=lambda p=park: show_element_details(p)).pack(pady=10)

    # Employee Interface Layout
    
    load_logo_image(emp_root, "logo.png") # Add logo image
    tk.Label(emp_root, text="Disney Employee Interface", font=("Helvetica", 18)).pack(pady=20)
    tk.Button(emp_root, text="Park Overview", command=lambda: show_park_overview(), width=20, height=2).pack(pady=10)
    tk.Button(emp_root, text="Magic Band Info", command=lambda: show_magic_band_management(), width=20, height=2).pack(pady=10)
    tk.Button(emp_root, text="Ride Info", command=lambda: show_ride_management(), width=20, height=2).pack(pady=10)
    tk.Button(emp_root, text="Restaurant Info", command=lambda: show_restaurant_management(), width=20, height=2).pack(pady=10)
    tk.Button(emp_root, text="View Shops", command=lambda: show_shop_management(), width=20, height=2).pack(pady=10)
    tk.Button(emp_root, text="View Elements", command=lambda: show_element_management(), width=20, height=2).pack(pady=10)
    
# ------------------------------------------------------------------

# Guest Interface
def guest_interface():
    
    # Create Employee UI Window
    guest_root = tk.Toplevel()
    guest_root.title("Disney Guest Interface") # Window Name
    guest_root.geometry("1000x700") # Window Size

    def show_park_overview():
        park_window = tk.Toplevel(guest_root)
        # Again, Toplevel will open an overlapping window!
        park_window.title("Park Overview") # Name of Overlapping Window
        park_window.geometry("800x600") # Window Size

        load_logo_image(park_window, "logo.png") # Add logo image
        tk.Label(park_window, text="Select a Park to View Details", font=("Helvetica", 14)).pack(pady=10) # Label on Overlapping Window

        def show_park_details(park):
            detail_window = tk.Toplevel(park_window)
            # Again, Toplevel will open an overlapping window, but now, on an overlapping window!
            detail_window.title(f"{park.park_name} Details") # Name of Double Overlapping Window
            detail_window.geometry("800x600")
            
            # Gather the Required Information to Show on Window
            # In each line, there a for loop, iterating through all rides, restaurants, shops, and elements (RESPECTIVELY)
            details = f"Rides: \n" + "\n".join([ride.ride_name for ride in park.rides]) + "\n\n" \
                      f"Restaurants: \n" + "\n".join([rest.name for rest in park.restaurants]) + "\n\n" \
                      f"Shops: \n" + "\n".join([shop.name for shop in park.shops]) + "\n\n" \
                      f"Elements: \n" + "\n".join([element.name for element in park.elements])

            # In a single label, show all details!
            load_logo_image(detail_window, "logo.png") # Add logo image
            tk.Label(detail_window, text=details, justify="center", font=("Helvetica", 12)).pack(pady=20, padx=20)

        # Rather than individually creating all overlapping windows for the parks, make a simple for loop!
        for park in disney_parks:
            tk.Button(park_window, text=park.park_name, command=lambda p=park: show_park_details(p)).pack(pady=10)
        # In the command=lambda, you're stating p=park and sending it in as a parameter for the command
        
        
        
    load_logo_image(guest_root, "characters.png") # Add characters image
    load_logo_image(guest_root, "logo.png") # Add logo image
    tk.Label(guest_root, text="Disney Guest Interface", font=("Helvetica", 18)).pack(pady=20)
    tk.Button(guest_root, text="Park Overview", command=lambda: show_park_overview(), width=20, height=2).pack(pady=10)
    
    
# Main Program Execution
main_screen()