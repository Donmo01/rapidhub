import os
import ctypes
import logging
from ctypes import wintypes

# Initialize logging
logging.basicConfig(filename='rapidhub.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
SE_FILE_OBJECT = 1
DACL_SECURITY_INFORMATION = 4

# Define necessary structures and functions
class SECURITY_DESCRIPTOR(ctypes.Structure):
    _fields_ = []

class ACL(ctypes.Structure):
    _fields_ = []

class TRUSTEE(ctypes.Structure):
    _fields_ = [
        ('pMultipleTrustee', wintypes.LPVOID),
        ('MultipleTrusteeOperation', wintypes.DWORD),
        ('TrusteeForm', wintypes.DWORD),
        ('TrusteeType', wintypes.DWORD),
        ('ptstrName', wintypes.LPWSTR)
    ]

class EXPLICIT_ACCESS(ctypes.Structure):
    _fields_ = [
        ('grfAccessPermissions', wintypes.DWORD),
        ('grfAccessMode', wintypes.DWORD),
        ('grfInheritance', wintypes.DWORD),
        ('Trustee', TRUSTEE)
    ]

SetNamedSecurityInfo = ctypes.windll.advapi32.SetNamedSecurityInfoW

def set_permissions(file_path, permissions, user):
    # Set explicit access
    explicit_access = EXPLICIT_ACCESS()
    explicit_access.grfAccessPermissions = permissions
    explicit_access.grfAccessMode = 3  # SET_ACCESS
    explicit_access.grfInheritance = 0  # NO_INHERITANCE

    trustee = TRUSTEE()
    trustee.TrusteeForm = 1  # TRUSTEE_IS_NAME
    trustee.ptstrName = user

    explicit_access.Trustee = trustee

    # Set security info
    result = SetNamedSecurityInfo(
        file_path,
        SE_FILE_OBJECT,
        DACL_SECURITY_INFORMATION,
        None,
        None,
        ctypes.byref(explicit_access),
        None
    )

    if result == 0:
        logging.info(f"Permissions set successfully for {user} on {file_path}")
    else:
        logging.error(f"Failed to set permissions for {user} on {file_path}. Error code: {result}")

if __name__ == "__main__":
    file_path = input("Enter the file path: ")
    permissions = int(input("Enter the permissions (in numeric form): "))
    user = input("Enter the username: ")

    if os.path.exists(file_path):
        set_permissions(file_path, permissions, user)
    else:
        logging.error(f"File {file_path} does not exist.")
        print("The specified file does not exist.")