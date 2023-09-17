from dataclasses import dataclass


@dataclass
class Bots:
    bot_token: str
    admin_id: int

@dataclass
class Settings:
    bots: Bots


def get_settings():
    config_file = open(r'.\config', 'r')

    return Settings(
        bots=Bots(
            bot_token=config_file.readline().replace('\n', ''),
            admin_id=int(config_file.readline())
        )
    )


settings = get_settings()
