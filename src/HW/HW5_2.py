

def main():
    square_feet = int(input('Please enter the square feet that has to be painted: '))
    price_paint_gallon = int(input('Please enter the paint price: '))
   
    Calculation(square_feet, price_paint_gallon)


    

def Calculation(square_feet, price_paint_gallon):
    gallons = square_feet / 100
    labour_hours = gallons * 8 
    total_price_gallon = gallons * price_paint_gallon
    company_charges = labour_hours * 35
    total_charges = company_charges + total_price_gallon
    print("Gallons: ", gallons)
    print("Labour hours: ", labour_hours)
    print('Total price of gallon: $%d' % total_price_gallon)
    print('Company_charges $%d' % company_charges)
    print("Total charges of this work will be: $%d" % total_charges)
    
main()

