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

# ------------------------------------------------------------------------------------------------

import tkinter as tk
# from tkinter import ttk # This is just the themed window set

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

        tk.Button(password_window, text="Login", command=validate_password).pack(pady=10) # Login Button

    # Buttons for the Main Window
    tk.Label(root, text="Welcome to the Disney System", font=("Helvetica", 18)).pack(pady=20)
    tk.Button(root, text="Employee Login", command=open_employee_interface, height=2, width=20).pack(pady=10)
    tk.Button(root, text="Guest Login", height=2, width=20).pack(pady=10)  # Placeholder (, command=lambda: pass)

    root.mainloop()

# Employee Interface
def employee_interface():
    
    # Create Employee UI Window
    emp_root = tk.Tk()
    emp_root.title("Disney Employee Interface") # Window Name
    emp_root.geometry("1000x700") # Window Size

    def show_park_overview():
        park_window = tk.Toplevel(emp_root)
        # Again, Toplevel will open an overlapping window!
        park_window.title("Park Overview") # Name of Overlapping Window
        park_window.geometry("800x600") # Window Size

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

        tk.Label(band_window, text="Magic Band Management", font=("Helvetica", 14)).pack(pady=10)

        def view_usage_report():
            report = magic_band_system.generate_usage_report()
            tk.Label(band_window, text=report, font=("Helvetica", 12)).pack(pady=10)

        def provide_new_band():
            tk.Label(band_window, text="Provide a New Magic Band (Simulated)", font=("Helvetica", 12)).pack(pady=10)

        def register_band():
            tk.Label(band_window, text="Register a Magic Band (Simulated)", font=("Helvetica", 12)).pack(pady=10)
            
        # Create Buttons for Magic Band Management Window
        tk.Button(band_window, text="View Usage Report", command=view_usage_report).pack(pady=5)
        tk.Button(band_window, text="Provide New Band", command=provide_new_band).pack(pady=5)
        tk.Button(band_window, text="Register Band", command=register_band).pack(pady=5)

    def show_ride_management():
        ride_window = tk.Toplevel(emp_root)
        # Again, Toplevel will open an overlapping window!
        ride_window.title("Ride Management") # Overlapping Window Name
        ride_window.geometry("800x600") # Overlapping Window Size

        tk.Label(ride_window, text="Select a Park to View Ride Info", font=("Helvetica", 14)).pack(pady=10)

        def show_ride_details(park):
            ride_detail_window = tk.Toplevel(ride_window)
            # Again, Toplevel will open an overlapping window, but again, on an overlapping window!
            ride_detail_window.title(f"{park.park_name} Rides") # Double Overlapping Window Name
            ride_detail_window.geometry("800x600") # Double Overlapping Window Size

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

        tk.Label(restaurant_window, text="Select a Park to View Restaurants", font=("Helvetica", 14)).pack(pady=10)

        def show_restaurant_details(park):
            rest_detail_window = tk.Toplevel(restaurant_window)
            # Again, Toplevel will open an overlapping window, but again, on an overlapping window!
            rest_detail_window.title(f"{park.park_name} Restaurants") # Double Overlapping Window Name
            rest_detail_window.geometry("800x600") # Double Overlapping Window Size
            
            # Create a simple for loop for each restaurant at a park instead of doing it individually.
            for restaurant in park.restaurants:
                def add_dish_window(restaurant):
                    add_dish_win = tk.Toplevel(rest_detail_window)
                    # Again, Toplevel will open an overlapping window, but now, on a DOUBLE overlapping window
                    add_dish_win.title("Add Dish") # Triple Overlapping Window Name
                    add_dish_win.geometry("400x200") # Triple Overlapping Window Size

                    tk.Label(add_dish_win, text="Enter Dish Name").pack(pady=5)
                    dish_name_entry = tk.Entry(add_dish_win) # Asks user for Name of Dish
                    dish_name_entry.pack(pady=5)

                    tk.Label(add_dish_win, text="Enter Price").pack(pady=5)
                    price_entry = tk.Entry(add_dish_win) # Asks user for Price of Dish
                    price_entry.pack(pady=5)

                    def add_dish():
                        dish_name = dish_name_entry.get()
                        price = float(price_entry.get())
                        restaurant.add_dish(dish_name, price) # Dish is created based on input of user
                        tk.Label(add_dish_win, text="Dish Added Successfully", fg="green").pack(pady=5)

                    tk.Button(add_dish_win, text="Add Dish", command=add_dish).pack(pady=10) # Button to add dish

                def show_restaurant_info():
                    info_window = tk.Toplevel(rest_detail_window) # Overlapping Window
                    info_window.title(f"{restaurant.name} Info") # Overlapping Window Name
                    info_window.geometry("800x600") # Overlapping Window Size
                    tk.Label(info_window, text=restaurant.get_restaurant_info(), justify="center", font=("Helvetica", 12)).pack(pady=10)
                    tk.Button(info_window, text="Add Dish", command=lambda: add_dish_window(restaurant)).pack(pady=10)

                tk.Button(rest_detail_window, text=restaurant.name, command=show_restaurant_info).pack(pady=5)

        for park in disney_parks:
            tk.Button(restaurant_window, text=park.park_name, command=lambda p=park: show_restaurant_details(p)).pack(pady=10)

    def show_shop_management():
        shop_window = tk.Toplevel(emp_root)
        # Again, Toplevel will open an overlapping window!
        shop_window.title("Shop Management") # Overlapping Window Name
        shop_window.geometry("800x600") # Overlapping Window Size

        tk.Label(shop_window, text="Select a Park to View Shops", font=("Helvetica", 14)).pack(pady=10)

        def show_shop_details(park):
            shop_detail_window = tk.Toplevel(shop_window)
            # Again, Toplevel will open an overlapping window, but again, on an overlapping window!
            shop_detail_window.title(f"{park.park_name} Shops") # Double Overlapping Window Name
            shop_detail_window.geometry("800x600") # Double Overlapping Window Size

            # Create a simple for loop for each shop at a park instead of doing it individually.
            for shop in park.shops:
                def add_item_window(shop):
                    add_item_win = tk.Toplevel(shop_detail_window) 
                    # Again, Toplevel will open an overlapping window, but now, on a DOUBLE overlapping window
                    add_item_win.title("Add Item") # Triple Overlapping Window Name
                    add_item_win.geometry("400x200") # Triple Overlapping Window Size

                    tk.Label(add_item_win, text="Enter Item Name").pack(pady=5)
                    item_name_entry = tk.Entry(add_item_win) # Asks user for Name of Item
                    item_name_entry.pack(pady=5)

                    tk.Label(add_item_win, text="Enter Price").pack(pady=5)
                    price_entry = tk.Entry(add_item_win) # Asks user for Price of Item
                    price_entry.pack(pady=5)

                    def add_item():
                        item_name = item_name_entry.get()
                        price = float(price_entry.get())
                        shop.add_item(item_name, price) # Creates Item based on User Input
                        tk.Label(add_item_win, text="Item Added Successfully", fg="green").pack(pady=5)

                    tk.Button(add_item_win, text="Add Item", command=add_item).pack(pady=10) # Button to add Item

                def show_shop_info():
                    info_window = tk.Toplevel(shop_detail_window) # Overlapping Window
                    info_window.title(f"{shop.name} Info") # Overlapping Window Name
                    info_window.geometry("800x600") # Overlapping Window Size
                    tk.Label(info_window, text=shop.get_shop_info(), justify="center", font=("Helvetica", 12)).pack(pady=10)
                    tk.Button(info_window, text="Add Item", command=lambda: add_item_window(shop)).pack(pady=10)

                tk.Button(shop_detail_window, text=shop.name, command=show_shop_info).pack(pady=5)

        # Create a simple loop for each park instead of doing it individually
        # (This loop contains the for loop above because the command in button below calls the for loop)
        for park in disney_parks:
            tk.Button(shop_window, text=park.park_name, command=lambda p=park: show_shop_details(p)).pack(pady=10)


    def show_element_management():
        element_window = tk.Toplevel(emp_root)
        # Again, Toplevel will open an overlapping window!
        element_window.title("Park Elements") # Overlapping Window Name
        element_window.geometry("800x600") # Overlapping Window Size

        tk.Label(element_window, text="Select a Park to View Elements", font=("Helvetica", 14)).pack(pady=10)

        def show_element_details(park):
            element_detail_window = tk.Toplevel(element_window)
            # Again, Toplevel will open an overlapping window, but again, on an overlapping window!
            element_detail_window.title(f"{park.park_name} Elements") # Double Overlapping Window Name
            element_detail_window.geometry("800x600") # Double Overlapping Window Size

            # Gather the Required Information to Display on Screen
            # Simple for loop iterating through element names in a park (from parameter)
            details = "\n".join([elem.name for elem in park.elements])
            
            # Display Details in a Single Label
            tk.Label(element_detail_window, text=details, justify="center", font=("Helvetica", 12)).pack(pady=20)

        # Create a simple for loop for each park instead of making each button individually
        for park in disney_parks:
            tk.Button(element_window, text=park.park_name, command=lambda p=park: show_element_details(p)).pack(pady=10)

    # Employee Interface Layout
    tk.Label(emp_root, text="Disney Employee Interface", font=("Helvetica", 18)).pack(pady=20)
    tk.Button(emp_root, text="Park Overview", command=show_park_overview, width=20, height=2).pack(pady=10)
    tk.Button(emp_root, text="Magic Band Info", command=show_magic_band_management, width=20, height=2).pack(pady=10)
    tk.Button(emp_root, text="Ride Info", command=show_ride_management, width=20, height=2).pack(pady=10)
    tk.Button(emp_root, text="Restaurant Info", command=show_restaurant_management, width=20, height=2).pack(pady=10)
    tk.Button(emp_root, text="View Shops", command=show_shop_management, width=20, height=2).pack(pady=10)
    tk.Button(emp_root, text="View Elements", command=show_element_management, width=20, height=2).pack(pady=10)

    emp_root.mainloop()

# Main Program Execution
main_screen()