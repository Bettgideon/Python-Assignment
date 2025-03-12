def calculate_discount(price, discount_percent):
    """Calculates the final price after applying a discount."""
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price  # Return the original price if the discount is less than 20%

# Prompt the user for input
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(original_price, discount_percentage)

# Display the result
if final_price == original_price:
    print(f"No discount applied. The final price remains: {original_price:.2f}")
else:
    print(f"After applying a {discount_percentage}% discount, the final price is: {final_price:.2f}")
