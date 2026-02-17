# Quick Start Guide

Get up and running with the Video Editor in 5 minutes!

## Installation (One-Time - 5 minutes)

### Step 1: Install Python
1. Download Python from https://www.python.org/downloads/
2. Run the installer
3. ⚠️ **IMPORTANT**: Check ☑ "Add Python to PATH"
4. Click "Install Now"

### Step 2: Install Video Editor
1. Extract the video editor folder to your computer (e.g., `C:\VideoEditor`)
2. Double-click `install.bat`
3. Wait 5-10 minutes for installation
4. Look for "Installation Complete!" message

## Your First Video (5 minutes)

### Step 1: Launch
- Double-click `run_editor.bat`
- Main window opens

### Step 2: Import Media
1. Click **"Import Video"**
   - Select your video files (e.g., intro.mp4, demo.mp4)
   - They appear in the Timeline

2. Click **"Import Image"** (optional)
   - Select photos (e.g., product_photo.jpg)
   - They appear in the Timeline

3. Click **"Import Audio"** (optional)
   - Select audio narration (e.g., script.mp3)
   - It appears in the Timeline

### Step 3: Preview
- Look at the Timeline panel (bottom) to see all your clips
- Preview shows order of clips

### Step 4: Export
1. Click **"Export Video"** (green button)
2. Choose quality:
   - **High** (1080p) - Best quality, larger file
   - **Medium** (720p) - Good quality, medium file
   - **Low** (480p) - Small file size
3. Choose where to save
4. Wait for rendering (takes time based on video length)
5. Done! Your video is ready

## Common Workflows

### Training Video with Narration
```
1. Import main video clips
2. Import narration audio
3. (Optional) Import product photos
4. Export as High quality MP4
```

### Simple Slideshow with Photos
```
1. Import multiple photos
2. (Optional) Import background music
3. Export as Medium quality MP4
```

### Multi-Part Tutorial
```
1. Import intro video
2. Import demonstration videos
3. Import conclusion video
4. (Optional) Add narration audio
5. Export as High quality MP4
```

## Tips for Success

✅ **DO**:
- Keep all video files in one organized folder
- Use consistent video resolution (all 1080p or all 720p)
- Save project file frequently
- Test with short clips first

❌ **DON'T**:
- Move video files after importing them
- Use very large video files (keep under 2GB each)
- Delete project files after exporting
- Mix very different resolutions

## Keyboard Tips (Mouse-Free Navigation)

- Tab: Move between buttons
- Enter: Click selected button
- Space: (in dialogs) Confirm

## File Organization Tip

```
My_Training_Videos/
├── Projects/           ← Save .vedproj files here
├── Raw_Videos/        ← Original video files
├── Audio/             ← Narration and music
├── Images/            ← Product photos
└── Final_Videos/      ← Exported results
```

## Need Help?

### Quick Fixes

**Application won't start?**
- Re-run `install.bat` as administrator

**Can't import video?**
- Check file format (use MP4 for best compatibility)
- Try converting video to MP4 first

**Export takes forever?**
- Use "Medium" or "Low" quality
- Close other programs
- Be patient with long videos

### More Help

- **Full Guide**: Open `USER_GUIDE.md`
- **Technical Info**: Open `DEVELOPER_NOTES.md`
- **Error Log**: Check `video_editor.log` in program folder

## Video Length Guidelines

| Video Length | Export Time (approx) |
|--------------|---------------------|
| 1 minute     | 2-5 minutes         |
| 5 minutes    | 10-25 minutes       |
| 10 minutes   | 20-50 minutes       |
| 30 minutes   | 1-2.5 hours         |

*Export time depends on your computer speed*

## Quality vs File Size

| Quality | Resolution | 5-min Video | Best For |
|---------|-----------|-------------|----------|
| High    | 1920x1080 | ~293 MB     | Final delivery, YouTube |
| Medium  | 1280x720  | ~147 MB     | Web sharing |
| Low     | 854x480   | ~73 MB      | Email, previews |

---

**You're Ready!** 🎉

Start creating professional training videos for Insoil!

For detailed features and advanced usage, see `USER_GUIDE.md`
