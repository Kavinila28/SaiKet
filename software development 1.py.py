def calculate_emi(principal, annual_rate, tenure_months):
    monthly_rate = annual_rate / (12 * 100)
    if monthly_rate == 0:
        return principal / tenure_months
    emi = (principal * monthly_rate * pow(1 + monthly_rate, tenure_months)) / (pow(1 + monthly_rate, tenure_months) - 1)
    return emi

def main():
    print("Loan EMI Calculator")
    try:
        principal = float(input("Enter the loan principal amount (P): "))
        annual_rate = float(input("Enter the annual interest rate (in %): "))
        tenure_months = int(input("Enter the loan tenure (in months): "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    if principal <= 0 or annual_rate < 0 or tenure_months <= 0:
        print("Please enter positive values for principal and tenure, and non-negative value for interest rate.")
        return

    emi = calculate_emi(principal, annual_rate, tenure_months)
    print(f"\nCalculated EMI: ₹{emi:,.2f} per month for {tenure_months} months.")

if __name__ == "__main__":
    main()