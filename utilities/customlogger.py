import logging
class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="C:\\Users\\PraveenKumar187\\Documents\\S2P\\Automation\\Content Intelligence\\Pytest\\Logs\\indexingscreen.log", format='%(asctime)s-%(levelname)s-%(message)s',
                            datefmt='%d-%b-%y %H:%M:%S')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
