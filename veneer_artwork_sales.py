#Class Definitions
class Art:
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner
  def __repr__(self):
    return "{name}. \"{art}\". {year}, {medium}. {owner_name}, {owner_location}.".format(name = self.artist, art = self.title, year = self.year, medium = self.medium, owner_name = self.owner.name, owner_location = self.owner.location)
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
  def __init__(self, name, location, is_museum):
    self.name = name
    self.location = location
    self.is_museum = is_museum
  def sell_artwork(self, artwork, price):
    if artwork.owner == self:
      new_listing = Listing(artwork, price, self.name)
      veneer.add_listing(new_listing)
    else:
      return "You don't own this piece of artwork"
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
    return "{} ${}M (USD)".format(self.art, self.price)

#marketplace and clients
veneer = Marketplace()
edytta = Client("Edytta Halpirt", "Private Collection", False)
moma = Client("The MOMA", "New York", True)
Annie = Client("Annabelle Sandholtz", "Provo, UT", False)
christina = Client("Christina Sandholtz", "Toronto, Canada", False)

#Artworks
girl_with_mandolin = Art("Picasso, Pablo", "Girl with a mandolin (Fany Tellier)", "oil on canvas", 1910, edytta)
girl_flowers = Art("Christina Sandholtz", "Girl With Flowers", "Watercolor", 2020, moma)

#sells and buys
edytta.sell_artwork(girl_with_mandolin, 6)
moma.buy_artwork(girl_with_mandolin)
christina.sell_artwork(girl_flowers, 5)

#Print Statements
print(girl_with_mandolin)
print(girl_flowers)
veneer.show_listings()
