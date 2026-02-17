#!/usr/bin/env python3
"""
Command-line interface for the Video Editor Program.
"""

import argparse
import sys
from video_editor import VideoEditor, VideoMerger, create_title_video


def trim_video(args):
    """Trim a video to specified time range."""
    print(f"Trimming video: {args.input}")
    print(f"Start: {args.start}s, End: {args.end}s")
    
    with VideoEditor(args.input) as editor:
        editor.trim(args.start, args.end)
        if args.fade_in or args.fade_out:
            editor.add_fade(args.fade_in, args.fade_out)
        output = editor.save(args.output)
    
    print(f"✓ Saved trimmed video to: {output}")


def add_text_to_video(args):
    """Add text overlay to a video."""
    print(f"Adding text to video: {args.input}")
    print(f"Text: '{args.text}'")
    
    with VideoEditor(args.input) as editor:
        position = ('center', args.position) if args.position in ['top', 'center', 'bottom'] else tuple(map(int, args.position.split(',')))
        editor.add_text(
            args.text,
            position=position,
            fontsize=args.fontsize,
            color=args.color,
            bg_color=args.bg_color,
            start_time=args.start_time,
            duration=args.duration
        )
        output = editor.save(args.output)
    
    print(f"✓ Saved video with text to: {output}")


def resize_video(args):
    """Resize a video."""
    print(f"Resizing video: {args.input}")
    
    with VideoEditor(args.input) as editor:
        if args.scale:
            print(f"Scale: {args.scale}x")
            editor.resize_video(scale=args.scale)
        else:
            print(f"Dimensions: {args.width}x{args.height}")
            editor.resize_video(width=args.width, height=args.height)
        output = editor.save(args.output)
    
    print(f"✓ Saved resized video to: {output}")


def crop_video(args):
    """Crop a video."""
    print(f"Cropping video: {args.input}")
    print(f"Crop region: ({args.x1}, {args.y1}) to ({args.x2}, {args.y2})")
    
    with VideoEditor(args.input) as editor:
        editor.crop_video(args.x1, args.y1, args.x2, args.y2)
        output = editor.save(args.output)
    
    print(f"✓ Saved cropped video to: {output}")


def change_speed(args):
    """Change video playback speed."""
    print(f"Changing speed of video: {args.input}")
    print(f"Speed factor: {args.factor}x")
    
    with VideoEditor(args.input) as editor:
        editor.set_speed(args.factor)
        output = editor.save(args.output)
    
    print(f"✓ Saved video with new speed to: {output}")


def merge_videos(args):
    """Merge multiple videos."""
    print(f"Merging {len(args.inputs)} videos")
    for i, video in enumerate(args.inputs, 1):
        print(f"  {i}. {video}")
    
    output = VideoMerger.concatenate_videos(
        args.inputs,
        args.output,
        transition_duration=args.transition
    )
    
    print(f"✓ Saved merged video to: {output}")


