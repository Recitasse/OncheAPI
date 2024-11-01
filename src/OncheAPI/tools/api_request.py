from contextlib import contextmanager
import logging
from typing import Callable


@contextmanager
def api(api_method: Callable, *args, **kwargs):
    """
    Exécute l'api avec les loggers
    :param api_method: Méthode de l'api
    :param args: args de la méthodes
    :param kwargs: kwargs de la méthode
    :return: data
    """
    data = None
    log = logging.getLogger("API_LOG")
    try:
        data = api_method(*args, **kwargs)
        log.info(f"Requête {api_method.__name__} effectuée.")
    except Exception as e:
        log.error(f"Requête erreur {api_method.__name__}.\n{e}.")
        data = {"state": False}
    finally:
        return data