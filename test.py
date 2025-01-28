import os
import sys

def test_command(cmd):
  print(os.system(cmd))

if __name__ == "__main__"
  test_command(sys.argv[1])
