from colorprt import ColorprtConfig
from colorprt._vars import Fore
__DEBUG__ = True
log_color = ColorprtConfig(Fore.BLUE)
log_error_color = ColorprtConfig(Fore.RED)


def logger(message: str, **kwds):
    if __DEBUG__:
        log_color(message, **kwds)


def logger_error(message: str, **kwds):
    if __DEBUG__:
        log_error_color(message, **kwds)
