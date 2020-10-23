import logging

log = logging.getLogger(__name__)

def set_logging_level(level: str) -> object:
    '''
    Set logging level

    Parameters
    ----------
    level: str
            level to log

    Returns
    -------
    Logging level object
    '''
    if(level.upper() == "DEBUG"):
        return logging.DEBUG
    elif(level.upper() == "INFO"):
        return logging.INFO
    elif(level.upper() == "WARNING"):
        return logging.WARNING
    elif(level.upper() == "CRITICAL"):
        return logging.CRITICAL
    else:
        return None