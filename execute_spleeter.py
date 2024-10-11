import os
import warnings

# Remove annoying tensorflow logs
warnings.filterwarnings("ignore", category=UserWarning)

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import sys  # noqa: E402
from spleeter.separator import Separator  # noqa: E402


def separate_audio(input_file: str, output_dir: str, codec: str):
    separator = Separator()

    separator.separate_to_file(input_file, output_dir, codec=codec)  # type: ignore


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: lite-spleeter <input_file> <output_dir> <codec>")
        sys.exit(2)

    input_file = sys.argv[1]
    output_dir = sys.argv[2]
    codec = sys.argv[3]
    separate_audio(input_file, output_dir, codec)
    sys.exit(0)
