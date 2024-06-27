import pytest
from unittest.mock import patch
from io import StringIO
from main import GymMembership

@pytest.fixture
def gym_membership():
    return GymMembership()

# Select Plan Tests
@patch('builtins.input', side_effect=['Premium'])
def test_select_plan_valid(mock_input, gym_membership):
    gym_membership.select_plan()
    assert gym_membership.selected_plan == 'Premium'

def test_select_plan_invalid_then_valid_message(gym_membership):
    with patch('builtins.input', side_effect=['Invalid', 'Basic']), \
         patch('builtins.print') as mock_print:
        gym_membership.select_plan()
        mock_print.assert_any_call("Error: Invalid membership plan selected.")
        assert gym_membership.selected_plan == 'Basic'

# Group Membership Tests
@patch('builtins.input', side_effect=['3'])
def test_set_group_membership_valid(mock_input, gym_membership):
    gym_membership.set_group_membership()
    assert gym_membership.total_members == 3

def test_set_group_membership_invalid_then_valid(gym_membership):
    with patch('builtins.input', side_effect=['-1', '4']), \
         patch('builtins.print') as mock_print:
        gym_membership.set_group_membership()
        mock_print.assert_any_call("Error: Number of members must be at least 1.")
        assert gym_membership.total_members == 4

# Customize Plan Tests
@patch('builtins.input', side_effect=['1, 3'])
def test_customize_plan_valid(mock_input, gym_membership):
    gym_membership.customize_plan()
    assert 'Personal Training' in gym_membership.selected_features
    assert 'Exclusive gym facilities' in gym_membership.selected_features

def test_customize_plan_invalid_message(gym_membership):
    expected_output = "Feature number 5 is not available."

    with patch('sys.stdout', new=StringIO()) as fake_out, \
         patch('builtins.input', side_effect=['5','1']):
        
        try:
            gym_membership.customize_plan()
        except ValueError as e:
            assert expected_output in str(e)
        except Exception:
            pass

    assert expected_output in fake_out.getvalue().strip()

# Calculate Cost Tests
def test_calculate_cost_plan_no_features(gym_membership):
    gym_membership.selected_plan = 'Premium'
    gym_membership.total_members = 1
    gym_membership.selected_features = []
    assert gym_membership.calculate_cost() == 100

def test_calculate_cost_plan_with_features(gym_membership):
    gym_membership.selected_plan = 'Basic'
    gym_membership.total_members = 1
    gym_membership.selected_features = ['Personal Training']
    assert gym_membership.calculate_cost() == 80

def test_calculate_cost_plan_with_premium_features(gym_membership):
    gym_membership.selected_plan = 'Basic'
    gym_membership.total_members = 1
    gym_membership.selected_features = ['Exclusive gym facilities', 'Specialized training programs']
    assert gym_membership.calculate_cost() == 161

def test_calculate_cost_with_group_discount(gym_membership):
    gym_membership.selected_plan = 'Basic'
    gym_membership.total_members = 3
    gym_membership.selected_features = []
    assert gym_membership.calculate_cost() == 135

def test_calculate_cost_with_total_cost_grater_than_400(gym_membership):
    gym_membership.selected_plan = 'Family'
    gym_membership.total_members = 3
    gym_membership.selected_features = ['Personal Training', 'Exclusive gym facilities']
    assert gym_membership.calculate_cost() == 491

def test_calculate_cost_with_total_cost_grater_than_200_lower_than_400(gym_membership):
    gym_membership.selected_plan = 'Family'
    gym_membership.total_members = 2
    gym_membership.selected_features = ['Personal Training']
    assert gym_membership.calculate_cost() == 277

# Confirm Membership Tests
@patch('sys.stdout', new_callable=StringIO)
@patch('builtins.input', side_effect=['confirm'])
def test_confirm_membership_confirm(mock_input, mock_stdout, gym_membership):
    gym_membership.selected_plan = 'Family'
    gym_membership.total_members = 2
    gym_membership.selected_features = ['Group Classes', 'Specialized training programs']
    assert gym_membership.confirm_membership() == 350

    expected_output = (
        "Membership Plan Confirmation\n"
        f"Selected Plan: {gym_membership.selected_plan}\n"
        f"Additional Features: {', '.join(gym_membership.selected_features) or 'None'}\n"
        "Total Cost: $350\n"
    )

    assert mock_stdout.getvalue() == expected_output

@patch('sys.stdout', new_callable=StringIO)
@patch('builtins.input', side_effect=['cancel'])
def test_confirm_membership_cancel(mock_input, mock_stdout, gym_membership):
    gym_membership.selected_plan = 'Family'
    gym_membership.total_members = 2
    gym_membership.selected_features = ['Group Classes', 'Specialized training programs']
    assert gym_membership.confirm_membership() == 350

    assert mock_stdout.getvalue().strip() == '-1'
