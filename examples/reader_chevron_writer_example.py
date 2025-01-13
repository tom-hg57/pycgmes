# SPDX-FileCopyrightText: 2025 Thomas Guenther <tom@toms-cafe.de>
#
# SPDX-License-Identifier: Apache-2.0

import sys
from pathlib import Path

from pycgmes.utils.base import Base
from pycgmes.utils.chevron_writer import ChevronWriter
from pycgmes.utils.reader import Reader

_curr_dir = Path(__file__).resolve().parent


def main(input_files: list[str]) -> None:
    output_dir = _curr_dir / "output"
    output_dir.mkdir(parents=True, exist_ok=True)
    import_result = read(input_files)
    objects = import_result["topology"]
    write(output_dir / "Example_Model", "Example_Model", objects)


def read(input_files: list[str]) -> dict:
    reader = Reader(cgmes_version_path="pycgmes.resources")
    return reader.parse_profiles(input_files)


def write(outputfile: Path, model_id: str, objects: dict[str, Base]) -> None:
    writer = ChevronWriter(objects)
    class_profile_map = ChevronWriter.get_class_profile_map(writer.objects.values())
    profile_file_map = writer.write(str(outputfile), model_id, class_profile_map)
    for idx, (profile, file) in enumerate(profile_file_map.items()):
        print(f"CIM outputfile {idx + 1} for {profile}: {file}")


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit("Too few arguments")
    input_files = sys.argv[1:]
    main(input_files)
