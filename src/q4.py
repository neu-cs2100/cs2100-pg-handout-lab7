from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import datetime

"""
Please fix the issues in these classes:
"""

class FileSystemItem(ABC):
    def __init__(self, name: str, parent: Optional['Directory'] = None):
        self.name = name
        self.parent = parent
        self.created_at = datetime.now()
    
    @abstractmethod
    def get_size(self) -> int:
        """Get size in bytes"""
        pass
    
    def get_path(self) -> str:
        """Get full path from root"""
        if self.parent is None:
            return self.name
        return f"{self.parent.get_path}/self.name"
    
    @abstractmethod
    def copy(self, new_name: str) -> 'FileSystemItem':
        """Create a copy of this item"""
        pass

class File(FileSystemItem):
    def __init__(self, name: str, content: str = "", parent: Optional['Directory'] = None):
        super().__init__(name, parent)
        self.content = content
    
    def get_size(self) -> int:
        return len(self.content.encode('utf-8'))
    
    def write(self, content: str) -> Optional[str]:
        self.content = content
        return f"Wrote {len(content)} characters to {self.name}"
    
    def read(self) -> str:
        return self.content
    
    def copy(self, new_name: str) -> 'File':
        return File(new_name, self.content, self.parent)

class Directory(FileSystemItem):
    def __init__(self, name: str, parent: Optional['Directory'] = None):
        super().__init__(name, parent)
        self.children: List[FileSystemItem] = []
    
    def get_size(self) -> int:
        """Directory size is sum of all children"""
        return sum(child.get_size() for child in self.children)
    
    def add_child(self, item: FileSystemItem) -> None:
        item.parent = self
        self.children.append(item)
        return f"Added {item.name} to {self.name}"
    
    def find_item(self, name: str) -> Optional[FileSystemItem]:
        """Find immediate child by name"""
        for child in self.children:
            if child.name == name:
                return child
        return None
    
    def list_contents(self) -> List[str]:
        """List all immediate children"""
        return [f"{child.__class__.__name__}: {child.name}" for child in self.children]
    
    def copy(self, new_name: str) -> 'Directory':
        """Deep copy directory and all contents"""
        new_dir = Directory(new_name, self.parent)
        for child in self.children:
            child_copy = child.copy(child.name)
            new_dir.add_child(child_copy)
        return new_dir

class SymbolicLink(FileSystemItem):
    def __init__(self, name: str, target: FileSystemItem, parent: Optional['Directory'] = None):
        super().__init__(name, parent)
        self.target = target
    
    def get_size(self) -> int:
        """Symbolic link size is the size of its target"""
        return self.target.get_size()
    
    def resolve(self) -> FileSystemItem:
        """Follow the link to get the actual target"""
        return self.target
    
    def copy(self, new_name: str) -> 'SymbolicLink':
        return SymbolicLink(new_name, self.parent, self.target)
    
    def read(self) -> str:
        """If target is a file, read its content"""
        if isinstance(self.target, File):
            return self.target.read()
        raise TypeError("Cannot read non-file target")