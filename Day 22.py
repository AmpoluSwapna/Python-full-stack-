swapna_details_ICIC = {
    'Name': 'swapna',
    'Adr': '123456789',
    'pan': 'GPCBU2073T',
    'ATMPIN': '2244',
    'Balance': 10000,   
    'MINI State':[]
}
All_attempts = 3
while All_attempts > 0:
    user_pin = input("Enter your 4 digit ATM PIN: ")
    if len(user_pin) == 4:
        if user_pin in swapna_details_ICIC['ATMPIN']:
            print('Welcome to ICIC ATM')
            choice_ = int(input('Enter\n1. Withdraw\n2. Deposit\n3. Check Balance: '))
            if choice_ == 1:
                with_m = int(input('Enter amount to withdraw: '))
                if with_m <= swapna_details_ICIC['Balance'] and with_m % 100 == 0:
                    swapna_details_ICIC['Balance'] -= with_m
                    print(f'Take your cash and the balance is {swapna_details_ICIC["Balance"]}')
                    swapna_details_ICIC['MINI State'].append(f'Withdraw:{with_m}')
                    print(f"{swapna_details_ICIC['MINI State']}")
                    user_opt = int(input('Enter \n1.Home Page \n2.Exit:')) 
                    if user_opt == 1:
                        print('Taking to Home Page')
                        continue   
                    elif user_opt == 2:
                        print('Thanks for visiting')
                        break
                else:
                    print('Insufficient balance or This ATM cannot provide change')
            elif choice_ == 2:
                depo_m = int(input('Enter amount to deposit: '))
                if depo_m % 100 == 0:
                    swapna_details_ICIC['Balance'] += depo_m
                    print(f'Amount deposited and total balance is {swapna_details_ICIC["Balance"]}')
                    swapna_details_ICIC['MINI State'].append(f'deposit:{depo_m}')
                    print(f"{swapna_details_ICIC['MINI State']}")
                    user_opt = int(input('Enter \n1.Home Page \n2.Exit:'))
                    if user_opt == 1:
                        print('Taking to Home Page')
                    elif user_opt == 2:
                        print('Thanks for visiting')
                        break  
                else:
                    print('This ATM does not accept change')
            elif choice_ == 3: 
                print(f'Your balance is {swapna_details_ICIC["Balance"]}')
            break
        else:
            All_attempts -= 1
            if All_attempts > 0:
                print(f'Incorrect PIN entered and you have {All_attempts} attempts left')
            else:
                print('Your card is blocked')
    else:
        print("PIN must contain exactly 4 digits")

