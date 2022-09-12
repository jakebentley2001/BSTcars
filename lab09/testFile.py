from Car import Car
from CarInventoryNode import CarInventoryNode
from CarInventory import CarInventory

def test_carInventory():
    bst = CarInventory()
    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 25000)
    car6 = Car("Suburu", "Van", 2021, 25000)
    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)

    assert bst.doesCarExist(car1) == True
    assert bst.doesCarExist(car2) == True
    assert bst.doesCarExist(car3) == True
    assert bst.doesCarExist(car4) == True
    assert bst.doesCarExist(car5) == True
    assert bst.doesCarExist(car6) == False

    assert bst.getBestCar("Nissan", "Leaf") == car1
    assert bst.getBestCar("Mercedes", "Sprinter") == car3
    assert bst.getBestCar("Honda", "Accord") == None

    assert bst.getWorstCar("Nissan", "Leaf") == car1
    assert bst.getWorstCar("Mercedes", "Sprinter") == car4
    assert bst.getBestCar("Honda", "Accord") == None

    assert bst.getTotalInventoryPrice() == 158000

    assert bst.inOrder() == \
"""\
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""

    assert bst.preOrder() == \
"""\
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""

    assert bst.postOrder() == \
"""\
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
"""

def test_carInventoryNode():
    car1 = Car("Dodge", "dart", 2015, 6000)
    car2 = Car("dodge", "DaRt", 2003, 5000)
    carNode = CarInventoryNode(car1)
    carNode.cars.append(car2)
    assert str(carNode) == 'Make: DODGE, Model: DART, Year: 2015, Price: $6000\n\
Make: DODGE, Model: DART, Year: 2003, Price: $5000\n'

def test_Car():
    c = Car("Honda", "CRV", 2007, 8000)
    assert str(c) == "Make: HONDA, Model: CRV, Year: 2007, Price: $8000"


#Tests that pass


#Test 1
def test_deleteSingleRoot():
    BST = CarInventory()
    car1 = Car("Mazda", "CX-5", 2022, 25000)
    BST.addCar(car1)
    assert BST.inOrder() == "Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000\n"
    BST.removeCar("Mazda", "CX-5", 2022, 25000)
    assert BST.root == None



#Test 2
def test_deleteRootOneChild():
    BST = CarInventory()
    
    car1 = Car("Tesla", "Model3", 2018, 50000)
    car2 = Car("Mazda", "CX-5", 2022, 25000)
    
    BST.addCar(car1)
    BST.addCar(car2)
    assert BST.inOrder() == \
"""\
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
""" 
    BST.removeCar("Tesla", "Model3", 2018, 50000)
    
    assert BST.inOrder() == "Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000\n"
    assert BST.root == car2
    


#test 3
def test_deleteLeaf():
    BST = CarInventory()
    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("BMW", "X5", 2022, 60000)
    car4 = Car("BMW", "X5", 2020, 58000)
    car5 = Car("Audi", "A3", 2021, 25000)

    BST.addCar(car1)
    BST.addCar(car2)
    BST.addCar(car3)
    BST.addCar(car4)
    BST.addCar(car5)
    
    assert BST.removeCar("Bentley","SClass",2016,6000) == False

    assert BST.inOrder() == \
"""\
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: BMW, Model: X5, Year: 2022, Price: $60000
Make: BMW, Model: X5, Year: 2020, Price: $58000
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""
    
    BST.removeCar("Tesla", "Model3", 2018, 50000)

    assert BST.inOrder() == \
"""\
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: BMW, Model: X5, Year: 2022, Price: $60000
Make: BMW, Model: X5, Year: 2020, Price: $58000
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
"""




#test 4
def test_deleteNodeOneChild():
    BST = CarInventory()
    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("BMW", "X5", 2022, 60000)
    car4 = Car("BMW", "X5", 2020, 58000)
    car5 = Car("Audi", "A3", 2021, 25000)

    BST.addCar(car1)
    BST.addCar(car2)
    BST.addCar(car3)
    BST.addCar(car4)
    BST.addCar(car5)
    
    BST.removeCar("BMW", "X5", 2022, 60000)
    assert BST.inOrder() == \
"""\
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: BMW, Model: X5, Year: 2020, Price: $58000
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""

    BST.removeCar("BMW", "X5", 2020, 58000)
    assert BST.root.left == car5
    assert BST.root.left.parent == car1
    


