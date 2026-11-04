
import pytest
from credit_card_rewards import (
    reward_points,
    late_payment_fee,
    card_status
)


# ==========================================
# REWARD POINTS TEST CASES
# ==========================================

def test_classic_grocery():
    assert reward_points("classic", 1000, "grocery", False) == 10


def test_gold_grocery():
    assert reward_points("gold", 1000, "grocery", False) == 20


def test_platinum_grocery():
    assert reward_points("platinum", 1000, "grocery", False) == 40


def test_invalid_card_tier():
    with pytest.raises(ValueError, match="unknown card tier"):
        reward_points("diamond", 1000, "grocery", False)


def test_zero_amount():
    with pytest.raises(ValueError, match="invalid amount"):
        reward_points("classic", 0, "grocery", False)


def test_negative_amount():
    with pytest.raises(ValueError, match="invalid amount"):
        reward_points("classic", -100, "grocery", False)


def test_fuel_category():
    assert reward_points("gold", 1000, "fuel", False) == 0


def test_dining_category():
    assert reward_points("classic", 1000, "dining", False) == 20


def test_travel_category():
    assert reward_points("gold", 1000, "travel", False) == 40


def test_weekend_bonus_gold():
    assert reward_points("gold", 1000, "grocery", True) == 70


def test_weekend_bonus_platinum():
    assert reward_points("platinum", 1000, "grocery", True) == 90


def test_classic_weekend_no_bonus():
    assert reward_points("classic", 1000, "grocery", True) == 10


# ==========================================
# LATE PAYMENT FEE TEST CASES
# ==========================================

def test_paid_on_time():
    assert late_payment_fee(5000, 0) == 0


def test_negative_days_late():
    assert late_payment_fee(5000, -5) == 0


def test_zero_outstanding():
    assert late_payment_fee(0, 10) == 0


def test_negative_outstanding():
    assert late_payment_fee(-500, 10) == 0


def test_fee_for_small_outstanding():
    assert late_payment_fee(500, 10) == 100


def test_fee_for_medium_outstanding():
    assert late_payment_fee(5000, 10) == 500


def test_fee_for_large_outstanding():
    assert late_payment_fee(15000, 10) == 1000


def test_late_payment_over_30_days():
    assert late_payment_fee(500, 31) == 850


def test_medium_outstanding_over_30_days():
    assert late_payment_fee(5000, 31) == 1250


def test_large_outstanding_over_30_days():
    assert late_payment_fee(15000, 31) == 1750


# ==========================================
# CARD STATUS TEST CASES
# ==========================================

def test_frozen_card():
    assert card_status(50, 0, True) == "frozen"


def test_blocked_card():
    assert card_status(50, 3, False) == "blocked"


def test_over_limit_risk():
    assert card_status(95, 0, False) == "over limit risk"


def test_watch_due_to_utilisation():
    assert card_status(50, 0, False) == "watch"


def test_watch_due_to_missed_payment():
    assert card_status(20, 1, False) == "watch"


def test_good_card_status():
    assert card_status(20, 0, False) == "good"


def test_exactly_90_percent_utilisation():
    assert card_status(90, 0, False) == "watch"


def test_exactly_30_percent_utilisation():
    assert card_status(30, 0, False) == "good"
