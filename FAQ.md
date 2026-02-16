# Frequently Asked Questions (FAQ)

Common questions and answers about the Video Editor application.

## Installation Questions

### Q1: Do I need programming knowledge to use this software?

**A:** No! The video editor is designed for non-programmers. You just click buttons and import files. No coding required.

---

### Q2: Why do I need to install Python?

**A:** Python is the "engine" that runs the video editor, like Windows is needed to run other programs. You install it once and then forget about it.

---

### Q3: How much disk space do I need?

**A:** 
- Python: ~30 MB
- Video Editor dependencies: ~500 MB
- Total for installation: ~535 MB
- Plus space for your videos (varies)

**Recommendation:** Have at least 2-3 GB free for comfortable use.

---

### Q4: What if I forgot to check "Add Python to PATH"?

**A:** You have two options:
1. Modify the Python installation (Add/Remove Programs → Python → Modify)
2. Uninstall Python completely and reinstall with the checkbox checked

See `INSTALLATION_TRAINING.md` for detailed steps.

---

### Q5: Can I install this on multiple computers?

**A:** Yes! Follow the installation steps on each computer. The software is free (MIT License).

---

### Q6: How long does installation take?

**A:**
- Python installation: 3-5 minutes
- Video Editor installation: 5-10 minutes
- **Total: 10-15 minutes**

---

## Usage Questions

### Q7: What video formats can I import?

**A:** Supported input formats:
- **Video:** MP4, AVI, MOV, MKV, WMV, FLV, WebM
- **Image:** JPG, JPEG, PNG, BMP, GIF, TIFF
- **Audio:** MP3, WAV, AAC, OGG, M4A, FLAC

**Recommendation:** Use MP4 for videos and JPG/PNG for images.

---

### Q8: What format should I export to?

**A:** Use **MP4** for almost everything:
- Works on all devices
- Good quality
- Reasonable file size
- Compatible with YouTube, Vimeo, etc.

Use AVI only if you need maximum quality for further editing.

---

### Q9: How long does video export take?

**A:** Approximate times (varies by computer):
- 1 minute video: 2-5 minutes
- 5 minute video: 10-25 minutes
- 10 minute video: 20-50 minutes

**Factors affecting speed:**
- Your computer's CPU speed
- Quality setting chosen (High takes longer)
- Video complexity
- Other programs running

---

### Q10: Can I edit the video like cutting specific parts?

**A:** Currently, the editor focuses on concatenating (joining) clips in sequence. For precise cutting:
1. Trim your videos before importing (using another tool)
2. Import only the parts you want
3. Arrange them in order

**Note:** Frame-level trimming features are in the underlying code but not yet in the GUI.

---

### Q11: How do I reorder clips?

**A:** Currently, clips play in the order you import them:
- First imported = plays first
- Second imported = plays second
- etc.

**Workaround:** Plan your order before importing, or re-import in the desired order.

---

### Q12: Can I add text to my videos?

**A:** The text overlay functionality is built into the code but not yet exposed in the GUI. Future versions will have a text button.

**Current workaround:** Create images with text using PowerPoint or Paint, then import as image clips.

---

### Q13: How do I add background music?

**A:** Import an audio file:
1. Click "Import Audio"
2. Select your music file (MP3 recommended)
3. The audio will play alongside your video

**Note:** Audio and video start at the same time and play together.

---

## File Management Questions

### Q14: Where should I save my projects?

**A:** Recommended structure:
```
My Documents/
├── VideoProjects/         ← Save .vedproj files here
├── RawMedia/             ← Keep original files here
│   ├── Videos/
│   ├── Images/
│   └── Audio/
└── ExportedVideos/       ← Save final MP4s here
```

---

### Q15: What is a .vedproj file?

**A:** It's your project file that contains:
- List of media files used
- Their order
- Export settings

**Important:** It does NOT contain the actual videos/images, just references to them.

---

### Q16: Can I move my media files after importing?

**A:** ⚠️ **NO!** If you move or rename files after importing:
- The project won't be able to find them
- You'll need to re-import them

**Best practice:** Organize files BEFORE importing, then don't move them.

---

### Q17: Can I delete a clip from the timeline?

**A:** Not directly in the current GUI. Workarounds:
1. Save your project with a new name
2. Manually edit the .vedproj file (for advanced users)
3. Start a new project without that clip

