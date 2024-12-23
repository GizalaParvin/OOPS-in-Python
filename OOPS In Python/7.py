#inheritence class of question 6
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
netflix.unsubscribe()

class PremiumSubscription(OTTSubscription):
    def __init__(self,subscription_id,plan,total_payment,screens):
       super(). __init__(subscription_id,plan,total_payment)
       self.max_screens = screens 
     

    def set_max_screens(self,screens):
        self.max_screens = screens
        print(f"Maximum screen set to {self.max_screens} in Premium plan") 
netflix = PremiumSubscription("12345","monthly",212,4)
netflix.subscribe()          
netflix.set_max_screens(4)