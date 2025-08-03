# WOOF

Version 1.0 License Apache 2.0 Platform Cross-platform 

 The most Paw-some Image File Format for your AI workflows

---

## Wait- What? You Can Just Make File Formats?

| Well- yes, but no, I'll come to that bit later, but before that, let me geek out about what this project is **WOOF** (Web Optimized Object Format) is a Python-based image file format designed to be efficient, practical, and cross-platform compatible. With support for RGBA transparency, metadata, and fast rendering capabilities, WOOF provides a modern alternative for image storage and manipulation. Whether you're a developer looking for a lightweight image format, an AI enthusiast wanting the best possible file format, a digital artist needing transparent image support, or just a curious coder who wants a .woof file extension, WOOF offers a simple yet powerful solution. | ![Sample WOOF Image](assets/sample-images/puppy.png) _The First image to ever be converted to .woof_ Note: GitHub doesn't support .woof files (YET), so had to display the original PNG source |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |

## 🐕 What Makes WOOF Special?

### 🎯 **Universal Compatibility**
- **100% PNG Compatible**: Every .woof file is a valid PNG file
- **Works Everywhere**: Opens in any image viewer, browser, or application
- **Zero Setup**: Just rename to .png for instant compatibility

### 🧠 **AI-Powered Features**
- **Embedded Intelligence**: Rich AI metadata stored invisibly in the image
- **Steganographic Storage**: Hidden data using advanced LSB techniques
- **LLM Context**: Enhanced understanding for AI vision models
- **Object Detection**: Pre-computed bounding boxes and classifications

### ⚡ **Performance Optimized**
- **Lightning Fast**: Optimized for AI inference and processing
- **Efficient Storage**: Smart compression without quality loss
- **Cross-Platform**: Works seamlessly on Windows, macOS, and Linux

## 🚀 Quick Start

### 📦 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/woof.git
cd woof

# Install dependencies
pip install -r requirements.txt

# Set up file associations (optional)
windows\associate_woof.bat  # Run as administrator
```

### 🔄 Creating WOOF Files

#### Command Line - Quick Conversion

```bash
# Convert any image to steganographic WOOF
python woof_format.py image.jpg output.woof

# Convert PNG with rich AI annotations
python convert.py image.png enhanced.woof
```

#### GUI Application - Full Featured

```bash
# Launch the WOOF GUI with AI features
python woof_gui.py
```

### 👁️ Viewing & Testing Cross-Compatibility

#### Standard Image Viewers (2 Setup Options)

```bash
# Option 1: Rename to .png (works instantly everywhere)
rename test.woof test.png
start test.png                    # Opens in default viewer

# Option 2: Set up file associations (makes .woof recognized)
windows\associate_woof.bat        # Run as administrator first
start test.woof                   # Now opens directly!
```

#### WOOF-Aware Applications (See AI Data)

```bash
# Launch WOOF viewer to see hidden AI metadata
python woof_gui.py

# Run compatibility demonstration
python final_demonstration.py
```

### 🧪 Real-World Example

```bash
# 1. Create a steganographic WOOF file
python woof_format.py "photo.jpg" "photo.woof"

# 2. Test universal compatibility - Choose your method:

# Method A: Rename to PNG (instant compatibility)
copy photo.woof photo.png          # Keep original + create PNG copy
start photo.png                    # Opens in any image viewer!

# Method B: File association setup (one-time setup)
windows\associate_woof.bat         # Run as admin (one-time setup)
start photo.woof                   # Now .woof files open directly!

