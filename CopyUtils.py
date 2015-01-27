import hashlib
import sys
import os
import shutil


class Copy:
    def __init__(self):
        raise NotImplementedError

    def copy_dirs(self, list_of_dirs):
        raise NotImplementedError
        # check no duplicates in list

    def copy_files(self, list_of_files):
        raise NotImplementedError
        # check no duplicates

    def copy_dir(self):
        raise NotImplementedError

    def copy_file(self, from_file_path_name, destination_file_path_name):
        if not os.path.isfile(from_file_path_name):
            raise FileNotFoundError("File " + from_file_path_name + " does not exist.")

        if os.path.isfile(destination_file_path_name):
            raise FileExistsError("File " + destination_file_path_name + " already exists.")

        try:
            checksum_object = ChecksumCalculator()
            file_from_checksum = self.checksum_object.calculate_checksum(self.file_from)
            shutil.copy2(from_file_path_name, destination_file_path_name)
            to_file_checksum = checksum_object.calculate_checksum(destination_file_path_name)
            if file_from_checksum != to_file_checksum:
                os.remove(destination_file_path_name)
                return False
            else:
                return True
        except:
            print("Unexpected error: ")
            sys.exc_info()[0]
            raise


class ChecksumCalculator:
    def __init__(self):
        self.version_check()

    @staticmethod
    def version_check():
        if sys.version_info.major < 3:
            exit("Python 3 or greater is required.")
        elif sys.version_info.minor < 4:
            exit("You appear to have Python 3 - but less than 3.4, which is required.")
        else:
            pass

    @staticmethod
    def calculate_checksum(file_path_name):
        """
        :return: Returns a checksum string that can be compared to validate that two files contain the same data.
        """
        if file_path_name is None:
            exit("Missing parameter: File path name")

        NUM_OF_BYTES = 65536
        hash_func = hashlib.sha1()
        try:
            with open(file_path_name, 'rb') as temp_file:
                buf = temp_file.read(NUM_OF_BYTES)
                while len(buf) > 0:
                    hash_func.update(buf)
                    buf = temp_file.read(NUM_OF_BYTES)
            return hash_func.hexdigest()
        except IOError as e:
            print("Unexpected IO error: ")
            sys.exc_info()[0]
            raise
        except:
            try:
                raise RuntimeError("An error occurred during calculate_checksum re-raising...")
            finally:
                print("Unexpected error: ")
                sys.exc_info()[0]
                raise


def main():
    raise NotImplementedError

if __name__ == '__main__':
    main()