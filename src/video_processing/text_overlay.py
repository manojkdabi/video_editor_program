"""
Text Overlay Module
Add text overlays to video clips
"""

import logging
from typing import Tuple, Optional
from moviepy import TextClip, CompositeVideoClip

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TextOverlay:
    """Text overlay operations for video clips"""
    
    @staticmethod
    def create_text_clip(
        text: str,
        duration: float,
        fontsize: int = 50,
        color: str = 'white',
        bg_color: Optional[str] = None,
        font: str = 'Arial',
        position: Tuple = ('center', 'bottom'),
        start_time: float = 0
    ):
        """
        Create a text clip with specified properties
        
        Args:
            text: Text to display
            duration: How long text should be shown (seconds)
            fontsize: Font size
            color: Text color
            bg_color: Background color (None for transparent)
            font: Font name
            position: Position on screen ('center', 'top', 'bottom', or tuple (x, y))
            start_time: When to start showing the text
        """
        try:
            # Create text clip
            txt_clip = TextClip(
                text=text,
                font_size=fontsize,
                color=color,
                font=font,
                bg_color=bg_color,
                size=None,  # Auto-size based on text
                duration=duration
            )
            
            # Set position
            txt_clip = txt_clip.with_position(position)
            
            # Set start time
            txt_clip = txt_clip.with_start(start_time)
            
            logger.info(f"Created text clip: '{text}'")
            return txt_clip
        except Exception as e:
            logger.error(f"Failed to create text clip: {e}")
            return None
    
    @staticmethod
    def add_text_to_video(video_clip, text_clip):
        """Add text overlay to video clip"""
        try:
            # Composite video with text
            result = CompositeVideoClip([video_clip, text_clip])
            logger.info("Added text overlay to video")
            return result
        except Exception as e:
            logger.error(f"Failed to add text to video: {e}")
            return video_clip
    
    @staticmethod
    def create_title_clip(
        title: str,
        duration: float = 3.0,
        fontsize: int = 70,
        color: str = 'white',
        bg_color: str = 'black',
        video_size: Tuple[int, int] = (1920, 1080)
    ):
        """Create a title screen clip"""
        try:
            txt_clip = TextClip(
                text=title,
                font_size=fontsize,
                color=color,
                font='Arial-Bold',
                bg_color=bg_color,
                size=video_size,
                duration=duration
            )
            
            txt_clip = txt_clip.with_position('center')
            
            logger.info(f"Created title clip: '{title}'")
            return txt_clip
        except Exception as e:
            logger.error(f"Failed to create title clip: {e}")
            return None
    
    @staticmethod
    def create_subtitle_clip(
        text: str,
        duration: float,
        start_time: float = 0,
        fontsize: int = 40,
        color: str = 'white',
        bg_color: str = 'black',
        position: Tuple = ('center', 'bottom')
    ):
        """Create a subtitle clip"""
        try:
            txt_clip = TextClip(
                text=text,
                font_size=fontsize,
                color=color,
                font='Arial',
                bg_color=bg_color,
                duration=duration
            )
            
            txt_clip = txt_clip.with_position(position)
            txt_clip = txt_clip.with_start(start_time)
            
            logger.info(f"Created subtitle clip: '{text}'")
            return txt_clip
        except Exception as e:
            logger.error(f"Failed to create subtitle clip: {e}")
            return None