# 3. Extract AI data (WOOF-aware apps see hidden metadata)
python woof_gui.py                 # Load .woof OR renamed .png - AI data intact!
```

## 🕴️ Next Steps

### File Association Setup

To make `.woof` files open directly in your system's default image viewer, run the appropriate setup script for your platform:

#### Windows

```bash
# Run as administrator to set up file associations
windows\associate_woof.bat
```

#### macOS

```bash
# Make executable and run
chmod +x macos/associate_woof_macos.sh
./macos/associate_woof_macos.sh
```

#### Linux/Cross-Platform

```bash
# Universal setup script that detects your OS
chmod +x scripts/associate_woof_crossplatform.sh
./scripts/associate_woof_crossplatform.sh
```

After running the appropriate script, double-clicking any `.woof` file will open it in your system's default image viewer (Paint, Preview, etc.) while preserving the hidden AI metadata for WOOF-aware applications.

**Note**: File association is optional - you can always rename `.woof` files to `.png` for instant compatibility with any image viewer.

## 🧪 Steganographic Format Specification

| File Structure **WOOF files ARE valid PNG files** with hidden data embedded using LSB steganography: **Standard PNG Structure**: Complete, valid PNG file **Hidden WOOF Header**: WOOF_STEG_V2 (12 bytes) **Size Field**: 32-bit length of compressed data **Compressed AI Data**: zlib-compressed JSON metadata Storage Method **Channels Used**: RGB only (preserves alpha transparency) **Bits Per Channel**: 2 LSBs modified (visually imperceptible) **Capacity**: 6 bits per pixel (width × height × 3 × 2 ÷ 8 bytes) **Compression**: zlib level 9 for maximum data density | 📁 WOOF File Structure: ┌─────────────────────┐ │    PNG Header       │ ← Standard PNG │                     │ │  RGB Image Data     │ ← Normal pixels + │  (with hidden data) │   hidden AI data │                     │   in 2 LSBs │  PNG Footer         │ ← Standard PNG └─────────────────────┘ 🔬 Pixel-Level Storage: Original: R[142] G[87] B[203] Binary:   10001110 01010111 11001011 After:    R[140] G[84] B[200]  Binary:   10001100 01010100 11001000                 ↑↑       ↑↑       ↑↑             Hidden data bits |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### 📊 AI Metadata Structure

```json
{
  "version": 2,
  "features": {
    "brightness": 126.642,
    "contrast": 67.335, 
    "edge_density": 0.738,
    "mean_rgb": [126.69, 126.6, 126.64],
    "dimensions": [400, 300]
  },
  "attention_maps": {
    "avg_attention": 117.86,
    "max_attention": 255,
    "attention_peaks": 12,
    "focus_regions": [[120, 80], [250, 150]]
  },
  "ai_annotations": {
    "object_classes": ["puppy", "background"],
    "bounding_boxes": [...],
    "preprocessing_params": {
      "mean_rgb": [0.485, 0.456, 0.406],
      "input_size": [224, 224],
      "normalization": "imagenet"
    },
    "llm_context": {
      "scene_description": "An adorable light brown puppy looking directly at the viewer",
      "visual_elements": ["soft fur", "large eyes", "playful expression", "indoor setting"],
      "suggested_tags": ["puppy", "cute", "pet", "portrait", "indoor"]
    }
  },
  "model_hints": {
    "recommended_models": ["ResNet50", "CLIP", "YOLO"],
    "complexity_score": 0.73,
    "processing_priority": "high_detail"
  }
}
```

## 🛠️ Tools & Applications

| 🖼️ GUI Application Complete interface with AI metadata viewer, steganographic converter, and cross-compatibility testing | 🔄 Steganographic Converter Command-line tool for embedding AI data in PNG-compatible WOOF files | 🌐 Universal Compatibility PNG-compatible format that works in any viewer after simple setup |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------- |

## 🔧 Technical Details

### Implementation

* Built with **Python 3.6+**
* Uses **Pillow/PIL** for image processing
* **NumPy** for efficient steganographic operations
* **zlib** for AI metadata compression
* **tkinter** for cross-platform GUI
* **JSON** for structured AI data storage

### Performance Characteristics

| Metric                    | Standard PNG | Steganographic WOOF | Difference               |
| ------------------------- | ------------ | ------------------- | ------------------------ |
| Viewer compatibility      | 100%         | 100% (after setup)  | Simple setup required    |
| Visual quality            | Perfect      | Perfect             | Imperceptible            |
| AI data capacity          | 0 bytes      | 650+ bytes          | Rich metadata            |
| Load time                 | Fast         | Fast                | No noticeable difference |
| LLM context understanding | Basic        | Better              | Significantly improved   |

### Real-World Applications

* **AI Training Datasets**: Embedded annotations eliminate separate metadata files
* **Computer Vision**: Pre-computed features accelerate model inference
* **Digital Asset Management**: Rich metadata without database dependency
* **Research Archives**: Self-documenting images with analysis results
* **Production Workflows**: Integration with existing tools (after setup or rename to .png)
* **LLM Vision Tasks**: Enhanced multimodal AI with embedded context
* **Automated Content Analysis**: Self-describing images for content pipelines
* **AI Model Training**: Consistent, portable annotations across platforms

### Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🧠 Credits & Acknowledgements

Initial idea inspired by the MEOW format project, which provided a creative starting point for innovative image formats.

## 📜 License

This project is released under the Apache 2.0 License. See the LICENSE file for details.

---

Made with ❤️ by the WOOF Team

_Paw-somely optimized (I mean- as far as our code takes it)_

## About

 The most Paw-some Image File Format for your AI workflows

### Topics

 open-source  metadata  machine-learning  png  ai  jpeg  images  file-format  steganography  woof  image-format  llm 
