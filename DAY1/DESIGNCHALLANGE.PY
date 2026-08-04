def main():
    print("********** RESTAURANT MENU **********")
    print("1. IDLY            - ₹50")
    print("2. DOSA            - ₹60")
    print("3. CHINESE DISH    - ₹100")
    print("4. BIRIYANI        - ₹2000")
    print("5. RICE            - ₹70")

    total = 0

    while True:
        choice = int(input("\nEnter Item Number (1-5): "))

        if choice == 1:
            item = "IDLY"
            price = 50
        elif choice == 2:
            item = "DOSA"
            price = 60
        elif choice == 3:
            item = "CHINESE DISH"
            price = 100
        elif choice == 4:
            item = "BIRIYANI"
            price = 2000
        elif choice == 5:
            item = "RICE"
            price = 70
        else:
            print("Invalid Choice!")
            continue

        qty = int(input("Enter Quantity: "))
        amount = price * qty
        total += amount

        print("Added:", item)
        print("Amount = ₹", amount)

        more = input("Add another item? (yes/no): ").lower()
        if more != "yes":
            break

    gst = total * 0.18
    grand_total = total + gst

    print("\n========== BILL ==========")
    print("Subtotal   : ₹", total)
    print("GST (18%)  : ₹", gst)
    print("Total Bill : ₹", grand_total)
    print("==========================")
    print("Thank You! Visit Again.")

if __name__ == "__main__":
    main()
