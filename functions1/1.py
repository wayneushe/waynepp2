#1
def grams_to_ounces(grams):
    conversion_factor = 28.3495231
    ounces = grams / conversion_factor
    return ounces

# Example usage
grams = 100  # You can change this value to test with different amounts
ounces = grams_to_ounces(grams)
print(ounces)