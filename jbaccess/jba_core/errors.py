from api_commons.error import ErrorCode

SOMETHING_WRONG = ErrorCode(0x001, "Something went wrong")
INCORRECT_CREDENTIALS = ErrorCode(0x002, "Incorrect credentials")
NOT_SUPPORTED = ErrorCode(0x003, "Not supported")
CONTROLLER_NOT_FOUND = ErrorCode(0x004, "Controller was not found")
DOOR_NOT_FOUND = ErrorCode(0x005, "Door was not found")
PLACE_NOT_FOUND = ErrorCode(0x006, "Person was not found")
PERSON_NOT_FOUND = ErrorCode(0x007, "Person was not found")
KEY_NOT_FOUND = ErrorCode(0x008, "Key was not found")
ROLE_NOT_FOUND = ErrorCode(0x009, "Role was not found")
ACL_NOT_FOUND = ErrorCode(0x00a, "ACL was not found")
CONTROLLER_MANAGE_FAILED = ErrorCode(0x00b, "Controller manage failed")
DOOR_MANAGE_FAILED = ErrorCode(0x00c, "Door manage failed")
PLACE_MANAGE_FAILED = ErrorCode(0x00d, "Person manage failed")
PERSON_MANAGE_FAILED = ErrorCode(0x00e, "Person manage failed")
KEY_MANAGE_FAILED = ErrorCode(0x00f, "Key manage failed")
ROLE_MANAGE_FAILED = ErrorCode(0x010, "Role manage failed")
ACL_MANAGE_FAILED = ErrorCode(0x011, "ACL manage failed")
PATTERN_NOT_FOUND = ErrorCode(0x012, "Pattern was not found")
PATTERN_MANAGE_FAILED = ErrorCode(0x013, "Pattern manage failed")
PATTERN_TIMINGS_INCORRECT = ErrorCode(0x014, "Pattern timings are incorrect")
DATE_PATTERNS_INCORRECT = ErrorCode(0x015, "Date patterns are incorrect")
ACL_ALREADY_ADDED = ErrorCode(0x016, "ACL was already added")
USER_NOT_FOUND = ErrorCode(0x016, "User was not found")
