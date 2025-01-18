# -----------------------------------------------
# Created By: Ali Khan (& Mr. Alexander's Class)
# Date: January 9-19, 2025
# DisneyWorld MagicBandSystem Culminating 
# -----------------------------------------------

from model_classes import *
from park_features import *

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

tk_colours =['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
'indian red', 'saddle brown', 'sandy brown',
'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
'pale violet red', 'maroon', 'medium violet red', 'violet red',
'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
'thistle', 'snow2', 'snow3',
'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',
'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',
'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']

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
    
# Function to Create Back Button on a Window
def back_button(window):
    back_button = tk.Button(window, text="Back", command=lambda: window.withdraw())
    back_button.pack(anchor="n", pady=5, padx=5)
    
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
                
                password_window.withdraw() # This is just going to "collapse" the widget:
                # Rather than destroying, this window is now unmapped and forgotten by the window manager!
                # I can still bring it back with .deiconify() :)
                employee_interface() # If password is correct, redirects you to the Employee UI!
                
            else:
                tk.Label(password_window, text="Incorrect Password", fg="red").pack()
                # (I know it's unnecessary to expect invalid entries, but this helps me when testing code)
                # You can also use Tkinter messagebox for an Error window to come up. That is also very simple
                # However, I wanted to implement code that we have taken up in class to show understanding.

        tk.Button(password_window, text="Login", command=lambda: validate_password()).pack(pady=10) # Login Button
        back_button(password_window)
        
    def open_guest_interface():
        
        id_window = tk.Toplevel(root)
        
        # Toplevel is something we haven't covered, but makes sense. This is crucial because
        # it is used to create a window on top of other windows
        # Learnt and Obtained Understanding from: https://www.geeksforgeeks.org/python-tkinter-toplevel-widget/
        
        id_window.title("Guest Login") # Title for Overlapped Window
        id_window.geometry("300x300") # Size of Window

        load_logo_image(id_window, "logo3.png")
        tk.Label(id_window, text="Enter Guest ID").pack(pady=10) # Asks user to enter Guest ID
        guest_id_entry = tk.Entry(id_window) 
        guest_id_entry.pack()
        
        tk.Label(id_window, text="Enter Your Favourite Colour! (Optional)").pack(pady=10) # Asks user to enter Guest ID
        fav_colour_entry = tk.Entry(id_window) 
        fav_colour_entry.pack()

        def validate_entry():
            
            # Check if Favourite Colour is a (Valid) Tkinter Colour! (For Background) --> Personalization
            if fav_colour_entry.get().lower() in tk_colours:
                fav_colour = (fav_colour_entry.get()).lower()
            else: # If not, no background colour :(
                fav_colour = None
                    
            guest_id = guest_id_entry.get()
            for guest in guests:
                
                if guest.guest_id == guest_id: # Checks to See if Guest Exists!
                    
                    id_window.withdraw() # This is just going to "collapse" the widget:
                    # Rather than destroying, this window is now unmapped and forgotten by the window manager!
                    # I can still bring it back with .deiconify() :)
                    # [This also acts as a solution to the tk.TclError] 
                    guest_interface(guest, fav_colour) # If password is correct, redirects you to the Guest UI!
                    
            else:
                tk.Label(id_window, text="Invalid Identification", fg="red").pack()
                # (I know it's unnecessary to expect invalid entries, but this helps me when testing code)
                # You can also use Tkinter messagebox for an Error window to come up. That is also very simple
                # However, I wanted to implement code that we have taken up in class to show understanding.

        tk.Button(id_window, text="Login", command=lambda: validate_entry()).pack(pady=10) # Login Button
        back_button(id_window)

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
            back_button(detail_window)
            tk.Label(detail_window, text=details, justify="center", font=("Helvetica", 12)).pack(pady=20, padx=20)

        # Rather than individually creating all overlapping windows for the parks, make a simple for loop!
        for park in disney_parks:
            tk.Button(park_window, text=park.park_name, command=lambda p=park: show_park_details(p)).pack(pady=10)
        # In the command=lambda, you're stating p=park and sending it in as a parameter for the command   
        back_button(park_window)
        
    def show_magic_band_management():
        band_window = tk.Toplevel(emp_root)
        # Again, Toplevel will open an overlapping window!
        band_window.title("Magic Band Management") # Overlapping Window Name
        band_window.geometry("800x600") # Overlapping Window Size

        load_logo_image(band_window, "logo.png") # Add logo image
        back_button(band_window)
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
            
            label = tk.Label(create_guest_window, text="")
            label.pack(pady=5)

            def add_guest():
                name = guest_name_entry.get()
                age = guest_age_entry.get()
                if age.isdigit(): # isdigit checks if a string is all numbers!! (BUILT-IN PYTHON FUNCTION)
                    new_guest = Guest(name, int(age)) # Creates New Guest Object
                    guests.append(new_guest) # Adds to list of Guests so Guest ID can be used!
                    label.configure(text=f"Guest created with ID: {new_guest.guest_id}", fg="green")
                    return
                
                label.configure(text=f"Invalid Input", fg="red")

            # Error message, helps me when testing. (Still avoiding messagebox in Employee UI)
            tk.Button(create_guest_window, text="Create Guest", command=lambda: add_guest()).pack(pady=10)
            back_button(create_guest_window)
            
        def provide_new_band():
            new_band_window = tk.Toplevel(band_window)
            # Again, Toplevel will open an overlapping window, but now, on another overlapping window!
            new_band_window.title("Provide New Magic Band") # Double Overlapping Window Name
            new_band_window.geometry("400x370") # Double Overlapping Window Size

            load_logo_image(new_band_window, "logo2.png") # Add logo image
            
            tk.Label(new_band_window, text="Enter Guest ID").pack(pady=5)
            guest_id_entry = tk.Entry(new_band_window) # Asks user for Guest ID
            guest_id_entry.pack(pady=5)

            label = tk.Label(new_band_window, text="")
            label.pack(pady=5)
            label2 = tk.Label(new_band_window, text="")
            label2.pack(pady=5)

            def create_band():
                
                guest_id = guest_id_entry.get()
                for guest in guests:
                    if guest.guest_id == guest_id: # Checks to See if Guest Exists!
                        new_band = MagicBand(guest) # If so, creates object!
                        guest.link_magic_band(new_band)
                        magic_band_system.register_band(new_band)
                        label.configure(text=f"Magic Band {new_band.band_id} created for and linked to {guest.name}", fg="green")
                        label2.configure(text=f"Band {new_band.band_id} automatically registered successfully", fg="blue")
                        return

                # Error message, helps me when testing. (Still avoiding messagebox in Employee UI)
                label.configure(text="Guest not found", fg="red")
                label2.configure(text="")

            tk.Button(new_band_window, text="Create Band", command=lambda: create_band()).pack(pady=10)
            back_button(new_band_window)
            
        def relink_band():
            relink_window = tk.Toplevel(band_window)
            # Again, Toplevel will open an overlapping window, but now, on another overlapping window!
            relink_window.title("Relink MagicBand") # Double Overlapping Window Name
            relink_window.geometry("400x300") # Double Overlapping Window Size

            load_logo_image(relink_window, "logo2.png") # Place the Logo
            
            tk.Label(relink_window, text="Enter Guest ID").pack(pady=5)
            guest_id_entry = tk.Entry(relink_window) # Ask User for Guest ID
            guest_id_entry.pack(pady=5)

            tk.Label(relink_window, text="Enter MagicBand ID to Relink").pack(pady=5)
            band_id_entry = tk.Entry(relink_window) # Ask User for Band ID
            band_id_entry.pack(pady=5)
            
            # Empty Label
            label = tk.Label(relink_window, text="")
            label.pack(pady=5)

            def relink():
                guest_id = guest_id_entry.get()
                band_id = int(band_id_entry.get())

                # Set Needed Variables to None (They Will Change Depending on User Input)
                guest_to_link = None
                band_to_relink = None
                original_owner = None

                # Valid Guest ID --> Valid Guest to Link!
                for guest in guests:
                    if guest.guest_id == guest_id:
                        guest_to_link = guest

                # Valid MagicBand ID --> Valid MagicBand to Relink!
                for band in magic_band_system.registered_bands:
                    if band.band_id == band_id:
                        band_to_relink = band
                        
                        # Looking for Whoever Currently Has this Band
                        for g in guests: 
                            if g.magic_band == band:
                                original_owner = g

                # If there's a valid guest and band, original owner loses their band and guest gets the relinked band!
                if guest_to_link != None and band_to_relink != None:
                    # According to OUR Program's logic, the MagicBands are ALWAYS "assigned"
                    # But if that wasn't the case, the following "if" statement becomes crucial
                    # (Kept it anyways because it makes me comfortable: Knowing an error cannot occur!)
                    if original_owner != None: 
                        original_owner.magic_band = None
                        guest_to_link.magic_band = band_to_relink
                        label.configure(text=f"MagicBand {band_id} linked to {guest_to_link.name}", fg="green")
                        return

                # Error message, helps me when testing. (Still avoiding messagebox in Employee UI)
                label.configure(text="Invalid Input", fg="red")

            tk.Button(relink_window, text="Relink Band", command=lambda: relink()).pack(pady=10)
            back_button(relink_window)
            
        def view_guest_details():
            guest_window = tk.Toplevel(band_window)
            # Again, Toplevel will open an overlapping window!
            guest_window.title("View Guest Details") # Overlapping Window Name
            guest_window.geometry("400x350") # Overlapping Window Size

            load_logo_image(guest_window, "logo2.png") # Add logo image
            back_button(guest_window)
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
                        details = guest.get_profile_summary()
                        info_label.configure(text=details)  # Update the existing label with new guest details
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
            back_button(location_window)
        
        def add_park_ticket():
            ticket_window = tk.Toplevel(band_window)
            # Again, Toplevel will open an overlapping window!
            ticket_window.title("Add Park Ticket") # Overlapping Window Name
            ticket_window.geometry("400x350") # Overlapping Window Size

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
                            if park.park_name.lower() == park_name.lower(): # Checks the name of Park
                                magic_band_system.purchase_park_tickets(band, park)
                                tk.Label(ticket_window, text="Ticket Added Successfully", fg="green").pack(pady=5)
                                return
                            
                # Error message, helps me when testing. (Still avoiding messagebox in Employee UI)
                tk.Label(ticket_window, text="Invalid Band or Park", fg="red").pack(pady=5)

            tk.Button(ticket_window, text="Add Ticket", command=lambda: purchase_ticket()).pack(pady=10)
            back_button(ticket_window)
            
        def view_usage_report():
            report_window = tk.Toplevel(band_window)
            # Again, Toplevel will open an overlapping window!
            report_window.title("View Usage Report") # Overlapping Window Name
            report_window.geometry("400x475") # Overlapping Window Size

            load_logo_image(report_window, "logo2.png") # Add logo image
            back_button(report_window)
            tk.Label(report_window, text="Enter MagicBand ID").pack(pady=5)
            band_id_entry = tk.Entry(report_window) # Asks for Band ID
            band_id_entry.pack(pady=5)
            
            tk.Button(report_window, text="View Magic Band Report", command=lambda: display_report()).pack(pady=10)
            info_label = tk.Label(report_window, text="")
            info_label.pack(pady=10)

            def display_report():
                band_id = int(band_id_entry.get())
                for band in magic_band_system.registered_bands:
                    if band.band_id == band_id: # Checks if the Magic Band is Registered
                        report = "\n".join(band.useage_history) # Had to figure out a way to not show the {}, [] (etc.) from the list
                        
                        # If the Band has been Used
                        if band.useage_history != []:
                            info_label.configure(text = report, fg = "black")  # Update the existing label with new Band Report
                            return
                        
                        # If the Band is Newly Created and Unused
                        else:
                            info_label.configure(text = "No Information Found! :(", fg = "black")  # Update the existing label with new Band Report
                            return
                
                # Error message, helps me when testing. (Still avoiding messagebox in Employee UI)
                info_label.configure(text = "Band not found", fg="red")

        def show_system_report():
            system_report_window = tk.Toplevel(band_window)
            # Again, Toplevel will open an overlapping window, but now, on an overlapping window!
            system_report_window.title(f"Magicband System Report") # Name of Double Overlapping Window
            system_report_window.geometry("400x200")
            
            # Gather the Required Information to Show on Window
            # In each line, there a for loop, iterating through all rides, restaurants, shops, and elements (RESPECTIVELY)
            system_report = magic_band_system.generate_usage_report()

            # In a single label, show the MagicBand System Report!
            load_logo_image(system_report_window, "logo2.png") # Add logo image
            tk.Label(system_report_window, text=system_report, justify="center", font=("Helvetica", 12)).pack(pady=20, padx=20)
            back_button(system_report_window)

        # Create Buttons for MagicBand Management
        tk.Button(band_window, text="Create New Guest", command=lambda: create_new_guest()).pack(pady=5)
        tk.Button(band_window, text="Provide New Band", command=lambda: provide_new_band()).pack(pady=5)
        tk.Button(band_window, text="Relink Band", command=lambda: relink_band()).pack(pady=5)
        tk.Button(band_window, text="View Guest Details", command=lambda: view_guest_details()).pack(pady=5)
        tk.Button(band_window, text="Find Band/Guest Location", command=lambda: find_location()).pack(pady=5)
        tk.Button(band_window, text="Add Park Ticket", command=lambda: add_park_ticket()).pack(pady=5)
        tk.Button(band_window, text="View Usage Reports", command=lambda: view_usage_report()).pack(pady=5)
        tk.Button(band_window, text="View System Report", command=lambda: show_system_report()).pack(pady=5)

    def show_ride_management():
        ride_window = tk.Toplevel(emp_root)
        # Again, Toplevel will open an overlapping window!
        ride_window.title("Ride Management") # Overlapping Window Name
        ride_window.geometry("800x600") # Overlapping Window Size

        load_logo_image(ride_window, "logo.png") # Add logo image
        back_button(ride_window)
        tk.Label(ride_window, text="Select a Park to View Ride Queue & Info", font=("Helvetica", 14)).pack(pady=10)

        def show_ride_details(park):
            ride_detail_window = tk.Toplevel(ride_window)
            # Again, Toplevel will open an overlapping window, but again, on an overlapping window!
            ride_detail_window.title(f"{park.park_name} Rides") # Double Overlapping Window Name
            ride_detail_window.geometry("600x450") # Double Overlapping Window Size

            load_logo_image(ride_detail_window, "logo.png") # Add logo image
            back_button(ride_detail_window)
            # Create a simple for loop for each ride at a park instead of doing it individually
            for ride in park.rides:
                tk.Button(ride_detail_window, text=ride.ride_name, command=lambda r=ride: new_info(r)).pack(pady=5)
                # Here, the command isn't a function or method. It is itself a Label being packed onto the window!
                # Rephrase: This button is packed on the screen. When clicked, it packs a label!
                
            # Labels BELOW Buttons    
            ride_info_label = tk.Label(ride_detail_window, text="", justify="left", font=("Helvetica", 10))
            ride_info_label.pack(pady=10)
            ride_queue_label = tk.Label(ride_detail_window, text="", justify="left", font=("Helvetica", 10))
            ride_queue_label.pack(pady=10)
            
            # Function to Rewrite Label (Depending on Selected Ride)
            def new_info(r):
                ride_info_label.configure(text=r.get_ride_info())
                ride_queue_label.configure(text=f"\nQueue Length: {len(r.queue)}")
            
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
        back_button(restaurant_window)
        tk.Label(restaurant_window, text="Select a Park to View Restaurants", font=("Helvetica", 14)).pack(pady=10)

        def show_restaurant_details(park):
            rest_detail_window = tk.Toplevel(restaurant_window)
            # Again, Toplevel will open an overlapping window, but again, on an overlapping window!
            rest_detail_window.title(f"{park.park_name} Restaurants") # Double Overlapping Window Name
            rest_detail_window.geometry("800x600") # Double Overlapping Window Size
            
            load_logo_image(rest_detail_window, "logo.png") # Add logo image
            back_button(rest_detail_window)
            # Create a simple for loop for each restaurant at a park instead of doing it individually.
            for restaurant in park.restaurants:
                
                def add_dish_window(restaurant=restaurant):
                    add_dish_win = tk.Toplevel(rest_detail_window)
                    # Again, Toplevel will open an overlapping window, but now, on a DOUBLE overlapping window
                    add_dish_win.title("Add Dish") # Triple Overlapping Window Name
                    add_dish_win.geometry("400x350") # Triple Overlapping Window Size

                    load_logo_image(add_dish_win, "logo2.png") # Add logo image
                    tk.Label(add_dish_win, text="Enter Dish Name").pack(pady=5)
                    dish_name_entry = tk.Entry(add_dish_win) # Asks user for Name of Dish
                    dish_name_entry.pack(pady=5)

                    tk.Label(add_dish_win, text="Enter Price").pack(pady=5)
                    price_entry = tk.Entry(add_dish_win) # Asks user for Price of Dish
                    price_entry.pack(pady=5)
                    back_button(add_dish_win)

                    def add_dish():
                        dish_name = dish_name_entry.get()
                        price = price_entry.get()
                        if dish_name != "" and price != "":
                            restaurant.add_dish(dish_name, price) # Dish is created based on input of user
                            tk.Label(add_dish_win, text="Dish Added Successfully", fg="green").pack(pady=5)
                            tk.Label(add_dish_win, text="Reload Restaurant Window To See Updated Menu!", fg="purple").pack(pady=5)
                            return
                        
                        tk.Label(add_dish_win, text = "Invalid Input", fg="red")

                    tk.Button(add_dish_win, text="Add Dish", command=lambda: add_dish()).pack(pady=10) # Button to add dish

                def show_restaurant_info(restaurant=restaurant):
                    info_window = tk.Toplevel(rest_detail_window) # Overlapping Window
                    info_window.title(f"{restaurant.name} Info") # Overlapping Window Name
                    info_window.geometry("800x600") # Overlapping Window Size
                    
                    load_logo_image(info_window, "logo.png") # Add logo image
                    tk.Label(info_window, text=restaurant.get_restaurant_info(), justify="center", font=("Helvetica", 12)).pack(pady=10)
                    tk.Button(info_window, text="Add Dish", command=lambda: add_dish_window(restaurant)).pack(pady=10)
                    back_button(info_window)

                tk.Button(rest_detail_window, text=restaurant.name, command=lambda r=restaurant:show_restaurant_info(r)).pack(pady=5)

        # Create a simple loop for each park instead of doing it individually
        # (This loop contains the for loop above because the command in button below calls the for loop)
        for park in disney_parks:
            tk.Button(restaurant_window, text=park.park_name, command=lambda p=park: show_restaurant_details(p)).pack(pady=10)

    def show_shop_management():
        shop_window = tk.Toplevel(emp_root)
        # Again, Toplevel will open an overlapping window!
        shop_window.title("Shop Management") # Overlapping Window Name
        shop_window.geometry("800x600") # Overlapping Window Size

        load_logo_image(shop_window, "logo.png") # Add logo image
        back_button(shop_window)
        tk.Label(shop_window, text="Select a Park to View Shops", font=("Helvetica", 14)).pack(pady=10)

        def show_shop_details(park):
            shop_detail_window = tk.Toplevel(shop_window)
            # Again, Toplevel will open an overlapping window, but again, on an overlapping window!
            shop_detail_window.title(f"{park.park_name} Shops") # Double Overlapping Window Name
            shop_detail_window.geometry("800x600") # Double Overlapping Window Size

            load_logo_image(shop_detail_window, "logo.png") # Add logo image
            back_button(shop_detail_window)
            # Create a simple for loop for each shop at a park instead of doing it individually.
            for shop in park.shops:
                def add_item_window(shop=shop):
                    add_item_win = tk.Toplevel(shop_detail_window) 
                    # Again, Toplevel will open an overlapping window, but now, on a DOUBLE overlapping window
                    add_item_win.title("Add Item") # Triple Overlapping Window Name
                    add_item_win.geometry("400x350") # Triple Overlapping Window Size

                    load_logo_image(add_item_win, "logo2.png") # Add logo image
                    tk.Label(add_item_win, text="Enter Item Name").pack(pady=5)
                    item_name_entry = tk.Entry(add_item_win) # Asks user for Name of Item
                    item_name_entry.pack(pady=5)

                    tk.Label(add_item_win, text="Enter Price").pack(pady=5)
                    price_entry = tk.Entry(add_item_win) # Asks user for Price of Item
                    price_entry.pack(pady=5)
                    back_button(add_item_win)

                    def add_item():
                        item_name = item_name_entry.get()
                        price = price_entry.get()
                        if item_name != "" and price != "":
                            shop.add_item(item_name, price) # Creates Item based on User Input
                            tk.Label(add_item_win, text="Item Added Successfully", fg="green").pack(pady=5)
                            tk.Label(add_item_win, text="Reload Shop Window To See Updated Inventory!", fg="purple").pack(pady=5)
                            return
                        
                        tk.Label(add_item_win, text = "Invalid Input", fg="red")

                    tk.Button(add_item_win, text="Add Item", command=lambda: add_item()).pack(pady=10) # Button to add Item

                def show_shop_info(shop=shop):
                    info_window = tk.Toplevel(shop_detail_window) # Overlapping Window
                    info_window.title(f"{shop.name} Info") # Overlapping Window Name
                    info_window.geometry("800x600") # Overlapping Window Size
                    
                    load_logo_image(info_window, "logo.png") # Add logo image
                    tk.Label(info_window, text=shop.get_shop_info(), justify="center", font=("Helvetica", 12)).pack(pady=10)
                    tk.Button(info_window, text="Add Item", command=lambda: add_item_window(shop)).pack(pady=10)
                    back_button(info_window)

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
        back_button(element_window)
        tk.Label(element_window, text="Select a Park to View Elements", font=("Helvetica", 14)).pack(pady=10)

        def show_element_details(park):
            element_detail_window = tk.Toplevel(element_window)
            # Again, Toplevel will open an overlapping window, but again, on an overlapping window!
            element_detail_window.title(f"{park.park_name} Elements") # Double Overlapping Window Name
            element_detail_window.geometry("800x600") # Double Overlapping Window Size

            load_logo_image(element_detail_window, "logo.png") # Add logo image
            back_button(element_detail_window)
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
    tk.Button(emp_root, text="Rides: Queue & Info", command=lambda: show_ride_management(), width=20, height=2).pack(pady=10)
    tk.Button(emp_root, text="Restaurant Info", command=lambda: show_restaurant_management(), width=20, height=2).pack(pady=10)
    tk.Button(emp_root, text="View Shops", command=lambda: show_shop_management(), width=20, height=2).pack(pady=10)
    tk.Button(emp_root, text="View Elements", command=lambda: show_element_management(), width=20, height=2).pack(pady=10)
    back_button(emp_root)
    
