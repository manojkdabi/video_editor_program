"""
Media Info Module
Extracts metadata from video and audio files
"""

import logging
from typing import Dict, Optional
from moviepy import VideoFileClip, AudioFileClip
from PIL import Image

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MediaInfo:
    """Extracts and provides media file information"""
    
    @staticmethod
    def get_video_info(filepath: str) -> Optional[Dict]:
        """Get video file information"""
        try:
            with VideoFileClip(filepath) as clip:
                info = {
                    'duration': clip.duration,
                    'fps': clip.fps,
                    'size': clip.size,  # (width, height)
                    'width': clip.w,
                    'height': clip.h,
                    'has_audio': clip.audio is not None,
                    'filepath': filepath
                }
                return info
        except Exception as e:
            logger.error(f"Failed to get video info for {filepath}: {e}")
            return None
    
    @staticmethod
    def get_audio_info(filepath: str) -> Optional[Dict]:
        """Get audio file information"""
        try:
            with AudioFileClip(filepath) as clip:
                info = {
                    'duration': clip.duration,
                    'fps': clip.fps,
                    'nchannels': clip.nchannels,
                    'filepath': filepath
                }
                return info
        except Exception as e:
            logger.error(f"Failed to get audio info for {filepath}: {e}")
            return None
    
    @staticmethod
    def get_image_info(filepath: str) -> Optional[Dict]:
        """Get image file information"""
        try:
            with Image.open(filepath) as img:
                info = {
                    'size': img.size,  # (width, height)
                    'width': img.width,
                    'height': img.height,
                    'format': img.format,
                    'mode': img.mode,
                    'filepath': filepath
                }
                return info
        except Exception as e:
            logger.error(f"Failed to get image info for {filepath}: {e}")
            return None
    
    @staticmethod
    def format_duration(seconds: float) -> str:
        """Format duration in seconds to HH:MM:SS.mmm"""
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = seconds % 60
        return f"{hours:02d}:{minutes:02d}:{secs:06.3f}"
    
    @staticmethod
    def format_resolution(width: int, height: int) -> str:
        """Format resolution as WxH"""
        return f"{width}x{height}"
