import pandas as pd


def transform_data(df):

    print("Starting data transformation...")

    # Remove duplicate orders
    df = df.drop_duplicates(subset=["order_id"])

    # Convert order_date to datetime
    df["order_date"] = pd.to_datetime(df["order_date"])

    # Check for missing values
    if df.isnull().sum().sum() > 0:
        print("Warning: Missing values found.")

    # Validate quantity
    if (df["quantity"] <= 0).any():
        raise ValueError("Quantity must be greater than zero.")

    # Validate price
    if (df["price"] <= 0).any():
        raise ValueError("Price must be greater than zero.")

    # Calculate subtotal
    df["subtotal"] = df["quantity"] * df["price"]

    # Calculate GST
    df["gst"] = df["subtotal"] * 0.18

    # Calculate total amount
    df["total_amount"] = df["subtotal"] + df["gst"]

    print("Data transformed successfully!")

    return df