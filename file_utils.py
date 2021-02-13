import os
import shutil

DEBUG = False


def zip_folder(folder_path: str) -> (str, str):
    print(f'ZIPPING {folder_path}\n')
    name = os.path.basename(folder_path)
    archive_from = os.path.dirname(folder_path)
    archive_to = os.path.basename(folder_path.strip(os.sep))
    if not DEBUG:
        shutil.make_archive(name, 'zip', archive_from, archive_to)
        try:
            shutil.move('%s.%s' % (name, 'zip'), archive_from)
        except:
            pass
        return folder_path, f'{folder_path}.zip'
    return folder_path, folder_path


def unzip_folder(folder_path: str) -> str:
    print(f'UNZIPPING {folder_path}\n')
    if not DEBUG:
        name = os.path.basename(folder_path)
        archive_from = os.path.dirname(folder_path)
        shutil.unpack_archive(folder_path, archive_from)
        # shutil.move('%s'%(name), 'extract')
    return os.path.join(archive_from, name)


def delete_file(file_path: str):
    try:
        print('DELETING File: ', file_path, '\n')
        if not DEBUG:
            os.remove(file_path)
    except:
        print('ERROR: File cannot be deleted or does not exist')


def delete_folder(folder_path: str) -> None:
    try:
        print('DELETING Folder: ', folder_path, '\n')
        if not DEBUG:
            shutil.rmtree(folder_path)
    except:
        print('ERROR: Folder cannot be deleted or does not exist')


def read_file(file_path: str) -> bytes:
    print('READING:', file_path, '\n')
    if not DEBUG:
        r = open(file_path, "rb")
        fileBytes = r.read()
        r.close()
        return fileBytes
    return b''


def write_file(file_path: str, bytes_to_write: bytes) -> str:
    print('WRITING BYTES to', file_path, '\n')
    if not DEBUG:
        with open(file_path, 'wb') as f:
            f.write(bytes_to_write)
        return file_path
    return None


def merk(file_path: str) -> str:
    '''
    Renames target file by adding .merk extension
    '''
    print('MERKing', file_path, '\n')
    if not DEBUG:
        oldPath = file_path
        newPath = f'{file_path}.merk'
        os.rename(oldPath, newPath)
        return newPath
    return file_path


def unmerk(file_path: str) -> str:
    '''
    Renames target file by removing .merk extension
    '''
    print('unMERKing', file_path, '\n')
    if not DEBUG:
        if '.merk' in file_path:
            oldPath = file_path
            newPath = file_path[:-5]
            os.rename(oldPath, newPath)
            return newPath
    return file_path
