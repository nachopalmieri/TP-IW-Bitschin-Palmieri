
from .base import File


class AudioFile(File): 
    @property
    def is_valid(self):
        return 'audio/' in self.file.content_type