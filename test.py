import unittest
from unittest.mock import patch
from io import StringIO

from main import GymMembership

class TestGymMembership(unittest.TestCase):
    def setUp(self):
        self.gym_membership = GymMembership()

    @patch('builtins.input', side_effect=['Premium'])
    def test_select_plan_valid(self, mock_input):
        self.gym_membership.select_plan()
        self.assertEqual(self.gym_membership.selected_plan, 'Premium')

    @patch('builtins.input', side_effect=['Invalid', 'Basic'])
    def test_select_plan_invalid_then_valid(self, mock_input):
        self.gym_membership.select_plan()
        self.assertEqual(self.gym_membership.selected_plan, 'Basic')

    @patch('builtins.input', side_effect=['3'])
    def test_set_group_membership_valid(self, mock_input):
        self.gym_membership.set_group_membership()
        self.assertEqual(self.gym_membership.total_members, 3)

    @patch('builtins.input', side_effect=['-1', '4'])
    def test_set_group_membership_invalid_then_valid(self, mock_input):
        self.gym_membership.set_group_membership()
        self.assertEqual(self.gym_membership.total_members, 4)
  
    @patch('builtins.input', side_effect=['1, 3'])
    def test_customize_plan_valid(self, mock_input):
        self.gym_membership.customize_plan()
        self.assertIn('Personal Training', self.gym_membership.selected_features)
        self.assertIn('Exclusive gym facilities', self.gym_membership.selected_features)

    @patch('builtins.input', side_effect=['5', '1, 2'])
    def test_customize_plan_invalid_then_valid(self, mock_input):
        self.gym_membership.customize_plan()
        self.assertIn('Personal Training', self.gym_membership.selected_features)
        self.assertIn('Group Classes', self.gym_membership.selected_features)
    
    def test_calculate_cost_plan_no_features(self):
        self.gym_membership.selected_plan = 'Premium'
        self.gym_membership.total_members = 1
        self.gym_membership.selected_features = []
        self.assertEqual(self.gym_membership.calculate_cost(), 100)

    def test_calculate_cost_plan_with_features(self):
        self.gym_membership.selected_plan = 'Basic'
        self.gym_membership.total_members = 1
        self.gym_membership.selected_features = ['Personal Training']
        self.assertEqual(self.gym_membership.calculate_cost(), 80)


    def test_calculate_cost_plan_with_premium_features(self):
        self.gym_membership.selected_plan = 'Basic'
        self.gym_membership.total_members = 1
        self.gym_membership.selected_features = ['Exclusive gym facilities', 'Specialized training programs']
        self.assertEqual(self.gym_membership.calculate_cost(), 161)

    def test_calculate_cost_with_group_discount(self):
        self.gym_membership.selected_plan = 'Basic'
        self.gym_membership.total_members = 3
        self.gym_membership.selected_features = []
        self.assertEqual(self.gym_membership.calculate_cost(), 135)

    def test_calculate_cost_with_total_cost_grater_than_400(self):
        self.gym_membership.selected_plan = 'Family'
        self.gym_membership.total_members = 3
        self.gym_membership.selected_features = ['Personal Training', 'Exclusive gym facilities']
        self.assertEqual(self.gym_membership.calculate_cost(), 491)

    def test_calculate_cost_with_total_cost_grater_than_200_lower_than_400(self):
        self.gym_membership.selected_plan = 'Family'
        self.gym_membership.total_members = 2
        self.gym_membership.selected_features = ['Personal Training']
        self.assertEqual(self.gym_membership.calculate_cost(), 277)  
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['confirm'])
    def test_confirm_membership_confirm(self, mock_input,mock_stdout):
        self.gym_membership.selected_plan = 'Family'
        self.gym_membership.total_members = 2
        self.gym_membership.selected_features = ['Group Classes', 'Specialized training programs']
        self.assertEqual(self.gym_membership.confirm_membership(), 350)


        expected_output = (
            "Membership Plan Confirmation\n"
            f"Selected Plan: {self.gym_membership.selected_plan}\n"
            f"Additional Features: {', '.join(self.gym_membership.selected_features) or 'None'}\n"
            "Total Cost: $350\n"
        )

        self.assertEqual(mock_stdout.getvalue(), expected_output)


    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['cancel'])
    def test_confirm_membership_cancel(self, mock_input,mock_stdout):
        self.gym_membership.selected_plan = 'Family'
        self.gym_membership.total_members = 2
        self.gym_membership.selected_features = ['Group Classes', 'Specialized training programs']
        self.assertEqual(self.gym_membership.confirm_membership(), 350)


        expected_output = (
            "Membership Plan Confirmation\n"
            f"Selected Plan: {self.gym_membership.selected_plan}\n"
            f"Additional Features: {', '.join(self.gym_membership.selected_features) or 'None'}\n"
            "-1\n"
        )

        self.assertEqual(mock_stdout.getvalue(), -1)



if __name__ == '__main__':
    unittest.main()
