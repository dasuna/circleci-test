# Import the Add function, and assert that it works correctly.
from main import Add

def TestAdd():
        assert Add(2,3) == 5
        print("Add Function works correctly")

def TestSub():
	assert Subtract(7,4) == 3
	print("Subtract Function works correctly")

if __name__ == '__main__':
        TestAdd()
	TestAdd()
	
