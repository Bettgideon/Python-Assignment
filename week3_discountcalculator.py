def calculate_discount(price, discount_percentage):
    if discount_percentage >= 20:
        discount_amount = (discount_percentage / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price  # No discount applied if percentage is less than 20

# Get user input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))
    
    # Validate that the discount is within a reasonable range (0 to 100)
    if not (0 <= discount_percentage <= 100):
        print("Invalid discount percentage! Please enter a value between 0 and 100.")
    else:
        final_price = calculate_discount(price, discount_percentage)
        print(f"Final price after discount: {final_price:.2f}")
except ValueError:
    print("Invalid input! Please enter a valid number.")
