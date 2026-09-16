"""
Tests for the decay simulation.

One complete test is given as a model. Add the two tests described in the
lab handout (a negative-rate test, and a test against the analytical law).
Run with:  pytest -v
"""

import numpy as np
import pytest
from decay import simulate, simulate_loop


def test_starts_at_N0():
    assert simulate(1000, 0.4)[0] == 1000


def test_rejects_negative_rate():
    with pytest.raises(ValueError):
        simulate(1000, -0.4)


def test_matches_law():
    N0 = 1000
    lam = 0.4
    dt = 0.05
    t = 2.0

    seeds = range(100)

    index = int(t / dt)

    results = [
        simulate(N0, lam, dt=dt, seed=seed)[index]
        for seed in seeds
    ]

    average = np.mean(results)
    expected = N0 * np.exp(-lam * t)

    assert average == pytest.approx(expected, rel=0.05)