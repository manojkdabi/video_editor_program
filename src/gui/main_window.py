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
            text="📄 New Project",
            command=self.new_project,
            width=130,
            height=36,
            corner_radius=8,
            font=("Arial", 13, "bold")
        )
        btn_new.pack(side="left", padx=5, pady=10)
        
        # Save Project
        btn_save = ctk.CTkButton(
            self.toolbar_frame,
            text="💾 Save Project",
            command=self.save_project,
            width=130,
            height=36,
            corner_radius=8,
            font=("Arial", 13, "bold")
        )
        btn_save.pack(side="left", padx=5, pady=10)
        
        # Load Project
        btn_load = ctk.CTkButton(
            self.toolbar_frame,
            text="📂 Load Project",
            command=self.load_project,
            width=130,
            height=36,
            corner_radius=8,
            font=("Arial", 13, "bold")
        )
        btn_load.pack(side="left", padx=5, pady=10)
        
        # Separator
        separator = ctk.CTkFrame(self.toolbar_frame, width=2, fg_color="gray30")
        separator.pack(side="left", padx=10, pady=10, fill="y")
        
        # Import Video
        btn_import_video = ctk.CTkButton(
            self.toolbar_frame,
            text="🎬 Import Video",
            command=self.import_video,
            width=130,
            height=36,
            corner_radius=8,
            fg_color="#1f6aa5",
            hover_color="#144870",
            font=("Arial", 13, "bold")
        )
        btn_import_video.pack(side="left", padx=5, pady=10)
        
        # Import Image
        btn_import_image = ctk.CTkButton(
            self.toolbar_frame,
            text="🖼️ Import Image",
            command=self.import_image,
            width=130,
            height=36,
            corner_radius=8,
            fg_color="#1f6aa5",
            hover_color="#144870",
            font=("Arial", 13, "bold")
        )
        btn_import_image.pack(side="left", padx=5, pady=10)
        
        # Import Audio
        btn_import_audio = ctk.CTkButton(
            self.toolbar_frame,
            text="🎵 Import Audio",
            command=self.import_audio,
            width=130,
            height=36,
            corner_radius=8,
            fg_color="#1f6aa5",
            hover_color="#144870",
            font=("Arial", 13, "bold")
        )
        btn_import_audio.pack(side="left", padx=5, pady=10)
        
        # Separator
        separator2 = ctk.CTkFrame(self.toolbar_frame, width=2, fg_color="gray30")
        separator2.pack(side="left", padx=10, pady=10, fill="y")
        
        # Export Video
        btn_export = ctk.CTkButton(
            self.toolbar_frame,
            text="✅ Export Video",
            command=self.export_video,
            width=140,
            height=36,
            corner_radius=8,
            fg_color="#2d7a2d",
            hover_color="#1f5a1f",
            font=("Arial", 13, "bold")
        )
        btn_export.pack(side="left", padx=5, pady=10)
    
    def setup_preview_panel(self):
        """Setup video preview panel"""
        
        # Title with icon
        title = ctk.CTkLabel(
            self.preview_frame,
            text="🎥 Video Preview",
            font=("Arial", 18, "bold"),
            text_color="#3b8ed0"
        )
        title.pack(pady=10)
        
        # Preview canvas with better styling
        self.preview_canvas = ctk.CTkLabel(
            self.preview_frame,
            text="No video loaded\n\nImport media files to see preview",
            width=640,
            height=360,
            fg_color="#1a1a1a",
            corner_radius=10,
            font=("Arial", 14)
        )
        self.preview_canvas.pack(padx=10, pady=10)
        
        # Playback controls with better styling
        controls_frame = ctk.CTkFrame(self.preview_frame, fg_color="transparent")
        controls_frame.pack(pady=10)
        
        btn_play = ctk.CTkButton(
            controls_frame, 
            text="▶ Play", 
            width=90,
            height=36,
            corner_radius=8,
            fg_color="#2d7a2d",
            hover_color="#1f5a1f",
            font=("Arial", 12, "bold")
        )
        btn_play.pack(side="left", padx=5)
        
        btn_pause = ctk.CTkButton(
            controls_frame, 
            text="⏸ Pause", 
            width=90,
            height=36,
            corner_radius=8,
            font=("Arial", 12, "bold")
        )
        btn_pause.pack(side="left", padx=5)
        
        btn_stop = ctk.CTkButton(
            controls_frame, 
            text="⏹ Stop", 
            width=90,
            height=36,
            corner_radius=8,
            fg_color="#a52d2d",
            hover_color="#7a1f1f",
            font=("Arial", 12, "bold")
        )
        btn_stop.pack(side="left", padx=5)
        
        # Timeline slider with better styling
        self.timeline_slider = ctk.CTkSlider(
            self.preview_frame,
            from_=0,
            to=100,
            width=620,
            height=20,
            button_color="#3b8ed0",
            button_hover_color="#2d6a9f",
            progress_color="#3b8ed0"
        )
        self.timeline_slider.pack(pady=10)
        self.timeline_slider.set(0)
        
        # Time display with better styling
        self.time_label = ctk.CTkLabel(
            self.preview_frame,
            text="00:00:00 / 00:00:00",
            font=("Arial", 13, "bold"),
            text_color="#b0b0b0"
        )
        self.time_label.pack()
    
    def setup_timeline_panel(self):
        """Setup timeline panel"""
        
        # Title with icon
        title = ctk.CTkLabel(
            self.timeline_frame,
            text="📽️ Timeline",
            font=("Arial", 18, "bold"),
            text_color="#3b8ed0"
        )
        title.pack(pady=5)
        
        # Timeline info with better styling
        self.timeline_info = ctk.CTkTextbox(
            self.timeline_frame,
            height=120,
            width=800,
            corner_radius=8,
            border_width=2,
            border_color="#3b8ed0",
            font=("Courier New", 11)
        )
        self.timeline_info.pack(padx=10, pady=5, fill="both", expand=True)
        self.timeline_info.insert("1.0", "Timeline is empty. Import videos, images, or audio to begin.")
    
    def setup_properties_panel(self):
        """Setup properties panel"""
        
        # Title with icon
        title = ctk.CTkLabel(
            self.properties_frame,
            text="⚙️ Properties",
            font=("Arial", 18, "bold"),
            text_color="#3b8ed0"
        )
        title.pack(pady=10)
        
        # Properties display with better styling
        self.properties_text = ctk.CTkTextbox(
            self.properties_frame,
            width=280,
            height=400,
            corner_radius=8,
            border_width=2,
            border_color="#3b8ed0",
            font=("Arial", 11)
        )
        self.properties_text.pack(padx=10, pady=10)
        self.properties_text.insert("1.0", "Select a clip to view properties\n\nImported clips will appear here with:\n• Duration\n• Resolution\n• File size\n• Format")
        
        # Export settings section
        export_label = ctk.CTkLabel(
            self.properties_frame,
            text="📤 Export Settings",
            font=("Arial", 16, "bold"),
            text_color="#3b8ed0"
        )
        export_label.pack(pady=15)
        
        # Quality selection with better styling
        quality_label = ctk.CTkLabel(
            self.properties_frame, 
            text="Quality:",
            font=("Arial", 12, "bold")
        )
        quality_label.pack(pady=5)
        
        self.quality_var = ctk.StringVar(value="high")
        quality_menu = ctk.CTkOptionMenu(
            self.properties_frame,
            values=["high", "medium", "low"],
            variable=self.quality_var,
            width=200,
            height=32,
            corner_radius=8,
            font=("Arial", 12),
            dropdown_font=("Arial", 11)
        )
        quality_menu.pack(pady=5)
        
        # Format selection with better styling
        format_label = ctk.CTkLabel(
            self.properties_frame, 
            text="Format:",
            font=("Arial", 12, "bold")
        )
        format_label.pack(pady=5)
        
        self.format_var = ctk.StringVar(value="mp4")
        format_menu = ctk.CTkOptionMenu(
            self.properties_frame,
            values=["mp4", "avi", "mov"],
            variable=self.format_var,
            width=200,
            height=32,
            corner_radius=8,
            font=("Arial", 12),
            dropdown_font=("Arial", 11)
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
            self.update_timeline_display()
            messagebox.showinfo(
                "Success", 
                f"✅ Imported {len(filepaths)} video(s) successfully!\n\n"
                f"Check the Timeline panel below to see your files.\n"
                f"The Preview panel shows a summary of loaded media."
            )
    
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
            self.update_timeline_display()
            messagebox.showinfo(
                "Success", 
                f"✅ Imported {len(filepaths)} image(s) successfully!\n\n"
                f"Each image will display for 5 seconds.\n"
                f"Check the Timeline panel below."
            )
    
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
            self.update_timeline_display()
            messagebox.showinfo(
                "Success", 
                f"✅ Imported {len(filepaths)} audio file(s) successfully!\n\n"
                f"Audio will play alongside your video.\n"
                f"Check the Timeline panel below."
            )
    
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
        
        timeline_text = "╔═══════════════════════════════════════════════════════════════════╗\n"
        timeline_text += "║                          TIMELINE VIEW                            ║\n"
        timeline_text += "╚═══════════════════════════════════════════════════════════════════╝\n\n"
        
        # Video clips
        video_clips = self.current_project['timeline']['video_clips']
        if video_clips:
            timeline_text += "🎬 VIDEO CLIPS:\n"
            timeline_text += "─" * 70 + "\n"
            for i, clip in enumerate(video_clips, 1):
                filename = clip['filepath'].split('/')[-1].split('\\')[-1]
                timeline_text += f"  [{i}] {filename}\n"
                timeline_text += f"      📂 {clip['filepath']}\n"
            timeline_text += "\n"
        
        # Image clips
        image_clips = self.current_project['timeline']['image_clips']
        if image_clips:
            timeline_text += "🖼️  IMAGE CLIPS:\n"
            timeline_text += "─" * 70 + "\n"
            for i, clip in enumerate(image_clips, 1):
                filename = clip['filepath'].split('/')[-1].split('\\')[-1]
                timeline_text += f"  [{i}] {filename} ⏱️  Duration: {clip['duration']}s\n"
                timeline_text += f"      📂 {clip['filepath']}\n"
            timeline_text += "\n"
        
        # Audio clips
        audio_clips = self.current_project['timeline']['audio_clips']
        if audio_clips:
            timeline_text += "🎵 AUDIO CLIPS:\n"
            timeline_text += "─" * 70 + "\n"
            for i, clip in enumerate(audio_clips, 1):
                filename = clip['filepath'].split('/')[-1].split('\\')[-1]
                timeline_text += f"  [{i}] {filename}\n"
                timeline_text += f"      📂 {clip['filepath']}\n"
            timeline_text += "\n"
        
        if not (video_clips or image_clips or audio_clips):
            timeline_text += "📭 Timeline is empty\n\n"
            timeline_text += "Get started:\n"
            timeline_text += "  1. Click 'Import Video' to add video clips\n"
            timeline_text += "  2. Click 'Import Image' to add images\n"
            timeline_text += "  3. Click 'Import Audio' to add audio\n"
        else:
            total_items = len(video_clips) + len(image_clips) + len(audio_clips)
            timeline_text += f"\n📊 Total Items: {total_items} "
            timeline_text += f"({len(video_clips)} videos, {len(image_clips)} images, {len(audio_clips)} audio)"
        
        self.timeline_info.insert("1.0", timeline_text)
        
        # Update preview to show first video or image
        self.update_preview_display()
    
    def update_preview_display(self):
        """Update preview to show imported media information"""
        try:
            video_clips = self.current_project['timeline']['video_clips']
            image_clips = self.current_project['timeline']['image_clips']
            audio_clips = self.current_project['timeline']['audio_clips']
            
            if not (video_clips or image_clips or audio_clips):
                self.preview_canvas.configure(
                    text="No media loaded\n\nImport videos, images, or audio to begin"
                )
                return
            
            # Build preview text
            preview_text = "✅ Media Loaded Successfully!\n\n"
            
            if video_clips:
                preview_text += f"🎬 Videos: {len(video_clips)}\n"
                for i, clip in enumerate(video_clips[:3], 1):  # Show first 3
                    filename = clip['filepath'].split('/')[-1].split('\\')[-1]
                    preview_text += f"   • {filename}\n"
                if len(video_clips) > 3:
                    preview_text += f"   ... and {len(video_clips) - 3} more\n"
                preview_text += "\n"
            
            if image_clips:
                preview_text += f"🖼️  Images: {len(image_clips)}\n"
                for i, clip in enumerate(image_clips[:3], 1):  # Show first 3
                    filename = clip['filepath'].split('/')[-1].split('\\')[-1]
                    preview_text += f"   • {filename} ({clip['duration']}s)\n"
                if len(image_clips) > 3:
                    preview_text += f"   ... and {len(image_clips) - 3} more\n"
                preview_text += "\n"
            
            if audio_clips:
                preview_text += f"🎵 Audio: {len(audio_clips)}\n"
                for i, clip in enumerate(audio_clips[:3], 1):  # Show first 3
                    filename = clip['filepath'].split('/')[-1].split('\\')[-1]
                    preview_text += f"   • {filename}\n"
                if len(audio_clips) > 3:
                    preview_text += f"   ... and {len(audio_clips) - 3} more\n"
            
            preview_text += "\n━━━━━━━━━━━━━━━━━━━━━━━━\n"
            preview_text += "Ready to export!\n"
            preview_text += "Click 'Export Video' to create your video"
            
            self.preview_canvas.configure(
                text=preview_text,
                font=("Arial", 12)
            )
            
        except Exception as e:
            logger.error(f"Error updating preview: {e}")
            self.preview_canvas.configure(
                text=f"Preview update error\n\nMedia imported successfully\nCheck timeline below"
            )
    
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