# ------------------------------------------------------------------

# Guest Interface
def guest_interface(guest, fav_colour):
    
    # Create Employee UI Window
    guest_root = tk.Toplevel(bg=fav_colour if fav_colour else None)
    guest_root.title("Disney Guest Interface") # Window Name
    guest_root.geometry("1000x800") # Window Size

    def show_park_overview():
        park_window = tk.Toplevel(guest_root, bg=fav_colour if fav_colour else None)
        # Again, Toplevel will open an overlapping window!
        park_window.title("Park Overview") # Name of Overlapping Window
        park_window.geometry("800x600") # Window Size

        load_logo_image(park_window, "logo.png") # Add logo image
        back_button(park_window)
        tk.Label(park_window, text="Select a Park to View Details", bg=fav_colour if fav_colour else None, font=("Helvetica", 14)).pack(pady=10) # Label on Overlapping Window

        def show_park_details(park):
            detail_window = tk.Toplevel(park_window, bg=fav_colour if fav_colour else None)
            # Again, Toplevel will open an overlapping window, but now, on an overlapping window!
            detail_window.title(f"{park.park_name} Details") # Name of Double Overlapping Window
            detail_window.geometry("800x600") # Size of Double Overlapping Window
            
            # Gather the Required Information to Show on Window
            # In each line, there a for loop, iterating through all rides, restaurants, shops, and elements (RESPECTIVELY)
            details = f"Rides: \n" + "\n".join([ride.ride_name for ride in park.rides]) + "\n\n" \
                      f"Restaurants: \n" + "\n".join([rest.name for rest in park.restaurants]) + "\n\n" \
                      f"Shops: \n" + "\n".join([shop.name for shop in park.shops]) + "\n\n" \
                      f"Elements: \n" + "\n".join([element.name for element in park.elements])

            # In a single label, show all details!
            load_logo_image(detail_window, "logo.png") # Add logo image
            back_button(detail_window)
            tk.Label(detail_window, text=details, bg=fav_colour if fav_colour else None, justify="center", font=("Helvetica", 12)).pack(pady=20, padx=20)

        # Rather than individually creating all overlapping windows for the parks, make a simple for loop!
        for park in disney_parks:
            tk.Button(park_window, text=park.park_name, command=lambda p=park: show_park_details(p)).pack(pady=10)
        # In the command=lambda, you're stating p=park and sending it in as a parameter for the command
        
    def show_my_account(guest):
        account_window = tk.Toplevel(guest_root, bg=fav_colour if fav_colour else None)
        # Again, Toplevel will open an overlapping window!
        account_window.title("My Magic Band") # Name of Overlapping Window
        account_window.geometry("400x400") # Window Size
        
        load_logo_image(account_window, "logo2.png") # Add logo image
        tk.Label(account_window, text="My Account", bg=fav_colour if fav_colour else None, font=("Helvetica", 16)).pack(pady=10)

        # Personal Details Button
        def view_personal_details():
            details_window = tk.Toplevel(account_window, bg=fav_colour if fav_colour else None)
            # Again, Toplevel will open an overlapping window, but now, on an overlapping window!
            details_window.title("Personal Details") # Name of Double Overlapping Window
            details_window.geometry("400x300") # Size of Double Overlapping Window
            
            load_logo_image(details_window, "logo2.png") # Add logo image
            details = guest.get_profile_summary()
            tk.Label(details_window, text=details, bg=fav_colour if fav_colour else None, justify="left", font=("Helvetica", 12)).pack(pady=20)
            back_button(details_window)

        # View Location Button
        def view_location():
            location_window = tk.Toplevel(account_window, bg=fav_colour if fav_colour else None)
            # Again, Toplevel will open an overlapping window, but now, on an overlapping window!
            location_window.title("Current Location") # Name of Double Overlapping Window
            location_window.geometry("400x300") # Size of Double Overlapping Window
            
            load_logo_image(location_window, "logo2.png") # Add logo image
            
            # Check if there's a Band AND The Band Has Location
            location = guest.magic_band.current_location if guest.magic_band and guest.magic_band.current_location else "Unknown"
            tk.Label(location_window, text=f"Current Location: {location}", bg=fav_colour if fav_colour else None, justify="center", font=("Helvetica", 12)).pack(pady=20)
            back_button(location_window)

        # Add Preferences Button
        def add_preferences():
            preferences_window = tk.Toplevel(account_window, bg=fav_colour if fav_colour else None)
            # Again, Toplevel will open an overlapping window, but now, on an overlapping window!
            preferences_window.title("Add Preferences") # Name of Double Overlapping Window
            preferences_window.geometry("400x300") # Size of Double Overlapping Window
            
            load_logo_image(preferences_window, "logo2.png") # Add logo image

            tk.Label(preferences_window, text="Enter Your Preferences", bg=fav_colour if fav_colour else None).pack(pady=10)
            preferences_entry = tk.Entry(preferences_window)
            preferences_entry.pack(pady=10)

            def update_preferences():
                preference = preferences_entry.get()
                if preference:
                    guest.update_preferences(preference)
                    tk.Label(preferences_window, text="Preferences Updated!", bg=fav_colour if fav_colour else None, fg="green").pack(pady=5)
                else:
                    tk.Label(preferences_window, text="Please enter a preference.", bg=fav_colour if fav_colour else None, fg="red").pack(pady=5)

            tk.Button(preferences_window, text="Add", command=lambda: update_preferences()).pack(pady=10)
            back_button(preferences_window)
            
        tk.Button(account_window, text="View Personal Details", command=lambda: view_personal_details()).pack(pady=10)
        tk.Button(account_window, text="View Location", command=lambda: view_location()).pack(pady=10)
        tk.Button(account_window, text="Add Preferences", command=lambda: add_preferences()).pack(pady=10)
        back_button(account_window)
        
    def rides():
        ride_window = tk.Toplevel(guest_root, bg=fav_colour if fav_colour else None)
        # Again, Toplevel will open an overlapping window!
        ride_window.title("Ride Management") # Overlapping Window Name
        ride_window.geometry("800x600") # Overlapping Window Size

        load_logo_image(ride_window, "logo.png") # Add logo image
        back_button(ride_window)
        tk.Label(ride_window, text="Select a Park to View Ride Queue & Info", bg=fav_colour if fav_colour else None, font=("Helvetica", 14)).pack(pady=10)

        def show_ride_details(park):
            ride_detail_window = tk.Toplevel(ride_window, bg=fav_colour if fav_colour else None)
            # Again, Toplevel will open an overlapping window, but again, on an overlapping window!
            ride_detail_window.title(f"{park.park_name} Rides") # Double Overlapping Window Name
            ride_detail_window.geometry("600x450") # Double Overlapping Window Size

            load_logo_image(ride_detail_window, "logo.png") # Add logo image
            back_button(ride_detail_window)
            # Create a simple for loop for each ride at a park instead of doing it individually
            for ride in park.rides:
                tk.Button(ride_detail_window, text=ride.ride_name, command=lambda r=ride: new_info(r)).pack(pady=5)
                # Here, the command isn't a function or method. It is itself a Label being packed onto the window!
                # Rephrase: This button is packed on the screen. When clicked, it packs a label!
                
            # Labels BELOW Buttons    
            ride_info_label = tk.Label(ride_detail_window, text="", bg=fav_colour if fav_colour else None, justify="left", font=("Helvetica", 10))
            ride_info_label.pack(pady=10)
            ride_queue_label = tk.Label(ride_detail_window, text="", bg=fav_colour if fav_colour else None, justify="left", font=("Helvetica", 10))
            ride_queue_label.pack(pady=10)
            
            # Function to Rewrite Label (Depending on Selected Ride)
            def new_info(r):
                ride_info_label.configure(text=r.get_ride_info())
                ride_queue_label.configure(text=f"\nQueue Length: {len(r.queue)}")
            
        # Create a simple for loop for each park instead of doing it individually.
        # (This loop contains the for loop above because the command in button below calls the for loop)
        for park in disney_parks:
            tk.Button(ride_window, text=park.park_name, command=lambda p=park: show_ride_details(p)).pack(pady=5)
        
    def restaurants():
        restaurant_window = tk.Toplevel(guest_root, bg=fav_colour if fav_colour else None)
        # Again, Toplevel will open an overlapping window!
        restaurant_window.title("Restaurant Management") # Overlapping Window Name
        restaurant_window.geometry("800x600") # Overlapping Window Size

        load_logo_image(restaurant_window, "logo.png") # Add logo image
        back_button(restaurant_window)
        tk.Label(restaurant_window, text="Select a Park to View Restaurants", bg=fav_colour if fav_colour else None, font=("Helvetica", 14)).pack(pady=10)

        def show_restaurant_details(park):
            rest_detail_window = tk.Toplevel(restaurant_window, bg=fav_colour if fav_colour else None)
            # Again, Toplevel will open an overlapping window, but again, on an overlapping window!
            rest_detail_window.title(f"{park.park_name} Restaurants") # Double Overlapping Window Name
            rest_detail_window.geometry("800x600") # Double Overlapping Window Size
            
            load_logo_image(rest_detail_window, "logo.png") # Add logo image
            back_button(rest_detail_window)
            # Create a simple for loop for each restaurant at a park instead of doing it individually.
            for restaurant in park.restaurants:

                def show_restaurant_info(restaurant=restaurant):
                    info_window = tk.Toplevel(rest_detail_window, bg=fav_colour if fav_colour else None) # Overlapping Window
                    info_window.title(f"{restaurant.name} Info") # Overlapping Window Name
                    info_window.geometry("800x600") # Overlapping Window Size
                    
                    load_logo_image(info_window, "logo.png") # Add logo image
                    tk.Label(info_window, text=restaurant.get_restaurant_info(), bg=fav_colour if fav_colour else None, justify="center", font=("Helvetica", 12)).pack(pady=10)
                    back_button(info_window)

                tk.Button(rest_detail_window, text=restaurant.name, command=lambda r=restaurant:show_restaurant_info(r)).pack(pady=5)

        # Create a simple loop for each park instead of doing it individually
        # (This loop contains the for loop above because the command in button below calls the for loop)
        for park in disney_parks:
            tk.Button(restaurant_window, text=park.park_name, command=lambda p=park: show_restaurant_details(p)).pack(pady=10)      
        
    def shops():
        shop_window = tk.Toplevel(guest_root, bg=fav_colour if fav_colour else None)
        # Again, Toplevel will open an overlapping window!
        shop_window.title("Shop Management") # Overlapping Window Name
        shop_window.geometry("800x600") # Overlapping Window Size

        load_logo_image(shop_window, "logo.png") # Add logo image
        back_button(shop_window)
        tk.Label(shop_window, text="Select a Park to View Shops", bg=fav_colour if fav_colour else None, font=("Helvetica", 14)).pack(pady=10)

        def show_shop_details(park):
            shop_detail_window = tk.Toplevel(shop_window, bg=fav_colour if fav_colour else None)
            # Again, Toplevel will open an overlapping window, but again, on an overlapping window!
            shop_detail_window.title(f"{park.park_name} Shops") # Double Overlapping Window Name
            shop_detail_window.geometry("800x600") # Double Overlapping Window Size

            load_logo_image(shop_detail_window, "logo.png") # Add logo image
            back_button(shop_detail_window)
            # Create a simple for loop for each shop at a park instead of doing it individually.
            for shop in park.shops:

                def show_shop_info(shop=shop):
                    info_window = tk.Toplevel(shop_detail_window, bg=fav_colour if fav_colour else None) # Overlapping Window
                    info_window.title(f"{shop.name} Info") # Overlapping Window Name
                    info_window.geometry("800x600") # Overlapping Window Size
                    
                    load_logo_image(info_window, "logo.png") # Add logo image
                    tk.Label(info_window, text=shop.get_shop_info(), bg=fav_colour if fav_colour else None, justify="center", font=("Helvetica", 12)).pack(pady=10)
                    back_button(info_window)

                tk.Button(shop_detail_window, text=shop.name, command=lambda s=shop: show_shop_info(s)).pack(pady=5)

        # Create a simple loop for each park instead of doing it individually
        # (This loop contains the for loop above because the command in button below calls the for loop)
        for park in disney_parks:
            tk.Button(shop_window, text=park.park_name, command=lambda p=park: show_shop_details(p)).pack(pady=10)        
        
    def elements():
        element_window = tk.Toplevel(guest_root, bg=fav_colour if fav_colour else None)
        # Again, Toplevel will open an overlapping window!
        element_window.title("Park Elements") # Overlapping Window Name
        element_window.geometry("800x600") # Overlapping Window Size

        load_logo_image(element_window, "logo.png") # Add logo image
        back_button(element_window)
        tk.Label(element_window, text="Select a Park to View Elements", bg=fav_colour if fav_colour else None, font=("Helvetica", 14)).pack(pady=10)

        def show_element_details(park):
            element_detail_window = tk.Toplevel(element_window, bg=fav_colour if fav_colour else None)
            # Again, Toplevel will open an overlapping window, but again, on an overlapping window!
            element_detail_window.title(f"{park.park_name} Elements") # Double Overlapping Window Name
            element_detail_window.geometry("800x600") # Double Overlapping Window Size

            load_logo_image(element_detail_window, "logo.png") # Add logo image
            back_button(element_detail_window)
            # Gather the Required Information to Display on Screen
            # Simple for loop iterating through element names in a park (from parameter)
            details = "\n\n\n\n".join([elem.name for elem in park.elements])
            
            # Display Details in a Single Label
            tk.Label(element_detail_window, text=details, bg=fav_colour if fav_colour else None, justify="center", font=("Helvetica", 12)).pack(pady=20)

        # Create a simple for loop for each park instead of making each button individually
        for park in disney_parks:
            tk.Button(element_window, text=park.park_name, command=lambda p=park: show_element_details(p)).pack(pady=10)   
    
    if guest.name[0].lower() in "abcdef":
        load_logo_image(guest_root, "mickey.png") # Add characters image
    elif guest.name[0].lower() in "ghijk":
        load_logo_image(guest_root, "goofy.png") # Add characters image
    elif guest.name[0].lower() in "lmnop":
        load_logo_image(guest_root, "genie.png") # Add characters image
    elif guest.name[0].lower() in "qrstu":
        load_logo_image(guest_root, "stitch.png") # Add characters image
    else: # If name starts with VWXYZ
        load_logo_image(guest_root, "simba.png") # Add characters image
    tk.Label(guest_root, text=f"Welcome, {guest.name}!", font=("Helvetica", 11), bg=fav_colour if fav_colour else None).pack()
    
    load_logo_image(guest_root, "logo.png") # Add logo image
    tk.Label(guest_root, text="Disney Guest Interface", font=("Helvetica", 18), bg=fav_colour if fav_colour else None).pack()
    tk.Button(guest_root, text="My Magic Band", command=lambda: show_my_account(guest), width=20, height=2).pack(pady=10)
    tk.Button(guest_root, text="Park Overview", command=lambda: show_park_overview(), width=20, height=2).pack(pady=10)
    tk.Button(guest_root, text="Rides: Queue & Info", command=lambda: rides(), width=20, height=2).pack(pady=10)
    tk.Button(guest_root, text="Restaurant Info", command=lambda: restaurants(), width=20, height=2).pack(pady=10)
    tk.Button(guest_root, text="View Shops", command=lambda: shops(), width=20, height=2).pack(pady=10)
    tk.Button(guest_root, text="View Elements", command=lambda: elements(), width=20, height=2).pack(pady=10)
    back_button(guest_root)
    
    
# Main Program Execution
main_screen()