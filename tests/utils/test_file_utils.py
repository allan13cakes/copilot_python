import os
import unittest


class TestFileUtils(unittest.TestCase):
    def test_get_root_folder(self):
        from utils.file_utils import get_root_folder
        root_folder = get_root_folder()
        self.assertTrue(os.path.exists(root_folder))
        print(root_folder)

    def test_get_project_folder(self):
        from utils.file_utils import get_project_folder
        project_folder = get_project_folder()
        self.assertTrue(os.path.exists(project_folder))
        print(project_folder)