"""
Example Script: Video Editor Usage
Demonstrates how to use the video editor programmatically
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from src.video_processing.editor import VideoEditor
from src.video_processing.effects import VideoEffects
from src.video_processing.text_overlay import TextOverlay
from src.video_processing.export import VideoExporter
from src.utils.project_manager import ProjectManager


def example_create_simple_video():
    """
    Example: Create a simple video from multiple clips
    
    This is a conceptual example showing the workflow.
    Actual execution requires video files to exist.
    """
    
    print("=" * 60)
    print("Example: Creating a Training Video")
    print("=" * 60)
    
    # Initialize editor
    editor = VideoEditor()
    print("\n1. Video Editor initialized")
    
    # Load video clips (would need actual files)
    print("\n2. Loading video clips...")
    print("   - Load intro video")
    print("   - Load demonstration video")
    print("   - Load conclusion video")
    
    # Example workflow
    steps = [
        "3. Trim clips to desired length",
        "4. Add fade in/out effects",
        "5. Add title and subtitle text overlays",
        "6. Add background music",
        "7. Concatenate all clips",
        "8. Export final video"
    ]
    
    for step in steps:
        print(f"\n{step}")
    
    print("\n" + "=" * 60)
    print("Video creation workflow complete!")
    print("=" * 60)


def example_project_workflow():
    """Example: Working with projects"""
    
    print("\n" + "=" * 60)
    print("Example: Project Management Workflow")
    print("=" * 60)
    
    # Create project manager
    pm = ProjectManager()
    print("\n1. Project Manager initialized")
    
    # Create new project
    project = pm.create_new_project()
    print("\n2. New project created")
    print(f"   Version: {project['version']}")
    print(f"   Created: {project['created']}")
    
    # Add clips to project
    print("\n3. Adding clips to timeline...")
    project['timeline']['video_clips'].append({
        'type': 'video',
        'filepath': 'intro.mp4',
        'start': 0,
        'end': 10.0
    })
    project['timeline']['image_clips'].append({
        'type': 'image',
        'filepath': 'product.jpg',
        'duration': 5.0
    })
    project['timeline']['audio_clips'].append({
        'type': 'audio',
        'filepath': 'narration.mp3',
        'start': 0,
        'end': None
    })
    
    print(f"   Added {len(project['timeline']['video_clips'])} video clips")
    print(f"   Added {len(project['timeline']['image_clips'])} image clips")
    print(f"   Added {len(project['timeline']['audio_clips'])} audio clips")
    
    # Save project (would save to actual file)
    print("\n4. Project ready to save")
    print("   Would save as: training_video_project.vedproj")
    
    print("\n" + "=" * 60)
    print("Project workflow complete!")
    print("=" * 60)


def example_export_options():
    """Example: Export quality options"""
    
    print("\n" + "=" * 60)
    print("Example: Export Quality Options")
    print("=" * 60)
    
    exporter = VideoExporter()
    
    print("\nAvailable Quality Presets:")
    print("-" * 60)
    
    for quality_name, settings in VideoExporter.QUALITY_PRESETS.items():
        print(f"\n{quality_name.upper()}:")
        print(f"  Resolution: {settings['resolution'][0]}x{settings['resolution'][1]}")
        print(f"  Bitrate: {settings['bitrate']}")
        print(f"  FPS: {settings['fps']}")
        print(f"  Codec: {settings['codec']}")
        
        # Estimate file size for different video lengths
        sizes = []
        for minutes in [1, 5, 10]:
            size = VideoExporter.estimate_file_size(minutes * 60, quality_name)
            sizes.append(f"{minutes}min={size:.1f}MB")
        print(f"  Estimated sizes: {', '.join(sizes)}")
    
    print("\n" + "=" * 60)


def example_video_effects():
    """Example: Available video effects"""
    
    print("\n" + "=" * 60)
    print("Example: Available Video Effects")
    print("=" * 60)
    
    effects = [
        ("Fade In", "Gradually increase opacity from black"),
        ("Fade Out", "Gradually decrease opacity to black"),
        ("Crossfade In", "Smooth transition in with crossfade"),
        ("Crossfade Out", "Smooth transition out with crossfade"),
        ("Fade In/Out", "Combined fade in and fade out"),
        ("Crossfade Transition", "Smooth blend between two clips")
    ]
    
    print("\nSupported Effects:")
    print("-" * 60)
    
    for name, description in effects:
        print(f"\n{name}:")
        print(f"  {description}")
    
    print("\n" + "=" * 60)


def example_text_overlays():
    """Example: Text overlay capabilities"""
    
    print("\n" + "=" * 60)
    print("Example: Text Overlay Capabilities")
    print("=" * 60)
    
    print("\nText Overlay Features:")
    print("-" * 60)
    
    features = [
        ("Title Clips", "Full-screen title with customizable background"),
        ("Subtitles", "Bottom-aligned text with background"),
        ("Custom Text", "Positioned anywhere with custom styling"),
        ("Font Control", "Choose font, size, and color"),
        ("Background", "Optional background color for readability"),
        ("Duration", "Set how long text appears"),
        ("Position", "Top, bottom, center, or custom coordinates")
    ]
    
    for name, description in features:
        print(f"\n{name}:")
        print(f"  {description}")
    
    print("\n" + "=" * 60)


def main():
    """Run all examples"""
    
    print("\n")
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 10 + "VIDEO EDITOR - USAGE EXAMPLES" + " " * 18 + "║")
    print("╚" + "═" * 58 + "╝")
    
    examples = [
        ("Simple Video Creation", example_create_simple_video),
        ("Project Management", example_project_workflow),
        ("Export Options", example_export_options),
        ("Video Effects", example_video_effects),
        ("Text Overlays", example_text_overlays)
    ]
    
    for i, (name, func) in enumerate(examples, 1):
        print(f"\n\n{'#' * 60}")
        print(f"# Example {i}: {name}")
        print(f"{'#' * 60}")
        func()
    
    print("\n\n" + "=" * 60)
    print("All examples completed!")
    print("=" * 60)
    print("\nFor actual usage:")
    print("1. Run 'python main.py' to launch the GUI")
    print("2. Or use the video processing modules programmatically")
    print("3. See DEVELOPER_NOTES.md for detailed documentation")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
