# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    def is_number(x):
        try:
            float(x)
            return True
        except ValueError:
            return False
    
    savings_balance = input("Enter the savings balance: ")
    if not is_number(savings_balance):
        print("Savings alance is not a number")
        return
    savings_balance = (float) (savings_balance)
    
    savings_interest = input("Enter the savings interest rate: ")
    if not is_number(savings_interest):
        print("Savings interest rate is not a number")
        return
    savings_interest = (float) (savings_interest)
    
    savings_maturity = input("Enter the number of months: ")
    if not savings_maturity.isdigit():
        print("Number of monthsis not a integer")
        return
    savings_maturity = (int) (savings_maturity)

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    # Code is written to print out the interest earned and updated savings account balance with interest earned for the
    # given months. The values are formatted to two decimal places and thousandths.
    print(f'savings interest: ${interest_earned:,.2f}, savings balance: ${updated_savings_balance:,.2f}')

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = input("Enter the CD balance: ")
    if not is_number(cd_balance):
        print("CD balance is not a number")
        return
    cd_balance = (float) (cd_balance)
    
    cd_interest = input("Enter the CD interest rate: ")
    if not is_number(cd_interest):
        print("CD interest rate is not a number")
        return
    cd_interest = (float) (cd_interest)
    
    cd_maturity = input("Enter the CD maturity in months: ")
    if not cd_maturity.isdigit():
        print("Number of months is not a integer")
        return
    cd_maturity = (int) (cd_maturity)

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f'CD interest: ${interest_earned:,.2f}, CD balance: ${updated_cd_balance:,.2f}')
    
if __name__ == "__main__":
    # Call the main functio
    main()