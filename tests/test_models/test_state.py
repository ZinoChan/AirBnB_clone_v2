import unittest
from models.state import State
from models.base_model import BaseModel

class TestState(unittest.TestCase):

    def setUp(self):
        """Set up testing instance"""
        self.state = State()

    def tearDown(self):
        """Tear down testing instance"""
        del self.state

    def test_instance_type(self):
        """Test if state is of type State"""
        self.assertIsInstance(self.state, State)

    def test_inheritance(self):
        """Test if State class inherits from BaseModel"""
        self.assertTrue(issubclass(self.state.__class__, BaseModel))

    def test_attribute_name_default(self):
        """Test if attribute 'name' is an empty string by default"""
        self.assertEqual(self.state.name, "")

    def test_attribute_name_assignment(self):
        """Test assignment to attribute 'name'"""
        new_name = "California"
        self.state.name = new_name
        self.assertEqual(self.state.name, new_name)


if __name__ == "__main__":
    unittest.main()
