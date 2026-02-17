#!/usr/bin/env python3
"""
Video Editor Program for InSoil
A simple yet powerful video editing tool for processing agricultural and educational content.
"""

import os
import logging
from typing import List, Tuple, Optional, Union
from moviepy import (
    VideoFileClip, 
    concatenate_videoclips, 
    CompositeVideoClip,
    TextClip,
    vfx
)

# Configure logging for the module
logging.basicConfig(level=logging.WARNING, format='%(levelname)s: %(message)s')


class VideoEditor:
    """Main video editor class for InSoil video processing."""
    
    def __init__(self, video_path: str):
        """
        Initialize the video editor with a video file.
        
        Args:
            video_path: Path to the input video file
        """
        if not os.path.exists(video_path):
            raise FileNotFoundError(f"Video file not found: {video_path}")
        
        self.video_path = video_path
        self.clip = VideoFileClip(video_path)
    
    def trim(self, start_time: float, end_time: float) -> 'VideoEditor':
        """
        Trim video to specified time range.
        
        Args:
            start_time: Start time in seconds
            end_time: End time in seconds
            
        Returns:
            Self for method chaining
        """
        self.clip = self.clip.subclip(start_time, end_time)
        return self
    
    def add_text(
        self, 
        text: str, 
        position: Tuple[Union[str, int], Union[str, int]] = ('center', 'bottom'),
        duration: Optional[float] = None,
        fontsize: int = 50,
        color: str = 'white',
        bg_color: str = 'black',
        start_time: float = 0
    ) -> 'VideoEditor':
        """
        Add text overlay to the video.
        
        Args:
            text: Text content to display
            position: Position tuple (x, y) or ('center', 'bottom') etc.
            duration: Duration to display text (None = entire video)
            fontsize: Font size
            color: Text color
            bg_color: Background color
            start_time: When to start showing the text
            
        Returns:
            Self for method chaining
        """
        # Validate start_time
        if start_time < 0:
            raise ValueError(f"start_time must be non-negative, got {start_time}")
        if start_time >= self.clip.duration:
            raise ValueError(
                f"start_time {start_time} is at or after the end of the clip "
                f"(duration {self.clip.duration})"
            )
        
        # Compute or validate duration
        if duration is None:
            duration = self.clip.duration - start_time
        else:
            if duration <= 0:
                raise ValueError(f"duration must be positive, got {duration}")
        
        txt_clip = TextClip(
            text, 
            fontsize=fontsize, 
            color=color,
            bg_color=bg_color,
            size=self.clip.size
        )
        txt_clip = txt_clip.set_position(position).set_duration(duration).set_start(start_time)
        
        self.clip = CompositeVideoClip([self.clip, txt_clip])
        return self
    
    def resize_video(self, width: Optional[int] = None, height: Optional[int] = None, scale: Optional[float] = None) -> 'VideoEditor':
        """
        Resize the video.
        
        Args:
            width: Target width in pixels
            height: Target height in pixels
            scale: Scale factor (alternative to width/height)
            
        Returns:
            Self for method chaining
        """
        if scale:
            self.clip = self.clip.with_effects([vfx.Resize(scale)])
        elif width and height:
            self.clip = self.clip.with_effects([vfx.Resize((width, height))])
        elif width:
            self.clip = self.clip.with_effects([vfx.Resize(width=width)])
        elif height:
            self.clip = self.clip.with_effects([vfx.Resize(height=height)])
        return self
    
    def crop_video(self, x1: int, y1: int, x2: int, y2: int) -> 'VideoEditor':
        """
        Crop the video to specified dimensions.
        
        Args:
            x1: Left coordinate
            y1: Top coordinate
            x2: Right coordinate
            y2: Bottom coordinate
            
        Returns:
            Self for method chaining
        """
        self.clip = self.clip.with_effects([vfx.Crop(x1=x1, y1=y1, x2=x2, y2=y2)])
        return self
    
    def add_fade(self, fade_in_duration: float = 0, fade_out_duration: float = 0) -> 'VideoEditor':
        """
        Add fade in/out effects.
        
        Args:
            fade_in_duration: Duration of fade in effect in seconds
            fade_out_duration: Duration of fade out effect in seconds
            
        Returns:
            Self for method chaining
        """
        effects = []
        if fade_in_duration > 0:
            effects.append(vfx.FadeIn(fade_in_duration))
        if fade_out_duration > 0:
            effects.append(vfx.FadeOut(fade_out_duration))
        if effects:
            self.clip = self.clip.with_effects(effects)
        return self
    
    def set_speed(self, factor: float) -> 'VideoEditor':
        """
        Change video playback speed.
        
        Args:
            factor: Speed factor (2.0 = 2x faster, 0.5 = 2x slower)
            
        Returns:
            Self for method chaining
        """
        self.clip = self.clip.with_effects([vfx.MultiplySpeed(factor)])
        return self
    
    def save(self, output_path: str, codec: str = 'libx264', audio_codec: str = 'aac', fps: Optional[int] = None) -> str:
        """
        Save the edited video to a file.
        
        Args:
            output_path: Path to save the output video
            codec: Video codec to use
            audio_codec: Audio codec to use
            fps: Frames per second (None = keep original)
            
        Returns:
            Path to the saved file
        """
        # Create output directory if it doesn't exist
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Set fps if not specified
        if fps is None:
            fps = self.clip.fps
        
        # Write the video file
        self.clip.write_videofile(
            output_path,
            codec=codec,
            audio_codec=audio_codec,
            fps=fps
        )
        
        return output_path
    
    def close(self):
        """Clean up resources."""
        if self.clip:
            self.clip.close()
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()


