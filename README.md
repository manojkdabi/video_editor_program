# Video Editor for Insoil Training Videos

A complete, user-friendly video editor application for Windows that allows creating professional training videos for Insoil soil testing device without requiring programming knowledge.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-brightgreen.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)

## Features

✅ **Timeline-Based Editing** - Visual timeline with drag-and-drop support
✅ **Multi-Track Support** - Video, image, and audio tracks
✅ **Audio Management** - Import and sync audio with volume control
✅ **Video Trimming** - Precise frame-level cutting and trimming
✅ **Image Integration** - Add photos with custom duration and transitions
✅ **Text Overlays** - Add titles, subtitles, and annotations
✅ **Transitions** - Fade in/out and crossfade effects
✅ **Export Options** - MP4, AVI, MOV with quality presets
✅ **Project Management** - Save and load projects
✅ **Windows Optimized** - Native Windows file dialogs and paths

## Quick Start

### Installation (One-Time Setup)

1. **Install Python 3.8 or higher** (if not already installed)
   - Download from: https://www.python.org/downloads/
   - ⚠️ **Important**: Check "Add Python to PATH" during installation

2. **Run the installation script**
   - Double-click `install.bat`
   - Wait for setup to complete (5-10 minutes)
   - You'll see "Installation Complete!" when done

### Launching the Editor

- Double-click `run_editor.bat`
- The video editor window will open

## Creating Your First Video

1. **Import Media**
   - Click "Import Video" to add raw video files
   - Click "Import Image" to add photos
   - Click "Import Audio" to add audio narration

2. **Arrange Timeline**
   - Your imported files appear in the timeline
   - Files are arranged in the order they were imported

3. **Preview**
   - Use playback controls to preview your video
   - Check timing and transitions

4. **Export**
   - Click "Export Video"
   - Choose quality (High/Medium/Low)
   - Select output location
   - Wait for rendering to complete

## System Requirements

- **Operating System**: Windows 10 or Windows 11
- **Python**: Version 3.8 or higher
- **RAM**: 4GB minimum (8GB recommended)
- **Disk Space**: 500MB for software + space for video files
- **Display**: 1280x720 or higher resolution

## Supported File Formats

### Input Formats
- **Video**: MP4, AVI, MOV, MKV, WMV, FLV, WebM
- **Image**: JPG, JPEG, PNG, BMP, GIF, TIFF
- **Audio**: MP3, WAV, AAC, OGG, M4A, FLAC

### Export Formats
- **MP4** (Recommended) - Best compatibility
- **AVI** - High quality, larger file size
- **MOV** - Good for further editing

## Quality Presets

| Preset | Resolution | Bitrate | Best For |
|--------|-----------|---------|----------|
| High   | 1920x1080 | 8000k   | Final delivery, YouTube |
| Medium | 1280x720  | 4000k   | Web sharing, smaller files |
| Low    | 854x480   | 2000k   | Email, quick previews |

## Project Structure

```
video_editor_program/
├── main.py                  # Application entry point
├── requirements.txt         # Python dependencies
├── install.bat             # Installation script
├── run_editor.bat          # Launch script
├── README.md               # This file
├── USER_GUIDE.md           # Detailed user guide
├── DEVELOPER_NOTES.md      # Technical documentation
├── src/
│   ├── gui/                # User interface components
│   │   └── main_window.py # Main application window
│   ├── video_processing/   # Video editing logic
│   │   ├── editor.py      # Core editing functions
│   │   ├── effects.py     # Transitions and effects
│   │   ├── text_overlay.py # Text rendering
│   │   └── export.py      # Export functionality
│   └── utils/             # Utility modules
│       ├── file_handler.py # File operations
│       ├── media_info.py   # Metadata extraction
│       └── project_manager.py # Project save/load
└── assets/                # Icons and fonts
```

## Troubleshooting

### Python Not Found
- **Problem**: "Python is not installed" error
- **Solution**: Install Python from https://python.org and check "Add Python to PATH"

### Installation Fails
- **Problem**: Error during `pip install`
- **Solution**: Try running as administrator, or use: `python -m pip install --upgrade pip`

### Application Won't Start
- **Problem**: Window closes immediately
- **Solution**: Check `video_editor.log` for error details

### Export Fails
- **Problem**: Video export crashes
- **Solution**: 
  - Ensure enough disk space
  - Try lower quality preset
  - Check that all media files still exist

### Slow Performance
- **Problem**: Preview is laggy
- **Solution**:
  - Close other applications
  - Use lower resolution videos for preview
  - Increase RAM if possible

## Getting Help

- **User Guide**: See `USER_GUIDE.md` for detailed feature documentation
- **Technical Issues**: Check `video_editor.log` for error messages
- **Developer Notes**: See `DEVELOPER_NOTES.md` for code structure

## Creating an Executable

To create a standalone `.exe` file:

```bash
# Activate virtual environment
venv\Scripts\activate.bat

# Install PyInstaller
pip install pyinstaller

# Create executable
pyinstaller --onefile --windowed --name VideoEditor main.py

# Executable will be in dist/VideoEditor.exe
```

## License

MIT License - See LICENSE file for details

## Credits

- **GUI Framework**: CustomTkinter
- **Video Processing**: MoviePy
- **Developed for**: Insoil Training Videos

---

**Version**: 1.0.0
**Last Updated**: February 2026
