from enum import Enum
# make a tests folder under the folder you're putting these files in
# add an empty __init__.py to the tests folder
from IcecreamExceptions import ExceededRemainingChoicesException, InvalidChoiceException, NeedsCleaningException, OutOfStockException
from IcecreamExceptions import InvalidPaymentException

class Usable:
    name = ""
    quantity = 0
    cost = 99

    def __init__(self, name, quantity = 10, cost=99):
        self.name = name
        self.quantity = quantity
        self.cost = cost

    # UCID: tbb
    # Date: 21 Oct 2022
    def use(self):
        self.quantity -= 1
        try: 
            if (self.quantity < 0):
                raise OutOfStockException
        except OutOfStockException:
            print("Your choice is out of stock. Please choose from the available options")
        return self.quantity 

    def in_stock(self):
        return self.quantity > 0

class Container(Usable):
    pass

class Flavor(Usable):
    pass

class Toppings(Usable):
    pass

class STAGE(Enum):
    Container = 1
    Flavor = 2
    Toppings = 3
    Pay = 4

class IceCreamMachine:
    # Constants https://realpython.com/python-constants/
    USES_UNTIL_CLEANING = 100
    MAX_SCOOPS = 3
    MAX_TOPPINGS = 3


    containers = [Container(name="Waffle Cone", cost=1.5), Container(name="Sugar Cone", cost=1), Container("Cup", cost=1)]
    flavors = [Flavor(name="Vanilla", quantity=100, cost=1), Flavor(name="Chocolate", quantity=100, cost=1), Flavor(name="Strawberry", quantity=100, cost=1)]
    toppings = [Toppings(name="Sprinkles", quantity=200, cost=.25), Toppings(name="Chocolate Chips", quantity=200, cost=.25), Toppings(name="M&Ms", quantity=200, cost=.25), \
    Toppings(name="Gummy Bears", quantity=200, cost=.25), Toppings(name="Peanuts", quantity=200, cost=.25)] 


    # variables
    remaining_uses = USES_UNTIL_CLEANING
    remaining_scoops = MAX_SCOOPS
    remaining_toppings = MAX_TOPPINGS
    total_sales = 0
    total_icecreams = 0

    inprogress_icecream = []
    currently_selecting = STAGE.Container

    # rules
    # 1 - container must be chosen first
    # 2 - can only use items if there's quantity remaining
    # 3 - scoops can't exceed max
    # 4 - toppings can't exceed max
    # 5 - a container and at least 1 scoop or toppings must be selected
    # 6 - proper cost must be calculated and shown to the user
    # 7 - cleaning must be done after certain number of uses before any more icecreams can be made
    # 8 - total sales should calculate properly based on cost calculation
    # 9 - total_icecreams should increment properly after a payment
    

    def pick_container(self, choice):
        for c in self.containers:
            if c.name.lower() == choice.lower():
                c.use()
                self.inprogress_icecream.append(c)
                return
        try:
            raise InvalidChoiceException
        except:
            print(f"\"{choice}\" is an invalid Choice, Choose only from the options below")

    # UCID: tbb
    # Date: 21 Oct 2022
    def pick_flavor(self, choice):
        try:
            if self.remaining_uses <= 0:
                raise NeedsCleaningException
            
            if self.remaining_scoops <= 0:
                raise ExceededRemainingChoicesException
        except NeedsCleaningException:
            print(f"The Ice Cream Machine is used to its maximum({self.USES_UNTIL_CLEANING}). It needs cleaning before any more icecreams can be made.")
            # confirm to clean and continue or else quit
            clean = input("What would you like to do? (continue or quit)\n")
            if clean == "continue":
                self.clean_machine()
                print("Machine cleaned Successfully!")
            else:
                exit()
        except ExceededRemainingChoicesException:
            print(f"You have reached maximum({self.MAX_SCOOPS}) number of scoops. Please choose toppings now!")
            # moving the current selection to toppings
            self.currently_selecting = STAGE.Toppings

        for f in self.flavors:
            if f.name.lower() == choice.lower():
                f.use()
                self.inprogress_icecream.append(f)
                self.remaining_scoops -= 1
                self.remaining_uses -= 1
                return
        try:
            raise InvalidChoiceException
        except:
            print(f"\"{choice}\" is an invalid Choice, Choose only from the options below")

    # UCID: tbb
    # Date: 21 Oct 2022
    def pick_toppings(self, choice):
        try:
            if self.remaining_toppings <= 0:
                raise ExceededRemainingChoicesException
        except ExceededRemainingChoicesException:
            print(f"You have reached maximum({self.MAX_TOPPINGS}) number of toppings. Proceed to pay...")
            # moving the current selection to payment
            self.currently_selecting = STAGE.Pay

        for t in self.toppings:
            if t.name.lower() == choice.lower():
                t.use()
                self.inprogress_icecream.append(t)
                self.remaining_toppings -= 1
                return
        # UCID: tbb
        # Date: 21 Oct 2022
        try:
            raise InvalidChoiceException
        except:
            print(f"\"{choice}\" is an invalid Choice, Choose only from the options below")

    def reset(self):
        self.remaining_scoops = self.MAX_SCOOPS
        self.remaining_toppings = self.MAX_TOPPINGS
        self.inprogress_icecream = []
        self.currently_selecting = STAGE.Container

    def clean_machine(self):
        self.remaining_uses = self.USES_UNTIL_CLEANING
        
    def handle_container(self, container):
        self.pick_container(container)
        self.currently_selecting = STAGE.Flavor

    def handle_flavor(self, flavor):
        if flavor == "next":
            self.currently_selecting = STAGE.Toppings
        else:
            self.pick_flavor(flavor)

    def handle_toppings(self, toppings):
        if toppings == "done":
            self.currently_selecting = STAGE.Pay
        else:
            self.pick_toppings(toppings)

    # UCID: tbb
    # Date: 21 Oct 2022
    def handle_pay(self, expected, total):
        if total == str(expected):
            print("Thank you! Enjoy your icecream!")
            self.total_icecreams += 1
            self.total_sales += float(expected) # only if successful
            self.reset()
        else:
            try: 
                raise InvalidPaymentException
            except InvalidPaymentException:
                print("Amount entered didn't match with the total. Please re-enter")
                self.run()
            
    # UCID: tbb
    # Date: 21 Oct 2022
    def calculate_cost(self):
        # TODO add the calculation expression/logic for the inprogress_icecream
        cost = 0
        # iterating through the in progress_icecream array to add up the cost of each choice
        for s in self.inprogress_icecream:
            cost += s.cost
        # returning the calculated cost in the currency format
        return "{:.2f}".format(cost)

    def run(self):
        if self.currently_selecting == STAGE.Container:
            container = input(f"Would you like a {', '.join(list(map(lambda c:c.name.lower(), filter(lambda c: c.in_stock(), self.containers))))}?\n")
            self.handle_container(container)
        elif self.currently_selecting == STAGE.Flavor:
            flavor = input(f"Would you like {', '.join(list(map(lambda f:f.name.lower(), filter(lambda f: f.in_stock(), self.flavors))))}? Or type next.\n")
            self.handle_flavor(flavor)
        elif self.currently_selecting == STAGE.Toppings:
            toppings = input(f"Would you like {', '.join(list(map(lambda t:t.name.lower(), filter(lambda t: t.in_stock(), self.toppings))))}? Or type done.\n")
            self.handle_toppings(toppings)
        elif self.currently_selecting == STAGE.Pay:
            expected = self.calculate_cost()
            total = input(f"Your total is ${expected}, please enter the exact value.\n")
            self.handle_pay(expected, total)
            choice = input("What would you like to do? (icecream or quit)\n")
            if choice == "quit":
                exit()
        self.run()

    def start(self):
        self.run()

    
if __name__ == "__main__":
    icm = IceCreamMachine()



