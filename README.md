`execute_spleeter` is a small Python script that wraps around lite-spleeter library, allowing you to easily create an executable binary for removing instruments from media files. This makes it ideal for backend servers, desktop applications, or any environment where you want to avoid installing Python.

## Features

• Standalone Executable: Run lite-spleeter without needing a Python installation.

• Easy Integration: Suitable for backend servers and desktop applications.

## Requirements

FFmpeg: Make sure the FFmpeg binary is either in the same directory as the execute_spleeter binary or installed globally on your system.

## Installation

• Download the Binary: Obtain the latest execute_spleeter binary from the releases page.

• Place FFmpeg: Ensure that the FFmpeg binary is accessible either in the same directory or globally.

## Usage

Run the executable from the command line:

```bash
./execute_spleeter <input_file> <output_dir> <codec>
```

• `input file`: Input file path

• `output_dir`: Output directory name

• `codec`: Output format: mp3, aac, ogg, wav etc.

## Build

If you want to build your own binary, ensure you have Python (lower than 3.9) installed and run the shell script:

```bash
git clone https://github.com/mohammadmansour200/execute_spleeter.git
```

```bash
sh ./create_exe.sh
```
