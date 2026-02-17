# Application Architecture

## System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                         USER INTERFACE                          │
│                      (CustomTkinter GUI)                        │
├─────────────────────────────────────────────────────────────────┤
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐      │
│  │ Toolbar  │  │ Preview  │  │ Timeline │  │Properties│      │
│  │          │  │          │  │          │  │          │      │
│  │ • New    │  │ • Video  │  │ • Videos │  │ • Quality│      │
│  │ • Save   │  │ • Play   │  │ • Images │  │ • Format │      │
│  │ • Load   │  │ • Pause  │  │ • Audio  │  │ • Export │      │
│  │ • Import │  │ • Stop   │  │ • Text   │  │          │      │
│  │ • Export │  │ • Seek   │  │          │  │          │      │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘      │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     MAIN WINDOW CONTROLLER                       │
│                      (main_window.py)                           │
├─────────────────────────────────────────────────────────────────┤
│  • Event Handling                                               │
│  • User Action Coordination                                     │
│  • State Management                                             │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      CORE MODULES LAYER                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────┐│
│  │ Video Processing │  │    Utilities     │  │ Project Mgmt ││
│  │                  │  │                  │  │              ││
│  │ • Editor         │  │ • FileHandler    │  │ • Save       ││
│  │ • Effects        │  │ • MediaInfo      │  │ • Load       ││
│  │ • TextOverlay    │  │                  │  │ • Validate   ││
│  │ • Export         │  │                  │  │              ││
│  └──────────────────┘  └──────────────────┘  └──────────────┘│
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                   EXTERNAL LIBRARIES                            │
├─────────────────────────────────────────────────────────────────┤
│  • MoviePy (video processing)                                   │
│  • PIL/Pillow (image handling)                                  │
│  • OpenCV (computer vision)                                     │
│  • NumPy (numerical operations)                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Data Flow Diagram

```
┌───────────┐
│   USER    │
└─────┬─────┘
      │ Actions
      ▼
┌───────────────────────────────────────────────────┐
│             GUI (Main Window)                     │
│  • Click Import Video                             │
│  • Click Export                                   │
│  • Adjust Settings                                │
└─────┬─────────────────────────────────────────────┘
      │ Commands
      ▼
┌───────────────────────────────────────────────────┐
│         Project Manager                           │
│  • Update timeline data                           │
│  • Track modifications                            │
│  • Save/Load state                                │
└─────┬─────────────────────────────────────────────┘
      │ Media Files
      ▼
┌───────────────────────────────────────────────────┐
│          File Handler                             │
│  • Validate file formats                          │
│  • Check file existence                           │
│  • Sanitize paths                                 │
└─────┬─────────────────────────────────────────────┘
      │ Validated Files
      ▼
┌───────────────────────────────────────────────────┐
│        Media Info                                 │
│  • Extract video metadata                         │
│  • Get duration, resolution                       │
│  • Get audio properties                           │
└─────┬─────────────────────────────────────────────┘
      │ Metadata
      ▼
┌───────────────────────────────────────────────────┐
│       Video Editor                                │
│  • Load clips                                     │
│  • Trim/Cut                                       │
│  • Concatenate                                    │
│  • Apply effects                                  │
│  • Add text overlays                              │
└─────┬─────────────────────────────────────────────┘
      │ Processed Clips
      ▼
┌───────────────────────────────────────────────────┐
│      Video Exporter                               │
│  • Apply quality settings                         │
│  • Encode video                                   │
│  • Save to disk                                   │
└─────┬─────────────────────────────────────────────┘
      │ Final Video
      ▼
┌───────────┐
│   DISK    │
│ (MP4/AVI) │
└───────────┘
```

## Module Dependencies

