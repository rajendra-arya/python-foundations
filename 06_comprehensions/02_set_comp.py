#set comp{} : unique values
#iterating from dictonary to get unique values

favorite_chais = ['Green Tea', 'Masala Tea', 'Elaichi Tea', 'Green Tea', 'Lemon Tea','Masala Tea']
#set comp

unique_tea= {tea for tea in favorite_chais} #if condition is optional
# {'Elaichi Tea', 'Lemon Tea', 'Green Tea', 'Masala Tea'}


sorted_unique_tea = {tea for tea in sorted(favorite_chais)} #sorted returns a sorted list
# {'Green Tea', 'Masala Tea', 'Elaichi Tea', 'Lemon Tea'}

# unique_tea_len_gt10 = {tea for tea in favorite_chais if len(tea)>10} #if condition is optional
# {'Elaichi Tea'}

print(favorite_chais)
print(sorted_unique_tea)


##nested comp
# find all unique spices from the recipes

recipes  = {"Masala Chai":["ginger","cardamom","clove"],
            "Elaichi Chai": ["cardamom","milk"],
            "Spicy Chai": ["ginger","black pepper","clove"]}

#Spice :final output
unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}
print(unique_spices)

# this has reduced this much code
# unique_spices = set() 
# for ingredients in recipes.values():
#     for spice in ingredients:
#         unique_spices.add(spice)
