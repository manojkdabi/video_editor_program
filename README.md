# Video Editor Program for InSoil

A powerful yet simple Python-based video editing tool designed for InSoil's agricultural and educational content creation needs. This program provides both a Python API and a command-line interface for common video editing tasks.

## Features

- **Video Trimming**: Cut videos to specific time ranges
- **Text Overlays**: Add titles, captions, and watermarks
- **Video Resizing**: Scale videos to different resolutions
- **Video Cropping**: Extract specific regions from videos
- **Speed Control**: Change playback speed (slow motion or fast forward)
- **Fade Effects**: Add professional fade in/out transitions
- **Video Merging**: Concatenate multiple videos with optional transitions
- **Title Generation**: Create standalone title screens
- **Batch Processing**: Process multiple videos with the same settings

## Installation

### Prerequisites

- Python 3.7 or higher
- FFmpeg (required by moviepy)

### Install FFmpeg

**On Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install ffmpeg
```

**On macOS:**
```bash
brew install ffmpeg
```

**On Windows:**
Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH.

### Install Python Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Command-Line Interface

The CLI provides quick access to common video editing tasks:

#### Trim a Video

```bash
python cli.py trim input.mp4 output.mp4 --start 10 --end 30
```

Add fade effects while trimming:
```bash
python cli.py trim input.mp4 output.mp4 --start 10 --end 30 --fade-in 1 --fade-out 2
```

#### Add Text Overlay

```bash
python cli.py text input.mp4 output.mp4 --text "InSoil Agriculture" --position bottom
```

With custom styling:
```bash
python cli.py text input.mp4 output.mp4 \
  --text "Regenerative Agriculture" \
  --position center \
  --fontsize 60 \
  --color white \
  --bg-color darkgreen
```

#### Resize Video

```bash
# Resize by dimensions
python cli.py resize input.mp4 output.mp4 --width 1280 --height 720

# Resize by scale factor
python cli.py resize input.mp4 output.mp4 --scale 0.5
```

#### Crop Video

```bash
python cli.py crop input.mp4 output.mp4 --x1 100 --y1 50 --x2 1820 --y2 1030
```

#### Change Speed

```bash
# Speed up (2x faster)
python cli.py speed input.mp4 output.mp4 --factor 2.0

# Slow down (2x slower)
python cli.py speed input.mp4 output.mp4 --factor 0.5
```

#### Merge Videos

```bash
python cli.py merge output.mp4 video1.mp4 video2.mp4 video3.mp4

# With transition effect
python cli.py merge output.mp4 video1.mp4 video2.mp4 --transition 1.0
```

#### Create Title Screen

```bash
python cli.py title output.mp4 --text "Welcome to InSoil" --duration 5
```

### Python API

For more complex workflows, use the Python API:

```python
from video_editor import VideoEditor, VideoMerger, create_title_video

# Basic editing
with VideoEditor('input.mp4') as editor:
    editor.trim(10, 30)
    editor.add_text('InSoil', position=('center', 'bottom'))
    editor.add_fade(fade_in_duration=1, fade_out_duration=2)
    editor.save('output.mp4')

# Merge multiple videos
VideoMerger.concatenate_videos(
    ['video1.mp4', 'video2.mp4', 'video3.mp4'],
    'merged.mp4',
    transition_duration=1.0
)

# Create title screen
create_title_video(
    'InSoil - Soil Health Technology',
    duration=5,
    output_path='title.mp4',
    bg_color='darkgreen'
)
```

## Examples

See `examples.py` for detailed examples including:

1. Basic video trimming
2. Adding text overlays
3. Resizing and cropping
4. Adding effects
5. Merging videos
6. Creating title screens
7. Complete promotional video workflow
8. Batch processing multiple videos

Run the examples file to see all available examples:

```bash
python examples.py
```

## Use Cases for InSoil

This video editor is particularly useful for:

- **Field Documentation**: Trim and annotate videos of agricultural practices
- **Educational Content**: Add titles and captions to instructional videos
- **Promotional Videos**: Create professional marketing content with titles and transitions
- **Progress Reports**: Merge time-lapse videos from different field locations
- **Social Media Content**: Resize videos for different platforms (Instagram, YouTube, etc.)
- **Training Materials**: Add text overlays explaining soil health techniques

## API Reference

### VideoEditor Class

Main class for editing individual videos.

**Methods:**
- `trim(start_time, end_time)` - Trim video to time range
- `add_text(text, position, duration, fontsize, color, bg_color, start_time)` - Add text overlay
- `resize_video(width, height, scale)` - Resize video
- `crop_video(x1, y1, x2, y2)` - Crop video
- `add_fade(fade_in_duration, fade_out_duration)` - Add fade effects
- `set_speed(factor)` - Change playback speed
- `save(output_path, codec, audio_codec, fps)` - Save edited video

### VideoMerger Class

Utility for merging multiple videos.

**Methods:**
- `concatenate_videos(video_paths, output_path, transition_duration)` - Merge videos

### Functions

- `create_title_video(text, duration, output_path, size, fontsize, color, bg_color)` - Create title screen

## Project Structure

```
video_editor_program/
├── video_editor.py    # Core video editing library
├── cli.py            # Command-line interface
├── examples.py       # Usage examples
├── requirements.txt  # Python dependencies
└── README.md        # This file
```

## Contributing

This is a specialized tool for InSoil's video editing needs. For feature requests or bug reports, please contact the development team.

## License

Copyright © 2026 InSoil. All rights reserved.

## Support

For questions or support, please refer to the examples provided or contact the InSoil technical team.
