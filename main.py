class GymMembership:
    
    membership_plans = {
        'Basic': [50, "No trainer", "35 daily minutes"],
        'Premium': [100, "Trainer", "50 daily minutes"],
        'Family': [150, "Two trainers", "Unlimited time"]
    }
    
    additional_features = ["More time", "Proteins included", "Personalized tools", "Own locker", "Any food"]
    members_plan = [0,0,0]

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
        plan_selected = int(input("\nSelect one plan with the number: \n"))
        number_members = int(input("\nWho many members?:  \n"))
        
        if plan_selected == 1:
            self.members_plan[0] += number_members
        elif plan_selected == 2:
            self.members_plan[1] += number_members
        elif plan_selected == 3:
            self.members_plan[2] += number_members
        



# Ejemplo de uso
membership = GymMembership()
membership.input_promt_plan()


