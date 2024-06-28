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

    def customize_plan(self):
        try:
            self.display_additional_features()
            features = input("Enter the numbers of the additional features you wish to add (comma-separated): ").split(',')
            feature_numbers = [int(feature.strip()) for feature in features]
            for num in feature_numbers:
                if num in self.additional_features:
                    self.selected_features.append(self.additional_features[num]['name'])
                elif num in self.premium_features:
                    self.selected_features.append(self.premium_features[num]['name'])
                else:
                    raise ValueError(f"Feature number {num} is not available.")
        except (ValueError, KeyError) as e:
            print(f"Error: {e}")
            self.customize_plan()

    def calculate_cost(self):
        base_cost = (self.membership_plans[self.selected_plan]['cost']) * self.total_members
        features_cost = sum(self.additional_features[num]['cost'] for num in range(1, 3) if self.additional_features[num]['name'] in self.selected_features)
        premium_features_cost = sum(self.premium_features[num]['cost'] for num in range(3, 5) if self.premium_features[num]['name'] in self.selected_features)
        total_cost = base_cost + features_cost + premium_features_cost

        if self.total_members >= 2:
            total_cost *= 0.9
        if total_cost > 400:
            total_cost -= 50
        elif total_cost > 200:
            total_cost -= 20

        if any(feature in self.selected_features for feature in ['Exclusive gym facilities', 'Specialized training programs']):
            total_cost *= 1.15

        return round(total_cost)

    def confirm_membership(self):
        try:
            total_cost = self.calculate_cost()
            print("Membership Plan Confirmation")
            print(f"Selected Plan: {self.selected_plan}")
            print(f"Additional Features: {', '.join(self.selected_features) or 'None'}")
            print(f"Total Cost: ${total_cost}")
            return total_cost
        except ValueError as e:
            print(f"Error: {str(e)}")
            return -1

def main():
    gym_membership = GymMembership()
    gym_membership.display_plans()
    gym_membership.select_plan()
    gym_membership.set_group_membership()
    gym_membership.customize_plan()
    total_cost = gym_membership.confirm_membership()
    print(f"Total Membership Cost: ${total_cost}")

if __name__ == "__main__":
    main()
#aad