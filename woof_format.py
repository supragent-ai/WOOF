#!/usr/bin/env python3
"""
WOOF Format Implementation
Web Optimized Object Format - A steganographic image format for AI workflows
"""

import os
import sys
import json
import zlib
import numpy as np
from PIL import Image
import argparse
from typing import Dict, Any, Tuple, Optional

class WOOFFormat:
    """Main WOOF format handler with steganographic capabilities"""
    
    WOOF_HEADER = b'WOOF_STEG_V2'
    VERSION = 2
    
    def __init__(self):
        self.supported_formats = ['.png', '.jpg', '.jpeg', '.bmp', '.tiff']
    
    def analyze_image_features(self, image: Image.Image) -> Dict[str, Any]:
        """Extract AI-relevant features from the image"""
        img_array = np.array(image)
        
        # Basic image statistics
        mean_rgb = np.mean(img_array[:, :, :3], axis=(0, 1))
        brightness = np.mean(img_array[:, :, :3])
        contrast = np.std(img_array[:, :, :3])
        
        # Edge density approximation
        gray = np.mean(img_array[:, :, :3], axis=2)
        edges = np.abs(np.diff(gray, axis=0)) + np.abs(np.diff(gray, axis=1))
        edge_density = np.mean(edges)
        
        # Attention map simulation
        attention_map = self._generate_attention_map(img_array)
        
        return {
            "brightness": float(brightness),
            "contrast": float(contrast),
            "edge_density": float(edge_density),
            "mean_rgb": mean_rgb.tolist(),
            "dimensions": list(image.size),
            "attention_maps": attention_map
        }
    
    def _generate_attention_map(self, img_array: np.ndarray) -> Dict[str, Any]:
        """Generate simulated attention maps for AI processing"""
        height, width = img_array.shape[:2]
        
        # Simulate attention based on brightness and contrast
        gray = np.mean(img_array[:, :, :3], axis=2)
        attention = np.abs(gray - np.mean(gray)) / 255.0
        
        # Find focus regions (high attention areas)
        threshold = np.percentile(attention, 90)
        focus_regions = np.where(attention > threshold)
        
        return {
            "avg_attention": float(np.mean(attention)),
            "max_attention": float(np.max(attention)),
            "attention_peaks": len(focus_regions[0]),
            "focus_regions": [
                [int(focus_regions[1][i]), int(focus_regions[0][i])] 
                for i in range(min(10, len(focus_regions[0])))
            ]
        }
    
    def generate_ai_annotations(self, image: Image.Image) -> Dict[str, Any]:
        """Generate AI annotations and context for the image"""
        # Simulate object detection results
        img_array = np.array(image)
        height, width = img_array.shape[:2]
        
        # Simple object detection simulation
        # In a real implementation, this would use actual AI models
        objects = self._detect_objects_simulation(img_array)
        
        return {
            "object_classes": objects,
            "bounding_boxes": self._generate_bounding_boxes(img_array, objects),
            "preprocessing_params": {
                "mean_rgb": [0.485, 0.456, 0.406],
                "input_size": [224, 224],
                "normalization": "imagenet"
            },
            "llm_context": self._generate_llm_context(image, objects)
        }
    
    def _detect_objects_simulation(self, img_array: np.ndarray) -> list:
        """Simulate object detection - in real implementation, use actual AI models"""
        # This is a simplified simulation
        # Real implementation would use YOLO, Faster R-CNN, etc.
        objects = ["puppy", "background"]
        
        # Add more objects based on image characteristics
        if np.mean(img_array[:, :, 0]) > 150:  # High red channel
            objects.append("warm_lighting")
        if np.std(img_array) > 50:  # High contrast
            objects.append("detailed_texture")
            
        return objects
    
    def _generate_bounding_boxes(self, img_array: np.ndarray, objects: list) -> list:
        """Generate simulated bounding boxes for detected objects"""
        height, width = img_array.shape[:2]
        boxes = []
        
        for obj in objects:
            if obj == "puppy":
                # Simulate puppy bounding box (center region)
                x1, y1 = width // 4, height // 4
                x2, y2 = 3 * width // 4, 3 * height // 4
                boxes.append({
                    "class": obj,
                    "bbox": [x1, y1, x2, y2],
                    "confidence": 0.95
                })
        
        return boxes
    
    def _generate_llm_context(self, image: Image.Image, objects: list) -> Dict[str, Any]:
        """Generate LLM-friendly context description"""
        width, height = image.size
        
        # Generate scene description based on detected objects
        if "puppy" in objects:
            scene_desc = "An adorable light brown puppy looking directly at the viewer"
            visual_elements = ["soft fur", "large eyes", "playful expression", "indoor setting"]
            suggested_tags = ["puppy", "cute", "pet", "portrait", "indoor"]
        else:
            scene_desc = "A general image with various visual elements"
            visual_elements = ["mixed content", "natural lighting"]
            suggested_tags = ["general", "image"]
        
        return {
            "scene_description": scene_desc,
            "visual_elements": visual_elements,
            "suggested_tags": suggested_tags
        }
    
    def create_metadata(self, image: Image.Image) -> Dict[str, Any]:
        """Create complete WOOF metadata structure"""
        features = self.analyze_image_features(image)
        ai_annotations = self.generate_ai_annotations(image)
        
        return {
            "version": self.VERSION,
            "features": features,
            "ai_annotations": ai_annotations,
            "model_hints": {
                "recommended_models": ["ResNet50", "CLIP", "YOLO"],
                "complexity_score": 0.73,
                "processing_priority": "high_detail"
            }
        }
    
    def embed_data(self, image: Image.Image, metadata: Dict[str, Any]) -> Image.Image:
        """Embed metadata into image using LSB steganography"""
        # Convert metadata to compressed bytes
        metadata_json = json.dumps(metadata, separators=(',', ':'))
        compressed_data = zlib.compress(metadata_json.encode('utf-8'), level=9)
        
        # Prepare header and size information
        header = self.WOOF_HEADER
        size_bytes = len(compressed_data).to_bytes(4, 'big')
        full_data = header + size_bytes + compressed_data
        
        # Convert to binary
        data_bits = ''.join(format(byte, '08b') for byte in full_data)
        
        # Embed in image
        img_array = np.array(image)
        height, width = img_array.shape[:2]
        
        # Check if image is large enough
        max_bits = height * width * 3 * 2  # 2 LSBs per RGB channel
        if len(data_bits) > max_bits:
            raise ValueError(f"Image too small to embed data. Need {len(data_bits)} bits, have {max_bits}")
        
        # Embed data in LSBs
        bit_index = 0
        for y in range(height):
            for x in range(width):
                for c in range(3):  # RGB channels only
                    if bit_index < len(data_bits):
                        # Clear LSB and set new bit
                        img_array[y, x, c] = (img_array[y, x, c] & 0xFE) | int(data_bits[bit_index])
                        bit_index += 1
                    else:
                        break
                if bit_index >= len(data_bits):
                    break
            if bit_index >= len(data_bits):
                break
        
        return Image.fromarray(img_array)
    
    def extract_data(self, image: Image.Image) -> Optional[Dict[str, Any]]:
        """Extract embedded metadata from image"""
        img_array = np.array(image)
        height, width = img_array.shape[:2]
        
        # Extract LSBs
        extracted_bits = ""
        for y in range(height):
            for x in range(width):
                for c in range(3):
                    extracted_bits += str(img_array[y, x, c] & 1)
        
        # Convert bits to bytes
        extracted_bytes = bytearray()
        for i in range(0, len(extracted_bits), 8):
            if i + 8 <= len(extracted_bits):
                byte_bits = extracted_bits[i:i+8]
                extracted_bytes.append(int(byte_bits, 2))
        
        # Check for WOOF header
        if len(extracted_bytes) < len(self.WOOF_HEADER):
            return None
        
        if extracted_bytes[:len(self.WOOF_HEADER)] != self.WOOF_HEADER:
            return None
        
        # Extract size and data
        size_start = len(self.WOOF_HEADER)
        size_bytes = extracted_bytes[size_start:size_start+4]
        data_size = int.from_bytes(size_bytes, 'big')
        
        data_start = size_start + 4
        compressed_data = extracted_bytes[data_start:data_start+data_size]
        
        # Decompress and parse
        try:
            decompressed_data = zlib.decompress(bytes(compressed_data))
            metadata = json.loads(decompressed_data.decode('utf-8'))
            return metadata
        except (zlib.error, json.JSONDecodeError):
            return None
    
    def convert_to_woof(self, input_path: str, output_path: str) -> bool:
        """Convert any image to WOOF format"""
        try:
            # Load image
            image = Image.open(input_path)
            
            # Convert to RGBA if needed
            if image.mode != 'RGBA':
                image = image.convert('RGBA')
            
            # Create metadata
            metadata = self.create_metadata(image)
            
            # Embed metadata
            woof_image = self.embed_data(image, metadata)
            
            # Save as PNG (WOOF files are valid PNGs)
            woof_image.save(output_path, 'PNG')
            
            print(f"✅ Successfully converted {input_path} to {output_path}")
            print(f"📊 Embedded {len(json.dumps(metadata))} bytes of AI metadata")
            
            return True
            
        except Exception as e:
            print(f"❌ Error converting {input_path}: {str(e)}")
            return False
    
    def extract_from_woof(self, input_path: str) -> Optional[Dict[str, Any]]:
        """Extract metadata from WOOF file"""
        try:
            image = Image.open(input_path)
            metadata = self.extract_data(image)
            
            if metadata:
                print(f"✅ Successfully extracted metadata from {input_path}")
                return metadata
            else:
                print(f"❌ No WOOF metadata found in {input_path}")
                return None
                
        except Exception as e:
            print(f"❌ Error extracting from {input_path}: {str(e)}")
            return None

def main():
    """Main command-line interface"""
    parser = argparse.ArgumentParser(description='WOOF Format Converter')
    parser.add_argument('input', help='Input image file')
    parser.add_argument('output', help='Output WOOF file')
    parser.add_argument('--extract', action='store_true', help='Extract metadata from WOOF file')
    
    args = parser.parse_args()
    
    woof = WOOFFormat()
    
    if args.extract:
        metadata = woof.extract_from_woof(args.input)
        if metadata:
            print(json.dumps(metadata, indent=2))
    else:
        success = woof.convert_to_woof(args.input, args.output)
        if success:
            print("🎉 WOOF conversion completed successfully!")

if __name__ == "__main__":
    main() 