"""
Video Editor Core Module
Core video editing functionality using MoviePy
"""

import logging
from typing import List, Optional, Tuple
from moviepy import VideoFileClip, ImageClip, AudioFileClip, CompositeVideoClip, concatenate_videoclips
import numpy as np

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class VideoEditor:
    """Core video editing operations"""
    
    def __init__(self):
        self.clips: List = []
        self.audio_clips: List = []
    
    def load_video_clip(self, filepath: str, start: float = 0, end: Optional[float] = None) -> Optional[VideoFileClip]:
        """Load a video clip with optional trimming"""
        try:
            clip = VideoFileClip(filepath)
            
            # Apply trimming if specified
            if end is not None:
                clip = clip.subclipped(start, end)
            elif start > 0:
                clip = clip.subclipped(start, clip.duration)
            
            logger.info(f"Loaded video clip: {filepath}")
            return clip
        except Exception as e:
            logger.error(f"Failed to load video clip {filepath}: {e}")
            return None
    
    def load_image_clip(self, filepath: str, duration: float = 5.0) -> Optional[ImageClip]:
        """Load an image as a video clip with specified duration"""
        try:
            clip = ImageClip(filepath, duration=duration)
            logger.info(f"Loaded image clip: {filepath}")
            return clip
        except Exception as e:
            logger.error(f"Failed to load image clip {filepath}: {e}")
            return None
    
    def load_audio_clip(self, filepath: str, start: float = 0, end: Optional[float] = None) -> Optional[AudioFileClip]:
        """Load an audio clip with optional trimming"""
        try:
            clip = AudioFileClip(filepath)
            
            # Apply trimming if specified
            if end is not None:
                clip = clip.subclipped(start, end)
            elif start > 0:
                clip = clip.subclipped(start, clip.duration)
            
            logger.info(f"Loaded audio clip: {filepath}")
            return clip
        except Exception as e:
            logger.error(f"Failed to load audio clip {filepath}: {e}")
            return None
    
    def trim_clip(self, clip, start: float, end: float):
        """Trim a clip to specified start and end times"""
        try:
            return clip.subclipped(start, end)
        except Exception as e:
            logger.error(f"Failed to trim clip: {e}")
            return clip
    
    def concatenate_clips(self, clips: List, method: str = "compose") -> Optional[VideoFileClip]:
        """Concatenate multiple video clips"""
        try:
            if not clips:
                logger.warning("No clips to concatenate")
                return None
            
            if len(clips) == 1:
                return clips[0]
            
            # Concatenate clips
            final_clip = concatenate_videoclips(clips, method=method)
            logger.info(f"Concatenated {len(clips)} clips")
            return final_clip
        except Exception as e:
            logger.error(f"Failed to concatenate clips: {e}")
            return None
    
    def resize_clip(self, clip, width: int, height: int):
        """Resize a clip to specified dimensions"""
        try:
            return clip.resized((width, height))
        except Exception as e:
            logger.error(f"Failed to resize clip: {e}")
            return clip
    
    def set_clip_position(self, clip, position: Tuple[int, int]):
        """Set clip position (x, y) on canvas"""
        try:
            return clip.with_position(position)
        except Exception as e:
            logger.error(f"Failed to set clip position: {e}")
            return clip
    
    def set_clip_start_time(self, clip, start_time: float):
        """Set when clip should start in the final video"""
        try:
            return clip.with_start(start_time)
        except Exception as e:
            logger.error(f"Failed to set clip start time: {e}")
            return clip
    
    def set_clip_duration(self, clip, duration: float):
        """Set clip duration"""
        try:
            return clip.with_duration(duration)
        except Exception as e:
            logger.error(f"Failed to set clip duration: {e}")
            return clip
    
    def add_audio_to_video(self, video_clip, audio_clip):
        """Add audio track to video clip"""
        try:
            return video_clip.with_audio(audio_clip)
        except Exception as e:
            logger.error(f"Failed to add audio to video: {e}")
            return video_clip
    
    def composite_clips(self, clips: List, size: Tuple[int, int] = (1920, 1080)):
        """Create composite video from multiple clips with positioning"""
        try:
            return CompositeVideoClip(clips, size=size)
        except Exception as e:
            logger.error(f"Failed to create composite: {e}")
            return None
    
    def close_clip(self, clip):
        """Close and cleanup a clip"""
        try:
            if clip is not None:
                clip.close()
        except Exception as e:
            logger.error(f"Failed to close clip: {e}")
