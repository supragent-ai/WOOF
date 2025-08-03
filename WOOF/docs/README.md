# WOOF Documentation

## Overview

WOOF (Web Optimized Object Format) is a steganographic image format designed for AI workflows. It embeds rich metadata into standard PNG files using LSB (Least Significant Bit) steganography, making it compatible with all existing image viewers while adding AI-specific capabilities.

## Technical Specification

### File Format

WOOF files are valid PNG files with embedded metadata:

- **Header**: Standard PNG header (89 50 4E 47 0D 0A 1A 0A)
- **Image Data**: RGB pixel data with LSB modifications
- **Hidden Data**: Compressed JSON metadata in LSBs
- **Footer**: Standard PNG footer

### Steganographic Method

- **Channels Used**: RGB only (preserves alpha transparency)
- **Bits Modified**: 2 LSBs per RGB channel
- **Capacity**: 6 bits per pixel
- **Compression**: zlib level 9 for metadata

### Metadata Structure

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
    "preprocessing_params": {...},
    "llm_context": {...}
  },
  "model_hints": {
    "recommended_models": ["ResNet50", "CLIP", "YOLO"],
    "complexity_score": 0.73,
    "processing_priority": "high_detail"
  }
}
```

## API Reference

### WOOFFormat Class

#### Methods

- `convert_to_woof(input_path, output_path)`: Convert image to WOOF format
- `extract_from_woof(input_path)`: Extract metadata from WOOF file
- `analyze_image_features(image)`: Extract AI-relevant features
- `generate_ai_annotations(image)`: Generate AI annotations
- `embed_data(image, metadata)`: Embed metadata using steganography
- `extract_data(image)`: Extract embedded metadata

#### Example Usage

```python
from woof_format import WOOFFormat

# Initialize
woof = WOOFFormat()

# Convert to WOOF
woof.convert_to_woof("image.jpg", "output.woof")

# Extract metadata
metadata = woof.extract_from_woof("output.woof")
print(metadata)
```

## Installation

```bash
# Clone repository
git clone https://github.com/yourusername/woof.git
cd woof

# Install dependencies
pip install -r requirements.txt

# Optional: Install as package
pip install -e .
```

## Usage Examples

### Command Line

```bash
# Convert image to WOOF
python woof_format.py image.jpg output.woof

# Extract metadata
python woof_format.py output.woof --extract
```

### GUI Application

```bash
# Launch GUI
python woof_gui.py
```

### Python API

```python
from woof_format import WOOFFormat
from PIL import Image

# Load image
image = Image.open("puppy.jpg")

# Create WOOF instance
woof = WOOFFormat()

# Generate metadata
metadata = woof.create_metadata(image)

# Embed metadata
woof_image = woof.embed_data(image, metadata)

# Save as WOOF
woof_image.save("puppy.woof", "PNG")
```

## File Association Setup

### Windows

```bash
# Run as Administrator
windows\associate_woof.bat
```

### macOS

```bash
chmod +x macos/associate_woof_macos.sh
./macos/associate_woof_macos.sh
```

### Linux

```bash
chmod +x scripts/associate_woof_crossplatform.sh
./scripts/associate_woof_crossplatform.sh
```

## Performance Characteristics

| Metric | PNG | WOOF | Notes |
|--------|-----|------|-------|
| Viewer Compatibility | 100% | 100% | After setup or rename |
| Visual Quality | Perfect | Perfect | Imperceptible changes |
| AI Data Capacity | 0 bytes | 650+ bytes | Rich metadata |
| Load Time | Fast | Fast | No noticeable difference |
| File Size | Base | +0.1% | Minimal overhead |

## Use Cases

### AI Training Datasets
- Embedded annotations eliminate separate metadata files
- Self-documenting images with analysis results
- Consistent, portable annotations across platforms

### Computer Vision
- Pre-computed features accelerate model inference
- Object detection results embedded in images
- Attention maps for focus regions

### Digital Asset Management
- Rich metadata without database dependency
- Self-describing images for content pipelines
- Enhanced search and categorization

### LLM Vision Tasks
- Enhanced multimodal AI with embedded context
- Scene descriptions and visual elements
- Suggested tags and processing hints

## Limitations

- Requires minimum image size for metadata embedding
- Metadata size limited by image dimensions
- LSB modifications are theoretically detectable
- Not suitable for lossy compression workflows

## Future Enhancements

- Support for additional image formats
- Enhanced AI model integration
- Real-time object detection
- Advanced steganographic techniques
- Web browser integration

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

Apache 2.0 License - see LICENSE file for details. 