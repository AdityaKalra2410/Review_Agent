from user_store import evaluate_rule


def test_evaluate_rule_simple():
    assert evaluate_rule("1 + 1", {}) == 2


def test_percentage_discount_is_applied():
    # Seeded failing test: the helper returns a fraction, not a percentage.
    assert evaluate_rule("price * 0.9", {"price": 100}) == 90.0


def test_known_broken_rounding():
    # Seeded failing test - this is expected to fail.
    assert evaluate_rule("0.1 + 0.2", {}) == 0.3
