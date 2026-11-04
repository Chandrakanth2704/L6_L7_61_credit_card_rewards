
import pytest
from credit_card_rewards import (
    reward_points,
    late_payment_fee,
    card_status
)


# ==========================================
# REWARD POINTS - BRANCH COVERAGE
# ==========================================

def test_invalid_tier_branch():
    with pytest.raises(ValueError):
        reward_points("diamond", 1000, "grocery", False)


def test_invalid_amount_branch():
    with pytest.raises(ValueError):
        reward_points("classic", -100, "grocery", False)


def test_valid_amount_branch():
    assert reward_points("gold", 1000, "grocery", False) == 20


def test_fuel_branch():
    assert reward_points("gold", 1000, "fuel", False) == 0


def test_dining_branch():
    assert reward_points("classic", 1000, "dining", False) == 20


def test_travel_branch():
    assert reward_points("gold", 1000, "travel", False) == 40


def test_other_category_branch():
    assert reward_points("gold", 1000, "shopping", False) == 20


def test_weekend_non_classic_branch():
    assert reward_points("gold", 1000, "grocery", True) == 70


def test_weekend_classic_branch():
    assert reward_points("classic", 1000, "grocery", True) == 10


def test_weekday_branch():
    assert reward_points("gold", 1000, "grocery", False) == 20


# ==========================================
# LATE PAYMENT FEE - BRANCH COVERAGE
# ==========================================

def test_zero_days_late():
    assert late_payment_fee(5000, 0) == 0


def test_negative_outstanding_branch():
    assert late_payment_fee(-100, 10) == 0


def test_small_outstanding_branch():
    assert late_payment_fee(500, 10) == 100


def test_medium_outstanding_branch():
    assert late_payment_fee(5000, 10) == 500


def test_large_outstanding_branch():
    assert late_payment_fee(15000, 10) == 1000


def test_exactly_1000_outstanding():
    assert late_payment_fee(1000, 10) == 100


def test_exactly_10000_outstanding():
    assert late_payment_fee(10000, 10) == 500


def test_more_than_30_days():
    assert late_payment_fee(500, 31) == 850


def test_exactly_30_days():
    assert late_payment_fee(500, 30) == 100


# ==========================================
# CARD STATUS - BRANCH COVERAGE
# ==========================================

def test_frozen_branch():
    assert card_status(95, 3, True) == "frozen"


def test_not_frozen_branch():
    assert card_status(20, 0, False) == "good"


def test_three_missed_payments():
    assert card_status(20, 3, False) == "blocked"


def test_two_missed_payments():
    assert card_status(20, 2, False) == "watch"


def test_over_90_utilisation():
    assert card_status(95, 0, False) == "over limit risk"


def test_exactly_90_utilisation():
    assert card_status(90, 0, False) == "watch"


def test_over_30_utilisation():
    assert card_status(50, 0, False) == "watch"


def test_exactly_30_utilisation():
    assert card_status(30, 0, False) == "good"


def test_missed_payment_watch():
    assert card_status(20, 1, False) == "watch"


def test_no_missed_payment():
    assert card_status(20, 0, False) == "good"
