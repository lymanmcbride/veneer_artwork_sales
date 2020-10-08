clients = {}
artworks = {}
#programs
def main():
    boot()
    main_menu()

#greetings
def boot():
    print("""
    Hello and welcome to the marketplace.
    Our system holds a current record of works of art and clients.
    Using our system, you may add works of art and clients to the system database,
    label works of art as 'for sale', and sell them to a new client.
    """)

def main_menu():
    main_choice = input("""
    What would you like to do?
    a: view artworks currently in the system
    b: view clients currently in the system
    c: add something to the system
    d: track a sale
    e: exit
    """).lower()
    if main_choice == "a":
        view_art()
        main_menu()
    elif main_choice == "b":
        view_clients()
        main_menu()
    elif main_choice == "c":
        change_choice()
    elif main_choice == "d":
        market_place()
    elif main_choice == "e":
        print("Thank you for using our system! Have an excellent day.")
    else:
        print("Please choose from one of the options by typing only the letter of your chosen option")
        main_menu()

#menu options
def change_choice():
    client_or_art = input("""
    What would you like to do?
    a. Add a client
    b. Add a piece of art
    """).lower()
    if client_or_art == "a":
        make_client()
        main_menu()
    elif client_or_art == "b":
        make_art()
        main_menu()
    else:
        print('Please input either "a" for add client, or "b" for add art')
        change_choice()

def view_art():
    for key in artworks.keys():
        art = artworks[key]
        print ("{} \n {} \n Owned by {}.\n".format(art.title, art.artist, art.owner))
    print("\n")

def view_clients():
    for key in clients.keys():
        print (clients[key])
    print("\n")


def market_place():
    print("The following artworks are currently for sale on the marketplace:")
    if veneer.listings != []:
        for art in veneer.listings:
            print(art)
    else:
        print("Nothing in the marketplace yet!")
    buy_or_list = input("""\n
    What would you like to do?
    a. Buy  from the marketplace
    b. List an artwork for sale
    """).lower()
    if buy_or_list == "a":
        if veneer.listings == []:
            print("There is nothing on the marketplace yet. Try listing something!")
            market_place()
        buy()
        main_menu()
    if buy_or_list == "b":
        sell()
        main_menu()
#Sell and Buy functions:
def sell():
    for key in clients.keys():
        print (clients[key].name)
    client_name = input("What is the name of the seller? Please choose from the above options\n").lower()
    if client_name in clients.keys():
        client = clients[client_name]
        print("\n\n" + client_name.title(), "owns the following artworks:")
        for key in artworks.keys():
            art = artworks[key]
            if art.owner == client:
                print("{}\n{}\n".format(art.title, art.artist))
        artwork_title = input("\nWhat is the entire title of the art being sold?\n").lower()
        if artwork_title in artworks.keys():
            artwork = artworks[artwork_title]
        price = int(input("What is the asking price? (numbers only)\n"))
        client.sell_artwork(artwork, price)
        return
    else:
        print("That name isn't in our list of clients")

def buy():
    for key in clients.keys():
        print (clients[key].name)
    client_name = input("What is the name of the buyer? Please choose from the above options\n").lower()
    if client_name in clients.keys():
        client = clients[client_name]
        artwork_title = input("What is the entire title of the art being sold?\n").lower()
        if artwork_title in artworks.keys():
            artwork = artworks[artwork_title]
        client.buy_artwork(artwork)
    else:
        add = input("That name isn't in our list of clients, would you like to add them now? y/n\n").lower()
        if add == "y":
            make_client()
        else:
            go_back = input("Would you like to input a new client? y/n").lower()
            if go_back == "y":
                buy()
            else:
                return


#instatiaton functions
def make_art(artist = None, title = None, medium = None, year = None, owner = None):
    if title == None:
        artist, title, medium, year, owner = get_artwork_information()
    key = title.lower()
    if key not in artworks:
        artworks[key] = Art(artist, title, medium, year, owner)
        print("Successfully added {}\'s {} to the database!".format(artist, title))
    else:
        print ("That artwork is already in the system")

