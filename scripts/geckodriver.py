import os
import shutil
import tarfile
import urllib.request


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class GeckoDriver:
    """Class GeckoDriver to install geckodriver for firefox browsers

    USAGE:
            GeckoDriver(version='v0.24.0', platform='linux64')

    """

    def __init__(self, version='v0.24.0', platform='linux64'):
        self.version = version

        if platform in {'linux32', 'linux64', 'macos', 'win32', 'win64'}:
            self.platform = platform
        else:
            raise AttributeError('check the platform attribute!')

        self.geckodriver_raw_url = "https://github.com/mozilla/geckodriver/releases/download/"

        self.filename = 'geckodriver-' + self.version + '-' + self.platform + '.tar.gz'

        self.geckodriver_download_url = self.geckodriver_raw_url + self.version + '/' + self.filename

        self.current_dir = ROOT_DIR

        self.PATH_dir = '/usr/local/bin'

    @staticmethod
    def is_installed():
        """checks if 'geckodriver' is already installed

        :return: boolean, True if geckodriver is already installed
        """

        if shutil.which("geckodriver") is None:
            return False
        else:
            return True

    def download(self):
        """downloads the geckodriver tarball
        """
        try:
            loc_filename, headers = urllib.request.urlretrieve(self.geckodriver_download_url, filename=self.current_dir + '/' + self.filename)
            self.__extract()
            self.__add_to_path()
        except Exception as e:
            print(e)

    def __extract(self):
        """extracts the geckodriver tarball
        """

        save_path = os.getcwd()

        for file in os.listdir(self.current_dir):
            if file.endswith('tar.gz'):
                os.chdir(self.current_dir)
                tar = tarfile.open(file, 'r:gz')
                tar.extractall()
                tar.close()
                os.remove(file)

        os.chdir(save_path)

    def __add_to_path(self):
        """adds the geckodriver to '/usr/local/bin'
        """
        # move geckodriver to /usr/local/bin/
        try:

            shutil.move(self.current_dir + '/geckodriver', self.PATH_dir)

        except PermissionError:
            print("PermissionError: check permission for moving geckodriver to '/usr/local/bin' !")
        except shutil.Error as e:
            print(e)


if __name__ == '__main__':
    if GeckoDriver().is_installed():
        GeckoDriver().download()

