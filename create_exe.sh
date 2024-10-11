#!/bin/sh

# Make a virtual enviroment
python -m venv venv

if [ "$OSTYPE" = "msys" ]; then
   source venv/Scripts/activate
else
   source venv/bin/activate
fi

# Install needed packages and create the executable
pip install lite-spleeter pyinstaller && pyinstaller --onefile --collect-all spleeter execute_spleeter.py

echo "Executable is located in the dist folder.
Jazak-allah khair for removing music from media files! enjoy ;)"


