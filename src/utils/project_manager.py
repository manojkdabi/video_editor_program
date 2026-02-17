"""
Project Manager Module
Handles saving and loading of video editor projects
"""

import json
import logging
from typing import Dict, Optional, List
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ProjectManager:
    """Manages video editor project files"""
    
    def __init__(self):
        self.current_project_path: Optional[str] = None
        self.project_modified: bool = False
    
    def create_new_project(self) -> Dict:
        """Create a new empty project"""
        return {
            'version': '1.0',
            'created': datetime.now().isoformat(),
            'modified': datetime.now().isoformat(),
            'timeline': {
                'video_clips': [],
                'image_clips': [],
                'audio_clips': [],
                'text_overlays': []
            },
            'export_settings': {
                'format': 'mp4',
                'resolution': '1920x1080',
                'quality': 'high',
                'fps': 30
            }
        }
    
    def save_project(self, project_data: Dict, filepath: str) -> bool:
        """Save project to file"""
        try:
            # Update modified timestamp
            project_data['modified'] = datetime.now().isoformat()
            
            with open(filepath, 'w') as f:
                json.dump(project_data, f, indent=4)
            
            self.current_project_path = filepath
            self.project_modified = False
            logger.info(f"Project saved to {filepath}")
            return True
        except Exception as e:
            logger.error(f"Failed to save project: {e}")
            return False
    
    def load_project(self, filepath: str) -> Optional[Dict]:
        """Load project from file"""
        try:
            with open(filepath, 'r') as f:
                project_data = json.load(f)
            
            self.current_project_path = filepath
            self.project_modified = False
            logger.info(f"Project loaded from {filepath}")
            return project_data
        except Exception as e:
            logger.error(f"Failed to load project: {e}")
            return None
    
    def mark_modified(self):
        """Mark project as modified"""
        self.project_modified = True
    
    def is_modified(self) -> bool:
        """Check if project has been modified"""
        return self.project_modified
    
    def get_current_project_path(self) -> Optional[str]:
        """Get current project file path"""
        return self.current_project_path
    
    def validate_project_data(self, project_data: Dict) -> bool:
        """Validate project data structure"""
        required_keys = ['version', 'timeline', 'export_settings']
        
        if not all(key in project_data for key in required_keys):
            return False
        
        timeline_keys = ['video_clips', 'image_clips', 'audio_clips', 'text_overlays']
        if not all(key in project_data['timeline'] for key in timeline_keys):
            return False
        
        return True
