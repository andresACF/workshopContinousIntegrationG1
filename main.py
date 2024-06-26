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