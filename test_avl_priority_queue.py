import unittest
from avl_priority_queue import AVLPriorityQueue
class TestAVLPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.pq = AVLPriorityQueue()

    def test_insert_and_extract_order(self):
        self.pq.insert("Завдання 1", 10)
        self.pq.insert("Завдання 2", 100)
        self.pq.insert("Завдання 3", 50)
        
        self.assertEqual(self.pq.extract_max(), ("Завдання 2", 100))
        self.assertEqual(self.pq.extract_max(), ("Завдання 3", 50))
        self.assertEqual(self.pq.extract_max(), ("Завдання 1", 10))

    def test_same_priority(self):
        self.pq.insert("A", 20)
        self.pq.insert("B", 20)
        self.pq.insert("C", 20)

        extracted = []
        for _ in range(3):
            val, prio = self.pq.extract_max()
            self.assertEqual(prio, 20)
            extracted.append(val)

        self.assertCountEqual(extracted, ["A", "B", "C"])

    def test_peek(self):
        self.pq.insert("Низький", 5)
        self.pq.insert("Високий", 99)
        self.assertEqual(self.pq.peek(), ("Високий", 99))
        self.assertEqual(self.pq.peek(), ("Високий", 99)) 
    
        self.assertEqual(self.pq.extract_max(), ("Високий", 99))
        self.assertEqual(self.pq.peek(), ("Низький", 5))

    def test_empty_queue_exceptions(self):
        with self.assertRaises(IndexError):
            self.pq.peek()
            
        with self.assertRaises(IndexError):
            self.pq.extract_max()

    def test_avl_balancing_stress_test(self):
        for i in range(1, 1001):
            self.pq.insert(f"Task_{i}", i)
            
        for i in range(1000, 0, -1):
            val, prio = self.pq.extract_max()
            self.assertEqual(prio, i)

if __name__ == '__main__':
    unittest.main()