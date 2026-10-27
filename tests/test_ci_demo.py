"""Temporary failure for the assignment's CI demonstration."""

import pytest


def test_ci_reports_a_failure():
    pytest.fail("Controlled CI failure: remove this demo after inspecting the failed run.")
