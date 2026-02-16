# Developer Notes

Technical documentation for the Video Editor application.

## Table of Contents

1. [Architecture Overview](#architecture-overview)
2. [Code Structure](#code-structure)
3. [Key Technologies](#key-technologies)
4. [Module Documentation](#module-documentation)
5. [Extending the Application](#extending-the-application)
6. [Common Modifications](#common-modifications)
7. [Development Setup](#development-setup)
8. [Testing](#testing)
9. [Building Distribution](#building-distribution)

## Architecture Overview

### Design Pattern

The application follows a **Model-View-Controller (MVC)** pattern:

- **Model**: Video processing modules (`src/video_processing/`)
- **View**: GUI components (`src/gui/`)
- **Controller**: Main window logic coordinating between view and model

### Data Flow

```
User Action (GUI) 
  → Main Window Handler
    → Project Manager (updates project state)
      → Video Editor (processes video)
        → Export (renders final video)
```

## Code Structure

```
src/
├── gui/
│   └── main_window.py          # Main application window and UI
├── video_processing/
│   ├── editor.py               # Core video editing operations
│   ├── effects.py              # Transitions and effects
│   ├── text_overlay.py         # Text rendering on video
│   └── export.py               # Video export and encoding
└── utils/
    ├── file_handler.py         # File validation and operations
    ├── media_info.py           # Extract video/audio metadata
    └── project_manager.py      # Project save/load functionality
```

## Key Technologies

### CustomTkinter (GUI)

- Modern, themed tkinter wrapper
- Cross-platform with native look
- Easy-to-use widget system

**Key Classes**:
- `CTk`: Main window
- `CTkFrame`: Container widget
- `CTkButton`: Button widget
- `CTkLabel`: Text/image display
- `CTkTextbox`: Multi-line text input

### MoviePy (Video Processing)

- High-level video editing library
- Based on FFMPEG
- Supports most video formats

**Key Classes**:
- `VideoFileClip`: Video file handling
- `ImageClip`: Image to video conversion
- `AudioFileClip`: Audio handling
- `CompositeVideoClip`: Combine multiple clips
- `concatenate_videoclips`: Join clips sequentially

### Important MoviePy v2.x Changes

This project uses **MoviePy v2.x** which has different APIs than v1.x:

```python
# v1.x (OLD - DON'T USE)
from moviepy.editor import VideoFileClip

# v2.x (NEW - USE THIS)
from moviepy import VideoFileClip
```

Effects are applied using `.with_effects()`:

```python
# v2.x syntax
clip = clip.with_effects([fadein(1.0), fadeout(1.0)])
```

## Module Documentation

### src/gui/main_window.py

**Purpose**: Main application window with all UI components

**Key Classes**:

#### `MainWindow(ctk.CTk)`
Main application window.

**Methods**:
- `setup_ui()`: Initialize UI layout
- `setup_toolbar()`: Create toolbar buttons
- `setup_preview_panel()`: Create video preview area
- `setup_timeline_panel()`: Create timeline display
- `setup_properties_panel()`: Create properties editor
- `import_video()`: Import video files
- `import_image()`: Import image files
- `import_audio()`: Import audio files
- `export_video()`: Export final video
- `save_project()`: Save project to file
- `load_project()`: Load project from file

#### `ExportDialog(ctk.CTkToplevel)`
Export progress window.

**Methods**:
- `start_export()`: Begin video export process

### src/video_processing/editor.py

**Purpose**: Core video editing operations

**Key Class**: `VideoEditor`

**Methods**:
- `load_video_clip(filepath, start, end)`: Load video with optional trimming
- `load_image_clip(filepath, duration)`: Load image as video clip
- `load_audio_clip(filepath, start, end)`: Load audio file
- `trim_clip(clip, start, end)`: Trim clip to specific duration
- `concatenate_clips(clips)`: Join multiple clips
- `resize_clip(clip, width, height)`: Resize video
- `set_clip_position(clip, position)`: Position clip on canvas
- `add_audio_to_video(video_clip, audio_clip)`: Attach audio to video
- `composite_clips(clips, size)`: Create composite from multiple clips

### src/video_processing/effects.py

**Purpose**: Video transitions and effects

**Key Class**: `VideoEffects`

**Methods**:
- `apply_fade_in(clip, duration)`: Fade in effect
- `apply_fade_out(clip, duration)`: Fade out effect
- `apply_crossfade_in(clip, duration)`: Crossfade in
- `apply_crossfade_out(clip, duration)`: Crossfade out
- `apply_fade_in_out(clip, in_dur, out_dur)`: Combined fade effect
- `create_crossfade_transition(clip1, clip2, duration)`: Crossfade between clips

### src/video_processing/text_overlay.py

**Purpose**: Text overlay functionality

**Key Class**: `TextOverlay`

**Methods**:
- `create_text_clip(text, duration, ...)`: Create text overlay
- `add_text_to_video(video_clip, text_clip)`: Composite text on video
- `create_title_clip(title, duration, ...)`: Create title screen
- `create_subtitle_clip(text, duration, ...)`: Create subtitle

### src/video_processing/export.py

**Purpose**: Video export and rendering

**Key Class**: `VideoExporter`

**Attributes**:
- `QUALITY_PRESETS`: Dictionary of quality settings

**Methods**:
- `export_video(clip, output_path, quality, format, callback)`: Export video
- `is_exporting()`: Check if export in progress
- `cancel_export()`: Cancel current export
- `get_quality_info(quality)`: Get preset details
- `estimate_file_size(duration, quality)`: Estimate output size

### src/utils/file_handler.py

**Purpose**: File operations and validation

**Key Class**: `FileHandler`

**Attributes**:
- `VIDEO_FORMATS`: List of supported video extensions
- `IMAGE_FORMATS`: List of supported image extensions
- `AUDIO_FORMATS`: List of supported audio extensions

**Methods**:
- `is_video_file(filepath)`: Check if file is video
- `is_image_file(filepath)`: Check if file is image
- `is_audio_file(filepath)`: Check if file is audio
- `validate_file_exists(filepath)`: Check file exists
- `get_safe_filename(filepath)`: Sanitize filename for Windows
- `ensure_directory_exists(directory)`: Create directory if needed
- `get_file_size_mb(filepath)`: Get file size in MB

### src/utils/media_info.py

**Purpose**: Extract media file metadata

**Key Class**: `MediaInfo`

**Methods**:
- `get_video_info(filepath)`: Get video metadata (duration, fps, size)
- `get_audio_info(filepath)`: Get audio metadata
- `get_image_info(filepath)`: Get image metadata
- `format_duration(seconds)`: Format seconds as HH:MM:SS.mmm
- `format_resolution(width, height)`: Format as WxH

### src/utils/project_manager.py

**Purpose**: Project file management

**Key Class**: `ProjectManager`

**Attributes**:
- `current_project_path`: Path to current project file
- `project_modified`: Whether project has unsaved changes

**Methods**:
- `create_new_project()`: Create empty project structure
- `save_project(project_data, filepath)`: Save to JSON file
- `load_project(filepath)`: Load from JSON file
- `mark_modified()`: Mark project as changed
- `is_modified()`: Check if project has unsaved changes
- `validate_project_data(project_data)`: Validate project structure

### Project Data Structure

```json
{
  "version": "1.0",
  "created": "2026-02-16T10:30:00",
  "modified": "2026-02-16T12:45:00",
  "timeline": {
    "video_clips": [
      {
        "type": "video",
        "filepath": "C:/videos/intro.mp4",
        "start": 0,
        "end": 10.5
      }
    ],
    "image_clips": [
      {
        "type": "image",
        "filepath": "C:/images/photo.jpg",
        "duration": 5.0
      }
    ],
    "audio_clips": [
      {
        "type": "audio",
        "filepath": "C:/audio/narration.mp3",
        "start": 0,
        "end": null
      }
    ],
    "text_overlays": []
  },
  "export_settings": {
    "format": "mp4",
    "resolution": "1920x1080",
    "quality": "high",
    "fps": 30
  }
}
```

## Extending the Application

### Adding New Video Effects

1. Add effect method to `src/video_processing/effects.py`:

```python
@staticmethod
def apply_blur_effect(clip, intensity: float = 1.0):
    """Apply blur effect to clip"""
    try:
        from moviepy.video.fx import GaussianBlur
        return clip.with_effects([GaussianBlur(intensity)])
    except Exception as e:
        logger.error(f"Failed to apply blur: {e}")
        return clip
```

2. Add UI button in `main_window.py`
3. Connect button to effect method

### Adding New Export Format

1. Update `VIDEO_FORMATS` in `file_handler.py`
2. Add format handling in `export.py`:

```python
elif format == 'webm':
    clip.write_videofile(
        output_path,
        fps=preset['fps'],
        codec='libvpx',
        audio_codec='libvorbis',
        logger=log_progress if progress_callback else None
    )
```

3. Add format option to properties panel

### Adding Text Overlay UI

1. Create new dialog class in `main_window.py`:

```python
class TextOverlayDialog(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        # Add text input fields
        # Add font/size/color selectors
        # Add position controls
```

2. Add "Add Text" button to toolbar
3. Connect to text overlay functionality

## Common Modifications

### Change Default Video Quality

Edit `main_window.py`:

```python
# In setup_properties_panel()
self.quality_var = ctk.StringVar(value="medium")  # Changed from "high"
```

### Change Preview Window Size

Edit `main_window.py`:

```python
# In setup_preview_panel()
self.preview_canvas = ctk.CTkLabel(
    self.preview_frame,
    text="No video loaded",
    width=800,    # Changed from 640
    height=450,   # Changed from 360
    fg_color="black"
)
```

### Add Custom Quality Preset

Edit `src/video_processing/export.py`:

```python
QUALITY_PRESETS = {
    # ... existing presets ...
    'ultra': {
        'resolution': (3840, 2160),
        'bitrate': '16000k',
        'fps': 60,
        'codec': 'libx264'
    }
}
```

### Change Default Image Duration

Edit `src/video_processing/editor.py`:

```python
def load_image_clip(self, filepath: str, duration: float = 10.0):  # Changed from 5.0
    # ... rest of method ...
```

## Development Setup

### Setting Up Development Environment

```bash
# Clone repository
git clone https://github.com/manojkdabi/video_editor_program.git
cd video_editor_program

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate.bat  # Windows
source venv/bin/activate   # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Run application
python main.py
```

### Installing Additional Dependencies

```bash
# Activate virtual environment first
venv\Scripts\activate.bat

# Install new package
pip install package_name

# Update requirements.txt
pip freeze > requirements.txt
```

## Testing

### Manual Testing Checklist

- [ ] Launch application successfully
- [ ] Import video file
- [ ] Import image file
- [ ] Import audio file
- [ ] Save project
- [ ] Load project
- [ ] Export video (MP4)
- [ ] Export video (AVI)
- [ ] Export video (MOV)
- [ ] Test each quality preset
- [ ] Verify exported video plays correctly

### Creating Test Videos

Use FFmpeg to create test videos:

```bash
# Create 10-second test video
ffmpeg -f lavfi -i testsrc=duration=10:size=1920x1080:rate=30 test_video.mp4

# Create test image
ffmpeg -f lavfi -i color=blue:s=1920x1080 -frames:v 1 test_image.png

# Create test audio
ffmpeg -f lavfi -i sine=frequency=1000:duration=10 test_audio.mp3
```

## Building Distribution

### Creating Standalone Executable

```bash
# Install PyInstaller
pip install pyinstaller

# Create executable
pyinstaller --onefile --windowed --name VideoEditor main.py

# Executable location
dist/VideoEditor.exe
```

### Creating Installer Package

Use Inno Setup or NSIS to create Windows installer:

1. Install Inno Setup
2. Create script including:
   - VideoEditor.exe
   - Python runtime (if bundled)
   - Required DLLs
   - Desktop shortcut
3. Compile installer

## Performance Optimization

### Memory Management

```python
# Always close clips when done
clip.close()

# Use context managers where possible
with VideoFileClip(filepath) as clip:
    # Process clip
    pass
# Automatically closed
```

### Threading for Long Operations

```python
import threading

def export_in_thread():
    thread = threading.Thread(target=video_exporter.export_video, args=(...))
    thread.daemon = True
    thread.start()
```

## Debugging

### Enable Debug Logging

Edit `main.py`:

```python
logging.basicConfig(
    level=logging.DEBUG,  # Changed from INFO
    # ... rest of config ...
)
```

### Common Issues

**Import Error**: Check Python version and dependencies
**Export Fails**: Check FFMPEG installation (bundled with MoviePy)
**UI Not Responsive**: Use threading for long operations
**Memory Issues**: Close clips after use, process in smaller batches

## Contributing

When making changes:

1. Test thoroughly with sample videos
2. Update documentation
3. Follow existing code style
4. Add error handling
5. Update version number

## Version History

- **1.0.0** (Feb 2026): Initial release
  - Basic timeline editing
  - Video/image/audio import
  - Multiple export formats
  - Project save/load

## Future Enhancements

Planned features:

- [ ] Real-time video preview
- [ ] More transition effects
- [ ] Video filters (brightness, contrast, etc.)
- [ ] Advanced text overlays with animations
- [ ] Undo/redo functionality
- [ ] Keyboard shortcuts
- [ ] Drag-and-drop timeline reordering
- [ ] Audio waveform visualization
- [ ] Multi-language support
- [ ] Plugin system

---

**Maintained for**: Insoil Training Videos
**Version**: 1.0.0
