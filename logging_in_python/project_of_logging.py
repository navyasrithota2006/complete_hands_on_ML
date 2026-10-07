import logging

#logging setting

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S',
    handlers = [
        logging.FileHandler("app1.log"),  #filename initialise
        logging.StreamHandler()  # to write and stream all the logs into the file
    ]
)
#get logger is used to create multiple logger
logger = logging.getLogger("ArithmeticApp")

def add(a,b):
    result = a+b
    logger.debug(f"Adding {a} + {b} = {result}")  #this line when executed the function ,it goes to app1.log file
    return result

def subtract(a,b):
    result = a-b
    logger.debug(f"subtract {a} - {b} = {result}")  #this line when executed the function ,it goes to app1.log file
    return result

def multiply(a,b):
    result = a*b
    logger.debug(f"multiplying {a} * {b} = {result}")  #this line when executed the function ,it goes to app1.log file
    return result

def division(a,b):
    try:
        result = a//b
        logger.debug(f"dividing {a} // {b} = {result}")  #this line when executed the function ,it goes to app1.log file
        return result
    except ZeroDivisionError:
        logger.error("Division by zero is error")
        return None

add(10,15)
subtract(15,10)
multiply(2,3)
division(25,0)