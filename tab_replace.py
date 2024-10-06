import argparse 
import os


parser = argparse.ArgumentParser(
    prog="Continuity Tab Replacer",
    description="Replaces 4 spaces with tabs in continuity file",
    epilog="Written by noah :D mwah",
)


parser.add_argument("filename")
args = parser.parse_args()

export_filename = f"replaced_{args.filename}"
export_file = open(export_filename, "w")

try:
    with open(args.filename, "r") as f:
        for line in f:
            new_line = line.replace("    ", "\t")
            export_file.write(new_line)
    print(f"Written changes to {export_filename}")
except FileNotFoundError:
    print(f"Error: No file found named {args.filename}")
    os.remove(export_filename)

export_file.close()
