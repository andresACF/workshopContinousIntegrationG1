import unittest
from unittest.mock import patch

from main import GymMembership

class TestGymMembership(unittest.TestCase):
    def setUp(self):
        self.gym_membership = GymMembership()

    def test_initial_membership_plans(self):
        self.assertIn('Basic', self.gym_membership.membership_plans)
        self.assertIn('Premium', self.gym_membership.membership_plans)
        self.assertIn('Family', self.gym_membership.membership_plans)
        self.assertEqual(self.gym_membership.membership_plans['Basic']['cost'], 50)
        self.assertEqual(self.gym_membership.membership_plans['Premium']['cost'], 100)
        self.assertEqual(self.gym_membership.membership_plans['Family']['cost'], 150)

    def test_initial_additional_features(self):
        self.assertIn(1, self.gym_membership.additional_features)
        self.assertIn(2, self.gym_membership.additional_features)
        self.assertEqual(self.gym_membership.additional_features[1]['name'], 'Personal Training')
        self.assertEqual(self.gym_membership.additional_features[2]['name'], 'Group Classes')

    def test_initial_premium_features(self):
        self.assertIn(3, self.gym_membership.premium_features)
        self.assertIn(4, self.gym_membership.premium_features)
        self.assertEqual(self.gym_membership.premium_features[3]['name'], 'Exclusive gym facilities')
        self.assertEqual(self.gym_membership.premium_features[4]['name'], 'Specialized training programs')

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

if __name__ == '__main__':
    unittest.main()
