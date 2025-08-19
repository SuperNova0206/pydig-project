# pydig/__init__.py

__version__ = "0.1.0"
__app_name__ = "pydig"

(
    SUCCESS,
    CONFIG_DIR_ERROR,
    CONFIG_FILE_ERROR,
    WRITE_DATA_ERROR,
    OUTPUT_LOCATION_ERROR,
    DOWNLOAD_DATA_ERROR,
    INTERNET_ERROR,
    DATA_ERROR,
    INCONNECT_DATA_ERROR,
    FORM_ERROR,
    VIDEO_NOT_FOUND_ERROR
) = range(11)

ERRORS = {
    CONFIG_DIR_ERROR : "creating config directory failed!",
    CONFIG_FILE_ERROR : "creating config file failed!",
    WRITE_DATA_ERROR : "assigning data to config file failed!",
    OUTPUT_LOCATION_ERROR : "creating pydig output data location failed!",
    DOWNLOAD_DATA_ERROR : "downloading data failed!",
    INTERNET_ERROR : "no internet connection!",
    DATA_ERROR : "data not found!",
    INCONNECT_DATA_ERROR : "incorrect data!",
    FORM_ERROR : "form does not exist!",
    VIDEO_NOT_FOUND_ERROR : "video not found!"
}
