# Troubleshooting Guide

Comprehensive solutions for common problems with the Video Editor.

## How to Use This Guide

1. Find your problem in the table of contents
2. Try the solutions in order (easiest to hardest)
3. Check the log file if problems persist
4. See "Getting More Help" section if still stuck

---

## Table of Contents

### Installation Problems
- [Python Won't Install](#python-wont-install)
- [Python Not Recognized](#python-not-recognized)
- [Installation Hangs](#installation-hangs)
- [Permission Denied Errors](#permission-denied-errors)
- [Module Not Found Errors](#module-not-found-errors)

### Launch Problems
- [Application Won't Start](#application-wont-start)
- [Window Closes Immediately](#window-closes-immediately)
- [Black Screen](#black-screen)
- [Error Messages on Launch](#error-messages-on-launch)

### Import Problems
- [Can't Import Video Files](#cant-import-video-files)
- [File Format Not Supported](#file-format-not-supported)
- [Files Don't Appear in Timeline](#files-dont-appear-in-timeline)
- [Import Button Doesn't Work](#import-button-doesnt-work)

### Export Problems
- [Export Fails Immediately](#export-fails-immediately)
- [Export Takes Forever](#export-takes-forever)
- [Export Crashes Partway](#export-crashes-partway)
- [Can't Find Exported Video](#cant-find-exported-video)
- [Exported Video Won't Play](#exported-video-wont-play)
- [Poor Quality After Export](#poor-quality-after-export)

### Project Problems
- [Can't Save Project](#cant-save-project)
- [Can't Load Project](#cant-load-project)
- [Missing Media Files Error](#missing-media-files-error)

### Performance Problems
- [Application is Slow](#application-is-slow)
- [Computer Freezes During Export](#computer-freezes-during-export)
- [High CPU Usage](#high-cpu-usage)
- [Out of Memory Errors](#out-of-memory-errors)

---

## Installation Problems

### Python Won't Install

**Problem:** Python installer fails or gives errors

**Solution 1: Check System Requirements**
- Verify you have Windows 10 or Windows 11
- Ensure you have administrator rights
- Check you have at least 500 MB free space

**Solution 2: Download Fresh Installer**
1. Delete the current Python installer
2. Go to https://www.python.org/downloads/
3. Download again
4. Try installing again

**Solution 3: Antivirus Interference**
1. Temporarily disable antivirus
2. Run Python installer
3. Re-enable antivirus after installation

**Solution 4: Existing Python Installation**
1. Check if Python is already installed
   - Open Command Prompt
   - Type: `python --version`
2. If Python exists:
   - Either use the existing version
   - Or uninstall first, then reinstall

---

### Python Not Recognized

**Problem:** Command Prompt says "python is not recognized"

**This is the #1 most common issue!**

**Root Cause:** You forgot to check "Add Python to PATH" during installation

**Solution 1: Modify Installation (Easiest)**
1. Open Control Panel
2. Go to "Programs and Features" or "Add/Remove Programs"
3. Find "Python 3.x"
4. Click "Modify"
5. Choose "Modify" again
6. Check "Add Python to environment variables"
7. Click "Install"

**Solution 2: Reinstall (If Modify Doesn't Work)**
1. Uninstall Python completely:
   - Control Panel → Programs → Uninstall Python
2. Restart computer
3. Download Python fresh
4. Run installer
5. **CHECK THE BOX:** "Add Python to PATH"
6. Install

**Solution 3: Manual PATH Addition (Advanced)**
1. Find Python installation folder (usually `C:\Users\YourName\AppData\Local\Programs\Python\Python3x`)
2. Copy the full path
3. Open System Properties → Environment Variables
4. Edit "Path" variable
5. Add Python folder path
6. Click OK
7. Restart Command Prompt

**Verification:**
```bash
python --version
```
Should show: `Python 3.x.x`

---

### Installation Hangs

**Problem:** `install.bat` stops responding or nothing happens

**Solution 1: Wait Longer**
- Installation can take 10-15 minutes
- Large downloads from internet
- Be patient, especially on slow connections

**Solution 2: Check Internet Connection**
1. Close the installation window
2. Verify internet is working (open a website)
3. Run `install.bat` again

**Solution 3: Run as Administrator**
1. Close installation window
2. Right-click `install.bat`
3. Choose "Run as administrator"
4. Click "Yes" when prompted

**Solution 4: Clear Temporary Files**
1. Close installation
2. Delete the `venv` folder (if it exists)
3. Open Command Prompt as administrator
4. Run: `pip cache purge`
5. Try `install.bat` again

**Solution 5: Manual Installation**
```bash
# Open Command Prompt in video editor folder
python -m venv venv
venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

---

### Permission Denied Errors

**Problem:** "Access denied" or "Permission error" during installation

**Solution 1: Run as Administrator**
1. Right-click `install.bat`
2. Select "Run as administrator"
3. Click "Yes" to allow changes

**Solution 2: Check Antivirus**
- Some antivirus software blocks installations
- Temporarily disable
- Run installation
- Re-enable afterward

**Solution 3: User Account Control**
1. Disable UAC temporarily:
   - Control Panel → User Accounts
   - Change User Account Control settings
   - Move slider to bottom
2. Run installation
3. Re-enable UAC after

**Solution 4: Install to Different Location**
1. Move video editor folder to:
   - `C:\VideoEditor` (simpler path)
   - Or your Desktop
2. Try installation again

---

### Module Not Found Errors

**Problem:** "ModuleNotFoundError" or "No module named..."

**Solution 1: Incomplete Installation**
1. Delete `venv` folder completely
2. Run `install.bat` again
3. Wait for "Installation Complete!"
4. Don't interrupt the process

**Solution 2: Check Internet Connection**
- Installation downloads from internet
- If connection dropped during install:
  1. Ensure stable connection
  2. Delete `venv` folder
  3. Run `install.bat` again

**Solution 3: Verify Requirements File**
1. Open `requirements.txt`
2. Verify it contains:
   ```
   customtkinter>=5.2.0
   Pillow>=10.0.0
   moviepy>=1.0.3
   numpy>=1.24.0
   pydub>=0.25.1
   opencv-python>=4.8.0
   python-dateutil>=2.8.2
   ```
3. If different or missing, re-download application

**Solution 4: Manual Module Installation**
```bash
venv\Scripts\activate
pip install customtkinter Pillow moviepy numpy pydub opencv-python python-dateutil
```

---

## Launch Problems

### Application Won't Start

**Problem:** Nothing happens when double-clicking `run_editor.bat`

**Solution 1: Check Installation**
- Verify `venv` folder exists
- If missing, run `install.bat`

**Solution 2: Run from Command Prompt**
```bash
# Navigate to video editor folder
cd C:\VideoEditor
run_editor.bat
```
- Watch for error messages
- Note what appears before it closes

**Solution 3: Check Python**
```bash
python --version
```
- Should show Python 3.8+
- If error, Python not properly installed

**Solution 4: Check Log File**
1. Open video editor folder
2. Look for `video_editor.log`
3. Open with Notepad
4. Read the last 10-20 lines
5. Look for ERROR messages

**Solution 5: Manual Launch**
```bash
cd C:\VideoEditor
venv\Scripts\activate
python main.py
```
- See errors directly in window

---

### Window Closes Immediately

**Problem:** Window flashes and closes right away

**Cause:** Usually a startup error

**Solution 1: Run from Command Prompt**
```bash
cd C:\VideoEditor
venv\Scripts\activate
python main.py
```
- Window stays open
- You can see the error
- Press Ctrl+C to close when done

**Solution 2: Check Dependencies**
- One dependency might be missing
- Delete `venv` folder
- Run `install.bat` again

**Solution 3: Check video_editor.log**
- Look for last ERROR entry
- Tells you what went wrong

**Solution 4: Tkinter Missing**
- CustomTkinter needs tkinter
- Install: `pip install tk`
- Or reinstall Python with tkinter enabled

---

### Black Screen

**Problem:** Window opens but is black or blank

**Solution 1: Wait**
- First launch takes 10-15 seconds
- Be patient

**Solution 2: Graphics Drivers**
- Update your graphics card drivers
- Restart computer
- Try again

**Solution 3: Compatibility Mode**
1. Right-click `run_editor.bat`
2. Properties → Compatibility
3. Check "Run in compatibility mode"
4. Choose Windows 10
5. Apply and OK

---

### Error Messages on Launch

**Problem:** Error popup when starting

**Common Errors and Solutions:**

**"DLL load failed"**
- Missing Visual C++ redistributables
- Download from Microsoft
- Install and restart

**"Failed to execute script"**
- PyInstaller issue (if using .exe)
- Use `run_editor.bat` instead
- Or rebuild executable

**"Import Error: DLL"**
- Missing system libraries
- Install Visual C++ Redistributable 2015-2022
- Restart computer

**"tkinter.TclError"**
- Display/graphics issue
- Update graphics drivers
- Check Windows display scaling (should be 100% or 125%)

---

## Import Problems

### Can't Import Video Files

**Problem:** File browser doesn't accept your video

**Solution 1: Check Format**
Supported: MP4, AVI, MOV, MKV, WMV, FLV, WebM

Not supported: Other formats

**Solution 2: Convert Video**
- Use free tool like VLC or HandBrake
- Convert to MP4
- Try importing again

**Solution 3: File Size**
- Very large files (>2GB) may cause issues
- Split into smaller segments first
- Or use video compression tool

**Solution 4: Check File Integrity**
- Try playing the video in Windows Media Player
- If it won't play, file might be corrupted
- Re-export or re-download video

---

### File Format Not Supported

**Problem:** Error says format not supported

**Solution:**
1. Check file extension (right-click → Properties)
2. If unsupported:
   - Use VLC Media Player to convert
   - File → Convert/Stream
   - Choose MP4 H.264
   - Save and use new file

**Common Conversions:**
- .flv → .mp4
- .webm → .mp4
- .mpeg → .mp4
- .3gp → .mp4

---

### Files Don't Appear in Timeline

**Problem:** Import seems successful but timeline is empty

**Solution 1: Check Timeline Panel**
- Look at bottom of window
- Scroll if necessary
- Files listed as text, not thumbnails

**Solution 2: Import Again**
1. Click Import button again
2. Select same files
3. Check if duplicates appear

**Solution 3: Check File Path**
- Files must exist on your computer
- Can't import from CD, USB that's been removed
- Move files to hard drive first

**Solution 4: Restart Application**
1. Close video editor
2. Relaunch
3. Try importing again

---

### Import Button Doesn't Work

**Problem:** Clicking import does nothing

**Solution 1: Wait**
- Give it 2-3 seconds
- Button may have delay

**Solution 2: Check Active Window**
- File browser might have opened behind main window
- Click on taskbar to find it
- Or Alt+Tab to switch windows

**Solution 3: Restart Application**
- Close and reopen
- Try again

---

## Export Problems

### Export Fails Immediately

**Problem:** Export button clicked but nothing happens or immediate error

**Solution 1: Check Timeline**
- Timeline must have at least one clip
- Import something first

**Solution 2: Check Disk Space**
- Need space for output video
- Check: Right-click C: drive → Properties
- Free up space if needed

**Solution 3: Output Location**
- Don't export to USB that's full
- Don't export to network drive (slow)
- Export to local hard drive (C:)

**Solution 4: File Permissions**
- Can't export to system folders
- Choose Documents or Desktop
- Create a specific folder for exports

---

### Export Takes Forever

**Problem:** Export is extremely slow

**Normal export times:**
- 1 min video: 2-5 min export
- 5 min video: 10-25 min export
- 10 min video: 20-50 min export

**If much slower:**

**Solution 1: Close Other Programs**
- Close browsers (especially Chrome)
- Close Office apps
- Close other video software
- Keep only video editor running

**Solution 2: Lower Quality**
- Use "Medium" instead of "High"
- Or "Low" for fastest export
- Quality difference often minimal

**Solution 3: Check CPU Usage**
1. Open Task Manager (Ctrl+Shift+Esc)
2. Look at CPU %
3. If 100%, something else is using CPU
4. Close that program

**Solution 4: Computer Specs**
- Old/slow computer takes longer
- Consider upgrading if regular user
- Or accept longer export times

**Solution 5: Break Into Parts**
- Export smaller segments
- Combine later if needed

---

### Export Crashes Partway

**Problem:** Export starts but fails before completion

**Solution 1: Check Disk Space**
- May run out during export
- Need at least 2x expected file size
- Free up space and try again

**Solution 2: Check Memory**
- Large videos need lots of RAM
- Close everything else
- Restart computer
- Try export again fresh

**Solution 3: Lower Quality**
- Try "Medium" or "Low"
- Uses less memory
- More stable

**Solution 4: Corrupted Source File**
- One of your videos might be damaged
- Export without suspicious files
- Narrow down which one causes problem

**Solution 5: Export to Different Location**
- External drive might have issues
- Try exporting to C:\Temp
- Move file after successful export

---

### Can't Find Exported Video

**Problem:** Export says successful but can't find the file

**Solution 1: Check Export Location**
- Note where you saved it during export
- Common locations:
  - Documents
  - Desktop
  - Downloads
  - Videos folder

**Solution 2: Search Windows**
1. Press Windows key
2. Type the filename
3. Check search results

**Solution 3: Check Recent Files**
- Open File Explorer
- Look in "Quick Access"
- Check "Recent files"

**Solution 4: Export Again**
- Choose export location carefully
- Write down the location
- Watch where save dialog points

---

### Exported Video Won't Play

**Problem:** Exported MP4 won't open or play

**Solution 1: Use Different Player**
- Try VLC Media Player (free)
- Windows Media Player might not work with all codecs
- Download VLC from videolan.org

**Solution 2: Check File Size**
- Right-click file → Properties
- If 0 bytes, export failed
- If suspiciously small, incomplete export

**Solution 3: Re-export**
- Try exporting again
- Use different quality setting
- Save to different location

**Solution 4: Format Choice**
- If MP4 doesn't work, try AVI
- AVI has broader compatibility
- Larger file but more reliable

---

### Poor Quality After Export

**Problem:** Video looks bad after exporting

**Solution 1: Check Quality Setting**
- Use "High" for best quality
- Medium is good for most uses
- Low is only for quick previews

**Solution 2: Source Quality**
- Output quality ≤ input quality
- If source is low quality, output will be too
- Use high-quality source videos

**Solution 3: Compression Artifacts**
- Normal for Medium/Low quality
- Use High quality if quality crucial
- Accept slightly larger file size

**Solution 4: Player Issues**
- Some players compress playback
- Try VLC Media Player
- Compare with source video

---

## Project Problems

### Can't Save Project

**Problem:** Save project doesn't work or gives error

**Solution 1: Check Permissions**
- Save to Documents (not system folders)
- Don't save to Program Files
- Choose location you have write access to

**Solution 2: File Name Issues**
- Don't use special characters: <>:"/\|?*
- Use simple names: "Project1", "Training_Video"
- Avoid very long filenames

**Solution 3: Disk Space**
- Project files are small (few KB)
- But need some space
- Check disk space

**Solution 4: Create Folder First**
- Make a "VideoProjects" folder
- In Documents
- Save all projects there

---

### Can't Load Project

**Problem:** Load project fails or gives error

**Solution 1: Check File Extension**
- Must be .vedproj file
- Not .txt or other format

**Solution 2: File Corruption**
- Project file might be damaged
- Try opening in Notepad
- Should see JSON text
- If gibberish, file is corrupt

**Solution 3: Version Mismatch**
- Old project from different version
- Usually still works
- May need to recreate if very old

---

### Missing Media Files Error

**Problem:** "Cannot find media file" when loading project

**Cause:** Original video/image/audio files were moved or deleted

**Solution 1: Find Original Files**
- Locate the original files
- Move them back to original location
- OR see Solution 2

**Solution 2: Re-import Files**
1. Note the error messages (which files missing)
2. Close error dialogs
3. Import the files again
4. Save project

**Solution 3: Update Project File (Advanced)**
1. Open .vedproj in Notepad
2. Find file paths
3. Update to new locations
4. Save
5. Load in video editor

**Prevention:**
- Never move files after importing
- Keep organized structure
- Back up everything together

---

## Performance Problems

### Application is Slow

**Problem:** Interface is laggy or unresponsive

**Solution 1: Close Other Programs**
- Browser tabs (especially Chrome)
- Other video software
- Office applications

**Solution 2: Restart Application**
- Close video editor
- Relaunch fresh

**Solution 3: Restart Computer**
- Clears memory
- Fresh start

**Solution 4: Check System Resources**
1. Task Manager (Ctrl+Shift+Esc)
2. Performance tab
3. Check:
   - CPU usage (should be <80%)
   - Memory (should have >2GB free)
   - Disk (should not be 100%)

**Solution 5: Upgrade Hardware**
- Add more RAM (8GB minimum)
- Use SSD instead of hard drive
- Faster CPU helps exports

---

### Computer Freezes During Export

**Problem:** Entire computer becomes unresponsive

**Solution 1: Don't Panic**
- Wait 5-10 minutes
- Export is CPU-intensive
- May seem frozen but working

**Solution 2: Check If Responding**
- Press Caps Lock key
- If keyboard light toggles, system alive
- If not, truly frozen

**Solution 3: Force Quit (If Necessary)**
1. Ctrl+Alt+Delete
2. Task Manager
3. Find Python process
4. End Task

**Solution 4: Prevent Freezing**
- Close all other programs first
- Don't use computer during export
- Run overnight for large exports
- Use Lower quality setting

---

### High CPU Usage

**Problem:** CPU constantly at 100%

**During Export:**
- This is NORMAL
- Video processing is CPU-intensive
- Computer may be slow during export
- Be patient, let it finish

**At Other Times:**
**Solution 1: Check Task Manager**
- What's using CPU?
- If not Python/video editor, close that program

**Solution 2: Background Processes**
- Windows Update downloading?
- Antivirus scanning?
- Let it finish, then use editor

---

### Out of Memory Errors

**Problem:** "Memory error" or application crashes

**Solution 1: Close Other Programs**
- Especially browsers
- Restart computer for fresh start

**Solution 2: Export in Parts**
- Split long video into segments
- Export separately
- Combine later if needed

**Solution 3: Lower Quality**
- Uses less RAM
- High quality needs more memory

**Solution 4: Add RAM**
- 8GB minimum recommended
- 16GB better for large projects
- Consider hardware upgrade

---

## Getting More Help

### Check Log File

**Location:** `video_editor.log` in application folder

**How to read:**
1. Open with Notepad
2. Scroll to bottom
3. Look for lines with "ERROR"
4. Note the error message

**What to look for:**
- Import errors: Missing dependencies
- File errors: Permission or path issues
- Memory errors: Need more RAM or close programs

---

### Documentation Resources

1. `INSTALLATION_TRAINING.md` - Installation help
2. `USAGE_TRAINING.md` - How to use
3. `FAQ.md` - Common questions
4. `USER_GUIDE.md` - Complete manual
5. `DEVELOPER_NOTES.md` - Technical details

---

### Before Asking for Help

Gather this information:
1. What were you doing when problem occurred?
2. What error message appeared (exact text)?
3. What's in video_editor.log (last 10 lines)?
4. Windows version?
5. Python version? (`python --version`)
6. When did problem start?

---

## Prevention Tips

Avoid problems by following these practices:

**File Organization:**
✓ Organize files before importing
✓ Keep files in stable location
✓ Don't move files after importing
✓ Back up regularly

**Project Management:**
✓ Save frequently (every 5 minutes)
✓ Use descriptive project names
✓ Keep projects in one folder
✓ Test export before final version

**System Maintenance:**
✓ Keep Windows updated
✓ Update graphics drivers
✓ Maintain free disk space (10GB+)
✓ Close unnecessary programs

**Best Practices:**
✓ Test with small videos first
✓ Export preview before final
✓ Use Medium quality for most uses
✓ Plan before starting to edit

---

**Last Updated:** February 2026

This guide covers the most common issues. If your problem isn't listed, check the other documentation or the log file for more specific error information.
