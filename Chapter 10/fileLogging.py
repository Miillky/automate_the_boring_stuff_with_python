import logging

logging.basicConfig(filename='./Chapter 10/myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.critical('Critical error! Critical error!')