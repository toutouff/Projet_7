from operator import attrgetter

class Action:
    """docstring for action."""

    def __init__(self,data):
        self.id = data[0]
        self.price = float(data[1])
        self.roi = float(data[2])

    def get_benef(self):
        return (self.price*self.roi)/100
    def get_roi(self):
        return self.roi

    def __str__(self):
        return "id: "+str(self.id)+",price: "+str(self.price)+",roi: "+str(self.roi)


class Client:
    def __init__(self):
        self.wallet = []
        self.money = 500
        self.benef = 0

    def buy(self, action):
        if action.price>0:
            if (self.money-action.price)>=0:
                self.wallet.append(action)
                self.money-=action.price
                return True
            else:
                return False
    def get_benef(self):
        self.benef = 0
        for action in self.wallet:
            temp_action_benef =(action.price*action.roi)/100
            self.benef+=temp_action_benef
        return self.benef
