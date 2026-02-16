"""
File Handler Module
Handles file operations for the video editor
"""

import os
import logging
from pathlib import Path
from typing import List, Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class FileHandler:
    """Handles file operations and validation"""
    
    # Supported file formats
    VIDEO_FORMATS = ['.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv', '.webm']
    IMAGE_FORMATS = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff']
    AUDIO_FORMATS = ['.mp3', '.wav', '.aac', '.ogg', '.m4a', '.flac']
    PROJECT_FORMAT = '.vedproj'
    
    @staticmethod
    def is_video_file(filepath: str) -> bool:
        """Check if file is a supported video format"""
        ext = Path(filepath).suffix.lower()
        return ext in FileHandler.VIDEO_FORMATS
    
    @staticmethod
    def is_image_file(filepath: str) -> bool:
        """Check if file is a supported image format"""
        ext = Path(filepath).suffix.lower()
        return ext in FileHandler.IMAGE_FORMATS
    
    @staticmethod
    def is_audio_file(filepath: str) -> bool:
        """Check if file is a supported audio format"""
        ext = Path(filepath).suffix.lower()
        return ext in FileHandler.AUDIO_FORMATS
    
    @staticmethod
    def validate_file_exists(filepath: str) -> bool:
        """Check if file exists"""
        return os.path.isfile(filepath)
    
    @staticmethod
    def get_safe_filename(filepath: str) -> str:
        """Get safe filename for Windows"""
        # Remove invalid characters for Windows filenames
        invalid_chars = '<>:"|?*'
        filename = os.path.basename(filepath)
        for char in invalid_chars:
            filename = filename.replace(char, '_')
        return filename
    
    @staticmethod
    def ensure_directory_exists(directory: str) -> bool:
        """Create directory if it doesn't exist"""
        try:
            os.makedirs(directory, exist_ok=True)
            return True
        except Exception as e:
            logger.error(f"Failed to create directory {directory}: {e}")
            return False
    
    @staticmethod
    def get_file_size_mb(filepath: str) -> float:
        """Get file size in megabytes"""
        try:
            size_bytes = os.path.getsize(filepath)
            return size_bytes / (1024 * 1024)
        except Exception as e:
            logger.error(f"Failed to get file size: {e}")
            return 0.0
    
    @staticmethod
    def filter_files_by_type(filepaths: List[str], file_type: str) -> List[str]:
        """Filter files by type (video, image, audio)"""
        filtered = []
        for filepath in filepaths:
            if file_type == 'video' and FileHandler.is_video_file(filepath):
                filtered.append(filepath)
            elif file_type == 'image' and FileHandler.is_image_file(filepath):
                filtered.append(filepath)
            elif file_type == 'audio' and FileHandler.is_audio_file(filepath):
                filtered.append(filepath)
        return filtered
