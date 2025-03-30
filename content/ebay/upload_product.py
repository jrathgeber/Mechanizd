
import ebaysdk

from ebaysdk import connection, trading


# Initialize connection with your credentials

api = connection(config_file='your_config.yaml')


# Create a new listing object

item = trading.Item()

item.Title = 'Awesome Gadget'

item.Description = 'A great new gadget!'

item.StartPrice = 19.99



# Send the listing request

response = api.execute(item.create_item())



print(f"Listing ID: {response.ItemID}")