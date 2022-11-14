class Inventory():
    def __init__(self, app):
        self.teaInventory = {"black_tea": 20, "green_tea": 20, "oolong_tea": 20}
        self.toppingsInventory = {"tapioca": 20, "lychee": 20, "red_bean":20, "pudding": 20}
        self.suppliesInventory = {"cups": 20, "straws": 20, "seals": 20}
        
        #never change
        self.teaOPTIONS = ['black', 'green', 'oolong']
        self.toppingsOPTIONS = ['tapioca', 'lychee', 'red_bean', 'pudding']
        self.sugarOPTIONS = ['100%', '75%', '50%', '25%', '0%']
        self.iceOPTIONS = ['100%', '75%', '50%', '25%', '0%']
        self.milkOPTIONS = ['whole', '2%', 'skim']
        