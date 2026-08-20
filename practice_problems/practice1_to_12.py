# Exercise 1: E-Commerce User Data Sanitizer
# Task
"""
Write a function sanitize_user_data(raw_users) that accepts a list of user dictionaries and returns a cleaned dictionary where:
Emails are trimmed of whitespace and converted to lowercase.
User interests (provided as a list with duplicates) are converted to a list of unique sorted tags.
Total purchase amount is calculated and added to the user profile under a key "total_spent".
"""

raw_users = [
    {
        "id": 101,
        "email": "  ALICE@Yahoo.COM ",
        "interests": ["tech", "coding", "tech", "python"],
        "purchases": [29.99, 49.50, 12.00]
    },
    {
        "id": 111,
        "email": "  Jane@gmail.COM ",
        "interests": ["cooking", "travelling", "tech", "vlogs"],
        "purchases": [153.99, 49.50, 125.00]
    }
]

def sanitize_user_data(raw_users):
    users_data = []
    for user in raw_users:
        user["email"] = user["email"].strip(" ").lower()
        user["interests"] = list(set(user["interests"]))
        user["total_spent"] = round(sum(user["purchases"]), 2) # round to 2 decimal
        users_data.append(user)
    return users_data

print(sanitize_user_data(raw_users))

# Exercise 2: Access Control & Rate Limiter
# Task
"""
Write a function evaluate_request_permission(user_profile, current_requests) that evaluates access based on the following rules:
Banned users ("status": "banned") are always rejected immediately.
"admin" users have unlimited requests (True).
"pro" users have a threshold of 1,000 requests.
"free" users have a threshold of 100 requests.
The function should return a tuple: (is_allowed: bool, remaining_quota: int, status_message: str).
"""

# Sample inputs to test different user profiles and scenarios:

test_users = [
    {
        "user_profile":
        {
            "id": 1,
            "role": "free",
            "status": "active"
        },
        "current_requests": 85  # Should allow (15 remaining)
    },
    {
        "user_profile": {"id": 2, "role": "free", "status": "active"},
        "current_requests": 105  # Should deny (0 remaining)
    },
    {
        "user_profile": {"id": 3, "role": "pro", "status": "active"},
        "current_requests": 450  # Should allow (550 remaining)
    },
    {
        "user_profile": {"id": 4, "role": "admin", "status": "active"},
        "current_requests": 2500  # Should allow (unlimited)
    },
    {
        "user_profile": {"id": 5, "role": "pro", "status": "banned"},
        "current_requests": 10  # Should deny immediately due to status
    }
]

def evaluate_request_permission(test_users):
    user_report = []
    is_allowed, remaining_quota, status_message = True, 0, ""

    for user in test_users:
        if user["user_profile"]["status"] == "banned":
            is_allowed = False
            status_message = "User is banned"

        if user["user_profile"]["role"] == "admin":
            is_allowed = True
            status_message = "Admin tier active"
            remaining_quota = "Unlimited"
        elif user["user_profile"]["role"] == "free":
            remaining_quota = 100 - user["current_requests"]
            if remaining_quota <= 0:
                is_allowed = False
                status_message = "Free tier request exceeded"
            else:
                status_message = "Free tier active"
        elif user["user_profile"]["role"] == "pro":
            remaining_quota = 1000 - user["current_requests"]
            if remaining_quota <= 0:
                is_allowed = False
                status_message = "Pro tier request exceeded"
            else:
                status_message = "Pro tier active"
        user_report.append((is_allowed, remaining_quota, status_message))
    return user_report

print(evaluate_request_permission(test_users))

# Exercise 3: Warehouse Inventory Audit Engine
# Task
"""
Write a function audit_inventory(inventory_db) that takes a dictionary where keys are SKU strings and values are tuples of (product_name, stock_count, reorder_threshold).
Your function should iterate over the database and return a summary report dictionary containing:
"""

# Sample input dictionary (SKU -> (product_name, stock_count, reorder_threshold))

inventory_db = {
    "SKU-1001": ("Mechanical Keyboard", 45, 10),
    "SKU-1002": ("Ergonomic Mouse", 4, 15),       # Low stock
    "SKU-1003": ("27-inch Monitor", 0, 5),         # Out of stock & Low stock
    "SKU-1004": ("USB-C Cable", 120, 30),
    "SKU-1005": ("Standing Desk", 2, 5),          # Low stock
    "SKU-1006": ("Noise-Canceling Headphones", 0, 8) # Out of stock & Low stock
}

def audit_inventory(inventory_db):
    low_stock_items, out_of_stock = [], []
    total_stock_units = 0

    for product_name, stock_count, reorder_threshold in inventory_db.values():

        if stock_count <= reorder_threshold:
            low_stock_items.append(product_name)

        if stock_count == 0:
            out_of_stock.append(product_name)

        total_stock_units += int(stock_count)

    return {
        "low_stock_items": low_stock_items,
        "out_of_stock": out_of_stock,
        "total_stock_units": total_stock_units
    }

print(audit_inventory(inventory_db))

# Exercise 4: Shopping Cart Discount Rules Engine
# Task
"""
Write a function calculate_cart_total(cart, promo_code=None):
cart is a list of tuples: [("Item Name", price, quantity), ...].
Calculate the subtotal based on price $\times$ quantity for each item.Apply discount rules:If subtotal is greater than $100, apply an automatic 10% discount.If promo_code == "SAVE20", take an additional 20% off the remaining balance.If promo_code == "FREESHIP", deduct a flat $5 shipping fee from the subtotal.Return the final grand total rounded to 2 decimal places.
"""

# Test Case 1: Subtotal under $100, no promo
cart_1 = [
    ("Wireless Mouse", 25.00, 2),
    ("Mousepad", 15.00, 1)
]  # Subtotal = 65.00

# Test Case 2: Subtotal over $100 (gets auto 10% off), plus SAVE20 code
cart_2 = [
    ("Mechanical Keyboard", 120.00, 1),
    ("USB Hub", 30.00, 2)
]  # Subtotal = 180.00 | Promo = "SAVE20"

# Test Case 3: Subtotal over $100, plus FREESHIP code
cart_3 = [
    ("Monitor Stand", 45.00, 2),
    ("HDMI Cable", 15.00, 2)
]  # Subtotal = 120.00 | Promo = "FREESHIP"

def calculate_cart_total(cart, promo_code=None):
    sub_total_list = []

    # sub_total = sum(price * qty for _, price, qty in cart)
    for cart_item in cart:
        price, qty = cart_item[1], cart_item[2]
        sub_total = price * qty
        sub_total_list.append(sub_total)
        total = sum(sub_total_list)

        # g_total = sub_total * 0.90 if sub_total > 100 else sub_total
        if total > 100:
            g_total = total*0.9
        else:
            g_total = total

        if promo_code == "SAVE20":
            g_total *= 0.8
        elif promo_code == "FREESHIP":
            g_total = total - 5

        return round(max(0.00, g_total),2)
print(calculate_cart_total(cart_1))
print(calculate_cart_total(cart_2, "SAVE20"))
print(calculate_cart_total(cart_3, "FREESHIP"))