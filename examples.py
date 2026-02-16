#!/usr/bin/env python3
"""
Example scripts demonstrating the Video Editor for InSoil.
These examples show common video editing tasks.
"""

from video_editor import VideoEditor, VideoMerger, create_title_video


def example_1_basic_trim():
    """Example 1: Basic video trimming."""
    print("\n=== Example 1: Trim a video ===")
    print("This example shows how to trim a video from 5 to 15 seconds.")
    print("""
with VideoEditor('input.mp4') as editor:
    editor.trim(5, 15)
    editor.save('output_trimmed.mp4')
    """)


def example_2_add_title():
    """Example 2: Add text overlay."""
    print("\n=== Example 2: Add text overlay ===")
    print("This example adds a title to a video.")
    print("""
with VideoEditor('input.mp4') as editor:
    editor.add_text(
        'InSoil - Regenerative Agriculture',
        position=('center', 'bottom'),
        fontsize=60,
        color='white',
        bg_color='darkgreen'
    )
    editor.save('output_with_text.mp4')
    """)


def example_3_resize_and_crop():
    """Example 3: Resize and crop video."""
    print("\n=== Example 3: Resize and crop ===")
    print("This example resizes a video to 1280x720 and crops a specific region.")
    print("""
with VideoEditor('input.mp4') as editor:
    editor.resize_video(width=1280, height=720)
    editor.crop_video(x1=100, y1=50, x2=1180, y2=670)
    editor.save('output_resized_cropped.mp4')
    """)


def example_4_add_effects():
    """Example 4: Add fade effects and change speed."""
    print("\n=== Example 4: Add effects ===")
    print("This example adds fade in/out effects and changes playback speed.")
    print("""
with VideoEditor('input.mp4') as editor:
    editor.add_fade(fade_in_duration=2, fade_out_duration=2)
    editor.set_speed(1.5)  # 1.5x faster
    editor.save('output_with_effects.mp4')
    """)


def example_5_merge_videos():
    """Example 5: Merge multiple videos."""
    print("\n=== Example 5: Merge videos ===")
    print("This example merges multiple videos with a transition effect.")
    print("""
video_files = ['video1.mp4', 'video2.mp4', 'video3.mp4']
VideoMerger.concatenate_videos(
    video_files,
    'merged_output.mp4',
    transition_duration=1.0
)
    """)


def example_6_create_title_screen():
    """Example 6: Create a title screen."""
    print("\n=== Example 6: Create title screen ===")
    print("This example creates a standalone title video.")
    print("""
create_title_video(
    'InSoil - Soil Health Technology',
    duration=5,
    output_path='title_screen.mp4',
    size=(1920, 1080),
    fontsize=80,
    color='white',
    bg_color='darkgreen'
)
    """)


def example_7_complete_workflow():
    """Example 7: Complete workflow for InSoil promotional video."""
    print("\n=== Example 7: Complete workflow ===")
    print("This example shows a complete workflow for creating an InSoil promotional video.")
    print("""
# Step 1: Create title screen
create_title_video(
    'InSoil\\nRegenerative Agriculture',
    duration=3,
    output_path='title.mp4',
    bg_color='darkgreen'
)

# Step 2: Process main content video
with VideoEditor('field_footage.mp4') as editor:
    editor.trim(10, 60)  # Take 50 seconds
    editor.resize_video(width=1920, height=1080)
    editor.add_text(
        'Restoring Soil Health',
        position=('center', 'bottom'),
        start_time=5,
        duration=10
    )
    editor.add_fade(fade_in_duration=1, fade_out_duration=2)
    editor.save('main_content.mp4')

# Step 3: Create end credits
create_title_video(
    'Learn more at insoil.com',
    duration=3,
    output_path='credits.mp4',
    fontsize=60,
    bg_color='darkgreen'
)

# Step 4: Merge all parts
VideoMerger.concatenate_videos(
    ['title.mp4', 'main_content.mp4', 'credits.mp4'],
    'final_promotional_video.mp4',
    transition_duration=0.5
)

print('✓ Promotional video created: final_promotional_video.mp4')
    """)


def example_8_batch_processing():
    """Example 8: Batch process multiple videos."""
    print("\n=== Example 8: Batch processing ===")
    print("This example shows how to process multiple videos with the same settings.")
    print("""
import os
from pathlib import Path

input_folder = 'raw_videos'
output_folder = 'processed_videos'

# Create output folder
os.makedirs(output_folder, exist_ok=True)

# Process all videos in the input folder
for video_file in Path(input_folder).glob('*.mp4'):
    print(f'Processing: {video_file.name}')
    
    output_path = os.path.join(output_folder, f'processed_{video_file.name}')
    
    with VideoEditor(str(video_file)) as editor:
        editor.resize_video(width=1920, height=1080)
        editor.add_text(
            'InSoil',
            position=('right', 'top'),
            fontsize=40
        )
        editor.save(output_path)
    
    print(f'✓ Saved: {output_path}')

print('✓ Batch processing complete!')
    """)


def main():
    """Display all examples."""
    print("=" * 70)
    print("Video Editor for InSoil - Example Scripts")
    print("=" * 70)
    
    example_1_basic_trim()
    example_2_add_title()
    example_3_resize_and_crop()
    example_4_add_effects()
    example_5_merge_videos()
    example_6_create_title_screen()
    example_7_complete_workflow()
    example_8_batch_processing()
    
    print("\n" + "=" * 70)
    print("For command-line usage, see: python cli.py --help")
    print("=" * 70)


if __name__ == "__main__":
    main()
