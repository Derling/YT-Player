from selenium import common

# TO-DO actually make a wrapper class for these errors
DRIVER_NOT_FOUND_ERROR = common.exceptions.WebDriverException
WEBPAGE_LOADING_ERROR = common.exceptions.ElementNotVisibleException