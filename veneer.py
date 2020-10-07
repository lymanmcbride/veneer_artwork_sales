clients = {}
artworks = {}
#programs
def main():
    pass

#Sell and Buy functions:
def sell():
    for key in clients.keys():
        print (clients[key].name)
    client_name = input("What is the name of the seller? Please choose from the above options").lower()
    if client_name in clients.keys():
        client = clients[client_name]
        artwork_title = input("What is the entire title of the art being sold?").lower()
        if artwork_title in artworks.keys():
            artwork = artworks[artwork_title]
        price = int(input("What is the asking price? (numbers only)"))
        client.sell_artwork(artwork, price)
    else:
        print("That name isn't in our list of clients")

def buy():
    for key in clients.keys():
        print (clients[key].name)
    client_name = input("What is the name of the buyer? Please choose from the above options").lower()
    if client_name in clients.keys():
        client = clients[client_name]
        artwork_title = input("What is the entire title of the art being sold?").lower()
        if artwork_title in artworks.keys():
            artwork = artworks[artwork_title]
        client.buy_artwork(artwork)
    else:
        add = input("That name isn't in our list of clients, would you like to add them now? y/n").lower()
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
    if artist == None:
        artist, title, medium, year, owner = get_artwork_information()
    key = title.lower()
    if key not in artworks:
        artworks[key] = Art(artist, title, medium, year, owner)
    else:
        print ("That artwork is already in the system")

def make_client(name = None, location = None, museum = None):
    if name == None:
        name, location, museum = get_client_information()
    key = name.lower()
    if key not in clients:
        clients[key] = Client(name, location, museum)
    else:
        print ("That client is already in the system.")

#getting functions:
def get_artwork_information():
    artist = input("Who is the artist?")
    title = input("What is the title of the work?")
    medium = input("What is the medium (ie: oil on canvas, watercolor, etc.)")
    year_string = input("What year was the artwork made?")
    year = int(year_string)
    owner = input("Who is the current owner of the artwork?")
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
            main()


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
make_client("Edytta Halpirt", "Private Collection", False)
make_client("The MOMA", "New York", True)
make_client("Yale", "New Haven, Ct.", True)
make_client("BYU", "Provo, Ut", True)

make_art("Vincent van Gogh", "Orchard Bordered by Cypresses", "oil on canvas", 1888, clients["yale"])
make_art("Toyin Ojih Odutola", "Projection Enclave", "Pastel, charcoal, and pencil on paper", 2018, clients["the moma"])
make_art("Carl Heinrich Bloch", "Christ Healing the Sick at Bethesda", "oil on canvas", 1883, clients["byu"])
#sells and buys
#edytta.sell_artwork(girl_with_mandolin, 6)
#moma.buy_artwork(girl_with_mandolin)
#christina.sell_artwork(girl_flowers, 5)

#Print Statements
#print(girl_with_mandolin)
#print(girl_flowers)
#veneer.show_listings()
sell()
buy()
print(veneer.listings)
print(artworks)