**Note:** Future versions will have a delete button.

---

## Technical Questions

### Q18: My computer is slow, will this work?

**A:** Minimum requirements:
- Windows 10 or 11
- 4 GB RAM (8 GB better)
- 2 GB free disk space

**If slow:**
- Close other programs while exporting
- Use "Low" or "Medium" quality
- Export smaller videos (break into parts)
- Consider upgrading RAM

---

### Q19: Does it work on Mac or Linux?

**A:** Currently optimized for **Windows only**.

The code uses Python which is cross-platform, but:
- Installation scripts are Windows batch files
- Tested only on Windows
- Some paths assume Windows structure

Mac/Linux versions would need adaptation.

---

### Q20: Can I use this commercially?

**A:** Yes! The software has an MIT License, which means:
- ✅ Free for commercial use
- ✅ Free to modify
- ✅ Free to distribute
- ✅ No restrictions

---

### Q21: Where are the video effects?

**A:** Basic effects (fade in/out, crossfade) are built into the code but not yet in the GUI. Current version focuses on basic concatenation.

**Future versions** will expose these in the interface.

---

## Troubleshooting Questions

### Q22: The application won't start - what do I do?

**A:** Check these steps:
1. Verify `venv` folder exists in the video editor directory
2. Try running `install.bat` again
3. Check `video_editor.log` for error messages
4. Right-click `run_editor.bat` and "Run as administrator"

See `TROUBLESHOOTING_GUIDE.md` for detailed solutions.

---

### Q23: I get "Module not found" errors

**A:** This means installation didn't complete:
1. Delete the `venv` folder
2. Make sure you have stable internet
3. Run `install.bat` again
4. Wait for "Installation Complete!" message

---

### Q24: Export fails or crashes

**A:** Try these solutions:
1. Use a lower quality preset
2. Close other programs
3. Check you have enough disk space
4. Try exporting to a different location
5. Break your video into smaller parts

---

### Q25: Where can I find error messages?

**A:** Check the log file:
- Location: `video_editor.log` in the application folder
- Open with: Notepad
- Look at: Last 10-20 lines

The log shows detailed error information.

---

## Project Management Questions

### Q26: How often should I save my project?

**A:** Save frequently!
- After importing all media
- Every 5-10 minutes
- Before exporting
- Before closing the application

**Tip:** Click "Save Project" whenever you make changes.

---

### Q27: Can I work on multiple projects?

**A:** Yes!
1. Each project is a separate .vedproj file
2. Save each with a different name
3. Load whichever one you want to work on

**Tip:** Use descriptive names like "Training_Video_Part1.vedproj"

---

### Q28: Can I share my project with someone else?

**A:** Yes, but with caution:
1. Give them the .vedproj file
2. **AND** give them ALL the media files
3. Keep the same folder structure
4. OR have them adjust file paths

**Better:** Just share the exported video file (MP4).

---

## Quality and Size Questions

### Q29: Which quality should I use?

**A:** 
- **High (1080p):** Final professional videos, YouTube uploads
- **Medium (720p):** 90% of uses, good balance ✓ Recommended
- **Low (480p):** Email attachments, quick previews

**When in doubt, use Medium!**

---

### Q30: Why is my exported file so large?

**A:** Video files are naturally large:
- High quality: ~60 MB per minute
- Medium quality: ~30 MB per minute
- Low quality: ~15 MB per minute

**To reduce size:**
- Use Medium or Low quality
- Shorten the video duration
- Use MP4 format (not AVI)

---

### Q31: The quality looks bad after export

**A:** Check these factors:
1. Source video quality (low quality in = low quality out)
2. Export quality setting (use High if needed)
3. Viewing method (some players compress)
4. Comparison fairness (comparing to original?)

**Tip:** High quality should look nearly identical to original.

---

## Update and Support Questions

### Q32: How do I update to a new version?

**A:** When a new version is released:
1. Download the new version
2. Extract to a new folder (or replace old folder)
3. Run `install.bat` again
4. Your projects (.vedproj files) will still work

---

### Q33: Where can I get help?

