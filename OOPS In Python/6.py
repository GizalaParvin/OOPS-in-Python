class OTTSubscription:
    def __init__(self,subscription_id,plan,total_payment):
        self.id=subscription_id
        self.plan=plan
        self.payment=total_payment
    def subscribe(self):
        print(f"Subscriber with {self.id} id subscription to the {self.plan} plan ")    
    def unsubscribe(self):
        print(f"Subscriber with {self.id} id UNsubscription to the {self.plan} plan ") 
netflix=OTTSubscription(12234,"monthly",100)        
netflix.plan
netflix.subscribe()

class PremiumSubscription(OTTSubscription):
    def __init__(self,subscription_id,plan,total_payment):
        self.id=subscription_id
        self.plan=plan
        self.payment=total_payment
    def subscribe(self):
        print(f"Subscriber with {self.id} id subscription to the {self.plan} plan ")    
    def unsubscribe(self):
        print(f"Subscriber with {self.id} id UNsubscription to the {self.plan} plan ") 
    def set_max_screens(self,screns):
        self.max_screns = screns
        print(f"maximum screen set to {self.max_screns} in Premium plan") 
netflix = PremiumSubscription("12345","monthly",212)
netflix.subscribe()          
netflix.set_max_screens(4)

