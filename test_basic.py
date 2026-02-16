"""
Basic test to verify project structure and imports
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

def test_imports():
    """Test that all modules can be imported"""
    
    print("Testing imports...")
    
    try:
        from src.utils.file_handler import FileHandler
        print("✓ FileHandler imported")
    except Exception as e:
        print(f"✗ FileHandler import failed: {e}")
        return False
    
    try:
        from src.utils.media_info import MediaInfo
        print("✓ MediaInfo imported")
    except Exception as e:
        print(f"✗ MediaInfo import failed: {e}")
        return False
    
    try:
        from src.utils.project_manager import ProjectManager
        print("✓ ProjectManager imported")
    except Exception as e:
        print(f"✗ ProjectManager import failed: {e}")
        return False
    
    try:
        from src.video_processing.editor import VideoEditor
        print("✓ VideoEditor imported")
    except Exception as e:
        print(f"✗ VideoEditor import failed: {e}")
        return False
    
    try:
        from src.video_processing.effects import VideoEffects
        print("✓ VideoEffects imported")
    except Exception as e:
        print(f"✗ VideoEffects import failed: {e}")
        return False
    
    try:
        from src.video_processing.text_overlay import TextOverlay
        print("✓ TextOverlay imported")
    except Exception as e:
        print(f"✗ TextOverlay import failed: {e}")
        return False
    
    try:
        from src.video_processing.export import VideoExporter
        print("✓ VideoExporter imported")
    except Exception as e:
        print(f"✗ VideoExporter import failed: {e}")
        return False
    
    print("\n✓ All imports successful!")
    return True


def test_file_handler():
    """Test FileHandler basic functionality"""
    
    print("\nTesting FileHandler...")
    
    from src.utils.file_handler import FileHandler
    
    # Test video file detection
    assert FileHandler.is_video_file("test.mp4") == True
    assert FileHandler.is_video_file("test.txt") == False
    print("✓ Video file detection works")
    
    # Test image file detection
    assert FileHandler.is_image_file("test.jpg") == True
    assert FileHandler.is_image_file("test.mp4") == False
    print("✓ Image file detection works")
    
    # Test audio file detection
    assert FileHandler.is_audio_file("test.mp3") == True
    assert FileHandler.is_audio_file("test.jpg") == False
    print("✓ Audio file detection works")
    
    print("✓ FileHandler tests passed!")
    return True


def test_project_manager():
    """Test ProjectManager basic functionality"""
    
    print("\nTesting ProjectManager...")
    
    from src.utils.project_manager import ProjectManager
    
    pm = ProjectManager()
    
    # Test new project creation
    project = pm.create_new_project()
    assert 'version' in project
    assert 'timeline' in project
    assert 'export_settings' in project
    print("✓ New project creation works")
    
    # Test validation
    assert pm.validate_project_data(project) == True
    print("✓ Project validation works")
    
    print("✓ ProjectManager tests passed!")
    return True


if __name__ == "__main__":
    print("=" * 50)
    print("Video Editor - Basic Tests")
    print("=" * 50)
    
    success = True
    
    # Run tests
    success = success and test_imports()
    success = success and test_file_handler()
    success = success and test_project_manager()
    
    print("\n" + "=" * 50)
    if success:
        print("✓ ALL TESTS PASSED")
    else:
        print("✗ SOME TESTS FAILED")
    print("=" * 50)
    
    sys.exit(0 if success else 1)
