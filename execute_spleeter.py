import platform
import os
import warnings

# Remove annoying tensorflow logs
warnings.filterwarnings("ignore")
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
# If you have cuda set, feel free to change this to 0
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

current_os = platform.system()

os.environ["FFMPEG_BINARY"] = "ffmpeg.exe" if current_os == "Windows" else "ffmpeg"

import sys  # noqa: E402
from spleeter.separator import Separator  # noqa: E402


def separate_audio(input_file: str, output_dir: str, codec: str, duration: float):
    separator = Separator("spleeter:2stems")

    separator.separate_to_file(input_file, output_dir, codec=codec, duration=duration)  # type: ignore


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: execute_spleeter <input_file> <output_dir> <codec> <duration>")
        sys.exit(2)

    input_file = sys.argv[1]
    output_dir = sys.argv[2]
    codec = sys.argv[3]
    duration = sys.argv[4]
    separate_audio(input_file, output_dir, codec, float(duration))
    print("Separation completed!")
    sys.exit(0)
