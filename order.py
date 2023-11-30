class Order:
    next_id = 1

    def __init__(self, items=None):
        self.id = Order.next_id
        Order.next_id += 1
        self.ready = False
        self.items = [""] * 3 if items is None else items

    def getId(self):
        return self.id

    def __str__(self):
        ready_status = "Ready" if self.ready else "Not Ready"
        items_list = "\n".join(self.items)
        return f"Order number: {self.id}\n{ready_status}\n{items_list}"


class OrderList:
    def __init__(self):
        self.orderList = []

    def addOrder(self, order):
        for i in range(len(self.orderList)):
            if self.orderList[i] is None:
                self.orderList[i] = order
                return
        self.orderList.append(order)

    def removeOrder(self, id):
        for i in range(len(self.orderList)):
            if self.orderList[i] is not None and self.orderList[i].getId() == id:
                self.orderList[i] = None
                return

    def readyOrder(self, id):
        for order in self.orderList:
            if order is not None and order.getId() == id:
                order.ready = True
                return

    def sortOrders(self):
        self.orderList = [order for order in self.orderList if order is not None]
        self.orderList.sort(key=lambda order: order.getId())

    def printOrder(self, id):
        for order in self.orderList:
            if order is not None and order.getId() == id:
                return str(order)
        return ""

    def printOrders(self):
        self.sortOrders()
        ready_orders = []
        preparing_orders = []
        for order in self.orderList:
            if order.ready:
                ready_orders.append(order)
            else:
                preparing_orders.append(order)
        ready_str = "\n".join(str(order.getId()) for order in ready_orders)
        preparing_str = "\n".join(str(order.getId()) for order in preparing_orders)
        return f"Ready\n{ready_str}\nPreparing\n{preparing_str}"


def main():
    restaurantOrders = OrderList()

    while True:
        print("1- Create order")
        print("2- Delete order")
        print("3- Ready order")
        print("4- Print order")
        print("5- Print all orders")
        print("6- Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            items = [input(f"Enter item {i + 1}: ") for i in range(3)]
            new_order = Order(items)
            restaurantOrders.addOrder(new_order)
            print("Order has been added")

        elif choice == 2:
            order_id = int(input("Enter order ID to remove: "))
            restaurantOrders.removeOrder(order_id)
            print("Order has been removed")

        elif choice == 3:
            order_id = int(input("Enter order ID to set as ready: "))
            restaurantOrders.readyOrder(order_id)
            print("Order has been set to 'Ready'")

        elif choice == 4:
            order_id = int(input("Enter order ID to print: "))
            order_str = restaurantOrders.printOrder(order_id)
            if order_str:
                print(order_str)
            else:
                print("No order with such ID")

        elif choice == 5:
            orders_str = restaurantOrders.printOrders()
            print(orders_str)

        elif choice == 6:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
