# Installation Training Guide

Complete step-by-step guide for installing the Video Editor application on Windows.

## Prerequisites Check

Before starting, verify:
- [ ] You have a Windows 10 or Windows 11 computer
- [ ] You have administrator access (for installation)
- [ ] You have stable internet connection
- [ ] You have at least 1 GB free disk space

## Training Objective

By the end of this training, you will:
1. Have Python installed on your computer
2. Have the Video Editor application installed and ready to use
3. Know how to launch the application
4. Understand basic troubleshooting steps

**Estimated Time:** 15-20 minutes

---

## Part 1: Installing Python (8-10 minutes)

### Why Do We Need Python?

Python is a programming language that our video editor is built with. Think of it like Microsoft Word needs Windows to run - our video editor needs Python to run.

### Step-by-Step Instructions

#### Step 1: Download Python

1. **Open your web browser** (Chrome, Edge, or Firefox)

2. **Visit the Python website:**
   - Type in the address bar: `https://www.python.org/downloads/`
   - Press Enter

3. **On the Python website:**
   - You'll see a big yellow button that says "Download Python 3.x.x"
   - Click this button
   - The file will start downloading (it's about 25-30 MB)

4. **Wait for download:**
   - Watch the bottom of your browser for the download to complete
   - Usually takes 1-2 minutes depending on your internet speed

**✓ Checkpoint:** You should now have a file named something like `python-3.x.x.exe` in your Downloads folder.

---

#### Step 2: Run the Python Installer

1. **Find the downloaded file:**
   - Open your **Downloads** folder
   - Look for `python-3.x.x.exe`
   - Double-click it to start installation

2. **VERY IMPORTANT - First Screen:**
   ```
   ┌─────────────────────────────────────────┐
   │  Install Python 3.x.x                   │
   │                                         │
   │  ☑ Add Python to PATH  ← CHECK THIS!  │
   │                                         │
   │  [Install Now]                          │
   │  [Customize installation]               │
   └─────────────────────────────────────────┘
   ```
   
   - **MUST DO:** Click the checkbox next to "Add Python to PATH"
   - This is the MOST IMPORTANT step!
   - Without this, the video editor won't work

3. **Click "Install Now":**
   - You may see a security warning asking "Do you want to allow this app to make changes?"
   - Click **Yes**

4. **Wait for installation:**
   - You'll see a progress bar
   - This takes 3-5 minutes
   - Do NOT close the window

5. **Success screen:**
   - When done, you'll see "Setup was successful"
   - Click **Close**

**✓ Checkpoint:** Python is now installed on your computer!

---

#### Step 3: Verify Python Installation

Let's make sure Python installed correctly:

1. **Open Command Prompt:**
   - Click the Windows Start button (bottom-left corner)
   - Type: `cmd`
   - Press Enter

2. **Test Python:**
   - In the black window that opens, type: `python --version`
   - Press Enter
   - You should see: `Python 3.x.x`

3. **If it works:**
   - Great! Python is installed correctly
   - You can close the black window

4. **If you see an error:**
   - "python is not recognized..." means you forgot to check "Add Python to PATH"
   - Don't worry! Go to the Troubleshooting section below

**✓ Checkpoint:** You can verify Python is working from the command line.

---

## Part 2: Installing Video Editor (7-10 minutes)

### What We're Doing

Now we'll install all the extra software (called "dependencies") that the video editor needs to work with videos and images.

### Step-by-Step Instructions

#### Step 1: Locate the Video Editor Folder

1. **Find where you saved the video editor:**
   - Recommended location: `C:\VideoEditor`
   - Or wherever you extracted/downloaded the folder

2. **Open the folder:**
   - You should see files like:
     - `install.bat`
     - `run_editor.bat`
     - `main.py`
     - `requirements.txt`
     - A folder called `src`

**✓ Checkpoint:** You can see the video editor files in a folder.

---

#### Step 2: Run the Installation Script

1. **Find install.bat:**
   - Look for a file called `install.bat`
   - It has a gear icon ⚙️

2. **Double-click install.bat:**
   - A black window will open
   - You'll see text appearing

3. **What you'll see:**
   ```
   ================================================
   Video Editor - Installation Script
   ================================================
   
   Python found! Checking version...
   Python 3.x.x
   
   Creating virtual environment...
   Activating virtual environment...
   Installing dependencies...
   ```

4. **Wait patiently:**
   - Installation takes 5-10 minutes
   - You'll see lots of text scrolling
   - This is normal!
   - DON'T close the window

5. **Watch for success:**
   ```
   ================================================
   Installation Complete!
   ================================================
   
   To run the video editor:
   1. Double-click run_editor.bat
   ```

6. **When done:**
   - Press any key to close the window
   - Or it will close automatically

**✓ Checkpoint:** Installation completed successfully!

---

#### Step 3: Verify Installation

Let's make sure everything installed correctly:

1. **Check for new folder:**
   - In your video editor folder
   - You should now see a folder called `venv`
   - This contains all the installed software

2. **Size check:**
   - Your video editor folder should now be about 500 MB
   - The `venv` folder contains most of this

**✓ Checkpoint:** The venv folder exists and installation is complete.

---

## Part 3: First Launch (2 minutes)

### Running the Video Editor

1. **Find run_editor.bat:**
   - In your video editor folder
   - Double-click `run_editor.bat`

2. **Wait a few seconds:**
   - A black window appears briefly
   - Then the Video Editor window opens

3. **Success!**
   - You should see the video editor interface:
     - Toolbar at the top
     - Preview area on the left
     - Timeline at the bottom
     - Properties panel on the right

4. **First launch:**
   - First time may take 10-15 seconds
   - Later launches will be faster

**✓ Checkpoint:** The Video Editor application is running!

---

## Troubleshooting Common Issues

### Issue 1: "Python is not recognized..."

**Problem:** When running `install.bat`, you see:
```
'python' is not recognized as an internal or external command
```

**Solution:**
1. You forgot to check "Add Python to PATH" during Python installation
2. Fix by reinstalling Python:
   - Go to Add/Remove Programs
   - Find "Python 3.x"
   - Click "Modify"
   - Choose "Modify" again
   - Check "Add Python to environment variables"
   - Click "Install"

**OR:**
1. Uninstall Python completely
2. Reinstall and make sure to check "Add Python to PATH"

---

### Issue 2: Installation Hangs or Freezes

**Problem:** The installation script stops and nothing happens

**Solution:**
1. Close the window (X button)
2. Check your internet connection
3. Try running `install.bat` again
4. If it fails again:
   - Right-click `install.bat`
   - Choose "Run as administrator"
   - Try again

---

### Issue 3: "Access Denied" Errors

**Problem:** You see permission errors during installation

**Solution:**
1. Close the installation window
2. Right-click `install.bat`
3. Choose "Run as administrator"
4. Click "Yes" when asked

---

### Issue 4: Application Won't Launch

**Problem:** Double-clicking `run_editor.bat` does nothing or window closes immediately

**Solution 1 - Check installation:**
1. Look for `venv` folder in video editor directory
2. If missing, run `install.bat` again

**Solution 2 - Check for errors:**
1. Open the video editor folder
2. Look for `video_editor.log` file
3. Open it with Notepad
4. Look at the last few lines for error messages

**Solution 3 - Reinstall:**
1. Delete the `venv` folder
2. Run `install.bat` again

---

### Issue 5: "Module Not Found" Errors

**Problem:** Error message about missing modules

**Solution:**
1. The installation didn't complete properly
2. Delete the `venv` folder
3. Run `install.bat` again
4. Make sure your internet connection is stable

---

## Testing Your Installation

### Quick Test Checklist

After installation, verify everything works:

- [ ] **Python Test:**
  - Open Command Prompt
  - Type: `python --version`
  - Should show Python 3.8 or higher

- [ ] **Installation Test:**
  - `venv` folder exists in video editor directory
  - Folder is about 500 MB

- [ ] **Launch Test:**
  - Double-click `run_editor.bat`
  - Application window opens
  - No error messages

- [ ] **Interface Test:**
  - You can see all panels (toolbar, preview, timeline, properties)
  - Buttons are clickable

---

## Next Steps

Congratulations! You've successfully installed the Video Editor.

**What to do next:**
1. Read `USAGE_TRAINING.md` to learn how to use the editor
2. Try the exercises in `TRAINING_EXERCISES.md`
3. Create your first video!

**Keep this guide:**
- Bookmark this page for future reference
- If you need to install on another computer, follow these steps again

---

## Installation Summary

### What You Installed:

1. **Python 3.x**
   - The programming language
   - About 30 MB

2. **Video Editor Dependencies:**
   - CustomTkinter (interface)
   - MoviePy (video processing)
   - Pillow (image handling)
   - And 4 other supporting libraries
   - Total: About 500 MB

3. **Video Editor Application:**
   - The main program files
   - About 5 MB

**Total Space Used:** Approximately 535 MB

---

## Support Resources

If you still have problems:

1. **Check the log file:**
   - `video_editor.log` in the application folder
   - Contains detailed error information

2. **Read other guides:**
   - `README.md` - Overview
   - `QUICK_START.md` - Quick reference
   - `USER_GUIDE.md` - Complete manual
   - `TROUBLESHOOTING_GUIDE.md` - More solutions

3. **Common file locations:**
   - Application: Where you extracted it (e.g., `C:\VideoEditor`)
   - Python: Usually `C:\Users\[YourName]\AppData\Local\Programs\Python`
   - Virtual environment: `[VideoEditor]\venv`

---

## Installation Complete! ✅

You're now ready to start creating videos!

**Time to celebrate! 🎉**

Proceed to `USAGE_TRAINING.md` to learn how to use your new video editor.
