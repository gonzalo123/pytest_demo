import pytest
import logging

logger = logging.getLogger(__name__)


@pytest.fixture
def setup():
    logger.info("Setup")
    item1 = 'item1'
    item2 = 'item2'
    yield item1, item2
    logger.info("safe teardown")


@pytest.fixture()
def fixture_demo():
    return "Gonzalo"
