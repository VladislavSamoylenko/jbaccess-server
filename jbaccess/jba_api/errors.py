from api_commons.error import ErrorCode

SOMETHING_WRONG = ErrorCode(0x001, "Something went wrong")
INCORRECT_CREDENTIALS = ErrorCode(0x002, "Incorrect credentials")
NOT_SUPPORTED = ErrorCode(0x003, "Not supported")
CALCULATION_FAILED = ErrorCode(0x004, "Calculation failed")
CONTROLLER_NOT_FOUND = ErrorCode(0x005, "Controller was not found")
DOOR_NOT_FOUND = ErrorCode(0x006, "Door was not found")
PLACE_NOT_FOUND = ErrorCode(0x007, "Person was not found")
PERSON_NOT_FOUND = ErrorCode(0x008, "Person was not found")
KEY_NOT_FOUND = ErrorCode(0x009, "Key was not found")
ROLE_NOT_FOUND = ErrorCode(0x00a, "Role was not found")
ACL_NOT_FOUND = ErrorCode(0x00b, "ACL was not found")
CONTROLLER_MANAGE_FAILED = ErrorCode(0x00c, "Controller was manage failed")
DOOR_MANAGE_FAILED = ErrorCode(0x00d, "Door was manage failed")
PLACE_MANAGE_FAILED = ErrorCode(0x00e, "Person was manage failed")
PERSON_MANAGE_FAILED = ErrorCode(0x00f, "Person was manage failed")
KEY_MANAGE_FAILED = ErrorCode(0x010, "Key was manage failed")
ROLE_MANAGE_FAILED = ErrorCode(0x011, "Role was manage failed")
ACL_MANAGE_FAILED = ErrorCode(0x012, "ACL was manage failed")
