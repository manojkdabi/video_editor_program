# Usage Training Guide

Hands-on training for using the Video Editor to create professional training videos.

## Training Overview

**Who is this for?** Anyone who needs to create training videos, even with no video editing experience.

**What you'll learn:**
1. How to start the application
2. How to import your media files
3. How to arrange content on the timeline
4. How to export your final video
5. Tips and tricks for better videos

**Training Duration:** 30-40 minutes (with exercises)

**Prerequisites:** 
- Video Editor installed (see `INSTALLATION_TRAINING.md`)
- Sample media files ready (videos, images, or audio)

---

## Module 1: Understanding the Interface (5 minutes)

### The Main Window

When you open the Video Editor, you'll see four main areas:

```
┌─────────────────────────────────────────────────────────────┐
│  [Toolbar]  New | Save | Load | Import Video/Image/Audio    │
├──────────────────────┬──────────────────────────────────────┤
│                      │                                      │
│   [Preview Panel]    │      [Properties Panel]              │
│                      │                                      │
│   • Video preview    │      • Quality settings              │
│   • Play controls    │      • Format options                │
│   • Timeline slider  │      • Export settings               │
│                      │                                      │
├──────────────────────┴──────────────────────────────────────┤
│                  [Timeline Panel]                           │
│                                                             │
│  Video Clips: intro.mp4, demo.mp4                          │
│  Image Clips: photo1.jpg                                   │
│  Audio Clips: narration.mp3                                │
└─────────────────────────────────────────────────────────────┘
```

### Let's Explore Each Area:

#### 1. Toolbar (Top)
- **New Project:** Start fresh
- **Save Project:** Save your work
- **Load Project:** Open saved work
- **Import Video:** Add video files
- **Import Image:** Add photos
- **Import Audio:** Add sound/music
- **Export Video:** Create final video (green button)

#### 2. Preview Panel (Left)
- **Preview Area:** See your video
- **Play Button (▶):** Play the video
- **Pause Button (⏸):** Pause playback
- **Stop Button (⏹):** Stop and reset
- **Timeline Slider:** Scrub through video
- **Time Display:** Shows current time and total duration

#### 3. Timeline Panel (Bottom)
- Shows all your clips in order
- Organized by type (video, image, audio)
- This is your "editing workspace"

#### 4. Properties Panel (Right)
- **Quality:** Choose High/Medium/Low
- **Format:** Choose MP4/AVI/MOV
- **Export Settings:** Configure output

**✓ Practice Exercise:**
- Launch the application
- Spend 2 minutes clicking around
- Try to identify each of the four areas
- Don't worry, you can't break anything!

---

## Module 2: Creating Your First Video (10 minutes)

### Scenario: Simple Training Video

Let's create a basic training video with:
- An introduction video
- A product photo
- A demonstration video
- Background narration

### Step 1: Start a New Project

1. **Launch the application:**
   - Double-click `run_editor.bat`
   - Wait for window to open

2. **Start fresh:**
   - Click **"New Project"** button
   - Timeline will be empty
   - You're ready to begin!

**✓ Checkpoint:** Timeline panel shows "Timeline is empty"

---

### Step 2: Import Your Video Files

1. **Click "Import Video"** button (in toolbar)

2. **Select your files:**
   - A file browser window opens
   - Navigate to your videos folder
   - Select one or more videos:
     - Click first video
     - Hold Ctrl and click more videos (for multiple)
   - Click **"Open"**

3. **What happens:**
   - A small popup says "Imported X video(s)"
   - Your videos appear in the Timeline panel under "VIDEO CLIPS:"

**Example:**
```
VIDEO CLIPS:
  1. C:\Videos\intro.mp4
  2. C:\Videos\demonstration.mp4
```

**✓ Practice Exercise:**
- Import 2-3 video files
- Check they appear in the timeline
- Note the file paths shown

**💡 Tip:** Videos will play in the order you import them (1, 2, 3...)

---

### Step 3: Import Images (Optional)

1. **Click "Import Image"** button

2. **Select your photos:**
   - Navigate to your images folder
   - Select photos (hold Ctrl for multiple)
   - Click **"Open"**

