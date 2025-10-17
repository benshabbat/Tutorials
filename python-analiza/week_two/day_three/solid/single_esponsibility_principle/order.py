# class Order:
#     def __init__(self, items: list[str], total_price: float):
#         self.items = items
#         self.total_price = total_price
        
#     def print_invoice(self):
#         print("Invoice")
#         for item in self.items:
#             print(f"- {item}")
#         print(f"Total: ${self.total_price:.2f}")    

class Order:
    def __init__(self, items: list[str], total_price: float):
        self.items = items
        self.total_price = total_price
        
                
class InvoicePrinter:
    def print_invoice(self, order: Order):
        print("Invoice")
        for item in order.items:
            print(f"- {item}")
        print(f"Total: ${order.total_price:.2f}")        