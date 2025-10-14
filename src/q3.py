from datetime import datetime
from typing import Dict, Any, Optional

"""
Please implement the methods and constructors in these two classes.
"""

class User:
    """A user of the system"""
    _next_id = 1
    
    def __init__(self, username: str, email: str, password: str, admin_level: int = 1) -> None:
        self.id = User._next_id
        User._next_id += 1
        self.admin_level = admin_level
    
    def authenticate(self, password: str) -> bool:
        """Return True if the password is correct"""
        pass
    
    def log_out(self) -> bool:
        """Return True if the user was previously logged in. Log them out."""
        pass
    
    def change_password(self, old_password: str, new_password: str) -> bool:
        """Return True if it worked"""
        pass
    
    def _get_default_permissions(self) -> list[str]:
        """Get permissions based on admin level"""
        base_permissions = ["read", "write"]
        if self.admin_level >= 2:
            base_permissions.extend(["delete", "modify_users"])
        if self.admin_level >= 3:
            base_permissions.extend(["system_admin", "manage_permissions"])
        return base_permissions

class AdminUser(User):
    """A user with admin privileges"""
    def __init__(self, username: str, email: str, password: str) -> None:
        """Initialize an AdminUser with admin level 3"""
        pass
    
    def promote_user(self, user: User, new_admin_level: int) -> bool:
        """Change the provided user's admin level"""
        pass
        
        # Check if "modify_users" is in this user's permissions
        # If so, change the specified user's admin level
        # Return True if it worked
    