class VideoMerger:
    """Utility class for merging multiple video clips."""
    
    @staticmethod
    def concatenate_videos(video_paths: List[str], output_path: str, transition_duration: float = 0) -> str:
        """
        Concatenate multiple videos into one.
        
        Args:
            video_paths: List of video file paths to concatenate
            output_path: Path to save the merged video
            transition_duration: Duration of crossfade transition between clips
            
        Returns:
            Path to the saved file
        """
        # Validate input
        if not video_paths:
            raise ValueError("video_paths cannot be empty")
        
        clips = []
        final_clip = None
        
        try:
            # Load all video clips
            for path in video_paths:
                if not os.path.exists(path):
                    raise FileNotFoundError(f"Video file not found: {path}")
                clips.append(VideoFileClip(path))
            
            # Apply crossfade if requested
            if transition_duration > 0:
                # Validate we have at least 2 clips for crossfade
                if len(clips) < 2:
                    raise ValueError(
                        "Crossfade transitions require at least 2 video clips. "
                        "Provide multiple videos or set transition_duration to 0."
                    )
                
                # Validate transition duration doesn't exceed shortest clip
                min_duration = min(clip.duration for clip in clips)
                if transition_duration > min_duration:
                    raise ValueError(
                        f"transition_duration ({transition_duration}s) exceeds the shortest clip "
                        f"duration ({min_duration}s). Please use a shorter transition."
                    )
                
                # Apply crossfade-in to all clips except the first
                for i in range(1, len(clips)):
                    clips[i] = clips[i].with_effects([vfx.CrossFadeIn(transition_duration)])
                final_clip = concatenate_videoclips(
                    clips,
                    method="compose",
                    padding=-transition_duration
                )
            else:
                final_clip = concatenate_videoclips(clips, method="compose")
            
            # Create output directory if needed
            output_dir = os.path.dirname(output_path)
            if output_dir and not os.path.exists(output_dir):
                os.makedirs(output_dir)
            
            final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
            
            return output_path
            
        finally:
            # Clean up all clips
            for clip in clips:
                try:
                    clip.close()
                except Exception as e:
                    logging.warning(f"Error closing clip during cleanup: {e}")
            if final_clip:
                try:
                    final_clip.close()
                except Exception as e:
                    logging.warning(f"Error closing final_clip during cleanup: {e}")


def create_title_video(
    text: str,
    duration: float,
    output_path: str,
    size: Tuple[int, int] = (1920, 1080),
    fontsize: int = 70,
    color: str = 'white',
    bg_color: str = 'black'
) -> str:
    """
    Create a simple title/text video.
    
    Args:
        text: Text to display
        duration: Duration in seconds
        output_path: Path to save the video
        size: Video dimensions (width, height)
        fontsize: Font size
        color: Text color
        bg_color: Background color
        
    Returns:
        Path to the saved file
    """
    txt_clip = TextClip(
        text,
        fontsize=fontsize,
        color=color,
        bg_color=bg_color,
        size=size,
        method='caption'
    ).set_duration(duration)
    
    # Create output directory if needed
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    txt_clip.write_videofile(output_path, fps=24, codec='libx264')
    txt_clip.close()
    
    return output_path


if __name__ == "__main__":
    print("Video Editor for InSoil")
    print("This module provides video editing capabilities.")
    print("Import this module to use VideoEditor, VideoMerger, and other utilities.")
