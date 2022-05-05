from pathlib import Path
import yaml

ROOT_DIR = Path(__file__).parent.parent
CONFIG_DIR = ROOT_DIR / "config"


class ApplicationConfig:
    def __init__(self, filename: str = "application.yml"):
        path_to_config = CONFIG_DIR / filename
        with open(path_to_config, "r") as app_conf:
            self.__cfg = yaml.load(app_conf, Loader=yaml.BaseLoader)

    @property
    def environments(self) -> dict: return self.__cfg.get('environments')
