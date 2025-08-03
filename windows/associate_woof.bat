@echo off
echo WOOF File Association Setup
echo ===========================
echo.
echo This script will associate .woof files with your default image viewer.
echo You need to run this as Administrator for it to work properly.
echo.

REM Check if running as administrator
net session >nul 2>&1
if %errorLevel% == 0 (
    echo Running as Administrator - proceeding with setup...
) else (
    echo ERROR: This script must be run as Administrator!
    echo Right-click on this file and select "Run as administrator"
    pause
    exit /b 1
)

echo.
echo Setting up .woof file association...

REM Create file association for .woof files
assoc .woof=woofimage
if %errorLevel% == 0 (
    echo ✓ Associated .woof extension with 'woofimage' type
) else (
    echo ✗ Failed to associate .woof extension
)

REM Set the default program for .woof files to open with default image viewer
ftype woofimage="%ProgramFiles%\Windows Photo Viewer\PhotoViewer.dll,ImageView_Fullscreen" "%%1"
if %errorLevel% == 0 (
    echo ✓ Set default program for .woof files
) else (
    echo ✗ Failed to set default program
)

echo.
echo WOOF file association setup complete!
echo.
echo You can now:
echo - Double-click .woof files to open them in your default image viewer
echo - Right-click .woof files and select "Open with" to choose a viewer
echo - Rename .woof files to .png for instant compatibility
echo.
echo Note: WOOF files are valid PNG files, so they will work in any image viewer.
echo The hidden AI metadata is preserved when viewing in standard image viewers.
echo.
pause 