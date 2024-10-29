import os
import re
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from mutagen.mp3 import HeaderNotFoundError

def sanitize_folder_name(name):
    """Sanitize folder name to remove invalid characters."""
    return re.sub(r'[<>:"/\\|?*]', '_', name)

def organize_music(music_folder, organize_by):
    """Organize music files by artist or album."""
    for root, _, files in os.walk(music_folder):
        for file in files:
            if file.endswith('.mp3'):
                file_path = os.path.join(root, file)
                try:
                    audio = MP3(file_path, ID3=EasyID3)
                except HeaderNotFoundError:
                    print(f"Skipping invalid MP3 file: {file_path}")
                    continue

                if organize_by == 'artist' and 'artist' in audio:
                    artist = audio['artist'][0]
                    target_folder = os.path.join(music_folder, sanitize_folder_name(artist))
                elif organize_by == 'album' and 'album' in audio:
                    album = audio['album'][0]
                    target_folder = os.path.join(music_folder, sanitize_folder_name(album))
                else:
                    continue

                os.makedirs(target_folder, exist_ok=True)
                try:
                    os.rename(file_path, os.path.join(target_folder, file))
                except OSError as e:
                    print(f"Error moving file {file_path}: {e}")

def delete_empty_folders(music_folder):
    """Delete empty folders in the music directory."""
    for root, dirs, _ in os.walk(music_folder):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if not os.listdir(dir_path):
                try:
                    os.rmdir(dir_path)
                except OSError as e:
                    print(f"Error deleting folder {dir_path}: {e}")

def get_valid_path(prompt):
    """Prompt the user for a valid path."""
    path = input(prompt)
    while not os.path.exists(path):
        print('Invalid path. Please enter a valid path.')
        path = input(prompt)
    return path

def get_valid_organize_by(prompt):
    """Prompt the user for a valid organize_by option."""
    organize_by = input(prompt)
    while organize_by not in ['artist', 'album']:
        print('Invalid input. Please enter either "artist" or "album".')
        organize_by = input(prompt)
    return organize_by

def main():
    """Main function to organize music files."""
    music_folder = get_valid_path('What is the path to your music folder? ')
    organize_by = get_valid_organize_by('How would you like to organize your music? (artist/album) ')
    
    organize_music(music_folder, organize_by)
    delete_empty_folders(music_folder)
    print('Music files organized successfully!')

if __name__ == '__main__':
    main()
