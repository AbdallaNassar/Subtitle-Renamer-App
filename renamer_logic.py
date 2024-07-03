import os

def rename_files(vid_path, sub_path, sub_format):
    try:
        # Get video files ending with .mp4, .mkv, or .avi in vid_path directory
        vid_files = [name for name in os.listdir(vid_path) if name.endswith(('.mp4', '.mkv', '.avi'))]
        # Get subtitle files ending with sub_format in sub_path directory
        sub_files = [name for name in os.listdir(sub_path) if name.endswith(sub_format)]
        # Sort subtitle files based on numeric part of filename if it contains digits
        sub_files.sort(key=lambda f: int(''.join(filter(str.isdigit, f))) if any(char.isdigit() for char in f) else 0)
    except:
        # Handle exceptions related to invalid directories
        return False, "Invalid directory."

    try:
        # Check if number of subtitle files matches number of video files and both are non-zero
        assert(len(sub_files) == len(vid_files) and len(sub_files) > 0 and len(vid_files) > 0)
        # Rename subtitle files corresponding to video files
        for vname, sname in zip(vid_files, sub_files):
            new_sub_name = os.path.splitext(vname)[0] + sub_format
            print(f"{sname} renamed to {new_sub_name}")
            os.rename(os.path.join(sub_path, sname), os.path.join(sub_path, new_sub_name))
        return True, "Files renamed successfully!"
    except AssertionError:
        # Handle assertion error for mismatch between number of video and subtitle files
        return False, "Mismatch between number of video and subtitle files."
