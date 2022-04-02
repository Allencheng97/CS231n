import sys
import os
import urllib.request
import tarfile
import zipfile
import progressbar
# Functions used to download dataset from the internet
def download_file(url, download_dir):
    filename = url.split('/')[-1]
    file_path = os.path.join(download_dir, filename)
    if not os.path.exists(file_path):
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)
        file_path, _ = urllib.request.urlretrieve(url=url,
                                                  filename=file_path,
                                                  reporthook=download_progress)
        print("Download finished. Extracting files.")
        if file_path.endswith(".zip"):
            zipfile.ZipFile(file=file_path, mode="r").extractall(download_dir)
        elif file_path.endswith((".tar.gz", ".tgz")):
            tarfile.open(name=file_path, mode="r:gz").extractall(download_dir)
        print("Extraction Done.")
    else:
        print("Data already downloaded.")

def download_progress(count, block_size, total_size):
    """
    Function used to track the progress of a download.
    """
