class Customers:
    greeting = "Welcome to Coffee Palace!"

c_1 = Customers()
c_1.name = "Samirah"
c_1.beverage = "Ice Caffe Latte"
c_1.food = "Cinnamon Roll"
c_1.total = 225

c_2 = Customers()
c_2.name = "Jerry"
c_2.beverage = "Caramel Macchiato"
c_2.food = "Glazed Doughnut"
c_2.total = 230

print(Customers.greeting)
print(c_1.beverage)
print(c_2.food)