def make_client(name = None, location = None, museum = None):
    if name == None:
        name, location, museum = get_client_information()
    key = name.lower()
    if key not in clients:
        clients[key] = Client(name, location, museum)
        print("Successfully added {} to the database!".format(name))

    else:
        print ("That client is already in the system.")

#getting functions:
def get_artwork_information():
    artist = input("Who is the artist?\n")
    title = input("What is the title of the work?\n")
    medium = input("What is the medium (ie: oil on canvas, watercolor, etc.)\n")
    year = int(input("What year was the artwork made?\n"))
    print("\n\n\nCurrent Clients:")
    view_clients()
    owner = input("Who owns the artwork? Type the name (not location) from the list above.\n")
    key = owner.lower()
    if key in clients:
        owner = clients[key]
        return artist, title, medium, year, owner
    else:
        next_step = input('That owner is not in our list of clientel. To add a new client type "c". To try again type "a". To do something else type "e"')
        if next_step.lower() == "c":
            make_client()
        elif next_step.lower() == "a":
            make_art()
        else:
            main_menu()


def get_client_information():
    name = input("Type the name of the client (if the client is an organization, type the name of the organization.)\n")
    location = input("Where are you located?\n")
    museum = input("Is the client a museum? y/n\n")
    if museum == "y":
        museum = True
    else:
        museum = False
    return name, location, museum

#Class Definitions
class Art:
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner
  def __repr__(self):
    return "{name}. \"{art}\". {year}, {medium}. {owner_name}, {owner_location}".format(name = self.artist, art = self.title, year = self.year, medium = self.medium, owner_name = self.owner.name, owner_location = self.owner.location)
class Marketplace:
  def __init__(self):
    self.listings = []
  def add_listing(self, new_listing):
    self.listings.append(new_listing)
  def remove_listing(self, listing):
    self.listings.remove(listing)
  def show_listings(self):
    for item in self.listings:
      print (item)
class Client:
  def __init__(self, name, location, is_museum = False):
    self.name = name
    self.location = location
    self.is_museum = is_museum
  def __repr__(self):
    return "{}, {}".format(self.name, self.location)
  def sell_artwork(self, artwork, price):
    if artwork.owner == self:
      new_listing = Listing(artwork, price, self.name)
      veneer.add_listing(new_listing)
    else:
      print("{} doesn't own {}".format(self.name, artwork.title))
      return
  def buy_artwork(self, artwork):
    if artwork.owner != self:
      art_listing = None
      for listing in veneer.listings:
        if listing.art == artwork:
          art_listing = listing
          break
      if art_listing != None:
        art_listing.art.owner = self
        veneer.remove_listing(art_listing)
class Listing:
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller
  def __repr__(self):
    return "{} ${} (USD)".format(self.art, self.price)

#marketplace and clients
veneer = Marketplace()

#default entries
def make_client_default(name = None, location = None, museum = None):
    key = name.lower()
    clients[key] = Client(name, location, museum)

def make_art_default(artist = None, title = None, medium = None, year = None, owner = None):
    key = title.lower()
    artworks[key] = Art(artist, title, medium, year, owner)

default_clients = [["Edytta Halpirt", "Private Collection", False], ["The MOMA", "New York", True], ["Yale", "New Haven, Ct.", True], ["BYU", "Provo, Ut", True]]
for client in default_clients:
    make_client_default(client[0], client[1], client[2])

default_art = [["Vincent van Gogh", "Orchard Bordered by Cypresses", "oil on canvas", 1888, clients["yale"]], ["Toyin Ojih Odutola", "Projection Enclave", "Pastel, charcoal, and pencil on paper", 2018, clients["the moma"]], ["Carl Heinrich Bloch", "Christ Healing the Sick at Bethesda", "oil on canvas", 1883, clients["byu"]]]
for art in default_art:
    make_art_default(art[0], art[1], art[2], art[3], art[4])




#main program
main()
