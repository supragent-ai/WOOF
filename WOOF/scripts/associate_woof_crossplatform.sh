#!/bin/bash

echo "WOOF File Association Setup (Cross-Platform)"
echo "============================================="
echo ""
echo "This script will help you associate .woof files with your default image viewer."
echo ""

# Detect operating system
OS="$(uname -s)"
case "${OS}" in
    Linux*)     MACHINE=Linux;;
    Darwin*)    MACHINE=Mac;;
    CYGWIN*)    MACHINE=Cygwin;;
    MINGW*)     MACHINE=MinGw;;
    *)          MACHINE="UNKNOWN:${OS}"
esac

echo "Detected OS: $MACHINE"
echo ""

if [ "$MACHINE" = "Linux" ]; then
    echo "Setting up .woof file association for Linux..."
    
    # Check for common desktop environments
    if [ -n "$XDG_CURRENT_DESKTOP" ]; then
        DESKTOP="$XDG_CURRENT_DESKTOP"
    elif [ -n "$DESKTOP_SESSION" ]; then
        DESKTOP="$DESKTOP_SESSION"
    else
        DESKTOP="unknown"
    fi
    
    echo "Desktop environment: $DESKTOP"
    
    # Create MIME type definition
    cat > /tmp/woof.xml << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<mime-info xmlns="http://www.freedesktop.org/standards/shared-mime-info">
  <mime-type type="image/x-woof">
    <comment>WOOF Image File</comment>
    <comment xml:lang="en">WOOF Image File</comment>
    <glob pattern="*.woof"/>
    <magic priority="50">
      <match type="string" value="\x89PNG" offset="0"/>
    </magic>
  </mime-type>
</mime-info>
EOF
    
    # Install MIME type
    if command -v xdg-mime >/dev/null 2>&1; then
        xdg-mime install /tmp/woof.xml
        echo "✓ Installed MIME type for .woof files"
        
        # Set default application
        if command -v xdg-open >/dev/null 2>&1; then
            # Try to find a suitable image viewer
            for viewer in eog gthumb gwenview feh display; do
                if command -v $viewer >/dev/null 2>&1; then
                    xdg-mime default $viewer.desktop image/x-woof
                    echo "✓ Set $viewer as default for .woof files"
                    break
                fi
            done
        fi
    else
        echo "ℹ xdg-mime not found, manual setup may be required"
    fi
    
    # Clean up
    rm -f /tmp/woof.xml
    
elif [ "$MACHINE" = "Mac" ]; then
    echo "For macOS, please run: ./macos/associate_woof_macos.sh"
    echo "This script is designed for Linux systems."
    
else
    echo "Unsupported operating system: $MACHINE"
    echo "Please use the appropriate script for your OS:"
    echo "- Windows: windows/associate_woof.bat"
    echo "- macOS: macos/associate_woof_macos.sh"
    echo "- Linux: This script"
fi

echo ""
echo "WOOF file association setup complete!"
echo ""
echo "You can now:"
echo "- Double-click .woof files to open them in your default image viewer"
echo "- Right-click .woof files and select 'Open With' to choose a viewer"
echo "- Rename .woof files to .png for instant compatibility"
echo ""
echo "Note: WOOF files are valid PNG files, so they will work in any image viewer."
echo "The hidden AI metadata is preserved when viewing in standard image viewers."
echo ""

# Test file creation
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