def create_title(args):
    """Create a title video."""
    print(f"Creating title video")
    print(f"Text: '{args.text}'")
    print(f"Duration: {args.duration}s")
    
    size = tuple(map(int, args.size.split('x'))) if args.size else (1920, 1080)
    
    output = create_title_video(
        args.text,
        args.duration,
        args.output,
        size=size,
        fontsize=args.fontsize,
        color=args.color,
        bg_color=args.bg_color
    )
    
    print(f"✓ Saved title video to: {output}")


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Video Editor Program for InSoil - Edit videos with ease",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Trim a video
  %(prog)s trim input.mp4 output.mp4 --start 10 --end 30
  
  # Add text overlay
  %(prog)s text input.mp4 output.mp4 --text "InSoil Agriculture" --position bottom
  
  # Resize video
  %(prog)s resize input.mp4 output.mp4 --width 1280 --height 720
  
  # Merge videos
  %(prog)s merge output.mp4 video1.mp4 video2.mp4 video3.mp4
  
  # Create title screen
  %(prog)s title output.mp4 --text "Welcome to InSoil" --duration 5
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Trim command
    trim_parser = subparsers.add_parser('trim', help='Trim video to specified time range')
    trim_parser.add_argument('input', help='Input video file')
    trim_parser.add_argument('output', help='Output video file')
    trim_parser.add_argument('--start', type=float, required=True, help='Start time in seconds')
    trim_parser.add_argument('--end', type=float, required=True, help='End time in seconds')
    trim_parser.add_argument('--fade-in', type=float, default=0, help='Fade in duration in seconds')
    trim_parser.add_argument('--fade-out', type=float, default=0, help='Fade out duration in seconds')
    trim_parser.set_defaults(func=trim_video)
    
    # Text command
    text_parser = subparsers.add_parser('text', help='Add text overlay to video')
    text_parser.add_argument('input', help='Input video file')
    text_parser.add_argument('output', help='Output video file')
    text_parser.add_argument('--text', required=True, help='Text to display')
    text_parser.add_argument('--position', default='bottom', help='Position: top, center, bottom, or x,y coordinates')
    text_parser.add_argument('--fontsize', type=int, default=50, help='Font size (default: 50)')
    text_parser.add_argument('--color', default='white', help='Text color (default: white)')
    text_parser.add_argument('--bg-color', default='black', help='Background color (default: black)')
    text_parser.add_argument('--start-time', type=float, default=0, help='Start time in seconds')
    text_parser.add_argument('--duration', type=float, default=None, help='Duration in seconds (default: entire video)')
    text_parser.set_defaults(func=add_text_to_video)
    
    # Resize command
    resize_parser = subparsers.add_parser('resize', help='Resize video')
    resize_parser.add_argument('input', help='Input video file')
    resize_parser.add_argument('output', help='Output video file')
    resize_group = resize_parser.add_mutually_exclusive_group(required=True)
    resize_group.add_argument('--scale', type=float, help='Scale factor (e.g., 0.5 for half size)')
    resize_group.add_argument('--width', type=int, help='Target width in pixels')
    resize_parser.add_argument('--height', type=int, help='Target height in pixels (used with --width)')
    resize_parser.set_defaults(func=resize_video)
    
    # Crop command
    crop_parser = subparsers.add_parser('crop', help='Crop video')
    crop_parser.add_argument('input', help='Input video file')
    crop_parser.add_argument('output', help='Output video file')
    crop_parser.add_argument('--x1', type=int, required=True, help='Left coordinate')
    crop_parser.add_argument('--y1', type=int, required=True, help='Top coordinate')
    crop_parser.add_argument('--x2', type=int, required=True, help='Right coordinate')
    crop_parser.add_argument('--y2', type=int, required=True, help='Bottom coordinate')
    crop_parser.set_defaults(func=crop_video)
    
    # Speed command
    speed_parser = subparsers.add_parser('speed', help='Change video playback speed')
    speed_parser.add_argument('input', help='Input video file')
    speed_parser.add_argument('output', help='Output video file')
    speed_parser.add_argument('--factor', type=float, required=True, help='Speed factor (2.0 = 2x faster, 0.5 = 2x slower)')
    speed_parser.set_defaults(func=change_speed)
    
    # Merge command
    merge_parser = subparsers.add_parser('merge', help='Merge multiple videos')
    merge_parser.add_argument('output', help='Output video file')
    merge_parser.add_argument('inputs', nargs='+', help='Input video files to merge')
    merge_parser.add_argument('--transition', type=float, default=0, help='Crossfade transition duration in seconds')
    merge_parser.set_defaults(func=merge_videos)
    
    # Title command
    title_parser = subparsers.add_parser('title', help='Create a title video')
    title_parser.add_argument('output', help='Output video file')
    title_parser.add_argument('--text', required=True, help='Title text')
    title_parser.add_argument('--duration', type=float, default=5, help='Duration in seconds (default: 5)')
    title_parser.add_argument('--size', default='1920x1080', help='Video size (default: 1920x1080)')
    title_parser.add_argument('--fontsize', type=int, default=70, help='Font size (default: 70)')
    title_parser.add_argument('--color', default='white', help='Text color (default: white)')
    title_parser.add_argument('--bg-color', default='black', help='Background color (default: black)')
    title_parser.set_defaults(func=create_title)
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    try:
        args.func(args)
    except Exception as e:
        print(f"✗ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