3. **Result:**
   - Images appear under "IMAGE CLIPS:"
   - Each image shows its duration (default: 5.0 seconds)

**Example:**
```
IMAGE CLIPS:
  1. C:\Images\product_photo.jpg (Duration: 5.0s)
  2. C:\Images\diagram.png (Duration: 5.0s)
```

**✓ Practice Exercise:**
- Import 1-2 image files
- Verify they appear in timeline

**💡 Tip:** Images will be shown for 5 seconds each in your video

---

### Step 4: Import Audio (Optional)

1. **Click "Import Audio"** button

2. **Select audio file:**
   - Find your audio file
   - Select it
   - Click **"Open"**

3. **Result:**
   - Audio appears under "AUDIO CLIPS:"

**Example:**
```
AUDIO CLIPS:
  1. C:\Audio\narration.mp3
```

**✓ Practice Exercise:**
- Import an audio file
- Check it appears in timeline

**💡 Tip:** Audio can be background music or voice narration

---

### Step 5: Review Your Timeline

After importing, your timeline should look like:

```
=== TIMELINE ===

VIDEO CLIPS:
  1. C:\Videos\intro.mp4
  2. C:\Videos\demonstration.mp4

IMAGE CLIPS:
  1. C:\Images\product_photo.jpg (Duration: 5.0s)

AUDIO CLIPS:
  1. C:\Audio\narration.mp3
```

**Understanding the order:**
1. intro.mp4 plays first
2. demonstration.mp4 plays second
3. product_photo.jpg shows for 5 seconds
4. Audio plays alongside video

**✓ Checkpoint:** Timeline shows all your imported media

---

### Step 6: Save Your Project

IMPORTANT: Save your work so you can continue later!

1. **Click "Save Project"** button

2. **Choose location:**
   - Pick a folder (e.g., Documents\VideoProjects)
   - Type a filename (e.g., "Training_Video_1")
   - Click **"Save"**

3. **Success:**
   - Popup says "Project saved successfully"
   - You now have a `.vedproj` file

**✓ Practice Exercise:**
- Save your project with a meaningful name
- Note where you saved it

**💡 Tip:** Save frequently! Click "Save Project" after any changes.

---

### Step 7: Export Your Video

Now let's create the actual video file!

1. **Click "Export Video"** (green button in toolbar)

2. **Choose quality:**
   - Look at Properties panel (right side)
   - Quality dropdown shows: High/Medium/Low
   - For practice, choose **"Medium"**

3. **Choose format:**
   - Format dropdown shows: mp4/avi/mov
   - Choose **"mp4"** (most common)

4. **Select output location:**
   - A save dialog opens
   - Choose where to save (e.g., Documents\Videos)
   - Type filename (e.g., "My_First_Video")
   - Click **"Save"**

5. **Wait for export:**
   - Export window shows "Exporting Video..."
   - Progress bar fills up
   - This can take several minutes!
   - Be patient, don't close the window

6. **Success!**
   - Popup says "Video exported successfully"
   - Shows the file location
   - Click **"OK"**

**✓ Checkpoint:** You now have a video file (e.g., `My_First_Video.mp4`)

---

### Step 8: Watch Your Video

1. **Find your exported video:**
   - Go to the location you chose
   - Find your `.mp4` file

2. **Play it:**
   - Double-click the file
   - It opens in your default video player
   - Watch your creation!

**✓ Practice Exercise:**
- Export a video
- Play it in Windows Media Player or VLC
- Verify it looks correct

**🎉 Congratulations!** You've created your first video!

---

## Module 3: Working with Projects (5 minutes)

### Saving Projects

**When to save:**
- After importing media
- After making any changes
- Before closing the application
- Every 5-10 minutes while working

**How to save:**
1. Click "Save Project"
2. Choose location and filename
3. File has `.vedproj` extension

**What's saved:**
- List of all media files used
- Order of clips
- Export settings
- Duration settings

**What's NOT saved:**
- The original video/image/audio files (keep these!)
- The final exported video (export separately)

---

### Loading Projects

**To continue working on a project:**

1. **Launch the application**

2. **Click "Load Project"**

3. **Find your .vedproj file:**
   - Navigate to where you saved it
   - Select the file
   - Click **"Open"**

