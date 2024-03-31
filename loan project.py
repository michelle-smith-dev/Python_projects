# Get details of loan
money_owed = float(input('How much money do you owe, in dollars?\n'))  # $50,000
apr = float(input('What is the annual percentage rate of the loan?\n'))  # 3%
payment = float(input('How much will you pay off each month in dollars?\n'))  # $1,000
months = int(input('How many months do you want to see the results for?\n'))  # 24

monthly_rate = apr/100/12

for x in range(months):
# Calculate interest to pay
    interest_paid = money_owed*monthly_rate

# Add in interest
    money_owed = money_owed + interest_paid

    if money_owed - payment < 0:
        # print('The last payment is', money_owed)
        # print('You paid off the loan in', x + 1, 'months')
        break

# Make payment
    money_owed = money_owed - payment
    # print('Paid', payment, 'of which', interest_paid, 'was interest', end=' ')
    # print('Now I owe', money_owed)


# import PySimpleGUI as sg
#
# sg.theme('DarkAmber')   # Add a touch of color
# # All the stuff inside your window.
# layout = [  [sg.Text('Some text on Row 1')],
#             [sg.Text('How much money do you owe, in dollars?\n'), sg.InputText()],
#             [sg.Text('Enter something on Row 2'), sg.InputText()],
#             [sg.Button('Ok'), sg.Button('Cancel')] ]
#
# # Create the Window
# window = sg.Window('Window Title', layout)
# # Event Loop to process "events" and get the "values" of the inputs
# while True:
#     event, values = window.read()
#     if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
#         break
#     print('You entered ', values[0])
#
# window.close()