import pytest
from fixture.driver import ChromeDriver

ENV_FIXTURE = None


@pytest.fixture(scope="session", autouse=True)
def stand(request):
    global ENV_FIXTURE
    ENV_FIXTURE = request.config.getoption("--stand")
    return ENV_FIXTURE


@pytest.fixture(scope='session')
def driver(stand):
    d = ChromeDriver(stand)
    yield d.driver
    d.driver.quit()


def pytest_addoption(parser):
    parser.addoption("--stand", default="prod", action="store", type=str,
                     help="Set value for environment. Available environments: dev, preprod, prod")