**A:** Resources available:
1. `INSTALLATION_TRAINING.md` - Installation help
2. `USAGE_TRAINING.md` - Usage help
3. `USER_GUIDE.md` - Complete manual
4. `TROUBLESHOOTING_GUIDE.md` - Problem solving
5. `DEVELOPER_NOTES.md` - Technical details
6. `video_editor.log` - Error details

---

### Q34: Can I request new features?

**A:** Yes! The software is open source. Feature requests can be submitted through the project's GitHub repository.

Popular requested features:
- Direct timeline editing
- Trim controls in GUI
- Text overlay button
- Clip reordering
- Undo/redo
- Real-time preview

---

### Q35: Is there a user community?

**A:** Currently, the software is designed for Insoil training video creation. Check with your organization for internal support or user groups.

---

## Best Practices Questions

### Q36: What's the best workflow?

**A:** Recommended workflow:
1. **Plan:** Script and organize (30 min)
2. **Gather:** Collect all media (30 min)
3. **Edit:** Import and arrange (20 min)
4. **Review:** Export and watch (20 min)
5. **Finalize:** Make changes and final export (20 min)

**Total:** About 2 hours for a 3-5 minute video.

---

### Q37: How do I make better training videos?

**A:** Tips for quality:
- **Keep it short:** 3-5 minutes ideal
- **One topic:** Don't try to cover everything
- **Good audio:** Clear narration is crucial
- **Steady camera:** Use tripod for recordings
- **Good lighting:** Film in well-lit areas
- **Test:** Show to someone before final version

---

### Q38: Should I use images or videos?

**A:** Guidelines:
- **Use video for:** Demonstrations, processes, movement
- **Use images for:** Diagrams, charts, text slides, highlights

**Tip:** Mix both! Use images to emphasize key points between video clips.

---

### Q39: How long should images show?

**A:** Default is 5 seconds:
- Too short: < 3 seconds (hard to read)
- Good: 5-8 seconds (current default)
- Too long: > 15 seconds (boring)

**Tip:** Time yourself reading the image out loud. Add 2 seconds to that.

---

### Q40: What mistakes should I avoid?

**A:** Common mistakes:
- ❌ Moving files after importing
- ❌ Not saving projects frequently
- ❌ Forgetting where you saved things
- ❌ Using very large video files (>2GB)
- ❌ Not testing before final export
- ❌ Mixing very different resolutions

**Do instead:**
- ✅ Organize files first, then don't move them
- ✅ Save every 5 minutes
- ✅ Use consistent folder structure
- ✅ Keep videos under 2GB each
- ✅ Export test versions first
- ✅ Use consistent video resolution

---

## Quick Reference

### Essential File Locations

```
Video Editor Installation:
└─ C:\VideoEditor\                    ← Installation folder
   ├─ run_editor.bat                  ← Double-click to start
   ├─ install.bat                     ← Used once for installation
   ├─ video_editor.log                ← Check for errors
   └─ venv\                           ← Python environment (don't touch)

Your Files:
└─ My Documents\
   ├─ VideoProjects\                  ← Save .vedproj here
   ├─ RawMedia\                       ← Keep originals here
   └─ ExportedVideos\                 ← Save MP4s here
```

### Quick Answers

| Question | Quick Answer |
|----------|--------------|
| Installation time? | 10-15 minutes |
| Programming needed? | No! |
| Best export format? | MP4 |
| Best quality? | Medium |
| File size for 5 min? | ~150 MB (Medium) |
| Export time for 5 min? | ~15 minutes |
| Save how often? | Every 5 minutes |
| Can move files? | No! Keep organized first |
| Works on Mac? | No, Windows only |
| Free to use? | Yes! MIT License |

---

## Still Have Questions?

1. **Check other documentation:**
   - Installation issues → `INSTALLATION_TRAINING.md`
   - Usage questions → `USAGE_TRAINING.md`
   - Technical details → `DEVELOPER_NOTES.md`
   - Problems → `TROUBLESHOOTING_GUIDE.md`

2. **Check the log file:**
   - `video_editor.log` in application folder
   - Contains detailed error information

3. **Try the exercises:**
   - `TRAINING_EXERCISES.md` has hands-on practice

4. **Read the code comments:**
   - All code is well-documented
   - See `src/` folder for implementation details

---

**Updated:** February 2026
**Version:** 1.0.0

This FAQ is regularly updated based on common user questions. If your question isn't here, check the other documentation files!
