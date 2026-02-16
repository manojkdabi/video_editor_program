# Video Editor - User Guide

Complete guide for creating training videos with the Insoil Video Editor.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Interface Overview](#interface-overview)
3. [Working with Video Clips](#working-with-video-clips)
4. [Adding Images](#adding-images)
5. [Audio Management](#audio-management)
6. [Text Overlays](#text-overlays)
7. [Timeline Operations](#timeline-operations)
8. [Exporting Videos](#exporting-videos)
9. [Project Management](#project-management)
10. [Tips and Best Practices](#tips-and-best-practices)

## Getting Started

### First Launch

1. Double-click `run_editor.bat`
2. The main window will open with four main sections:
   - **Toolbar** (top) - Quick access buttons
   - **Preview** (left) - Video preview and playback controls
   - **Timeline** (bottom) - Your video timeline
   - **Properties** (right) - Settings and export options

### Creating Your First Project

1. Click **"New Project"** to start fresh
2. The timeline will be empty and ready for content

## Interface Overview

### Toolbar Buttons

| Button | Function |
|--------|----------|
| New Project | Create a new empty project |
| Save Project | Save current project to file |
| Load Project | Open an existing project |
| Import Video | Add video files to timeline |
| Import Image | Add photos to timeline |
| Import Audio | Add audio files to timeline |
| Export Video | Render and save final video |

### Preview Panel

- **Video Preview Area**: Shows current frame
- **Play/Pause/Stop**: Control playback
- **Timeline Slider**: Scrub through video
- **Time Display**: Current position and total duration

### Timeline Panel

Shows all clips in your project:
- Video clips listed first
- Image clips listed second
- Audio clips listed last

### Properties Panel

- **Properties Display**: Shows selected clip details
- **Export Settings**:
  - Quality: High/Medium/Low
  - Format: MP4/AVI/MOV

## Working with Video Clips

### Importing Videos

1. Click **"Import Video"**
2. Browse to your video files
3. Select one or multiple videos (Ctrl+Click for multiple)
4. Click "Open"
5. Videos appear in the timeline

### Supported Video Formats

- MP4 (recommended)
- AVI
- MOV
- MKV
- WMV
- FLV
- WebM

### Video File Recommendations

- **Resolution**: 1920x1080 or 1280x720
- **Format**: MP4 for best compatibility
- **Codec**: H.264 recommended
- **File Size**: Keep individual files under 2GB

## Adding Images

### Importing Images

1. Click **"Import Image"**
2. Select one or multiple image files
3. Images appear in the timeline

### Image Settings

- **Default Duration**: 5 seconds
- You can adjust duration in the timeline

### Supported Image Formats

- JPG/JPEG
- PNG (supports transparency)
- BMP
- GIF
- TIFF

### Image Best Practices

- Use high-resolution images (1920x1080 or higher)
- PNG format for images with transparency
- Keep file sizes reasonable (< 10MB each)

## Audio Management

### Importing Audio

1. Click **"Import Audio"**
2. Select your audio file
3. Audio appears in the timeline

### Supported Audio Formats

- MP3 (recommended)
- WAV (high quality, larger size)
- AAC
- OGG
- M4A
- FLAC

### Audio Tips

- **Narration**: Use MP3 format at 128kbps or higher
- **Background Music**: Keep volume lower than narration
- **Quality**: 44.1kHz sample rate recommended

## Text Overlays

### Adding Text (Future Feature)

Text overlay functionality is planned for future versions. Current version supports:
- Title screens
- Basic subtitles
- Annotations

## Timeline Operations

### Understanding the Timeline

The timeline shows all your media in order:

```
VIDEO CLIPS:
  1. intro_video.mp4
  2. demonstration.mp4

IMAGE CLIPS:
  1. product_photo.jpg (Duration: 5.0s)

AUDIO CLIPS:
  1. narration.mp3
```

### Arranging Clips

- Clips play in the order they appear
- To rearrange: remove and re-import in desired order

### Removing Clips

Current version: Manual project editing
Future version: Will have delete buttons

## Exporting Videos

### Export Process

1. Click **"Export Video"**
2. Choose quality preset:
   - **High**: 1920x1080, best quality
   - **Medium**: 1280x720, balanced
   - **Low**: 854x480, small file size
3. Select format (MP4 recommended)
4. Choose save location
5. Click "Save"
6. Wait for rendering to complete

### Export Quality Guide

#### High Quality (1080p)
- **Use for**: Final delivery, YouTube, professional use
- **File size**: ~50-100MB per minute
- **Resolution**: 1920x1080
- **Bitrate**: 8000k

#### Medium Quality (720p)
- **Use for**: Web sharing, presentations
- **File size**: ~25-50MB per minute
- **Resolution**: 1280x720
- **Bitrate**: 4000k

#### Low Quality (480p)
- **Use for**: Email, quick previews, mobile viewing
- **File size**: ~10-25MB per minute
- **Resolution**: 854x480
- **Bitrate**: 2000k

### Export Time Estimates

- **1 minute video**: 2-5 minutes export time
- **5 minute video**: 10-25 minutes export time
- **10 minute video**: 20-50 minutes export time

*Export time depends on your computer's CPU and video complexity*

## Project Management

### Saving Projects

1. Click **"Save Project"**
2. Choose location and filename
3. Project saved with `.vedproj` extension

### Loading Projects

1. Click **"Load Project"**
2. Browse to your `.vedproj` file
3. Click "Open"
4. Project loads with all clips

### What Gets Saved

Project files store:
- List of video files used
- List of image files used
- List of audio files used
- Clip durations and settings
- Export settings

### What Doesn't Get Saved

- Original media files (must keep them)
- Rendered videos (export separately)
- Temporary preview files

### Backup Best Practices

1. Keep all original media files organized
2. Save project files regularly
3. Use descriptive project names
4. Back up both project files and media files

## Tips and Best Practices

### Organizing Media Files

```
Insoil_Training_Videos/
├── Project_Files/
│   ├── video1_project.vedproj
│   └── video2_project.vedproj
├── Raw_Videos/
│   ├── intro.mp4
│   └── demo.mp4
├── Images/
│   ├── photo1.jpg
│   └── photo2.jpg
├── Audio/
│   ├── narration1.mp3
│   └── music.mp3
└── Exports/
    ├── final_video1.mp4
    └── final_video2.mp4
```

### Video Creation Workflow

1. **Plan**: Write script, gather all media
2. **Organize**: Sort files into folders
3. **Import**: Add all media to project
4. **Arrange**: Order clips on timeline
5. **Review**: Preview entire video
6. **Export**: Render final video
7. **Save**: Save project file for future edits

### Performance Tips

- Close other applications while exporting
- Use lower quality for preview/testing
- Keep video files on fast drive (SSD if available)
- Restart application if it becomes slow

### Quality Tips

- Use consistent video resolution across clips
- Maintain consistent audio levels
- Use high-quality source material
- Test export with short section first

### Common Mistakes to Avoid

❌ Don't move or rename media files after importing
❌ Don't use very large video files (>2GB)
❌ Don't mix very different resolutions
❌ Don't forget to save your project
❌ Don't delete project files after export

✅ Do keep organized folder structure
✅ Do save projects frequently
✅ Do test export with short clips first
✅ Do keep backups of important projects
✅ Do use consistent naming conventions

## Keyboard Shortcuts (Future Feature)

Planned for future versions:
- Space: Play/Pause
- Ctrl+S: Save Project
- Ctrl+N: New Project
- Ctrl+O: Open Project
- Delete: Remove selected clip

## Troubleshooting Common Issues

### Video Won't Import
- Check file format is supported
- Ensure file isn't corrupted
- Try converting to MP4 first

### Audio Not Syncing
- Check audio file duration matches video
- Ensure audio format is supported
- Try WAV format if MP3 has issues

### Export Takes Too Long
- Use lower quality preset
- Break video into smaller sections
- Check CPU usage isn't at 100% from other apps

### Application Crashes
- Check `video_editor.log` file
- Ensure enough RAM available
- Try smaller/fewer clips

### Preview Not Showing
- Check video codec is supported
- Try restarting application
- Ensure graphics drivers are updated

## Getting More Help

- **Log File**: Check `video_editor.log` for errors
- **Technical Details**: See `DEVELOPER_NOTES.md`
- **Updates**: Check for new versions

---

**Happy Video Editing!**

Created for Insoil Training Videos
Version 1.0.0
