import unittest

from tasks import add_task, complete_task, delete_task


class TestTaskManager(unittest.TestCase):
    def test_add_task(self):
        tasks = []
        task = add_task(tasks, "Study DevOps")
        self.assertEqual(len(tasks), 1)
        self.assertEqual(task["title"], "Study DevOps")
        self.assertFalse(task["done"])

    def test_add_empty_title_rejected(self):
        with self.assertRaises(ValueError):
            add_task([], "   ")

    def test_complete_task(self):
        tasks = []
        add_task(tasks, "Write report")
        complete_task(tasks, 1)
        self.assertTrue(tasks[0]["done"])

    def test_delete_task(self):
        tasks = []
        add_task(tasks, "Old task")
        delete_task(tasks, 1)
        self.assertEqual(len(tasks), 0)

    def test_delete_invalid_id(self):
        with self.assertRaises(ValueError):
            delete_task([], 99)


if __name__ == "__main__":
    unittest.main()