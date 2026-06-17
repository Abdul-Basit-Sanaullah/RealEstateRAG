import pandas as pd

df = pd.read_csv("data/Housing.csv")

def search_property(question):

    question = question.lower()

    if "2 bedroom" in question:
        result = df[df["bedrooms"] == 2]

        if len(result) == 0:
            return "No 2-bedroom houses found."

        avg_price = result["price"].mean()

        return f"The average price of 2-bedroom houses is {avg_price:,.0f}"

    if "3 bedroom" in question:
        result = df[df["bedrooms"] == 3]

        if len(result) == 0:
            return "No 3-bedroom houses found."

        avg_price = result["price"].mean()

        return f"The average price of 3-bedroom houses is {avg_price:,.0f}"

    if "most expensive" in question:
        house = df.loc[df["price"].idxmax()]

        return (
            f"Most expensive house:\n"
            f"Price: {house['price']:,.0f}\n"
            f"Bedrooms: {house['bedrooms']}\n"
            f"Bathrooms: {house['bathrooms']}\n"
            f"Area: {house['area']}"
        )

    if "cheapest" in question:
        house = df.loc[df["price"].idxmin()]

        return (
            f"Cheapest house:\n"
            f"Price: {house['price']:,.0f}\n"
            f"Bedrooms: {house['bedrooms']}\n"
            f"Bathrooms: {house['bathrooms']}\n"
            f"Area: {house['area']}"
        )

    if "average price" in question:
        avg_price = df["price"].mean()

        return f"The average property price is {avg_price:,.0f}"

    if "parking" in question:
        count = len(df[df["parking"] > 0])

        return f"There are {count} houses with parking available."

    return None