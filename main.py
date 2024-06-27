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