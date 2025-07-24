# public struct SalesData. Include the following properties: date sold, department name, product ID, quantity sold, Unit Price

from datetime import datetime
import random
from faker import Faker
class SalesData:
    def __init__(self, date_sold: str, department_name: str, product_id: int, quantity_sold: int, unit_price: float):
        self.date_sold = datetime.strptime(date_sold, '%Y-%m-%d')
        self.department_name = department_name
        self.product_id = product_id
        self.quantity_sold = quantity_sold
        self.unit_price = unit_price

    def __str__(self):
        return (f"SalesData(date_sold={self.date_sold.strftime('%Y-%m-%d')}, "
                f"department_name='{self.department_name}', product_id={self.product_id}, "
                f"quantity_sold={self.quantity_sold}, unit_price={self.unit_price})")
    
    # In the above class create the GeneralSalesData method returns 1000 SalesData records. It assigns random values to each field of the class
    @staticmethod
    def generate_general_sales_data(num_records=1000):
               
        fake = Faker()
        sales_data_list = []
        
        for _ in range(num_records):
            date_sold = fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d')
            department_name = fake.company()
            product_id = random.randint(1000, 9999)
            quantity_sold = random.randint(1, 100)
            unit_price = round(random.uniform(5.0, 500.0), 2)
            
            sales_data = SalesData(date_sold, department_name, product_id, quantity_sold, unit_price)
            sales_data_list.append(sales_data)
        
        return sales_data_list
    
    def quaterlySalesReport(self):
        #create a dictionary to store the quaterly sales data
        quarterly_sales = {}
        for record in SalesData.generate_general_sales_data():
            quarter = (record.date_sold.month - 1) // 3 + 1
            year = record.date_sold.year
            key = f"{year}-Q{quarter}"
            
            if key not in quarterly_sales:
                quarterly_sales[key] = {
                    'total_quantity': 0,
                    'total_revenue': 0.0
                }
            
            quarterly_sales[key]['total_quantity'] += record.quantity_sold
            quarterly_sales[key]['total_revenue'] += record.quantity_sold * record.unit_price
        #print the quaterly sales report
        for key, value in quarterly_sales.items():
            print(f"{key}: Total Quantity Sold = {value['total_quantity']}, Total Revenue = ${value['total_revenue']:.2f}")

        def GetQuarterlySalesReport(self, month):
            if month < 1 or month > 12:
                raise ValueError("Month must be between 1 and 12.")
            quarter = (month - 1) // 3 + 1
            return f"Quarter {quarter} of the year {self.date_sold.year}"
            


