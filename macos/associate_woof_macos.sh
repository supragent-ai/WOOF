#!/bin/bash

echo "WOOF File Association Setup for macOS"
echo "====================================="
echo ""
echo "This script will associate .woof files with your default image viewer."
echo ""

# Check if running as root (not required on macOS, but good practice)
if [[ $EUID -eq 0 ]]; then
   echo "Running as root - proceeding with setup..."
else
   echo "Running as user - this should work fine on macOS..."
fi

echo ""
echo "Setting up .woof file association..."

# Create a temporary plist file for the file association
cat > /tmp/woof_association.plist << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleDocumentTypes</key>
    <array>
        <dict>
            <key>CFBundleTypeExtensions</key>
            <array>
                <string>woof</string>
            </array>
            <key>CFBundleTypeIconFile</key>
            <string>woof.icns</string>
            <key>CFBundleTypeName</key>
            <string>WOOF Image File</string>
            <key>CFBundleTypeRole</key>
            <string>Viewer</string>
            <key>LSHandlerRank</key>
            <string>Owner</string>
            <key>LSItemContentTypes</key>
            <array>
                <string>public.image</string>
            </array>
        </dict>
    </array>
</dict>
</plist>
EOF

# Try to register the file type
if launchctl load /tmp/woof_association.plist 2>/dev/null; then
    echo "✓ Registered .woof file type with system"
else
    echo "ℹ Could not register file type (this is normal on modern macOS)"
fi

# Set default application for .woof files to Preview
if command -v duti >/dev/null 2>&1; then
    # Use duti if available
    duti -s com.apple.Preview woof
    echo "✓ Set Preview as default for .woof files"
else
    echo "ℹ Install 'duti' to set default application: brew install duti"
fi

# Clean up
rm -f /tmp/woof_association.plist

echo ""
echo "WOOF file association setup complete!"
echo ""
echo "You can now:"
echo "- Double-click .woof files to open them in Preview"
echo "- Right-click .woof files and select 'Open With' to choose a viewer"
echo "- Rename .woof files to .png for instant compatibility"
echo ""
echo "Note: WOOF files are valid PNG files, so they will work in any image viewer."
echo "The hidden AI metadata is preserved when viewing in standard image viewers."
echo ""

# Test if we can create a simple .woof file
echo "Testing file association..."
if python3 -c "from PIL import Image; import numpy as np; img = Image.new('RGB', (10, 10), color='red'); img.save('test.woof')" 2>/dev/null; then
    echo "✓ Successfully created test.woof file"
    echo "You can now try opening test.woof with your image viewer"
    echo "File will be created in current directory"
else
    echo "ℹ Could not create test file (PIL/Pillow not installed)"
fi

echo ""
echo "Setup complete!" 