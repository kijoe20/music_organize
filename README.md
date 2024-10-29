# Music Organizer

This script organizes your music files by artist or album.

## Requirements

- Python 3.x
- `mutagen` library

You can install the required library using pip:

```sh
pip install mutagen
```

## Usage

1. Clone the repository or download the script.
2. Open a terminal and navigate to the directory containing `musicorganize.py`.
3. Run the script:

```sh
python 

musicorganize.py


```

4. Follow the prompts to provide the path to your music folder and choose how you want to organize your music (by artist or album).

## Example

```sh
What is the path to your music folder? /path/to/your/music
How would you like to organize your music? (artist/album) artist
```

The script will organize your music files and delete any empty folders.

## Functions

- [`sanitize_folder_name`](musicorganize.py): Sanitizes folder names to remove invalid characters.
- [`organize_music`](musicorganize.py): Organizes music files by artist or album.
- [`delete_empty_folders`](musicorganize.py): Deletes empty folders in the music directory.
- [`get_valid_path`](musicorganize.py): Prompts the user for a valid path.
- [`get_valid_organize_by`](musicorganize.py): Prompts the user for a valid organize_by option.
- [`main`](musicorganize.py): Main function to organize music files.

## License

This project is licensed under the MIT License.
```

This `README.md` file provides a clear guide on how to use the script, including installation, usage, and a brief description of the functions.