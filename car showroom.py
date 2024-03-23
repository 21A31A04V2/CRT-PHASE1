class Car_show_room:
    def init(self,company):
        self.company = company
        self.models = {
            "Jak One": ["tata", "ford", "toyota"],
                      }
        self.prices = {
            "Jak One":
                      {
                "tata": 1000000,
                "ford": 1200000,
                "toyota": 1500000,
                      }
            
                       }
        self.cgst = 0.05  
        self.sgst = 0.05  
        self.insurance_rate = 0.1

    def company_info(self):
        print("Welcome to {self.company} car family.")

    def show_models(self):
        print("Models available for {self.company}:")
        for model in self.models.get(self.company,[]):
            print("model")

    def calculate_price(self, model):
        base_price = self.prices.get(self.company, {}).get(model,0)
        if base_price == 0:
            print("Invalid model selected.")
            return

        cgst_amount = base_price * self.cgst
        sgst_amount = base_price * self.sgst
        insurance_amount = base_price * self.insurance_rate
        
        total_price = base_price + cgst_amount + sgst_amount + insurance_amount

        print(f"On road price for {self.company} {model}: ${total_price:.2f}")


car = Carshowroom("varun motors ")
car.company.info("marutisuzuki")
car.show.models("swift")
car.calculate.price("Model1")
