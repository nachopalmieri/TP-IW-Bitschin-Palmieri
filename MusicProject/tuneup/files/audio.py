
from .base import File
import librosa

class AudioFile(File):
    
    def _load_content(self):
        file_content = super()._load_content()
        return librosa.load(file_content, sr=None)
    
    @property
    def is_valid(self):
        
        if 'audio/' not in self.file.content_type:
            return False
        
        try:
            
            # Tries to load data from audio file
            self._load_content()
        
        except RuntimeError as error:
            print("Error verifying audio file: ", error)
            return False
    
    @property
    def audio_data(self):
        return self._load_content()