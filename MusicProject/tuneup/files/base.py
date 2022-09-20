
from django.core.files import File as BaseFile


class File(BaseFile):
    
    def _load_content(self):
        """ Custom internal content loader."""
        
        if not self.readable():
            raise RuntimeError("File is not readable at the moment.")
        
        return self
    
    @property
    def extension(self):
        return '.%s' % self.name.split('.')[-1]
    
    @property
    def is_valid(self):
        """ Detects is valid metadata and content for this file kind. """
        return True