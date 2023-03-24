# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

print( "Meirah's Recipes" )

# Ingredients stored in variables
filetmignon = 1         # 8-10 oz each
oliveoil = 1                    # tbsp
salt = 0.5                      # tsp
yourfavoriteseasoning  = 2    # tsp
time = 20                       # mins

print( "" )
print( "Filet Mignon in the Air Fryer Recipe" )
print( "" )
print(filetmignon  , "\t filet mignon steak" )
print( oliveoil, "\t tbsp of olive oil" )
print( salt, "\t tsps of salt" )
print( time, "\t mins at 380F, time will vary depending on how you want the meat, rare, medium, well done" )

print( "" )
batchQuantity = float( input( "How many batches would you like to make? (0.5 for half, 2 for double): " ) )

filetmignon = 1 * batchQuantity
oliveoil = 1 * batchQuantity
salt = 0.5 * batchQuantity
yourfavoriteseasoning = 2 * batchQuantity
Time = 20 * batchQuantity


print( "" )
print( "Filet Mignon Recipe", batchQuantity, "batches" )
print( "" )
print(filetmignon  , "\t filet mignon steaks" )
print( oliveoil, "\t tbsp of olive oil" )
print( salt, "\t tsps of salt" )
print( yourfavoriteseasoning, " \t tsps of your favorite seasoning" )
print( time, "\t mins at 380F, time will vary depending on how you want the meat, rare - well done" )
