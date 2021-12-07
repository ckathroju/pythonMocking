#!/usr/bin/env python3

##
## A sample script showing construction and use of mocks
##

from unittest import mock
import unittest

# import the class we are testing
from gpa_calculator import gpa_calculation_mgr, gpa_converter, gpa_term_info

class gpaTestCase(unittest.TestCase):
	
	## TESTING BULLET POINT 1
	
	# Testing high, mid and low range values for A+

	def test_grade100(self):
		numerGrade = 100
		letter = gpa_converter.getLetterForNumericGrade(numerGrade)
		self.assertEqual(letter, "A+")
	
	def test_grade95(self):
		numerGrade = 95
		letter = gpa_converter.getLetterForNumericGrade(numerGrade)
		self.assertEqual(letter, "A+")
		
	def test_grade90(self):
		numerGrade = 90
		letter = gpa_converter.getLetterForNumericGrade(numerGrade)
		self.assertEqual(letter, "A+")

	# Testing high, mid and low range values for A

	def test_grade89(self):
		numerGrade = 89
		letter = gpa_converter.getLetterForNumericGrade(numerGrade)
		self.assertEqual(letter, "A")

	def test_grade87(self):
		numerGrade = 87
		letter = gpa_converter.getLetterForNumericGrade(numerGrade)
		self.assertEqual(letter, "A")

	def test_grade85(self):
		numerGrade = 85
		letter = gpa_converter.getLetterForNumericGrade(numerGrade)
		self.assertEqual(letter, "A")

	# Testing high, mid and low range values for A-

	def test_grade84(self):
		numerGrade = 84
		letter = gpa_converter.getLetterForNumericGrade(numerGrade)
		self.assertEqual(letter, "A-")

	def test_grade82(self):
		numerGrade = 82
		letter = gpa_converter.getLetterForNumericGrade(numerGrade)
		self.assertEqual(letter, "A-")

	def test_grade80(self):
		numerGrade = 80
		letter = gpa_converter.getLetterForNumericGrade(numerGrade)
		self.assertEqual(letter, "A-")

	# Testing high, mid and low range values for B+

	def test_grade79(self):
		numerGrade = 79
		letter = gpa_converter.getLetterForNumericGrade(numerGrade)
		self.assertEqual(letter, "B+")

	def test_grade78(self):
		numerGrade = 78
		letter = gpa_converter.getLetterForNumericGrade(numerGrade)
		self.assertEqual(letter, "B+")

	def test_grade77(self):
		numerGrade = 77
		letter = gpa_converter.getLetterForNumericGrade(numerGrade)
		self.assertEqual(letter, "B+")

	# Testing high, mid and low range values for B

	def test_grade76(self):
		numerGrade = 76
		letter = gpa_converter.getLetterForNumericGrade(numerGrade)
		self.assertEqual(letter, "B")

	def test_grade74_5(self):
		numerGrade = 74.5
		letter = gpa_converter.getLetterForNumericGrade(numerGrade)
		self.assertEqual(letter, "B")

	def test_grade73(self):
		numerGrade = 73
		letter = gpa_converter.getLetterForNumericGrade(numerGrade)
		self.assertEqual(letter, "B")

	# Testing high, mid and low range values for B-

	def test_grade72(self):
		numerGrade = 72
		letter = gpa_converter.getLetterForNumericGrade(numerGrade)
		self.assertEqual(letter, "B-")

	def test_grade71(self):
		numerGrade = 71
		letter = gpa_converter.getLetterForNumericGrade(numerGrade)
		self.assertEqual(letter, "B-")

	def test_grade70(self):
		numerGrade = 70
		letter = gpa_converter.getLetterForNumericGrade(numerGrade)
		self.assertEqual(letter, "B-")

	# Testing high, mid and low range values for C+

	def test_grade69(self):
		numerGrade = 69
		letter = gpa_converter.getLetterForNumericGrade(numerGrade)
		self.assertEqual(letter, "C+")

	def test_grade68(self):
		numerGrade = 68
		letter = gpa_converter.getLetterForNumericGrade(numerGrade)
		self.assertEqual(letter, "C+")

	def test_grade67(self):
		numerGrade = 67
		letter = gpa_converter.getLetterForNumericGrade(numerGrade)
		self.assertEqual(letter, "C+")

	# Testing high, mid and low range values for C

	def test_grade66(self):
		numerGrade = 66
		letter = gpa_converter.getLetterForNumericGrade(numerGrade)
		self.assertEqual(letter, "C")

	def test_grade64_5(self):
		numerGrade = 64.5
		letter = gpa_converter.getLetterForNumericGrade(numerGrade)
		self.assertEqual(letter, "C")

	def test_grade63(self):
		numerGrade = 63
		letter = gpa_converter.getLetterForNumericGrade(numerGrade)
		self.assertEqual(letter, "C")

	# Testing high, mid and low range values for C-

	def test_grade62(self):
		numerGrade = 62
		letter = gpa_converter.getLetterForNumericGrade(numerGrade)
		self.assertEqual(letter, "C-")

	def test_grade61(self):
		numerGrade = 61
		letter = gpa_converter.getLetterForNumericGrade(numerGrade)
		self.assertEqual(letter, "C-")

	def test_grade60(self):
		numerGrade = 60
		letter = gpa_converter.getLetterForNumericGrade(numerGrade)
		self.assertEqual(letter, "C-")

	# Testing high, mid and low range values for D+

	def test_grade59(self):
		numerGrade = 59
		letter = gpa_converter.getLetterForNumericGrade(numerGrade)
		self.assertEqual(letter, "D+")

	def test_grade58(self):
		numerGrade = 58
		letter = gpa_converter.getLetterForNumericGrade(numerGrade)
		self.assertEqual(letter, "D+")

	def test_grade57(self):
		numerGrade = 57
		letter = gpa_converter.getLetterForNumericGrade(numerGrade)
		self.assertEqual(letter, "D+")

	# Testing high, mid and low range values for D

	def test_grade56(self):
		numerGrade = 56
		letter = gpa_converter.getLetterForNumericGrade(numerGrade)
		self.assertEqual(letter, "D")

	def test_grade54_5(self):
		numerGrade = 54.5
		letter = gpa_converter.getLetterForNumericGrade(numerGrade)
		self.assertEqual(letter, "D")

	def test_grade53(self):
		numerGrade = 53
		letter = gpa_converter.getLetterForNumericGrade(numerGrade)
		self.assertEqual(letter, "D")

	# Testing high, mid and low range values for D-

	def test_grade52(self):
		numerGrade = 52
		letter = gpa_converter.getLetterForNumericGrade(numerGrade)
		self.assertEqual(letter, "D-")

	def test_grade51(self):
		numerGrade = 51
		letter = gpa_converter.getLetterForNumericGrade(numerGrade)
		self.assertEqual(letter, "D-")

	def test_grade50(self):
		numerGrade = 50
		letter = gpa_converter.getLetterForNumericGrade(numerGrade)
		self.assertEqual(letter, "D-")

	# Testing high, mid and low range values for F

	def test_grade49(self):
		numerGrade = 49
		letter = gpa_converter.getLetterForNumericGrade(numerGrade)
		self.assertEqual(letter, "F")

	def test_grade24_5(self):
		numerGrade = 24.5
		letter = gpa_converter.getLetterForNumericGrade(numerGrade)
		self.assertEqual(letter, "F")

	def test_grade0(self):
		numerGrade = 0
		letter = gpa_converter.getLetterForNumericGrade(numerGrade)
		self.assertEqual(letter, "F")
	
	## TESTING BULLET POINT 2

	# Check if grades for 90 - 100% are added to the list

	@mock.patch.object(gpa_converter, 'getLetterForNumericGrade', autospec=True)
	def test_getLetter90_100(self, mock_getLetter):

		student = gpa_calculation_mgr.calc_manager("STUDENT", "ID")
		student.addNumericGrade("Fall 2021", 100)
		mock_getLetter.assert_called_with(100)
		student.addNumericGrade("Fall 2021", 95)
		mock_getLetter.assert_called_with(95)
		student.addNumericGrade("Fall 2021", 90)
		mock_getLetter.assert_called_with(90)
		mock_getLetter.assert_called()

	# Check if grades for 85 - 89% are added to the list

	@mock.patch.object(gpa_converter, 'getLetterForNumericGrade', autospec=True)
	def test_getLetter85_89(self, mock_getLetter):

		student = gpa_calculation_mgr.calc_manager("STUDENT", "ID")
		student.addNumericGrade("Fall 2021", 89)
		mock_getLetter.assert_called_with(89)
		student.addNumericGrade("Fall 2021", 97)
		mock_getLetter.assert_called_with(97)
		student.addNumericGrade("Fall 2021", 85)
		mock_getLetter.assert_called_with(85)
		mock_getLetter.assert_called()

	# Check if grades for 80 - 84% are added to the list

	@mock.patch.object(gpa_converter, 'getLetterForNumericGrade', autospec=True)
	def test_getLetter80_84(self, mock_getLetter):

		student = gpa_calculation_mgr.calc_manager("STUDENT", "ID")
		student.addNumericGrade("Fall 2021", 84)
		mock_getLetter.assert_called_with(84)
		student.addNumericGrade("Fall 2021", 82)
		mock_getLetter.assert_called_with(82)
		student.addNumericGrade("Fall 2021", 80)
		mock_getLetter.assert_called_with(80)
		mock_getLetter.assert_called()

	# Check if grades for 77 - 79% are added to the list

	@mock.patch.object(gpa_converter, 'getLetterForNumericGrade', autospec=True)
	def test_getLetter77_79(self, mock_getLetter):

		student = gpa_calculation_mgr.calc_manager("STUDENT", "ID")
		student.addNumericGrade("Fall 2021", 79)
		mock_getLetter.assert_called_with(79)
		student.addNumericGrade("Fall 2021", 78)
		mock_getLetter.assert_called_with(78)
		student.addNumericGrade("Fall 2021", 77)
		mock_getLetter.assert_called_with(77)
		mock_getLetter.assert_called()

	# Check if grades for 73 - 76% are added to the list

	@mock.patch.object(gpa_converter, 'getLetterForNumericGrade', autospec=True)
	def test_getLetter73_76(self, mock_getLetter):

		student = gpa_calculation_mgr.calc_manager("STUDENT", "ID")
		student.addNumericGrade("Fall 2021", 76)
		mock_getLetter.assert_called_with(76)
		student.addNumericGrade("Fall 2021", 74.5)
		mock_getLetter.assert_called_with(74.5)
		student.addNumericGrade("Fall 2021", 73)
		mock_getLetter.assert_called_with(73)
		mock_getLetter.assert_called()

	# Check if grades for 70 - 72% are added to the list

	@mock.patch.object(gpa_converter, 'getLetterForNumericGrade', autospec=True)
	def test_getLetter70_72(self, mock_getLetter):

		student = gpa_calculation_mgr.calc_manager("STUDENT", "ID")
		student.addNumericGrade("Fall 2021", 72)
		mock_getLetter.assert_called_with(72)
		student.addNumericGrade("Fall 2021", 71)
		mock_getLetter.assert_called_with(71)
		student.addNumericGrade("Fall 2021", 70)
		mock_getLetter.assert_called_with(70)
		mock_getLetter.assert_called()

	# Check if grades for 67 - 69% are added to the list

	@mock.patch.object(gpa_converter, 'getLetterForNumericGrade', autospec=True)
	def test_getLetter67_69(self, mock_getLetter):

		student = gpa_calculation_mgr.calc_manager("STUDENT", "ID")
		student.addNumericGrade("Fall 2021", 69)
		mock_getLetter.assert_called_with(69)
		student.addNumericGrade("Fall 2021", 68)
		mock_getLetter.assert_called_with(68)
		student.addNumericGrade("Fall 2021", 67)
		mock_getLetter.assert_called_with(67)
		mock_getLetter.assert_called()

	# Check if grades for 63 - 66% are added to the list

	@mock.patch.object(gpa_converter, 'getLetterForNumericGrade', autospec=True)
	def test_getLetter63_66(self, mock_getLetter):

		student = gpa_calculation_mgr.calc_manager("STUDENT", "ID")
		student.addNumericGrade("Fall 2021", 66)
		mock_getLetter.assert_called_with(66)
		student.addNumericGrade("Fall 2021", 64.5)
		mock_getLetter.assert_called_with(64.5)
		student.addNumericGrade("Fall 2021", 63)
		mock_getLetter.assert_called_with(63)
		mock_getLetter.assert_called()

	# Check if grades for 60 - 62% are added to the list

	@mock.patch.object(gpa_converter, 'getLetterForNumericGrade', autospec=True)
	def test_getLetter60_62(self, mock_getLetter):

		student = gpa_calculation_mgr.calc_manager("STUDENT", "ID")
		student.addNumericGrade("Fall 2021", 62)
		mock_getLetter.assert_called_with(62)
		student.addNumericGrade("Fall 2021", 61)
		mock_getLetter.assert_called_with(61)
		student.addNumericGrade("Fall 2021", 60)
		mock_getLetter.assert_called_with(60)
		mock_getLetter.assert_called()

	# Check if grades for 57 - 59% are added to the list

	@mock.patch.object(gpa_converter, 'getLetterForNumericGrade', autospec=True)
	def test_getLetter57_59(self, mock_getLetter):

		student = gpa_calculation_mgr.calc_manager("STUDENT", "ID")
		student.addNumericGrade("Fall 2021", 59)
		mock_getLetter.assert_called_with(59)
		student.addNumericGrade("Fall 2021", 58)
		mock_getLetter.assert_called_with(58)
		student.addNumericGrade("Fall 2021", 57)
		mock_getLetter.assert_called_with(57)
		mock_getLetter.assert_called()

	# Check if grades for 53 - 56% are added to the list

	@mock.patch.object(gpa_converter, 'getLetterForNumericGrade', autospec=True)
	def test_getLetter53_56(self, mock_getLetter):

		student = gpa_calculation_mgr.calc_manager("STUDENT", "ID")
		student.addNumericGrade("Fall 2021", 56)
		mock_getLetter.assert_called_with(56)
		student.addNumericGrade("Fall 2021", 54.5)
		mock_getLetter.assert_called_with(54.5)
		student.addNumericGrade("Fall 2021", 53)
		mock_getLetter.assert_called_with(53)
		mock_getLetter.assert_called()

	# Check if grades for 50 - 52% are added to the list

	@mock.patch.object(gpa_converter, 'getLetterForNumericGrade', autospec=True)
	def test_getLetter50_52(self, mock_getLetter):

		student = gpa_calculation_mgr.calc_manager("STUDENT", "ID")
		student.addNumericGrade("Fall 2021", 52)
		mock_getLetter.assert_called_with(52)
		student.addNumericGrade("Fall 2021", 51)
		mock_getLetter.assert_called_with(51)
		student.addNumericGrade("Fall 2021", 50)
		mock_getLetter.assert_called_with(50)
		mock_getLetter.assert_called()

	# Check if grades for 0 - 49% are added to the list

	@mock.patch.object(gpa_converter, 'getLetterForNumericGrade', autospec=True)
	def test_getLetter0_49(self, mock_getLetter):

		student = gpa_calculation_mgr.calc_manager("STUDENT", "ID")
		student.addNumericGrade("Fall 2021", 49)
		mock_getLetter.assert_called_with(49)
		student.addNumericGrade("Fall 2021", 24.5)
		mock_getLetter.assert_called_with(24.5)
		student.addNumericGrade("Fall 2021", 0)
		mock_getLetter.assert_called_with(0)
		mock_getLetter.assert_called()

	## TESTING BULLET POINT 3
	
	# Testing if letter grade results a GPA for the matching term

	def test_termLetter(self):
		student = gpa_calculation_mgr.calc_manager("STUDENT", "ID")
		student.addLetterGrade("Fall 2021", "A+")
		gpa = gpa_converter.getGPAforLetterGrade("A+")
		self.assertEqual(gpa, 4.3)

	# Testing if numeric grade results a GPA for the matching term

	def test_termNumeric(self):
		student = gpa_calculation_mgr.calc_manager("STUDENT", "ID")
		student.addNumericGrade("Fall 2021", 89)
		gpa = gpa_converter.getGPAforNumericGrade(89)
		self.assertEqual(gpa, 4.0)
	
	# Testing removing a term

	def test_removeTerm(self):
		student = gpa_calculation_mgr.calc_manager("STUDENT", "ID")
		student.addLetterGrade("Fall 2021", "A+")
		student.removeInfoForTerm("Fall 2021")
		result = student.getTermGPA("Fall 2021")
		self.assertEqual(float('-inf'), result)
	
	# Testing adding and removing two terms

	def test_removeTwoTerms(self):
		student = gpa_calculation_mgr.calc_manager("STUDENT", "ID")
		student.addLetterGrade("Fall 2021", "A+")
		student.addLetterGrade("Winter 2022", "B+")
		student.removeInfoForTerm("Fall 2021")
		gpa = student.getTermGPA("Fall 2021")
		gpaTerm22 = student.getTermGPA("Winter 2022")
		self.assertEqual(float('-inf'), gpa)
		self.assertEqual(gpaTerm22, 3.3)

## If being run as a program, run the test suite.
## This allows this suite to be loaded and run within other
## larger test suites and treated as a module
if __name__ == '__main__':
        unittest.main()
