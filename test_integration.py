"""
Integration test for video processing modules
Tests video, image, and audio handling without GUI
"""

import sys
from pathlib import Path
import tempfile
import os

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from src.video_processing.editor import VideoEditor
from src.video_processing.effects import VideoEffects
from src.video_processing.export import VideoExporter
from src.utils.file_handler import FileHandler
from src.utils.project_manager import ProjectManager


def test_video_editor_initialization():
    """Test VideoEditor can be instantiated"""
    print("\nTesting VideoEditor initialization...")
    editor = VideoEditor()
    assert editor is not None
    assert editor.clips == []
    assert editor.audio_clips == []
    print("✓ VideoEditor initialized successfully")
    return True


def test_video_effects():
    """Test VideoEffects class methods exist"""
    print("\nTesting VideoEffects...")
    
    # Test static methods exist
    assert hasattr(VideoEffects, 'apply_fade_in')
    assert hasattr(VideoEffects, 'apply_fade_out')
    assert hasattr(VideoEffects, 'apply_crossfade_in')
    assert hasattr(VideoEffects, 'apply_crossfade_out')
    assert hasattr(VideoEffects, 'apply_fade_in_out')
    assert hasattr(VideoEffects, 'create_crossfade_transition')
    
    print("✓ All VideoEffects methods available")
    return True


def test_video_exporter():
    """Test VideoExporter initialization and presets"""
    print("\nTesting VideoExporter...")
    
    exporter = VideoExporter()
    assert exporter is not None
    assert not exporter.is_exporting()
    
    # Test quality presets
    assert 'high' in VideoExporter.QUALITY_PRESETS
    assert 'medium' in VideoExporter.QUALITY_PRESETS
    assert 'low' in VideoExporter.QUALITY_PRESETS
    
    # Test quality info retrieval
    high_info = VideoExporter.get_quality_info('high')
    assert high_info is not None
    assert 'resolution' in high_info
    assert 'bitrate' in high_info
    assert 'fps' in high_info
    assert high_info['resolution'] == (1920, 1080)
    
    # Test file size estimation
    estimated_size = VideoExporter.estimate_file_size(60, 'high')  # 1 minute video
    assert estimated_size > 0
    print(f"  Estimated file size for 1 minute 'high' quality: {estimated_size:.2f} MB")
    
    print("✓ VideoExporter working correctly")
    return True


def test_file_handler_comprehensive():
    """Comprehensive FileHandler tests"""
    print("\nTesting FileHandler comprehensively...")
    
    # Test all video formats
    video_formats = ['.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv', '.webm']
    for fmt in video_formats:
        assert FileHandler.is_video_file(f"test{fmt}") == True
    print(f"✓ All {len(video_formats)} video formats recognized")
    
    # Test all image formats
    image_formats = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff']
    for fmt in image_formats:
        assert FileHandler.is_image_file(f"test{fmt}") == True
    print(f"✓ All {len(image_formats)} image formats recognized")
    
    # Test all audio formats
    audio_formats = ['.mp3', '.wav', '.aac', '.ogg', '.m4a', '.flac']
    for fmt in audio_formats:
        assert FileHandler.is_audio_file(f"test{fmt}") == True
    print(f"✓ All {len(audio_formats)} audio formats recognized")
    
    # Test safe filename
    unsafe = '<test>file:name?.txt'
    safe = FileHandler.get_safe_filename(unsafe)
    assert '<' not in safe and '>' not in safe and ':' not in safe
    print(f"✓ Safe filename conversion works: '{unsafe}' → '{safe}'")
    
    # Test filter files by type
    files = ['video.mp4', 'image.jpg', 'audio.mp3', 'doc.txt']
    video_files = FileHandler.filter_files_by_type(files, 'video')
    assert len(video_files) == 1 and video_files[0] == 'video.mp4'
    print("✓ File filtering by type works")
    
    print("✓ FileHandler comprehensive tests passed")
    return True


def test_project_manager_comprehensive():
    """Comprehensive ProjectManager tests"""
    print("\nTesting ProjectManager comprehensively...")
    
    pm = ProjectManager()
    
    # Test new project structure
    project = pm.create_new_project()
    assert project['version'] == '1.0'
    assert 'created' in project
    assert 'modified' in project
    assert len(project['timeline']['video_clips']) == 0
    assert len(project['timeline']['image_clips']) == 0
    assert len(project['timeline']['audio_clips']) == 0
    print("✓ New project structure correct")
    
    # Test modification tracking
    assert not pm.is_modified()
    pm.mark_modified()
    assert pm.is_modified()
    print("✓ Modification tracking works")
    
    # Test save and load with temp file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.vedproj', delete=False) as f:
        temp_path = f.name
    
    try:
        # Add some data
        project['timeline']['video_clips'].append({
            'type': 'video',
            'filepath': 'test.mp4',
            'start': 0,
            'end': None
        })
        
        # Save
        success = pm.save_project(project, temp_path)
        assert success
        assert os.path.exists(temp_path)
        print("✓ Project save works")
        
        # Load
        loaded = pm.load_project(temp_path)
        assert loaded is not None
        assert loaded['version'] == '1.0'
        assert len(loaded['timeline']['video_clips']) == 1
        assert loaded['timeline']['video_clips'][0]['filepath'] == 'test.mp4'
        print("✓ Project load works")
        
    finally:
        if os.path.exists(temp_path):
            os.unlink(temp_path)
    
    print("✓ ProjectManager comprehensive tests passed")
    return True


def test_export_settings():
    """Test export quality presets in detail"""
    print("\nTesting export settings...")
    
    presets = VideoExporter.QUALITY_PRESETS
    
    for quality_name, settings in presets.items():
        print(f"  {quality_name.upper()}:")
        print(f"    Resolution: {settings['resolution'][0]}x{settings['resolution'][1]}")
        print(f"    Bitrate: {settings['bitrate']}")
        print(f"    FPS: {settings['fps']}")
        print(f"    Codec: {settings['codec']}")
        
        # Verify all required keys present
        assert 'resolution' in settings
        assert 'bitrate' in settings
        assert 'fps' in settings
        assert 'codec' in settings
    
    print("✓ All export presets valid")
    return True


def test_project_data_structure():
    """Test that project data structure matches specification"""
    print("\nTesting project data structure...")
    
    pm = ProjectManager()
    project = pm.create_new_project()
    
    # Verify structure matches DEVELOPER_NOTES.md specification
    required_keys = ['version', 'created', 'modified', 'timeline', 'export_settings']
    for key in required_keys:
        assert key in project, f"Missing key: {key}"
    
    timeline_keys = ['video_clips', 'image_clips', 'audio_clips', 'text_overlays']
    for key in timeline_keys:
        assert key in project['timeline'], f"Missing timeline key: {key}"
    
    export_keys = ['format', 'resolution', 'quality', 'fps']
    for key in export_keys:
        assert key in project['export_settings'], f"Missing export settings key: {key}"
    
    print("✓ Project data structure matches specification")
    return True


def run_all_tests():
    """Run all integration tests"""
    print("=" * 60)
    print("Video Editor - Integration Tests")
    print("=" * 60)
    
    tests = [
        test_video_editor_initialization,
        test_video_effects,
        test_video_exporter,
        test_file_handler_comprehensive,
        test_project_manager_comprehensive,
        test_export_settings,
        test_project_data_structure
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"✗ Test failed: {test.__name__}")
            print(f"  Error: {e}")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"Results: {passed} passed, {failed} failed out of {len(tests)} tests")
    print("=" * 60)
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