#test 5
def test_deleteRootWithTwoChildren():
    BST = CarInventory()
    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("BMW", "X5", 2022, 60000)
    car4 = Car("BMW", "X5", 2020, 58000)
    car5 = Car("Audi", "A3", 2021, 25000)
    car6 = Car("Fierrari", "IDK", 2022, 60000)
    car7 = Car("Cadillac", "Suede", 2018, 50000)
    car8 = Car("Jeep", "OffRoad", 2020, 58000)
    car9 = Car("LandRover", "Luxury", 2021, 25000)
    BST.addCar(car1)
    BST.addCar(car2)
    BST.addCar(car3)
    BST.addCar(car4)
    BST.addCar(car5)
    BST.addCar(car6)
    BST.addCar(car7)
    BST.addCar(car8)
    BST.addCar(car9)
    assert BST.inOrder() == \
"""\
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: BMW, Model: X5, Year: 2022, Price: $60000
Make: BMW, Model: X5, Year: 2020, Price: $58000
Make: CADILLAC, Model: SUEDE, Year: 2018, Price: $50000
Make: FIERRARI, Model: IDK, Year: 2022, Price: $60000
Make: JEEP, Model: OFFROAD, Year: 2020, Price: $58000
Make: LANDROVER, Model: LUXURY, Year: 2021, Price: $25000
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""
    BST.removeCar("Fierrari", "IDK", 2022, 60000)
    assert BST.inOrder() == \
"""\
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: BMW, Model: X5, Year: 2022, Price: $60000
Make: BMW, Model: X5, Year: 2020, Price: $58000
Make: CADILLAC, Model: SUEDE, Year: 2018, Price: $50000
Make: JEEP, Model: OFFROAD, Year: 2020, Price: $58000
Make: LANDROVER, Model: LUXURY, Year: 2021, Price: $25000
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""
    
    BST.removeCar("Jeep", "OffRoad", 2020, 58000)
    assert BST.inOrder() == \
"""\
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: BMW, Model: X5, Year: 2022, Price: $60000
Make: BMW, Model: X5, Year: 2020, Price: $58000
Make: CADILLAC, Model: SUEDE, Year: 2018, Price: $50000
Make: LANDROVER, Model: LUXURY, Year: 2021, Price: $25000
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""
    BST.removeCar("BMW", "X5", 2022, 60000)
    BST.removeCar("BMW", "X5", 2020, 58000)
    
   
    assert BST.inOrder() == \
"""\
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: CADILLAC, Model: SUEDE, Year: 2018, Price: $50000
Make: LANDROVER, Model: LUXURY, Year: 2021, Price: $25000
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""
    
    BST.removeCar("LandRover", "Luxury", 2021, 25000)
    
    assert BST.inOrder() == \
"""\
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: CADILLAC, Model: SUEDE, Year: 2018, Price: $50000
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""
    assert BST.preOrder() == \
"""\
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
Make: CADILLAC, Model: SUEDE, Year: 2018, Price: $50000
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""


def test_getSuccessor():
    BST = CarInventory()
    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("BMW", "X5", 2022, 60000)
    car4 = Car("BMW", "X5", 2020, 58000)
    car5 = Car("Audi", "A3", 2021, 25000)

    BST.addCar(car1)
    BST.addCar(car2)
    BST.addCar(car3)
    BST.addCar(car4)
    BST.addCar(car5)

    assert BST.getSuccessor("BMW","X5") == car1



