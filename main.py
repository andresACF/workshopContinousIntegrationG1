
class GymMembership:
    def __init__(self):
        self.membership_plans = {
            'Basic': {'cost': 50, 'features': []},
            'Premium': {'cost': 100, 'features': ['Exclusive gym facilities', 'Specialized training programs']},
            'Family': {'cost': 150, 'features': []}
        }
        self.additional_features = {
            1: {'name': 'Personal Training', 'cost': 30},
            2: {'name': 'Group Classes', 'cost': 20}
        }
        self.premium_features = {
            3: {'name': 'Exclusive gym facilities', 'cost': 50},
            4: {'name': 'Specialized training programs', 'cost': 40}
        }
        self.selected_plan = None
        self.selected_features = []
        self.total_members = 1
    
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
        
        def discounts_group_memberships(self):
    index = 0
    base_cost = 0
    for k in self.memberships_plan.keys:
        if (self.plan_selected == 1):
            index = 0
            base_cost = self.memberships_plan.get(k)[1]
        elif (self.plan_selected == 2):
            index = 1
            base_cost = self.memberships_plan.get(k)[1]
        else:
            index = 2
            base_cost = self.memberships_plan.get(k)[1]
    num_members = self.members_plan[index]
    total_cost = base_cost * num_members
    if num_members >= 2:
        discount = total_cost * 0.10
        total_cost -= discount
        print(f"A 10% discount has been applied for group membership. You saved ${discount:.2f}.")
    else:
        print(f"Sign up with one or more friends to receive a 10% discount!")

    return total_cost

def special_offer_discounts(total_cost):
    if (total_cost > 400):
        total_cost = total_cost - 50
        print(f"A discount of $50 has been apply")
        return total_cost
    elif (total_cost > 200):
        total_cost = total_cost - 20
        print(f"A discount of $20 has been apply")
        return total_cost
    print(f"You don't meet the requirements to apply a discount")
    return total_cost

premium_features = ["access to exclusive gym facilities", "specialized training programs"]

def premium_membership_cost(base_cost, premium_features_cost, is_premium):
    total_cost = base_cost + premium_features_cost
    if is_premium:
        surcharge = total_cost * 0.15
        total_cost += surcharge
        print(f"A 15% surcharge has been applied for premium membership features. The surcharge amount is ${surcharge:.2f}.")
    else:
        print("No premium features selected.")

    return total_cost

    def display_plans(self):
        print("Available Membership Plans:")
        for plan, details in self.membership_plans.items():
            print(f"{plan}: ${details['cost']} - Features: {', '.join(details['features']) or 'None'}")

    def select_plan(self):
        try:
            plan = input("Enter the name of the membership plan you wish to select: ")
            if plan in self.membership_plans:
                self.selected_plan = plan
            else:
                raise ValueError("Invalid membership plan selected.")
        except ValueError as e:
            print(f"Error: {e}")
            self.select_plan()

    def set_group_membership(self):
        try:
            members_count = int(input("Enter the number of members for the group membership: "))
            if members_count < 1:
                raise ValueError("Number of members must be at least 1.")
            self.total_members = members_count
        except ValueError as e:
            print(f"Error: {e}")
            self.set_group_membership()

    def display_additional_features(self):
        print("Available Additional Features:")
        for num, feature in self.additional_features.items():
            print(f"{num}. {feature['name']}: ${feature['cost']}")
        for num, feature in self.premium_features.items():
            print(f"{num}. {feature['name']} (Premium): ${feature['cost']}")

