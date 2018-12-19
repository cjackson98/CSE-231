"""
CSE 231 project 5
prompt for a file
    if file doesnt exist, try again
for each line in the file, get the various numbers and use them to calculate roi
use a holder variable to compare current sales number to max sales number
reset both when the product changes
"""
def open_file():
    '''prompt for file name, open file, return file pointer'''
    while 1==1:
        try:    
            filename = input("Input a file name: ")
            fp=open(filename,'r')
            break
        except FileNotFoundError:
            print("Unable to open file. Please try again.")
    fp=open(filename,'r')
    return fp
    
def revenue(num_sales, sale_price):
    '''revenue = sales * price'''
    rev=num_sales*sale_price
    return rev

def cost_of_goods_sold(num_ads, ad_price, num_sales, production_cost):
    '''costs of goods sold = advertising total + production total'''
    cost=(num_ads*ad_price)+(num_sales*production_cost)
    return cost

def calculate_ROI(num_ads, ad_price, num_sales, sale_price, production_cost):
    '''ROI = (Revenue - Cost of goods sold)/Cost of goods sold'''
    rev=revenue(num_sales, sale_price)
    cost=cost_of_goods_sold(num_ads, ad_price, num_sales, production_cost)
    roi=(rev-cost)/cost
    return roi

def main():

    file = open_file()
    
    print()
    print("RobCo AdStats M4000")
    print("-------------------")
    print() 
    max_sales=0
    max_roi=0
    prev_product=''
    for line in file:
        line2=line
        line=line.split()
        product=line2[0:27]
        ad=line2[27:54]
        max_roi=0
        if prev_product!=product:
            production_cost=float(line[-1])
            sale_price=float(line[-2])
            num_sales=float(line[-3])
            ad_price=float(line[-4])
            num_ads=float(line[-5])
            prev_product=product
            roi=calculate_ROI(num_ads, ad_price, num_sales, sale_price, production_cost)
            roi=round(roi,2)
            if roi>max_roi:
                max_roi=roi
            if num_sales>max_sales:
                max_sales=num_sales
            max_sales=int(max_sales)
            roi=round(roi,2)
            print(product)
            print("  {:27s}{:>11s}".format("Best-Performing Ad","sales"))
            print("  {:27s}{:>11}".format(ad,max_sales))
            print()
            print("  {:27s}{:>11s}".format("Best ROI","percent"))
            print("  {:27s}{:>11.2f}%".format(ad,max_roi))
            print()

if __name__ == "__main__":
    main()