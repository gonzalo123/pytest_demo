from app import sum
import os





def test_sum():
    assert sum(1, 2) == 3



def test_mock(monkeypatch):
    monkeypatch.setattr(os, "getenv", lambda key: f'XXX:{key}')

    assert os.getenv('GONZALO') == 'XXX:GONZALO'


def test_fixture(fixture_demo):
    assert fixture_demo == 'Gonzalo'


def test_setup(setup):
    item1, item2 = setup
    assert item1 == 'item1'
    assert item2 == 'item2'
