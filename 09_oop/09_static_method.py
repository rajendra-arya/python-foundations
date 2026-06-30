# class ChaiUtils:
#     def clean_ingredients(self, text):
#         return [item.strip() for item in text.split(',')]

# raw = "    water,     milk ,  giner  ,   honey      "

# cleaned = ChaiUtils()
# print(cleaned.clean_ingredients(raw)) #['water', 'milk', 'giner', 'honey']


#with static method
class ChaiUtils:
    def clean_ingredients(text): # No self here!
        return [item.strip() for item in text.split(',')]

raw = "    water,     milk ,  giner  ,   honey      "

cleaned = ChaiUtils.clean_ingredients(raw)
print(cleaned) #['water', 'milk', 'giner', 'honey']