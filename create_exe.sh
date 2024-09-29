#!/bin/sh

# Make sure python's version is lower than 3.9
if python -c "import sys; exit(0 if sys.version_info <= (9, ) else 1)"; then

  # Make a virtual enviroment
  pip install virtualenv && python -m venv venv

  if [[ "$OSTYPE" == "msys" ]]; then
    source venv/Scripts/activate
  else
    source venv/bin/activate
  fi

  # Install needed packages and create the executable
  pip install spleeter pyinstaller && pyinstaller --onefile execute_spleeter.py

  echo "
  Executable is located in the dist folder.
  Jazak-allah khair for removing music from media files! enjoy ;)
  "

else
  echo "Spleeter requires a python version lower than 3.9"
fi
