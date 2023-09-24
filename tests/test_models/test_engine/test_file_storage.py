import unittest
import os
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()

    def test_all(self):
        result = self.storage.all()
        self.assertIsInstance(result, dict)

    def test_new(self):
        bm = BaseModel()
        self.storage.new(bm)
        key = "BaseModel." + bm.id
        self.assertIn(key, self.storage.all())

    def test_save_and_reload(self):
        bm = BaseModel()
        self.storage.new(bm)
        self.storage.save()

        self.assertTrue(os.path.exists('file.json'))
        self.storage.reload()
        self.assertIn("BaseModel." + bm.id, self.storage.all())

    def test_save(self):
        bm = BaseModel()
        time_before_save = datetime.utcnow()
        bm.save()
        self.assertTrue(bm.updated_at > time_before_save)

if __name__ == '__main__':
    unittest.main()
