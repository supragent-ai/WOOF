#!/usr/bin/env python3
"""
WOOF GUI Application
A user-friendly interface for WOOF format operations
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import json
import os
from PIL import Image, ImageTk
from woof_format import WOOFFormat
import threading

class WOOFGUI:
    """Main GUI application for WOOF format operations"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("WOOF - Web Optimized Object Format")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')
        
        self.woof = WOOFFormat()
        self.current_image_path = None
        self.current_woof_path = None
        
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the user interface"""
        # Main title
        title_frame = tk.Frame(self.root, bg='#f0f0f0')
        title_frame.pack(pady=10)
        
        title_label = tk.Label(
            title_frame, 
            text="🐕 WOOF Format Converter", 
            font=("Arial", 20, "bold"),
            bg='#f0f0f0',
            fg='#2c3e50'
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            title_frame,
            text="The most Paw-some Image File Format for your AI workflows",
            font=("Arial", 10),
            bg='#f0f0f0',
            fg='#7f8c8d'
        )
        subtitle_label.pack()
        
        # Main content frame
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Left panel - Image operations
        left_panel = tk.Frame(main_frame, bg='#ffffff', relief=tk.RAISED, bd=2)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        # Image display
        self.image_label = tk.Label(left_panel, text="No image loaded", bg='#ffffff')
        self.image_label.pack(pady=20)
        
        # Buttons frame
        buttons_frame = tk.Frame(left_panel, bg='#ffffff')
        buttons_frame.pack(pady=10)
        
        # Load image button
        load_btn = tk.Button(
            buttons_frame,
            text="📁 Load Image",
            command=self.load_image,
            bg='#3498db',
            fg='white',
            font=("Arial", 10, "bold"),
            relief=tk.FLAT,
            padx=20,
            pady=5
        )
        load_btn.pack(pady=5)
        
        # Convert to WOOF button
        self.convert_btn = tk.Button(
            buttons_frame,
            text="🔄 Convert to WOOF",
            command=self.convert_to_woof,
            bg='#27ae60',
            fg='white',
            font=("Arial", 10, "bold"),
            relief=tk.FLAT,
            padx=20,
            pady=5,
            state=tk.DISABLED
        )
        self.convert_btn.pack(pady=5)
        
        # Load WOOF button
        load_woof_btn = tk.Button(
            buttons_frame,
            text="📂 Load WOOF File",
            command=self.load_woof_file,
            bg='#e67e22',
            fg='white',
            font=("Arial", 10, "bold"),
            relief=tk.FLAT,
            padx=20,
            pady=5
        )
        load_woof_btn.pack(pady=5)
        
        # Right panel - Metadata display
        right_panel = tk.Frame(main_frame, bg='#ffffff', relief=tk.RAISED, bd=2)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))
        
        # Metadata title
        metadata_title = tk.Label(
            right_panel,
            text="🧠 AI Metadata",
            font=("Arial", 14, "bold"),
            bg='#ffffff',
            fg='#2c3e50'
        )
        metadata_title.pack(pady=10)
        
        # Metadata display
        self.metadata_text = scrolledtext.ScrolledText(
            right_panel,
            width=40,
            height=25,
            font=("Consolas", 9),
            bg='#f8f9fa',
            fg='#2c3e50',
            relief=tk.FLAT
        )
        self.metadata_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = tk.Label(
            self.root,
            textvariable=self.status_var,
            relief=tk.SUNKEN,
            anchor=tk.W,
            bg='#ecf0f1',
            fg='#2c3e50'
        )
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
    def load_image(self):
        """Load an image file"""
        file_path = filedialog.askopenfilename(
            title="Select Image File",
            filetypes=[
                ("Image files", "*.png *.jpg *.jpeg *.bmp *.tiff"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            try:
                # Load and display image
                image = Image.open(file_path)
                
                # Resize for display (max 300x300)
                display_size = (300, 300)
                image.thumbnail(display_size, Image.Resampling.LANCZOS)
                
                # Convert to PhotoImage for tkinter
                photo = ImageTk.PhotoImage(image)
                
                self.image_label.configure(image=photo, text="")
                self.image_label.image = photo  # Keep a reference
                
                self.current_image_path = file_path
                self.convert_btn.config(state=tk.NORMAL)
                
                self.status_var.set(f"Loaded: {os.path.basename(file_path)}")
                
                # Show basic image info
                self.show_basic_info(image)
                
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load image: {str(e)}")
                self.status_var.set("Error loading image")
    
    def show_basic_info(self, image):
        """Show basic image information"""
        info = f"Image Information:\n"
        info += f"Size: {image.size[0]} x {image.size[1]} pixels\n"
        info += f"Mode: {image.mode}\n"
        info += f"Format: {image.format}\n"
        
        self.metadata_text.delete(1.0, tk.END)
        self.metadata_text.insert(tk.END, info)
    
    def convert_to_woof(self):
        """Convert loaded image to WOOF format"""
        if not self.current_image_path:
            messagebox.showwarning("Warning", "Please load an image first")
            return
        
        # Ask for output path
        output_path = filedialog.asksaveasfilename(
            title="Save WOOF File",
            defaultextension=".woof",
            filetypes=[("WOOF files", "*.woof"), ("All files", "*.*")]
        )
        
        if output_path:
            self.status_var.set("Converting to WOOF...")
            
            # Run conversion in separate thread
            def convert_thread():
                try:
                    success = self.woof.convert_to_woof(self.current_image_path, output_path)
                    
                    if success:
                        self.root.after(0, lambda: self.conversion_success(output_path))
                    else:
                        self.root.after(0, lambda: self.conversion_failed())
                        
                except Exception as e:
                    self.root.after(0, lambda: self.conversion_error(str(e)))
            
            threading.Thread(target=convert_thread, daemon=True).start()
    
    def conversion_success(self, output_path):
        """Handle successful conversion"""
        self.current_woof_path = output_path
        self.status_var.set(f"Successfully created: {os.path.basename(output_path)}")
        
        # Extract and display metadata
        metadata = self.woof.extract_from_woof(output_path)
        if metadata:
            self.display_metadata(metadata)
        
        messagebox.showinfo("Success", f"Image converted to WOOF format!\nSaved as: {output_path}")
    
    def conversion_failed(self):
        """Handle conversion failure"""
        self.status_var.set("Conversion failed")
        messagebox.showerror("Error", "Failed to convert image to WOOF format")
    
    def conversion_error(self, error_msg):
        """Handle conversion error"""
        self.status_var.set("Conversion error")
        messagebox.showerror("Error", f"Conversion error: {error_msg}")
    
    def load_woof_file(self):
        """Load a WOOF file and extract metadata"""
        file_path = filedialog.askopenfilename(
            title="Select WOOF File",
            filetypes=[
                ("WOOF files", "*.woof"),
                ("PNG files", "*.png"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            try:
                # Try to extract metadata
                metadata = self.woof.extract_from_woof(file_path)
                
                if metadata:
                    self.current_woof_path = file_path
                    self.display_metadata(metadata)
                    self.status_var.set(f"Loaded WOOF file: {os.path.basename(file_path)}")
                    
                    # Also display the image
                    image = Image.open(file_path)
                    display_size = (300, 300)
                    image.thumbnail(display_size, Image.Resampling.LANCZOS)
                    photo = ImageTk.PhotoImage(image)
                    self.image_label.configure(image=photo, text="")
                    self.image_label.image = photo
                    
                else:
                    messagebox.showwarning("Warning", "No WOOF metadata found in this file")
                    self.status_var.set("No WOOF metadata found")
                    
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load WOOF file: {str(e)}")
                self.status_var.set("Error loading WOOF file")
    
    def display_metadata(self, metadata):
        """Display metadata in the text area"""
        self.metadata_text.delete(1.0, tk.END)
        
        # Format metadata nicely
        formatted_json = json.dumps(metadata, indent=2)
        
        # Add some highlighting
        self.metadata_text.insert(tk.END, "WOOF Metadata:\n")
        self.metadata_text.insert(tk.END, "=" * 50 + "\n\n")
        self.metadata_text.insert(tk.END, formatted_json)
        
        # Highlight key sections
        self.highlight_metadata()
    
    def highlight_metadata(self):
        """Add syntax highlighting to metadata display"""
        # This is a simple highlighting implementation
        # In a full implementation, you might use a proper syntax highlighter
        
        # Highlight version
        self.metadata_text.tag_add("version", "1.0", "1.20")
        self.metadata_text.tag_config("version", foreground="#e74c3c", font=("Consolas", 9, "bold"))
        
        # Highlight features
        self.metadata_text.tag_add("features", "4.0", "4.20")
        self.metadata_text.tag_config("features", foreground="#27ae60", font=("Consolas", 9, "bold"))
        
        # Highlight AI annotations
        self.metadata_text.tag_add("ai_annotations", "15.0", "15.30")
        self.metadata_text.tag_config("ai_annotations", foreground="#3498db", font=("Consolas", 9, "bold"))

def main():
    """Main application entry point"""
    root = tk.Tk()
    app = WOOFGUI(root)
    
    # Set window icon (if available)
    try:
        root.iconbitmap('assets/woof_icon.ico')
    except:
        pass
    
    root.mainloop()

if __name__ == "__main__":
    main() 