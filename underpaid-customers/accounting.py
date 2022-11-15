MELON_COST = 1.00

def print_payment_status(payment_data_filename):
    """Calculate cost of melons and determine who has underpaid."""

    with open(payment_data_filename) as file:
        for line in file:
            # get a list of first, last name, and the payment
            order = line.rstrip().split('|')

            full_name = order[1]
            first_name = full_name.split(' ')[0]

            # Get no. of melons in the order and amount customer paid
            melons_qty = float(order[2])
            amt_paid = float(order[3])
            
            # Calculate expected price of customer's order
            expected_price = melons_qty * MELON_COST

            # Print general payment info
            print(f"{full_name} paid ${amt_paid:.2f}, expected",
                f"${expected_price:.2f}")

            # If customer overpaid, print that they've overpaid for their melons. If
            # customer underpaid, print that they've underpaid for their melons.
            if expected_price < amt_paid:
                print(f"{first_name} has overpaid for their melons.")
            elif expected_price > amt_paid:
                print(f"{first_name} has underpaid for their melons.")

print_payment_status('customer-orders.txt')