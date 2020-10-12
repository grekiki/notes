import unittest
import random

class TestWebsite(unittest.TestCase):
  def dump_file_to_cache(self):
    with open("app/cache/"+str(random.random())+".txt","w") as f:
      f.write("spam")
      print("Dumped a file to ")
    return -1
  def test_a(self):
    self.assertNotEqual(0, self.dump_file_to_cache())

if __name__ == "__main__":
  unittest.main()