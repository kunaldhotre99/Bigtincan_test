import unittest
import SubordinateModule

class TestSubordinateModule(unittest.TestCase): # defining a class for test

	def test_getSubOrdinates_Admin(self): # defining a test method for testing the output for admin's subordinates
		self.assertEqual(SubordinateModule.getSubOrdinates(1),[{'Id': 4, 'Name': 'Mary Manager', 'Role': 2}, 
			{'Id': 3, 'Name': 'Sam Supervisor', 'Role': 3}, 
			{'Id': 2, 'Name': 'Emily Employee', 'Role': 4}, 
			{'Id': 5, 'Name': 'Steve Trainer', 'Role': 5}])

	def test_getSubOrdinates_Employee(self): # defining a test method for testing the output for employee's subordinates
		self.assertEqual(SubordinateModule.getSubOrdinates(2),"User has no subordinates")

	def test_getSubOrdinates_Supervisor(self): # defining a test method for testing the output for supervisor's subordinates
		self.assertEqual(SubordinateModule.getSubOrdinates(3),[{'Id': 2, 'Name': 'Emily Employee', 'Role': 4}, 
			{'Id': 5, 'Name': 'Steve Trainer', 'Role': 5}])

	def test_getSubOrdinates_Manager(self): # defining a test method for testing the output for manager's subordinates
		self.assertEqual(SubordinateModule.getSubOrdinates(4),[{'Id': 3, 'Name': 'Sam Supervisor', 'Role': 3}, 
			{'Id': 2, 'Name': 'Emily Employee', 'Role': 4}, 
			{'Id': 5, 'Name': 'Steve Trainer', 'Role': 5}])

	def test_getSubOrdinates_Trainer(self): # defining a test method for testing the output for trainer's subordinates
		self.assertEqual(SubordinateModule.getSubOrdinates(5),"User has no subordinates")

	def test_getSubOrdinates_try_except(self): # defining a test method for testing the functions ability to catch exception.
		self.assertEqual(SubordinateModule.getSubOrdinates(6),"Value must be between 1 and 5")



if __name__ == '__main__':
	unittest.main()