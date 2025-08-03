#!/usr/bin/env python3
"""
WOOF Format Demonstration
A comprehensive demonstration of WOOF format capabilities
"""

import os
import sys
import json
import time
from PIL import Image, ImageDraw, ImageFont
from woof_format import WOOFFormat

def create_demo_image():
    """Create a demo image for testing"""
    # Create a simple demo image
    width, height = 400, 300
    image = Image.new('RGBA', (width, height), (255, 255, 255, 255))
    draw = ImageDraw.Draw(image)
    
    # Draw a simple puppy-like shape
    # Body (oval)
    draw.ellipse([100, 150, 300, 250], fill=(139, 69, 19), outline=(101, 67, 33), width=2)
    
    # Head (circle)
    draw.ellipse([150, 80, 250, 180], fill=(160, 82, 45), outline=(101, 67, 33), width=2)
    
    # Ears
    draw.ellipse([130, 60, 170, 100], fill=(139, 69, 19), outline=(101, 67, 33), width=2)
    draw.ellipse([230, 60, 270, 100], fill=(139, 69, 19), outline=(101, 67, 33), width=2)
    
    # Eyes
    draw.ellipse([170, 110, 190, 130], fill=(255, 255, 255), outline=(0, 0, 0), width=2)
    draw.ellipse([210, 110, 230, 130], fill=(255, 255, 255), outline=(0, 0, 0), width=2)
    draw.ellipse([175, 115, 185, 125], fill=(0, 0, 0))
    draw.ellipse([215, 115, 225, 125], fill=(0, 0, 0))
    
    # Nose
    draw.ellipse([195, 140, 205, 150], fill=(0, 0, 0))
    
    # Mouth
    draw.arc([180, 150, 220, 170], 0, 180, fill=(0, 0, 0), width=2)
    
    # Add text
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except:
        font = ImageFont.load_default()
    
    draw.text((10, 10), "WOOF Demo Image", fill=(0, 0, 0), font=font)
    draw.text((10, 35), "Puppy Portrait", fill=(139, 69, 19), font=font)
    
    return image

def demonstrate_woof_capabilities():
    """Demonstrate WOOF format capabilities"""
    print("🐕 WOOF Format Demonstration")
    print("=" * 50)
    print()
    
    # Create demo image
    print("1. Creating demo image...")
    demo_image = create_demo_image()
    demo_image.save("demo_puppy.png")
    print("   ✓ Created demo_puppy.png")
    print()
    
    # Initialize WOOF format
    woof = WOOFFormat()
    
    # Convert to WOOF
    print("2. Converting to WOOF format...")
    start_time = time.time()
    success = woof.convert_to_woof("demo_puppy.png", "demo_puppy.woof")
    conversion_time = time.time() - start_time
    
    if success:
        print(f"   ✓ Converted to demo_puppy.woof in {conversion_time:.3f} seconds")
    else:
        print("   ✗ Conversion failed")
        return
    print()
    
    # Extract metadata
    print("3. Extracting AI metadata...")
    metadata = woof.extract_from_woof("demo_puppy.woof")
    
    if metadata:
        print("   ✓ Successfully extracted metadata")
        print(f"   📊 Metadata size: {len(json.dumps(metadata))} bytes")
        print()
        
        # Display key metadata
        print("4. Key Metadata Analysis:")
        print("   - Version:", metadata.get("version", "Unknown"))
        print("   - Image dimensions:", metadata.get("features", {}).get("dimensions", "Unknown"))
        print("   - Brightness:", f"{metadata.get('features', {}).get('brightness', 0):.2f}")
        print("   - Contrast:", f"{metadata.get('features', {}).get('contrast', 0):.2f}")
        print("   - Detected objects:", metadata.get("ai_annotations", {}).get("object_classes", []))
        print()
        
        # Show LLM context
        llm_context = metadata.get("ai_annotations", {}).get("llm_context", {})
        if llm_context:
            print("5. LLM Context:")
            print("   Scene description:", llm_context.get("scene_description", "N/A"))
            print("   Visual elements:", ", ".join(llm_context.get("visual_elements", [])))
            print("   Suggested tags:", ", ".join(llm_context.get("suggested_tags", [])))
            print()
    else:
        print("   ✗ Failed to extract metadata")
        return
    
    # Test compatibility
    print("6. Testing compatibility...")
    
    # Test PNG compatibility
    try:
        png_image = Image.open("demo_puppy.woof")
        print("   ✓ WOOF file opens as PNG in standard image viewers")
    except Exception as e:
        print(f"   ✗ PNG compatibility test failed: {e}")
    
    # Test metadata preservation after rename
    try:
        import shutil
        shutil.copy("demo_puppy.woof", "demo_puppy_renamed.png")
        renamed_metadata = woof.extract_from_woof("demo_puppy_renamed.png")
        if renamed_metadata:
            print("   ✓ Metadata preserved after renaming to .png")
        else:
            print("   ✗ Metadata lost after renaming")
    except Exception as e:
        print(f"   ✗ Rename test failed: {e}")
    
    print()
    
    # Performance comparison
    print("7. Performance Analysis:")
    
    # File sizes
    png_size = os.path.getsize("demo_puppy.png")
    woof_size = os.path.getsize("demo_puppy.woof")
    
    print(f"   PNG file size: {png_size:,} bytes")
    print(f"   WOOF file size: {woof_size:,} bytes")
    print(f"   Size difference: {woof_size - png_size:,} bytes")
    print(f"   Overhead: {((woof_size - png_size) / png_size * 100):.2f}%")
    print()
    
    # Show file structure
    print("8. File Structure Analysis:")
    print("   WOOF files are valid PNG files with hidden metadata")
    print("   - PNG header and structure: Preserved")
    print("   - RGB pixel data: Modified with LSB steganography")
    print("   - Alpha channel: Unmodified (transparency preserved)")
    print("   - Hidden data: AI metadata in compressed JSON format")
    print()
    
    # Cleanup
    print("9. Cleanup...")
    try:
        os.remove("demo_puppy_renamed.png")
        print("   ✓ Cleaned up temporary files")
    except:
        pass
    
    print()
    print("🎉 WOOF Demonstration Complete!")
    print()
    print("Files created:")
    print("  - demo_puppy.png (original)")
    print("  - demo_puppy.woof (WOOF format)")
    print()
    print("You can now:")
    print("  - Open demo_puppy.woof in any image viewer")
    print("  - Rename it to .png for instant compatibility")
    print("  - Use the WOOF GUI to view hidden metadata")
    print("  - Process it with AI tools that understand WOOF format")

def main():
    """Main demonstration function"""
    try:
        demonstrate_woof_capabilities()
    except KeyboardInterrupt:
        print("\n\nDemonstration interrupted by user")
    except Exception as e:
        print(f"\n\nDemonstration failed: {e}")
        print("Make sure you have installed the required dependencies:")
        print("  pip install -r requirements.txt")

if __name__ == "__main__":
    main() 