import sys
import time
from functools import reduce
lst = {'t':'Toffee','b':'Biscuit','i':'Ice cream','c':'Chocolate'}
items_price = {'t':50, 'b':70, 'i':90, 'c':40}
stock = {'t':10, 'b':15, 'i':0, 'c':50}
bill_lst = []
total = []
price_lst = list(items_price.values())
key_lst = list(lst.keys())
val_lst = list(lst.values())

print('\t\tWelcome to M mart Vending Machine')    
cnt = 'y'
while cnt == 'y':
    print('Select product: ')
    for i in range(len(val_lst)):
        print('Press ',key_lst[i],' for',val_lst[i],', Price:',price_lst[i])
    product = input()
    bill_lst.append(product)
    if stock[product] == 0:
        print('Sorry...')
        print(lst[product],' is out of stock')
        ask_stock = input('Do you want to buy another product? Yes/no[y/n] ')
        if ask_stock == 'y':
            continue
        else:
            break
    else:
        count = int(input('How many '+lst[product]+' you want to buy? '))

        if count > stock[product]:
            bill_lst.append(stock[product])
            print('Only',stock[product],lst[product]+' available')
            buy = input('Do you want to buy or decline? Buy/Decline[b/d]')
            if buy == 'b':
                count = stock[product]        
        else:   
            print('Item is available! We are proceeding your order')
            count = count
            bill_lst.append(count)
            
        while items_price[product]*count:
            
            add_money1 = int(input('Add money: '))
            if add_money1 < items_price[product]*count:
                print('Insufficient money')
                print('Add extra Rs.',items_price[product]*count-add_money1,'to this product')
                ask = input('Do you want to buy or exit? Buy/Exit[b/e] ')
                if ask == 'b':
                    add_money2 = int(input('Add more money: '))
                    if add_money1+add_money2 == items_price[product]*count:
                        print('Preparing your '+lst[product])
                        print('Please wait...')
                        time.sleep(3)
                        print('Take your '+lst[product])
                        total.append(items_price[product]*count)
                        break
                    elif add_money1+add_money2 > items_price[product]*count:
                        print('Preparing your '+lst[product])
                        print('Please wait...')
                        time.sleep(3)
                        print('Take your '+lst[product])
                        print('Take a change: ',(add_money1+add_money2)-items_price[product]*count)
                        print('Thank You!!!')
                        total.append(items_price[product]*count)
                        break
                    else:
                        pass # Following condition
                else:
                    sys.exit()
            elif add_money1 > items_price[product]*count:
                print('Preparing your '+lst[product])
                print('Please wait...')
                time.sleep(3)
                print('Take your '+lst[product])
                print('Take a change: ',(add_money1)-items_price[product]*count)
                print('Thank You!!!')
                total.append(items_price[product]*count)
                break 
            else:
                print('Preparing your '+lst[product])
                print('Please wait...')
                time.sleep(3)
                print('Take your '+lst[product])
                print('Thank You!!!')
                total.append(items_price[product]*stock[product])
                break
        more = input('Do you want to buy more? Yes/No[y/n] ')
        if more == 'y':
            continue
        else:
            break

#-----------------------BILL---------------------------------
        
if sum(total) > 0:
    bill = input('Do you want to print bill? Yes/No[y/n]')
    if bill == 'y':
        customer = input('Enter your name: ')
        pro = []
        count1 = []
        for i in range(len(bill_lst)):
            if i%2 == 0:
                pro.append(bill_lst[i])
        for i in range(len(bill_lst)):

            if i%2 != 0:
                count1.append(bill_lst[i])

        print('\t\t\tM Mart')
        print(time.strftime('\tBill Date: %A, %d %B %Y (%I:%M:%S %p)',time.localtime()))
        print('\tName: ',customer)
        print('\nSr.no\tParticulars\tRate\t\tQty\t\tPrice')
        for i in range(len(pro)):
            print(i+1,'\t',lst[pro[i]],'\t',items_price[pro[i]],'\t\t',count1[i],'\t\t',count1[i]*items_price[pro[i]])
        print('\t Items: ',i+1,'\t\t   Qty: ',reduce(lambda x,y: x+y, count1),end='  ')
        print('\t  Total:',reduce(lambda x,y:x+y, total))
        print('\t\t\tThank you!!!')
    else:
        print('Thanks for saving trees!!!!!!')
else:
    print('Thank you')


## 1) if i want to buy 10 toffee (rs.500) and i add money rs.100, it will ask me to add rs 400 then also i add rs 100 then
##    code should ask me again to add money till product price is fullfilled.
## 2) 2) Update stock value after product redeem
