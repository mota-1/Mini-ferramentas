import os

def convert_bytes_to_readable_size(bytes):
    if bytes < 1024:
        return f"{bytes} bytes"
    elif bytes < 1024 ** 2:
        return f"{bytes / 1024:.2f} KB"
    elif bytes < 1024 ** 3:
        return f"{bytes / (1024 ** 2):.2f} MB"
    else:
        return f"{bytes / (1024 ** 3):.2f} GB"

# def get_largest_files(directory, num_files):
#     file_sizes = []

#     for foldername, _, filenames in os.walk(directory):
#         for filename in filenames:
#             filepath = os.path.join(foldername, filename)
#             filesize = os.path.getsize(filepath)
#             file_sizes.append((filepath, filesize))

#     file_sizes.sort(key=lambda x: x[1], reverse=True)

#     largest_files = file_sizes[:num_files]

#     return largest_files


# if __name__ == '__main__':
#     directory = input("Enter the directory path to search: ")
#     num_files = int(input("Enter the number of largest files to display: "))

#     largest_files = get_largest_files(directory, num_files)

#     print(f"\nTop {num_files} largest files in '{directory}':")
#     for file in largest_files:
#         filepath, filesize = file
#         readable_size = convert_bytes_to_readable_size(filesize)
#         print(f"{filepath} ({readable_size})")
def get_largest_folders(directory, num_folders):
    folder_sizes = {}

    for foldername, _, filenames in os.walk(directory):
        folder_size = sum(os.path.getsize(os.path.join(foldername, filename)) for filename in filenames)
        folder_sizes[foldername] = folder_size

    largest_folders = sorted(folder_sizes.items(), key=lambda x: x[1], reverse=True)[:num_folders]

    return largest_folders

if __name__ == '__main__':
    directory = input("Enter the directory path to search: ")
    num_folders = int(input("Enter the number of largest folders to display: "))

    largest_folders = get_largest_folders(directory, num_folders)

    print(f"\nTop {num_folders} largest folders in '{directory}':")
    for folder, folder_size in largest_folders:
        readable_size = convert_bytes_to_readable_size(folder_size)
        print(f"{folder} ({readable_size})")