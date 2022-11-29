#Program for Bank transaction

balance=20000
print('Banking Trasanction')
print('1.Credit')
print('2.Debit')
print('3. Balance')
ch=int(input('Enter your choice:'))
if ch==1:
       amt=int(input('Enter amount:'))
       balance=balance+amt
       print('Amount Credited:',amt)
       print('Mail balance:',balance)
elif ch==2:
    amt=int(input('Enter amount:'))
    if amt>balance:
            print('Insufficient balance in your account')
    else:
        balance=balance-amt
        print('Amount Deducted:',amt)
        print('Mail Balance:',balance)
        print('Transaction is being processed successfully')
elif ch==3:
    print('Main balance:',balance)
else:
    print('Invalid option')
