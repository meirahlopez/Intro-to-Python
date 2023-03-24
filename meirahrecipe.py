# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

print( "Meirah's Recipes" )

# Ingredients stored in variables
rackoflamb = 1                  # rack
oliveoil = 2                   # tbsp
salt = 0.5                      # tsp
rosemary = 2                    # cups
thyme = 1                       # tsp
garlic = 1                      # tsp
time = 20                       # mins

print( "" )
print( "Lamb Rack in the Air Fryer Recipe" )
print( "" )
print(rackoflamb  , "\t rack of Lamb (1 rack is 8 chops)" )
print( oliveoil, "\t tbsp of olive oil" )
print( salt, "\t tsps of salt" )
print( rosemary, "\t tsps of rosemary")
print( thyme, "\t tsps of thyme" )
print( garlic, " \t tsps of garlic" )
print( time, "\t mins at 380F, time will vary depending on how you want the meat, rare, medium, well done" )

print( "" )
batchQuantity = float( input( "How many batches would you like to make? (0.5 for half, 2 for double): " ) )

rackoflamb = 1 * batchQuantity
oliveoil = 2 * batchQuantity
salt = 0.5 * batchQuantity
rosemary = 2 * batchQuantity
thyme = 1 * batchQuantity
garlic = 1 * batchQuantity
Time = 20 * batchQuantity


print( "" )
print( "Lamb Rack Recipe", batchQuantity, "batches" )
print( "" )
print(rackoflamb  , "\t rack of Lamb (1 rack is 8 chops)" )
print( oliveoil, "\t tbsp of olive oil" )
print( salt, "\t tsps of salt" )
print( rosemary, "\t tsps of rosemary")
print( thyme, "\t tsps of thyme" )
print( garlic, " \t tsps of garlic" )
print( time, "\t mins at 380F, time will vary depending on how you want the meat, rare - well done" )