4. **Project loads:**
   - Popup says "Project loaded successfully"
   - Timeline shows all your clips again

**✓ Practice Exercise:**
- Close the application
- Reopen it
- Load your saved project
- Verify all clips are still there

**💡 Tip:** Keep your .vedproj files organized in one folder

---

### Project File Management

**Best practices:**

```
My Documents/
├── VideoProjects/           ← Your .vedproj files
│   ├── Training_1.vedproj
│   ├── Training_2.vedproj
│   └── Demo_Video.vedproj
│
├── RawMedia/               ← Original files
│   ├── Videos/
│   ├── Images/
│   └── Audio/
│
└── ExportedVideos/         ← Final videos
    ├── Training_1.mp4
    └── Training_2.mp4
```

**⚠️ Important:**
- Don't move or rename original media files after importing
- Keep all media files in one organized location
- Back up your projects and media files

---

## Module 4: Understanding Export Settings (5 minutes)

### Quality Presets

| Quality | Resolution | File Size (5 min video) | Best For |
|---------|-----------|------------------------|----------|
| **High** | 1920x1080 (Full HD) | ~293 MB | Final delivery, YouTube, Professional use |
| **Medium** | 1280x720 (HD) | ~147 MB | Web sharing, Presentations, Most uses |
| **Low** | 854x480 (SD) | ~73 MB | Email attachments, Quick previews, Mobile |

### Choosing the Right Quality

**Use High when:**
- Final professional video
- Uploading to YouTube/Vimeo
- Maximum quality needed
- File size not a concern

**Use Medium when:**
- Sharing online
- Good balance needed
- Most common choice
- Works for 90% of uses

**Use Low when:**
- Email attachment (size limit)
- Quick preview/draft
- Storage space limited
- Mobile viewing only

**✓ Practice Exercise:**
- Export the same project 3 times
- Try High, Medium, and Low
- Compare file sizes
- Watch each one to see differences

---

### Export Formats

**MP4 (Recommended):**
- ✅ Works everywhere
- ✅ Small file size
- ✅ Good quality
- Use this 99% of the time

**AVI:**
- ✅ Highest quality
- ❌ Very large files
- Use for archival or further editing

**MOV:**
- ✅ Good quality
- ⚠️ Better on Mac
- Use if specifically requested

**💡 Tip:** When in doubt, use MP4 at Medium quality!

---

## Module 5: Tips & Tricks (5 minutes)

### Planning Your Video

**Before you start editing:**

1. **Write a script:**
   - What message do you want to convey?
   - What order makes sense?
   - How long should it be?

2. **Gather all media first:**
   - Collect all videos
   - Prepare all images
   - Record all narration
   - Organize in folders

3. **Make a simple plan:**
   ```
   1. Intro video (0:30)
   2. Product photo (0:05)
   3. Demo video (2:00)
   4. Closing video (0:30)
   Total: 3:05
   ```

---

### Creating Better Videos

**Video tips:**
- Keep videos short and focused
- Use good lighting in recordings
- Stable camera (use tripod if possible)
- Clear audio without background noise

**Image tips:**
- Use high-resolution images (1920x1080 or larger)
- Keep text readable
- Consistent style across images
- Avoid cluttered backgrounds

**Audio tips:**
- Record in quiet environment
- Speak clearly and at consistent volume
- Use good microphone if possible
- Edit audio separately before importing

---

### Common Workflow

**For Insoil training videos:**

1. **Preparation (1 hour):**
   - Plan content and script
   - Record/gather all media
   - Organize files in folders

2. **Editing (30 minutes):**
   - Launch video editor
   - Import all media
   - Check order in timeline
   - Save project

3. **Review (10 minutes):**
   - Export at Medium quality
   - Watch the full video
   - Note any problems

4. **Final (15 minutes):**
   - Make any needed changes
   - Export at High quality
   - Verify final video

**Total time:** About 2 hours for a 3-5 minute training video

---

### Keyboard Shortcuts

Currently, the editor uses mouse/click actions:
- Tab key: Move between buttons
- Enter: Activate selected button
- Click: All other actions

**💡 Future versions will have more shortcuts!**

---

