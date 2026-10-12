import unittest
import tasks


class TaskTests(unittest.TestCase):
    def setUp(self):
        tasks._tasks.clear()

    def test_add_task(self):
        t = tasks.add_task("a")
        self.assertEqual(t["title"], "a")

    def test_complete_task(self):
        t = tasks.add_task("a")
        self.assertTrue(tasks.complete_task(t["id"])["done"])


if __name__ == "__main__":
    unittest.main()
