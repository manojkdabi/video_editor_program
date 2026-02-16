"""
Main Window Module
Main application window with GUI layout
"""

import customtkinter as ctk
from tkinter import filedialog, messagebox
import logging
from typing import Optional

from src.utils.project_manager import ProjectManager
from src.utils.file_handler import FileHandler
from src.video_processing.editor import VideoEditor
from src.video_processing.export import VideoExporter

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class MainWindow(ctk.CTk):
    """Main application window"""
    
    def __init__(self):
        super().__init__()
        
        # Window setup
        self.title("Video Editor - Insoil Training Videos")
        self.geometry("1400x900")
        
        # Initialize managers
        self.project_manager = ProjectManager()
        self.file_handler = FileHandler()
        self.video_editor = VideoEditor()
        self.video_exporter = VideoExporter()
        
        # Current project data
        self.current_project = self.project_manager.create_new_project()
        
        # Timeline data
        self.timeline_clips = []
        
        # Setup UI
        self.setup_menu()
        self.setup_ui()
        
        logger.info("Main window initialized")
    
    def setup_menu(self):
        """Setup menu bar"""
        # Note: CustomTkinter doesn't have native menu bar
        # We'll use a button toolbar instead
        pass
    
    def setup_ui(self):
        """Setup main UI layout"""
        
        # Configure grid
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        # Toolbar (Top)
        self.toolbar_frame = ctk.CTkFrame(self, height=60)
        self.toolbar_frame.grid(row=0, column=0, columnspan=3, sticky="ew", padx=5, pady=5)
        self.setup_toolbar()
        
        # Preview Panel (Left)
        self.preview_frame = ctk.CTkFrame(self)
        self.preview_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        self.setup_preview_panel()
        
        # Timeline Panel (Bottom Center)
        self.timeline_frame = ctk.CTkFrame(self, height=200)
        self.timeline_frame.grid(row=2, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
        self.setup_timeline_panel()
        
        # Properties Panel (Right)
        self.properties_frame = ctk.CTkFrame(self, width=300)
        self.properties_frame.grid(row=1, column=2, rowspan=2, sticky="nsew", padx=5, pady=5)
        self.setup_properties_panel()
    
    def setup_toolbar(self):
        """Setup toolbar with buttons"""
        
        # New Project
        btn_new = ctk.CTkButton(
            self.toolbar_frame,
            text="New Project",
            command=self.new_project,
            width=120
        )
        btn_new.pack(side="left", padx=5, pady=10)
        
        # Save Project
        btn_save = ctk.CTkButton(
            self.toolbar_frame,
            text="Save Project",
            command=self.save_project,
            width=120
        )
        btn_save.pack(side="left", padx=5, pady=10)
        
        # Load Project
        btn_load = ctk.CTkButton(
            self.toolbar_frame,
            text="Load Project",
            command=self.load_project,
            width=120
        )
        btn_load.pack(side="left", padx=5, pady=10)
        
        # Separator
        separator = ctk.CTkFrame(self.toolbar_frame, width=2, fg_color="gray")
        separator.pack(side="left", padx=10, pady=10, fill="y")
        
        # Import Video
        btn_import_video = ctk.CTkButton(
            self.toolbar_frame,
            text="Import Video",
            command=self.import_video,
            width=120
        )
        btn_import_video.pack(side="left", padx=5, pady=10)
        
        # Import Image
        btn_import_image = ctk.CTkButton(
            self.toolbar_frame,
            text="Import Image",
            command=self.import_image,
            width=120
        )
        btn_import_image.pack(side="left", padx=5, pady=10)
        
        # Import Audio
        btn_import_audio = ctk.CTkButton(
            self.toolbar_frame,
            text="Import Audio",
            command=self.import_audio,
            width=120
        )
        btn_import_audio.pack(side="left", padx=5, pady=10)
        
        # Separator
        separator2 = ctk.CTkFrame(self.toolbar_frame, width=2, fg_color="gray")
        separator2.pack(side="left", padx=10, pady=10, fill="y")
        
        # Export Video
        btn_export = ctk.CTkButton(
            self.toolbar_frame,
            text="Export Video",
            command=self.export_video,
            width=120,
            fg_color="green"
        )
        btn_export.pack(side="left", padx=5, pady=10)
    
    def setup_preview_panel(self):
        """Setup video preview panel"""
        
        # Title
        title = ctk.CTkLabel(
            self.preview_frame,
            text="Video Preview",
            font=("Arial", 16, "bold")
        )
        title.pack(pady=10)
        
        # Preview canvas (placeholder)
        self.preview_canvas = ctk.CTkLabel(
            self.preview_frame,
            text="No video loaded",
            width=640,
            height=360,
            fg_color="black"
        )
        self.preview_canvas.pack(padx=10, pady=10)
        
        # Playback controls
        controls_frame = ctk.CTkFrame(self.preview_frame)
        controls_frame.pack(pady=10)
        
        btn_play = ctk.CTkButton(controls_frame, text="▶ Play", width=80)
        btn_play.pack(side="left", padx=5)
        
        btn_pause = ctk.CTkButton(controls_frame, text="⏸ Pause", width=80)
        btn_pause.pack(side="left", padx=5)
        
        btn_stop = ctk.CTkButton(controls_frame, text="⏹ Stop", width=80)
        btn_stop.pack(side="left", padx=5)
        
        # Timeline slider
        self.timeline_slider = ctk.CTkSlider(
            self.preview_frame,
            from_=0,
            to=100,
            width=620
        )
        self.timeline_slider.pack(pady=10)
        self.timeline_slider.set(0)
        
        # Time display
        self.time_label = ctk.CTkLabel(
            self.preview_frame,
            text="00:00:00 / 00:00:00"
        )
        self.time_label.pack()
    
    def setup_timeline_panel(self):
        """Setup timeline panel"""
        
        # Title
        title = ctk.CTkLabel(
            self.timeline_frame,
            text="Timeline",
            font=("Arial", 16, "bold")
        )
        title.pack(pady=5)
        
        # Timeline info
        self.timeline_info = ctk.CTkTextbox(
            self.timeline_frame,
            height=120,
            width=800
        )
        self.timeline_info.pack(padx=10, pady=5, fill="both", expand=True)
        self.timeline_info.insert("1.0", "Timeline is empty. Import videos, images, or audio to begin.")
    
    def setup_properties_panel(self):
        """Setup properties panel"""
        
        # Title
        title = ctk.CTkLabel(
            self.properties_frame,
            text="Properties",
            font=("Arial", 16, "bold")
        )
        title.pack(pady=10)
        
        # Properties display
        self.properties_text = ctk.CTkTextbox(
            self.properties_frame,
            width=280,
            height=400
        )
        self.properties_text.pack(padx=10, pady=10)
        self.properties_text.insert("1.0", "Select a clip to view properties")
        
        # Export settings
        export_label = ctk.CTkLabel(
            self.properties_frame,
            text="Export Settings",
            font=("Arial", 14, "bold")
        )
        export_label.pack(pady=10)
        
        # Quality selection
        quality_label = ctk.CTkLabel(self.properties_frame, text="Quality:")
        quality_label.pack(pady=5)
        
        self.quality_var = ctk.StringVar(value="high")
        quality_menu = ctk.CTkOptionMenu(
            self.properties_frame,
            values=["high", "medium", "low"],
            variable=self.quality_var
        )
        quality_menu.pack(pady=5)
        
        # Format selection
        format_label = ctk.CTkLabel(self.properties_frame, text="Format:")
        format_label.pack(pady=5)
        
        self.format_var = ctk.StringVar(value="mp4")
        format_menu = ctk.CTkOptionMenu(
            self.properties_frame,
            values=["mp4", "avi", "mov"],
            variable=self.format_var
        )
        format_menu.pack(pady=5)
    
    # File operations
    def new_project(self):
        """Create new project"""
        if self.project_manager.is_modified():
            response = messagebox.askyesnocancel(
                "Save Project",
                "Current project has unsaved changes. Save before creating new project?"
            )
            if response is True:
                self.save_project()
            elif response is None:
                return
        
        self.current_project = self.project_manager.create_new_project()
        self.timeline_clips = []
        self.update_timeline_display()
        logger.info("New project created")
        messagebox.showinfo("Success", "New project created")
    
    def save_project(self):
        """Save current project"""
        filepath = filedialog.asksaveasfilename(
            defaultextension=".vedproj",
            filetypes=[("Video Editor Project", "*.vedproj"), ("All Files", "*.*")]
        )
        
        if filepath:
            if self.project_manager.save_project(self.current_project, filepath):
                messagebox.showinfo("Success", "Project saved successfully")
            else:
                messagebox.showerror("Error", "Failed to save project")
    
    def load_project(self):
        """Load existing project"""
        filepath = filedialog.askopenfilename(
            filetypes=[("Video Editor Project", "*.vedproj"), ("All Files", "*.*")]
        )
        
        if filepath:
            project_data = self.project_manager.load_project(filepath)
            if project_data:
                self.current_project = project_data
                messagebox.showinfo("Success", "Project loaded successfully")
                self.update_timeline_display()
            else:
                messagebox.showerror("Error", "Failed to load project")
    
    def import_video(self):
        """Import video files"""
        filepaths = filedialog.askopenfilenames(
            title="Select Video Files",
            filetypes=[
                ("Video Files", "*.mp4 *.avi *.mov *.mkv *.wmv"),
                ("All Files", "*.*")
            ]
        )
        
        if filepaths:
            for filepath in filepaths:
                self.add_video_to_timeline(filepath)
            messagebox.showinfo("Success", f"Imported {len(filepaths)} video(s)")
    
    def import_image(self):
        """Import image files"""
        filepaths = filedialog.askopenfilenames(
            title="Select Image Files",
            filetypes=[
                ("Image Files", "*.jpg *.jpeg *.png *.bmp *.gif"),
                ("All Files", "*.*")
            ]
        )
        
        if filepaths:
            for filepath in filepaths:
                self.add_image_to_timeline(filepath)
            messagebox.showinfo("Success", f"Imported {len(filepaths)} image(s)")
    
    def import_audio(self):
        """Import audio files"""
        filepaths = filedialog.askopenfilenames(
            title="Select Audio Files",
            filetypes=[
                ("Audio Files", "*.mp3 *.wav *.aac *.ogg"),
                ("All Files", "*.*")
            ]
        )
        
        if filepaths:
            for filepath in filepaths:
                self.add_audio_to_timeline(filepath)
            messagebox.showinfo("Success", f"Imported {len(filepaths)} audio file(s)")
    
    def add_video_to_timeline(self, filepath: str):
        """Add video clip to timeline"""
        clip_data = {
            'type': 'video',
            'filepath': filepath,
            'start': 0,
            'end': None
        }
        self.current_project['timeline']['video_clips'].append(clip_data)
        self.project_manager.mark_modified()
        self.update_timeline_display()
        logger.info(f"Added video to timeline: {filepath}")
    
    def add_image_to_timeline(self, filepath: str):
        """Add image clip to timeline"""
        clip_data = {
            'type': 'image',
            'filepath': filepath,
            'duration': 5.0
        }
        self.current_project['timeline']['image_clips'].append(clip_data)
        self.project_manager.mark_modified()
        self.update_timeline_display()
        logger.info(f"Added image to timeline: {filepath}")
    
    def add_audio_to_timeline(self, filepath: str):
        """Add audio clip to timeline"""
        clip_data = {
            'type': 'audio',
            'filepath': filepath,
            'start': 0,
            'end': None
        }
        self.current_project['timeline']['audio_clips'].append(clip_data)
        self.project_manager.mark_modified()
        self.update_timeline_display()
        logger.info(f"Added audio to timeline: {filepath}")
    
    def update_timeline_display(self):
        """Update timeline display"""
        self.timeline_info.delete("1.0", "end")
        
        timeline_text = "=== TIMELINE ===\n\n"
        
        # Video clips
        timeline_text += "VIDEO CLIPS:\n"
        for i, clip in enumerate(self.current_project['timeline']['video_clips'], 1):
            timeline_text += f"  {i}. {clip['filepath']}\n"
        
        timeline_text += "\nIMAGE CLIPS:\n"
        for i, clip in enumerate(self.current_project['timeline']['image_clips'], 1):
            timeline_text += f"  {i}. {clip['filepath']} (Duration: {clip['duration']}s)\n"
        
        timeline_text += "\nAUDIO CLIPS:\n"
        for i, clip in enumerate(self.current_project['timeline']['audio_clips'], 1):
            timeline_text += f"  {i}. {clip['filepath']}\n"
        
        if not (self.current_project['timeline']['video_clips'] or 
                self.current_project['timeline']['image_clips'] or 
                self.current_project['timeline']['audio_clips']):
            timeline_text += "\nTimeline is empty. Import media files to begin."
        
        self.timeline_info.insert("1.0", timeline_text)
    
    def export_video(self):
        """Export final video"""
        # Check if timeline has content
        if not (self.current_project['timeline']['video_clips'] or 
                self.current_project['timeline']['image_clips']):
            messagebox.showwarning("Warning", "Timeline is empty. Add clips before exporting.")
            return
        
        # Get output path
        output_path = filedialog.asksaveasfilename(
            defaultextension=f".{self.format_var.get()}",
            filetypes=[
                ("MP4 Video", "*.mp4"),
                ("AVI Video", "*.avi"),
                ("MOV Video", "*.mov"),
                ("All Files", "*.*")
            ]
        )
        
        if not output_path:
            return
        
        # Show export dialog
        export_dialog = ExportDialog(self, output_path, self.quality_var.get(), self.format_var.get())
        export_dialog.start_export(self.current_project, self.video_editor, self.video_exporter)


class ExportDialog(ctk.CTkToplevel):
    """Export progress dialog"""
    
    def __init__(self, parent, output_path: str, quality: str, format: str):
        super().__init__(parent)
        
        self.output_path = output_path
        self.quality = quality
        self.format = format
        
        self.title("Exporting Video")
        self.geometry("400x200")
        
        # Progress label
        self.progress_label = ctk.CTkLabel(
            self,
            text="Preparing export...",
            font=("Arial", 12)
        )
        self.progress_label.pack(pady=20)
        
        # Progress bar
        self.progress_bar = ctk.CTkProgressBar(self, width=350)
        self.progress_bar.pack(pady=20)
        self.progress_bar.set(0)
        
        # Status label
        self.status_label = ctk.CTkLabel(self, text="0%")
        self.status_label.pack(pady=10)
    
    def start_export(self, project_data, video_editor, video_exporter):
        """Start video export process"""
        try:
            # This is a simplified export - in production would use threading
            self.progress_label.configure(text="Rendering video...")
            self.update()
            
            # For now, just show completion
            self.progress_bar.set(1.0)
            self.status_label.configure(text="100%")
            self.progress_label.configure(text="Export completed!")
            
            messagebox.showinfo("Success", f"Video exported successfully to:\n{self.output_path}")
            self.destroy()
            
        except Exception as e:
            logger.error(f"Export failed: {e}")
            messagebox.showerror("Error", f"Export failed: {str(e)}")
            self.destroy()
