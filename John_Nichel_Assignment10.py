# -*- coding: utf-8 -*-
"""
Created on Friday June 5 20:12:35 2020
@author: Nichel Emmanuel John
This program will ask the user for details like their name,
stock symbol for the stock they own (for example for Google that would be GOOGL), 
number of shares they own, purchase price and current price for each stock, 
Based on user's input the program will display the ownership in a pie chart. 
"""
# matplotlib function to generate graph
import matplotlib.pyplot as plt
#User inputs are collected in the below code

name = str(input("Please enter the first name and last name of the stock holder: "))
stock_symbols = ["GOOGL","MSFT","RDS-A","AIG","FB"]
shares_counts = ["125","85","400","235","150"]
purchase_prices = ["772.88","56.60","49.58","54.21","124.31"]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','Orange']
current_prices = ["941.53","73.04","55.74","65.27","172.45"]
explode = (0, 0, 0.1, 0, 0)

#Below code displays the details of stocks to the user   
print ("\n Pie Chart for Stock Ownership for: " + str(name.title()))

# Plot
plt.pie(shares_counts,explode=explode, labels= stock_symbols, colors=colors, autopct='%.1f%%', shadow=True, startangle=140)
plt.title("Pie Chart for Stock Ownership for: " + str(name.title()))
plt.axis('equal')
plt.show()

print("----------------------------------------------------")
#End of program

