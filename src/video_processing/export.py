"""
Video Export Module
Export functionality for final video rendering
"""

import logging
import os
from typing import Optional, Dict, Callable

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class VideoExporter:
    """Video export and rendering operations"""
    
    # Quality presets
    QUALITY_PRESETS = {
        'high': {
            'resolution': (1920, 1080),
            'bitrate': '8000k',
            'fps': 30,
            'codec': 'libx264'
        },
        'medium': {
            'resolution': (1280, 720),
            'bitrate': '4000k',
            'fps': 30,
            'codec': 'libx264'
        },
        'low': {
            'resolution': (854, 480),
            'bitrate': '2000k',
            'fps': 24,
            'codec': 'libx264'
        }
    }
    
    def __init__(self):
        self.export_in_progress = False
    
    def export_video(
        self,
        clip,
        output_path: str,
        quality: str = 'high',
        format: str = 'mp4',
        progress_callback: Optional[Callable] = None
    ) -> bool:
        """
        Export video clip to file
        
        Args:
            clip: MoviePy clip to export
            output_path: Output file path
            quality: Quality preset ('high', 'medium', 'low')
            format: Output format ('mp4', 'avi', 'mov')
            progress_callback: Callback function for progress updates
        
        Returns:
            True if export successful, False otherwise
        """
        try:
            self.export_in_progress = True
            
            # Get quality settings
            if quality not in self.QUALITY_PRESETS:
                quality = 'high'
            
            preset = self.QUALITY_PRESETS[quality]
            
            # Ensure output directory exists
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            # Add extension if not present
            if not output_path.endswith(f'.{format}'):
                output_path = f"{output_path}.{format}"
            
            logger.info(f"Starting export to {output_path}")
            logger.info(f"Quality: {quality}, Format: {format}")
            
            # Define logger function for progress
            def log_progress(t):
                if progress_callback:
                    try:
                        progress_percent = (t / clip.duration) * 100
                        progress_callback(progress_percent, t, clip.duration)
                    except:
                        pass
            
            # Export based on format
            if format == 'mp4':
                clip.write_videofile(
                    output_path,
                    fps=preset['fps'],
                    codec=preset['codec'],
                    bitrate=preset['bitrate'],
                    audio_codec='aac',
                    logger=log_progress if progress_callback else None
                )
            elif format == 'avi':
                clip.write_videofile(
                    output_path,
                    fps=preset['fps'],
                    codec='png',  # Use PNG codec for AVI
                    audio_codec='pcm_s16le',
                    logger=log_progress if progress_callback else None
                )
            elif format == 'mov':
                clip.write_videofile(
                    output_path,
                    fps=preset['fps'],
                    codec='libx264',
                    audio_codec='aac',
                    logger=log_progress if progress_callback else None
                )
            else:
                logger.error(f"Unsupported format: {format}")
                return False
            
            self.export_in_progress = False
            logger.info(f"Export completed: {output_path}")
            return True
            
        except Exception as e:
            self.export_in_progress = False
            logger.error(f"Export failed: {e}")
            return False
    
    def is_exporting(self) -> bool:
        """Check if export is in progress"""
        return self.export_in_progress
    
    def cancel_export(self):
        """Cancel current export (if possible)"""
        # Note: MoviePy doesn't easily support cancellation
        # This would require more advanced threading implementation
        self.export_in_progress = False
        logger.info("Export cancellation requested")
    
    @staticmethod
    def get_quality_info(quality: str) -> Optional[Dict]:
        """Get quality preset information"""
        return VideoExporter.QUALITY_PRESETS.get(quality)
    
    @staticmethod
    def estimate_file_size(duration: float, quality: str) -> float:
        """Estimate output file size in MB"""
        preset = VideoExporter.QUALITY_PRESETS.get(quality, VideoExporter.QUALITY_PRESETS['high'])
        
        # Extract bitrate value (e.g., '8000k' -> 8000)
        bitrate_str = preset['bitrate'].replace('k', '')
        bitrate_kbps = int(bitrate_str)
        
        # Calculate approximate file size
        # File size (MB) = (bitrate in kbps * duration in seconds) / (8 * 1024)
        file_size_mb = (bitrate_kbps * duration) / (8 * 1024)
        
        return file_size_mb
