# Quick Start Guide - Video Editor for InSoil

This guide will help you get started with the Video Editor Program quickly.

## Installation

1. **Install FFmpeg** (required):
   ```bash
   # Ubuntu/Debian
   sudo apt-get update && sudo apt-get install ffmpeg
   
   # macOS
   brew install ffmpeg
   ```

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify installation**:
   ```bash
   python3 test_basic.py
   ```
   You should see: `✓ All tests passed!`

## Quick Examples

### Example 1: Trim a Video (CLI)

```bash
python cli.py trim field_video.mp4 trimmed.mp4 --start 10 --end 60
```

### Example 2: Add Text to Video (CLI)

```bash
python cli.py text field_video.mp4 branded.mp4 \
  --text "InSoil - Regenerative Agriculture" \
  --position bottom \
  --color white \
  --bg-color darkgreen
```

### Example 3: Create Title Screen (CLI)

```bash
python cli.py title intro.mp4 \
  --text "InSoil Presents" \
  --duration 5 \
  --bg-color darkgreen
```

### Example 4: Merge Videos (CLI)

```bash
python cli.py merge final.mp4 intro.mp4 main.mp4 outro.mp4 --transition 1
```

### Example 5: Complete Workflow (Python API)

```python
from video_editor import VideoEditor, VideoMerger, create_title_video

# Create title
create_title_video(
    'InSoil - Soil Health',
    duration=3,
    output_path='title.mp4',
    bg_color='darkgreen'
)

# Edit main video
with VideoEditor('raw_footage.mp4') as editor:
    editor.trim(5, 45)
    editor.resize_video(width=1920, height=1080)
    editor.add_text('Visit insoil.com', position=('right', 'bottom'), 
                   start_time=35, duration=10)
    editor.add_fade(fade_in_duration=1, fade_out_duration=2)
    editor.save('main.mp4')

# Create credits
create_title_video(
    'Thank You',
    duration=2,
    output_path='credits.mp4',
    bg_color='darkgreen'
)

# Merge all
VideoMerger.concatenate_videos(
    ['title.mp4', 'main.mp4', 'credits.mp4'],
    'final_video.mp4',
    transition_duration=0.5
)
```

## Common Use Cases

### Social Media Posts
```bash
# Resize for Instagram (1:1)
python cli.py resize video.mp4 instagram.mp4 --width 1080 --height 1080

# Resize for YouTube (16:9)
python cli.py resize video.mp4 youtube.mp4 --width 1920 --height 1080
```

### Time-lapse Videos
```bash
# Speed up 10x
python cli.py speed field_timelapse.mp4 fast.mp4 --factor 10.0
```

### Documentation Videos
```bash
# Add title and trim
python cli.py trim raw.mp4 temp.mp4 --start 0 --end 120
python cli.py text temp.mp4 final.mp4 \
  --text "Soil Restoration Process" \
  --position top \
  --start-time 0 \
  --duration 120
```

## Tips

1. **Chain operations in Python** for complex edits:
   ```python
   with VideoEditor('input.mp4') as editor:
       editor.trim(10, 60)\
             .resize_video(width=1920, height=1080)\
             .add_text('InSoil', position=('right', 'top'))\
             .add_fade(fade_in_duration=1, fade_out_duration=2)\
             .save('output.mp4')
   ```

2. **Use batch processing** for multiple files (see `examples.py` Example 8)

3. **Check CLI help** for each command:
   ```bash
   python cli.py trim --help
   python cli.py text --help
   ```

4. **Test on a small clip first** before processing large videos

## Troubleshooting

- **Import errors**: Make sure all dependencies are installed (`pip install -r requirements.txt`)
- **FFmpeg errors**: Verify FFmpeg is installed (`ffmpeg -version`)
- **Memory issues**: Process large videos in smaller chunks using trim first
- **Slow processing**: Video editing is CPU-intensive; be patient with large files

## Next Steps

- Read the full README.md for detailed documentation
- Run `python examples.py` to see all available examples
- Explore the Python API in `video_editor.py`
- Check CLI commands with `python cli.py --help`

For questions or issues, contact the InSoil technical team.
