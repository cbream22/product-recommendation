from product_data import products

# Step 3: Print the first few products to understand the structure
print("First few products from catalog:")
print(products[:3])  # sample preview

# Step 4: Collect customer preferences
customer_preferences = []

while True:
    preference = input("Enter a product preference (or 'N' to finish): ")
    if preference.lower() == "n":
        break
    customer_preferences.append(preference)

print("\nCustomer preferences (raw list):", customer_preferences)

# Step 6: Convert preferences to a set
customer_preferences = set(customer_preferences)
print("Customer preferences (as set):", customer_preferences)

# Step 7: Convert product tags to sets
for product in products:
    product["tags"] = set(product["tags"])

# Step 8: Count matching tags
def count_matches(product_tags, customer_preferences):
    return len(product_tags.intersection(customer_preferences))

# Step 9: Recommendation function
def recommend_products(products, customer_preferences):
    recommendations = []
    for product in products:
        matches = count_matches(product["tags"], customer_preferences)
        if matches > 0:  # only recommend if there's at least one match
            recommendations.append({
                "name": product["name"],
                "matches": matches
            })
    return sorted(recommendations, key=lambda x: x["matches"], reverse=True)

# Step 10: Print the results
results = recommend_products(products, customer_preferences)
print("\nRecommended Products:")
for r in results:
    print(f"- {r['name']} (matches: {r['matches']})")

"""
Design Memo

This program's core operations include loops, list-to-set conversion, 
and set intersections. The loop structure is necessary for iterating through 
the product list and collecting user input. Converting lists into sets is 
important because sets remove duplicate entries automatically and allow for 
efficient membership testing. The key operation for comparing user preferences 
to product tags is the set intersection, which quickly identifies overlapping 
tags between two sets.

The customer preferences are stored in a list, then converted into a set 
to remove duplicates. Similarly, each product's tags are converted into a set 
to be compared using set operations. The function `count_matches` 
uses intersection to return the number of matching preferences for each product. 
The recommendation function then loops through all products, calculates match 
scores, and sorts them in descending order so that the most relevant products 
appear first.

If this code had to handle 1,000+ products, the logic would remain the same 
because sets are highly efficient. However, performance improvements might 
include using a database or search indexing to avoid looping through every 
product in memory. Additionally, the recommendation system 
could scale further by assigning weights to preferences or using more advanced 
algorithms such as collaborative filtering. For the current project, though, 
sets provide a simple and fast way to match user interests to available products.
"""