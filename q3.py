from datetime import datetime
from typing import Dict, Any, Optional

"""
Please implement the methods and constructors in these stub classes.
"""

class BaseModel:
    """Base class for all database models"""
    _next_id = 1
    
    def __init__(self) -> None:
        self.id = BaseModel._next_id
        BaseModel._next_id += 1
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def save(self) -> bool:
        self.updated_at = datetime.now()
        print(f"Saving {self.__class__.__name__} with ID {self.id}")
        return True
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert model to dictionary representation"""
        result = {}
        for attr_name in dir(self):
            if not attr_name.startswith('_') and not callable(getattr(self, attr_name)):
                result[attr_name] = getattr(self, attr_name)
        return result
    
    def update_fields(self, **kwargs: dict[str, Any]) -> None:
        """Update multiple fields at once"""
        for field, value in kwargs.items():
            if hasattr(self, field):
                setattr(self, field, value)
        self.save()

class User(BaseModel):
    def __init__(self, username: str, email: str, password: str):
        pass
    
    def authenticate(self, password: str) -> bool:
        """Return True if it worked"""
        pass
    
    def deactivate(self) -> bool:
        """Return True if it worked"""
        pass
    
    def change_password(self, old_password: str, new_password: str) -> bool:
        """Return True if it worked"""
        pass
    
    def to_dict(self) -> Dict[str, Any]:
        """Override to exclude private password"""
        pass

class AdminUser(User):
    def __init__(self, username: str, email: str, password: str, admin_level: int = 1):
        self.admin_level = admin_level
    
    def _get_default_permissions(self) -> list[str]:
        """Get permissions based on admin level"""
        base_permissions = ["read", "write"]
        if self.admin_level >= 2:
            base_permissions.extend(["delete", "modify_users"])
        if self.admin_level >= 3:
            base_permissions.extend(["system_admin", "manage_permissions"])
        return base_permissions
    
    def promote_user(self, user: User, new_admin_level: int) -> bool:
        """Convert regular user to admin"""
        
        # Check if "modify_users" is in this user's permissions
        # If so, change the user's admin level
        # Return True if it worked
    
    def get_admin_info(self) -> str:
        pass
    