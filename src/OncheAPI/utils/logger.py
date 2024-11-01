import logging


def create_custom_logger(name_logger: str = "BDD",
                         file_name: str = "bdd.log") -> logging.Logger:
    """
    Créer le logger au format bdd
    :param name_logger: nom du logger
    :param file_name: nom du fichier
    :return: Logger
    """
    logger = logging.getLogger(f"{name_logger}.log")
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    fh = logging.FileHandler(file_name)
    fh.setLevel(logging.INFO)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger

API_LOG = create_custom_logger("API_LOG", "api_log")