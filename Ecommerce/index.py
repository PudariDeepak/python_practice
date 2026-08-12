class User:
    def __init__(self,id,name,password,role):
        self.id = id
        self.name = name
        self.password = password
        self.role = role

    def user_details(self):
        return f"{self.id},{self.name},{self.password},{self.role}\n"

class Auth:
    def register(self):
        id = input("Enter the user id: ")
        name = input("Enter the user name: ")
        password = input("Enter the user password: ")
        role = input("Enter the user role: ")

        user = User(id,name,password,role)

        is_found = False
        with open("users.txt","r") as file:
            lines = file.readlines()

        for line in lines:
            details = line.strip().split(",")
            if (details[1] == name):
                is_found = True
        if (is_found):
            print("user already exist")
        else:
            with open("users.txt","a") as file:
                file.write(user.user_details())
                print("Registration completed! ")

    def login(self):
        name = input("Enter the user name: ")
        password = input("Enter the user password: ")

        with open("users.txt","r") as file:
            lines = file.readlines()

        is_found = False
        for line in lines:
            details = line.strip().split(",")
            if (details[1] == name):
                is_found = True
                if details[2] == password:
                    print("Login successful..")
                    break
                else:
                    print("Incorrect password")
                    break

        if (is_found == False):
            print("user not exist.Please register...")


class Product:
    def __init__(self,id,product_name,price,quantity):
        self.id = id
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def product_details(self):
        return f"{self.id},{self.product_name},{self.price},{self.quantity}\n"

class Admin:
    def add_products(self):
        id = input("Enter product id: ")
        product_name = input("Enter product name: ")
        price = input("Enter product price: ")
        quantity = int(input("Enter product quantity: "))
        product = Product(id,product_name,price,quantity)

        with open("products.txt","r") as file:
            lines = file.readlines()

        with open("products.txt","w") as file:
            is_found = False
            for line in lines:
                details = line.strip().split(",")
                if(details[1] == product_name):
                    is_found = True
                    quantity = int(details[3])+quantity
                    file.write(f"{details[0]},{details[1]},{details[2]},{quantity}\n")
                else:
                    file.write(line)

        if(is_found ==False):
            with open("products.txt","a") as file:
                file.write(product.product_details())
            print("Product added successfully.")

    def update_products(self):
        id = input("Enter id for update product: ")
        with open("products.txt","r") as file:
            lines = file.readlines()

        with open("products.txt","w") as file:
            is_found = False
            for line in lines:
                details = line.strip().split(",")
                if(details[0] == id):
                    is_found = True
                    product_name = input(f"Enter the updated product_name from {details[1]} to: ")
                    price = input(f"Enter the updated price from {details[2]} to: ")
                    quantity = input(f"Enter the updated quantity from {details[3]} to:")
                    file.write(f"{id},{product_name},{price},{quantity}\n")
                else:
                    file.write(line)
            if is_found == True:
                print("Product updated successfully.")
            else:
                print("Product not found.")

    def delete_products(self):
        id = input("Enter id for deleting the product: ")
        with open("products.txt","r") as file:
            lines = file.readlines()

        with open("products.txt","w") as file:
            is_found = False
            for line in lines:
                details = line.strip().split(",")
                if details[0] != id:
                    file.write(line)
                else:
                    is_found = True
            if (is_found):
                print("Product deleted successfully..")
            else:
                print("Product not found")

    def view_products(self):
        with open("products.txt","r") as file:
            lines = file.readlines()
            print("-"*40)
            print(f"|{'Id':<5}|{'Product':<10}|{'Price':<10}|{'Quantity':<10}|")
            print("-"*40)
            for line in lines:
                details = line.strip().split(",")
                print(f"|{details[0] : <5}|{details[1] : <10}|{details[2] : <10}|{details[3] : <10}|")
            print("-"*40)





    

admin = Admin()
#admin.add_products()
#admin.update_products()
#admin.delete_products()
admin.view_products()