## Module 6: Troubleshooting During Use (5 minutes)

### Problem: Can't Import File

**Error:** File doesn't appear after importing

**Solutions:**
1. Check file format (must be supported format)
2. Try converting video to MP4 first
3. Ensure file isn't corrupted (try playing it first)
4. Check file isn't in use by another program

---

### Problem: Export Takes Forever

**Situation:** Export seems stuck or very slow

**Normal times:**
- 1 minute video: 2-5 minutes export
- 5 minute video: 10-25 minutes export
- 10 minute video: 20-50 minutes export

**If abnormally slow:**
1. Close other programs
2. Check CPU usage (Task Manager)
3. Try Lower quality preset
4. Restart computer and try again
5. Break into smaller videos

---

### Problem: Timeline Doesn't Show Clips

**Issue:** Imported files don't appear in timeline

**Solutions:**
1. Check you clicked Import and selected files
2. Look carefully at timeline panel (bottom)
3. Try importing again
4. Restart application
5. Check video_editor.log for errors

---

### Problem: Can't Find Exported Video

**Issue:** Don't know where video saved

**Solution:**
1. When exporting, note the save location
2. Check your Documents folder
3. Search Windows for the filename
4. Export again and carefully note location

---

## Practice Exercises

### Exercise 1: Basic Video (Beginner)

**Goal:** Create a 3-clip video

**Steps:**
1. Import 3 short videos
2. Verify order in timeline
3. Save project as "Exercise_1"
4. Export as Medium quality MP4
5. Watch the result

**Time:** 15 minutes

---

### Exercise 2: Mixed Media (Intermediate)

**Goal:** Create video with videos and images

**Steps:**
1. Import 2 videos
2. Import 2 images
3. Import 1 audio file
4. Save project
5. Export at Medium quality
6. Review the video
7. Note how images show for 5 seconds each

**Time:** 20 minutes

---

### Exercise 3: Full Training Video (Advanced)

**Goal:** Create a complete Insoil training video

**Requirements:**
- 1 intro video
- 3-4 demonstration videos
- 2-3 product images
- Background narration audio
- 3-5 minutes total length

**Steps:**
1. Plan the content order
2. Import all media
3. Save project frequently
4. Export at High quality
5. Review carefully
6. Make corrections if needed
7. Re-export if necessary

**Time:** 45-60 minutes

---

## Summary & Next Steps

### What You Learned

✅ How to navigate the interface
✅ How to import media files
✅ How to manage the timeline
✅ How to save and load projects
✅ How to export videos
✅ Tips for better videos
✅ Common troubleshooting

### Next Steps

1. **Practice:**
   - Do all three exercises
   - Experiment with different media
   - Try different export settings

2. **Advanced Learning:**
   - Read `USER_GUIDE.md` for all features
   - Check `DEVELOPER_NOTES.md` for customization
   - See `TRAINING_EXERCISES.md` for more practice

3. **Real Projects:**
   - Start creating actual Insoil training videos
   - Build a library of reusable components
   - Develop your own workflow

### Quick Reference Card

```
ESSENTIAL ACTIONS:
├─ Start: Double-click run_editor.bat
├─ Import: Click Import Video/Image/Audio buttons
├─ Save: Click Save Project (do this often!)
├─ Export: Click Export Video (green button)
└─ Exit: Close window (save first!)

EXPORT SETTINGS:
├─ Quality: Medium (for most uses)
├─ Format: MP4 (universal compatibility)
└─ Location: Choose a consistent folder

REMEMBER:
├─ Save projects frequently
├─ Keep original media organized
├─ Don't move files after importing
└─ Be patient during export
```

---

## Congratulations! 🎉

You now know how to use the Video Editor to create professional training videos!

**You're ready to:**
- Create Insoil training videos independently
- Help others learn the software
- Develop efficient workflows
- Produce high-quality content

**Keep learning:**
- Try new techniques
- Experiment with settings
- Share tips with colleagues
- Request features you need

---

**Training Complete!**

For additional help, see:
- `FAQ.md` - Frequently asked questions
- `TROUBLESHOOTING_GUIDE.md` - Problem solutions
- `USER_GUIDE.md` - Complete feature reference

Happy video editing! 🎬
