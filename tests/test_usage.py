
from core.usage_tracker import UsageTracker


def test_initial_usage():

    tracker = UsageTracker()

    assert tracker.total_requests == 0
    assert tracker.total_input_tokens == 0
    assert tracker.total_output_tokens == 0
    assert tracker.total_cost == 0.0


def test_record_usage():

    tracker = UsageTracker()

    tracker.record(
        input_tokens=100,
        output_tokens=200,
        cost=0.001
    )

    assert tracker.total_requests == 1
    assert tracker.total_input_tokens == 100
    assert tracker.total_output_tokens == 200
    assert tracker.total_cost == 0.001


def test_multiple_requests():

    tracker = UsageTracker()

    tracker.record(100, 200, 0.001)
    tracker.record(50, 150, 0.002)

    assert tracker.total_requests == 2
    assert tracker.total_input_tokens == 150
    assert tracker.total_output_tokens == 350
    assert abs(tracker.total_cost - 0.003) < 1e-9


def test_zero_usage():

    tracker = UsageTracker()

    tracker.record()

    assert tracker.total_requests == 1
    assert tracker.total_input_tokens == 0
    assert tracker.total_output_tokens == 0
    assert tracker.total_cost == 0.0
