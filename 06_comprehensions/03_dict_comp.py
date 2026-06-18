#dictonary comp {} : just output is key-value pair rest same like set

tea_prices_inr = {"Masala Tea":40,
                  "Green Tea":50,
                  "Lemon Tea":200}

tea_prices_inr = {key: f"₹ {round(value/90,2)}" for key, value in tea_prices_inr.items()}

print(tea_prices_inr)
# {'Masala Tea': '₹ 0.44', 'Green Tea': '₹ 0.56', 'Lemon Tea': '₹ 2.22'}
