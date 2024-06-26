class GymMembership:
    
    membership_plans = {
        '1': ["Basic", 50, "No trainer", "35 daily minutes"],
        '2': ["Premium", 100, "Trainer", "50 daily minutes"],
        '3': ["Family", "Two trainers", "Unlimited time"]
    }
    
    additional_features = ["More time", "Proteins included", "Personalized tools"]
    members_plan = [0,0,0]
    plan_selected = None
    plan_copy_selected = []

    def __init__(self):
        pass
    
    def display_plan(self):
        for num, (plan, details) in enumerate(self.membership_plans.items(), start=1):
            print(f"Plan {num}: {plan}")
            print(f"Price: ${details[0]}")
            print(f"Trainer: {details[1]}")
            print(f"Daily Time: {details[2]}")
            print("----------------------")

    def input_promt_plan(self):
        self.display_plan()
        self.plan_selected = int(input("\nSelect one plan with the number: \n"))
        number_members = int(input("\nWho many members?:  \n"))
        
        if self.plan_selected == 1:
            self.members_plan[0] = number_members
        elif self.plan_selected == 2:
            self.members_plan[1] = number_members
        elif self.plan_selected == 3:
            self.members_plan[2] = number_members

        self.plan_copy_selected = self.membership_plans.get(str(self.plan_selected))

        self.add_additionally_features()

    def add_additionally_features(self):
        confirmation = True

        while confirmation: 
            option = int(input("Do you want add other features? Write the number\n1. Yes\n2. No"))

            if option == 2 :
                confirmation = False
                break

            
            for feauture in self.additional_features:
                num = 1
                print(f"{num} {feauture}\n")
                num +=1
            
            add_feature = int(input("Add Some funcionalities: \n"))
            self.plan_copy_selected.append()
                       
        



# Ejemplo de uso
membership = GymMembership()
membership.input_promt_plan()