```
main.py
  └── src.gui.main_window
       ├── src.utils.project_manager
       ├── src.utils.file_handler
       ├── src.video_processing.editor
       │    ├── moviepy.VideoFileClip
       │    ├── moviepy.ImageClip
       │    ├── moviepy.AudioFileClip
       │    └── moviepy.CompositeVideoClip
       ├── src.video_processing.effects
       │    ├── moviepy.video.fx.FadeIn
       │    ├── moviepy.video.fx.FadeOut
       │    ├── moviepy.video.fx.CrossFadeIn
       │    └── moviepy.video.fx.CrossFadeOut
       ├── src.video_processing.text_overlay
       │    └── moviepy.TextClip
       └── src.video_processing.export
            └── VideoFileClip.write_videofile()
```

## Class Hierarchy

```
Application Classes
├── MainWindow (CTk)
│   ├── ProjectManager
│   ├── FileHandler
│   ├── VideoEditor
│   └── VideoExporter
│
├── ExportDialog (CTkToplevel)
│
└── Utility Classes
    ├── FileHandler (static methods)
    ├── MediaInfo (static methods)
    ├── VideoEffects (static methods)
    └── TextOverlay (static methods)
```

## Timeline Data Structure

```json
{
  "version": "1.0",
  "created": "2026-02-16T10:00:00",
  "modified": "2026-02-16T12:00:00",
  "timeline": {
    "video_clips": [
      {
        "type": "video",
        "filepath": "C:/videos/intro.mp4",
        "start": 0.0,
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
        "start": 0.0,
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

## File System Layout

```
C:\VideoEditor\
├── main.py                    # Entry point
├── install.bat               # Setup script
├── run_editor.bat           # Launch script
├── requirements.txt         # Dependencies
├── video_editor.log         # Runtime logs
│
├── venv\                    # Virtual environment (created by install.bat)
│   ├── Scripts\
│   │   ├── python.exe
│   │   └── activate.bat
│   └── Lib\
│
├── src\                     # Source code
│   ├── gui\
│   ├── video_processing\
│   └── utils\
│
├── assets\                  # Resources
│   ├── icons\
│   └── fonts\
│
└── projects\               # User projects (created by user)
    └── my_video.vedproj
```

## Processing Pipeline

```
1. IMPORT
   User → GUI → FileHandler → Validation
                                   ↓
2. LOAD                           OK?
   filepath → MediaInfo → metadata  
                    ↓               
3. ADD TO TIMELINE                 
   metadata → ProjectManager → timeline_data
                                   ↓
4. EDIT (Optional)
   timeline → VideoEditor → trim/effects/text
                                   ↓
5. EXPORT
   timeline → VideoEditor → composite
                                   ↓
   composite → VideoExporter → encode
                                   ↓
   encoded → write_videofile → output.mp4
```

## Error Handling Flow

```
┌─────────────┐
│ User Action │
└──────┬──────┘
       │
       ▼
┌─────────────────┐
│ Try Operation   │
└──────┬──────────┘
       │
       ├─Success──────► Continue
       │
       └─Error────┐
                  │
                  ▼
           ┌─────────────┐
           │   Logger    │ ──► video_editor.log
           │  (record)   │
           └──────┬──────┘
                  │
                  ▼
           ┌─────────────┐
           │  User Alert │ ──► MessageBox
           │  (friendly) │
           └─────────────┘
```

## Export Quality Pipeline

```
USER SELECTION
  │
  ├─ High (1080p)
  │   └─► Resolution: 1920x1080, Bitrate: 8000k, FPS: 30
  │
  ├─ Medium (720p)
  │   └─► Resolution: 1280x720, Bitrate: 4000k, FPS: 30
  │
  └─ Low (480p)
      └─► Resolution: 854x480, Bitrate: 2000k, FPS: 24

APPLY SETTINGS
  ↓
ENCODE WITH FFMPEG (via MoviePy)
  ↓
OUTPUT FILE
```

## Memory Management

```
Video Clip Loading
  └─► Load into memory (RAM)
       │
       ├─ Process (edit, effects)
       │
       ├─ Export (write to disk)
       │
       └─► Close clip (free memory)

Multiple Clips
  └─► Sequential processing
       └─► Load → Process → Close → Next
```

---

This architecture ensures:
- ✅ Clean separation of concerns
- ✅ Maintainable code structure
- ✅ Easy to extend with new features
- ✅ Robust error handling
- ✅ Efficient resource management
