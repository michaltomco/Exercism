import pytest


def pytest_configure(config):
    config.addinivalue_line("markers", "task(taskno): mark test with a task number")
