"""
Video Effects Module
Transitions and effects for video clips
"""

import logging
from moviepy import VideoFileClip
from moviepy.video.fx import FadeIn, FadeOut, CrossFadeIn, CrossFadeOut

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class VideoEffects:
    """Video transition and effect operations"""
    
    @staticmethod
    def apply_fade_in(clip, duration: float = 1.0):
        """Apply fade in effect to clip"""
        try:
            return clip.with_effects([FadeIn(duration)])
        except Exception as e:
            logger.error(f"Failed to apply fade in: {e}")
            return clip
    
    @staticmethod
    def apply_fade_out(clip, duration: float = 1.0):
        """Apply fade out effect to clip"""
        try:
            return clip.with_effects([FadeOut(duration)])
        except Exception as e:
            logger.error(f"Failed to apply fade out: {e}")
            return clip
    
    @staticmethod
    def apply_crossfade_in(clip, duration: float = 1.0):
        """Apply crossfade in effect to clip"""
        try:
            return clip.with_effects([CrossFadeIn(duration)])
        except Exception as e:
            logger.error(f"Failed to apply crossfade in: {e}")
            return clip
    
    @staticmethod
    def apply_crossfade_out(clip, duration: float = 1.0):
        """Apply crossfade out effect to clip"""
        try:
            return clip.with_effects([CrossFadeOut(duration)])
        except Exception as e:
            logger.error(f"Failed to apply crossfade out: {e}")
            return clip
    
    @staticmethod
    def apply_fade_in_out(clip, fade_in_duration: float = 1.0, fade_out_duration: float = 1.0):
        """Apply both fade in and fade out effects"""
        try:
            clip = clip.with_effects([
                FadeIn(fade_in_duration),
                FadeOut(fade_out_duration)
            ])
            return clip
        except Exception as e:
            logger.error(f"Failed to apply fade in/out: {e}")
            return clip
    
    @staticmethod
    def create_crossfade_transition(clip1, clip2, transition_duration: float = 1.0):
        """Create crossfade transition between two clips"""
        try:
            # Apply fade out to first clip
            clip1 = VideoEffects.apply_fade_out(clip1, transition_duration)
            
            # Apply fade in to second clip
            clip2 = VideoEffects.apply_fade_in(clip2, transition_duration)
            
            # Overlap the clips
            clip2 = clip2.with_start(clip1.duration - transition_duration)
            
            return [clip1, clip2]
        except Exception as e:
            logger.error(f"Failed to create crossfade transition: {e}")
            return [clip1, clip2]
