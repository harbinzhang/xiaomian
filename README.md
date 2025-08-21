# Audio Processing and Video Generation Tool

## Overview
This project is a Python-based audio processing and video generation tool that extracts songs from audio files, processes PowerPoint presentations, and creates videos by combining audio with slide images.

## YouTube Channel
Visit our YouTube channel: [笑眠](https://www.youtube.com/@%E7%AC%91%E7%9C%A0-r2z)

## Features
- **Audio Song Detection**: Automatically detects and removes background music/songs from audio files using silence detection algorithms
- **Dynamic Audio Processing**: Processes multiple audio files in batch with configurable parameters
- **PowerPoint Integration**: Programmatically creates and modifies PowerPoint presentations
- **Video Generation**: Combines audio files with slide images to create MP4 videos using FFmpeg

## Technical Stack
- **Python**: Core programming language
- **pydub**: Audio processing and manipulation
- **python-pptx**: PowerPoint file creation and manipulation
- **FFmpeg**: Video generation from audio and images
- **AudioSegment**: Audio format conversion and analysis

## Project Structure
```
xiaomian/
├── main.py                 # Main application entry point
├── test.py                 # Test scripts
├── Makefile               # FFmpeg command reference
├── views/                 # Presentation and visual assets
│   ├── Pptx.py           # PowerPoint handling module
│   ├── slides/           # Individual slide images (PNG)
│   └── *.pptx            # PowerPoint template files
├── test/                  # Test directory with sample files
│   ├── main.py           # Test implementation
│   ├── *.mp3             # Sample audio files
│   └── *.png             # Sample images
└── mp3_source/           # Audio source files (referenced in code)
```

## Core Components

### Audio Processing (`main.py`)
- **Song Detection**: Uses silence detection to identify and separate songs from speech
- **Configurable Parameters**:
  - `kSTEP`: Processing step size (50ms)
  - `kSONG_MIN_LENGTH`: Minimum song duration (7000ms)
  - `kSONG_INTERVAL`: Splitting chunk length (1000ms)
  - `kSONG_THRESHOLD`: Maximum distance for concatenation (700ms)

### PowerPoint Handler (`views/Pptx.py`)
- Creates presentations from templates
- Populates slides with dynamic content
- Batch processes slide images

### Video Generation
- Combines audio files with static images
- Creates MP4 videos using FFmpeg
- Batch processes multiple files

## Key Functions

### `HandleSound(name)`
Processes an MP3 file to detect and remove songs:
- Loads audio file
- Detects silence periods
- Identifies song segments
- Exports processed audio without songs

### `GenerateVideo()`
Creates videos from processed audio and slide images:
- Scans for processed audio files
- Matches with corresponding slide images
- Generates MP4 videos using FFmpeg

### `PrepareViews()`
Prepares PowerPoint presentations:
- Loads template presentations
- Populates with content
- Saves modified presentations

## Usage

### Process Audio Files
```python
# Process a single audio file
HandleSound("filename_without_extension")

# Process multiple files
for i in range(8, 20):
    HandleSound(str(i))
```

### Generate Videos
```python
# Generate videos from processed audio and slides
GenerateVideo()
```

### Create PowerPoint Presentations
```python
from views.Pptx import Pptx

pptx_writer = Pptx("./views/model.pptx")
pptx_writer.PopulatePageByName("Slide Title")
pptx_writer.Save("output.pptx")
```

## Dependencies
- pydub
- python-pptx
- FFmpeg (system dependency)

## Installation
```bash
# Install Python dependencies
pip install pydub python-pptx

# Install FFmpeg (macOS)
brew install ffmpeg

# Install FFmpeg (Ubuntu/Debian)
sudo apt-get install ffmpeg
```

## FFmpeg Command Reference
Convert image + audio to video:
```bash
ffmpeg -loop 1 -r 1 -i image.png -i audio.mp3 -c:a copy -shortest -c:v libx264 output.mp4
```

## Notes
- The project processes audio files to detect and remove background music while preserving speech
- Processed files are exported to subdirectories for organization
- Video generation requires matching audio and image files with the same base name