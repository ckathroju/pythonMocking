# Author Information
**Siri Chandana Kathroju**

**12/3/2021**

# A3 Starter Code

This directory contains an updated GPA calculator library within the
subdirectory `gpa_calculator` as well a sample to start your test
suite


# How to Run

Run the test suite using this command:

	python3 mock_sample.py


# TESTING BULLET POINT 1

**1. What the test case will verify?**

Each of the test cases will verify the high, middle and low range numerical values for grades A+ to F. The getLetterForNumericGrade() method will retrieve a letter grade for the numeric grade. It then calls the assertEqual() method to check if the letter matches the grade that's passed into the function.

*NOTE: This process continues for all the grades from 100 to 0 or A+ to F*

For example,

numerGrade = 100, 95 and 90 will be converted to a letter by gpa_converter.getLetterForNumericGrade(numerGrade) and self.assertEqual(letter, "A+") will check if the letter matches A+

numerGrade = 89, 87, 85 will be converted to a letter by gpa_converter.getLetterForNumericGrade(numerGrade) and self.assertEqual(letter, "A") will check if the letter matches A

numerGrade = 69, 68, 67 will be converted to a letter by gpa_converter.getLetterForNumericGrade(numerGrade) and self.assertEqual(letter, "C") will check if the letter matches C

**2. Whether mocks are used, and if so, how?**

Mocks were not used for these test cases.

**3. What supplied arguments will be provided, and to which functions?**

numericGrade = 100, 95, 90, 89, 87, 85, 84, 82, 80, 79, 78, 77, 76, 74.5, 73, 72, 71, 70, 69, 68, 67, 66, 64.5, 63, 62, 61, 60, 59, 58, 57, 56, 54.5, 53, 52, 51, 50, 49, 24.5 or 0

-- Testing high, mid and low range values for A+ --

getLetterForNumericGrade(percentageGrade)
--> letter = gpa_converter.getLetterForNumericGrade(numerGrade)

"A+", "A", "A-", 
"B+", "B", "B-", 
"C+", "C", "C-", 
"D+", "D", "D-", or 
"F"

--> self.assertEqual(letter, "A+")

**4. What expected values will be observed?**

| Function | Expected Value |
|----------|----------------|
| test_grade100 | 'A+' |
| test_grade95 | 'A+' |
| test_grade90 | 'A+' |
| test_grade89 | 'A' |
| test_grade87 | 'A' |
| test_grade85 | 'A' |
| test_grade84 | 'A-' |
| test_grade82 | 'A-' |
| test_grade80 | 'A-' |
| test_grade79 | 'B+' |
| test_grade78 | 'B+' |
| test_grade77 | 'B+' |
| test_grade76 | 'B' |
| test_grade74_5 | 'B' |
| test_grade73 | 'B' |
| test_grade72 | 'B-' |
| test_grade71 | 'B-' |
| test_grade70 | 'B-' |
| test_grade69 | 'C+' |
| test_grade68 | 'C+' |
| test_grade67 | 'C+' |
| test_grade66 | 'C' |
| test_grade64_5 | 'C' |
| test_grade63 | 'C' |
| test_grade62 | 'C-' |
| test_grade61 | 'C-' |
| test_grade60 | 'C-' |
| test_grade59 | 'D+' |
| test_grade58 | 'D+' |
| test_grade57 | 'D+' |
| test_grade56 | 'D' |
| test_grade54_5 | 'D' |
| test_grade53 | 'D' |
| test_grade52 | 'D-' |
| test_grade51 | 'D-' |
| test_grade50 | 'D-' |
| test_grade49 | 'F' |
| test_grade24_5 | 'F' |
| test_grade0 | 'F' |

# Test Status

**5. This section lists each test in the suite, and its current status (PASS or FAIL)**

test_grade100 (PASS)
test_grade95 (PASS)
test_grade90 (PASS)

test_grade89 (PASS)
test_grade87 (PASS)
test_grade85 (PASS)

test_grade84 (PASS)
test_grade82 (PASS)
test_grade80 (PASS)

test_grade79 (PASS)
test_grade78 (PASS)
test_grade77 (PASS)

test_grade76 (PASS)
test_grade74_5 (PASS)
test_grade73 (PASS)

test_grade72 (PASS)
test_grade71 (PASS)
test_grade70 (PASS)

test_grade69 (PASS)
test_grade68 (PASS)
test_grade67 (PASS)

test_grade66 (PASS)
test_grade64_5 (PASS)
test_grade63 (PASS)

test_grade62 (PASS)
test_grade61 (PASS)
test_grade60 (PASS)

test_grade59 (PASS)
test_grade58 (PASS)
test_grade57 (PASS)

test_grade56 (PASS)
test_grade54_5 (PASS)
test_grade53 (PASS)

test_grade52 (PASS)
test_grade51 (PASS)
test_grade50 (PASS)

test_grade49 (PASS)
test_grade24_5 (PASS)
test_grade0 (PASS)

# TESTING BULLET POINT 2

**1. What the test case will verify?**

Each of the test cases will verify if the addition of grades call the lettergrade conversion functions the appropriate number of times. The getLetterForNumericGrade() conversion function retrieves the letter grade for the high, middle and low numeric grades. The addNumericGrade() will check if those numerical grades have been successfully added to the list/term.

*NOTE: This process continues for all the grades from 100 to 0 or A+ to F*

For example,

Calls the getLetterForNumericGrade for grades 100, 95 and 90 and student.addNumericGrade(self, term, percentageGrade) will check if each of those grades; 100, 95 and 90 have been added to the term; Fall 2021

Calls the getLetterForNumericGrade for grades 79, 78 and 77 and student.addNumericGrade(self, term, percentageGrade) will check if all each of those grades; 79, 78 and 77 have been added to the term; Fall 2021

Calls the getLetterForNumericGrade for grades 62, 61 and 60 and student.addNumericGrade(self, term, percentageGrade) will check if all each of those grades; 62, 61 and 60 have been added to the term; Fall 2021

**2. Whether mocks are used, and if so, how?**

Mocks were used for these test cases. It allows me to replace parts that are part of the system under test with mock objects and makes assertions about how they have been used. I didn't have to make stubs throughout the test suite and simply just made assertions for the methods that were being used and arguments they were called with. I used the @mock.patch.object to replace a method on the gpa_converter, and see if it was called correctly

I chose to use @mock.patch.object to make calls to addNumericGrade() through the gpa_converter object level.
I used this because it replaces only a single method that I wanted to test on the gpa_converter object, the method being getLetterForNumericGrade().

**3. What supplied arguments will be provided, and to which functions?**

--> term = "Fall 2021"

--> percentageGrade = 100, 95, 90, 89, 87, 85, 84, 82, 80, 79, 78, 77, 76, 74.5, 73, 72, 71, 70, 69, 68, 67, 66, 64.5, 63, 62, 61, 60, 59, 58, 57, 56, 54.5, 53, 52, 51, 50, 49, 24.5 or 0

-- Check if grades for 90 - 100% are added to the list --

getLetterForNumericGrade(percentageGrade)

addNumericGrade(self, term, percentageGrade)
--> student.addNumericGrade("Fall 2021", 100)
--> mock_getLetter.assert_called_with(100)

--> student.addNumericGrade("Fall 2021", 95)
--> mock_getLetter.assert_called_with(95)

--> student.addNumericGrade("Fall 2021", 90)
--> mock_getLetter.assert_called_with(90)

mock_getLetter.assert_called()

**4. What expected values will be observed?**

| Function | Expected Value |
|----------|----------------|
| test_getLetter90_100 | 100, 95, 90 |
| test_getLetter85_89 | 89, 87, 85 |
| test_getLetter80_84 | 84, 82, 80 |
| test_getLetter77_79 | 79, 78, 77 |
| test_getLetter73_76 | 76, 74.5, 73 |
| test_getLetter70_72 | 72, 71, 70 |
| test_getLetter67_69 | 69, 68, 67 |
| test_getLetter63_66 | 66, 64.5, 63|
| test_getLetter60_62 | 62, 61, 60 |
| test_getLetter57_59 | 59, 58, 57 |
| test_getLetter53_56 | 56, 54.5, 53 |
| test_getLetter50_52 | 52, 51, 50 |
| test_getLetter0_49 | 49, 24.5, 0 |

# Test Status

**5. This section lists each test in the suite, and its current status (PASS or FAIL)**

test_getLetter90_100 (PASS)

test_getLetter85_89 (PASS)

test_getLetter80_84 (PASS)

test_getLetter77_79 (PASS)

test_getLetter73_76 (PASS)

test_getLetter70_72 (PASS)

test_getLetter67_69 (PASS)

test_getLetter63_66 (PASS)

test_getLetter60_62 (PASS)

test_getLetter57_59 (PASS)

test_getLetter53_56 (PASS)

test_getLetter50_52 (PASS)

test_getLetter0_49 (PASS)

# TESTING BULLET POINT 3

**1. What the test case will verify?**

The test cases; test_termLetter and test_termNumeric check if the right grades are being placed into the terms correctly and test case; test_removeTerm checks if the term info gets removed correctly, it will return negative infinity if the term doesn't exist. test_removeTwoTerms checks if the right GPA gets displayed appropriately for two different terms, whether a term does or does not get removed.

The addLetterGrade() and getGPAforLetterGrade() methods will add the letter grade to the list and tests if the letter grades results the right GPA for self term. The addNumericGrade() and getGPAforNumericGrade will add the numeric grade to the list and checks if the numeric grades results the right GPA for self term. assertEqual will check if the GPA value and the passed in value. 

The addLetterGrade() method will add a letter grade to the list/term and the removeInfoForTerm() will remove the entire term. The getTermGPA() will retrieve a GPA for the matching term if it exists otherwise assertEqual will return a negative infinity.

**2. Whether mocks are used, and if so, how?**

Mocks were not used for these test cases.

**3. What supplied arguments will be provided, and to which functions?**

-- Testing if letter grade results a GPA for the matching term --

addLetterGrade(self, termName, lettergrade)
--> addLetterGrade("Fall 2021", "A+")

getGPAforLetterGrade(grade)
--> getGPAforLetterGrade("A+")

-- Testing if numeric grade results a GPA for the matching term --

addNumericGrade(self, term, percentageGrade)
--> addNumericGrade("Fall 2021", 89)

getGPAforNumericGrade(percentageGrade)
--> getGPAforNumericGrade(89)

-- Testing removing a term --

removeInfoForTerm(self, termName)
--> removeInfoForTerm("Fall 2021")

getTermGPA(self, termName)
--> getTermGPA("Fall 2021")

-- Testing adding and removing two terms --

--> addLetterGrade("Fall 2021", "A+")
--> addLetterGrade("Winter 2022", "B+")
--> removeInfoForTerm("Fall 2021")
--> gpa = student.getTermGPA("Fall 2021")

This will result a negative infinity because the term does not exist anymore.

--> gpaTerm22 = student.getTermGPA("Winter 2022")

This will return a GPA of 3.3 for a letter grade of B+

**4. What expected values will be observed?**

# Test Status

| Function | Expected Value |
|----------|----------------|
| test_termLetter | 4.3 |
| test_termNumeric | 4.0 |
| test_removeTerm | '-inf' |

**5. This section lists each test in the suite, and its current status (PASS or FAIL)**

test_termLetter (PASS)

test_termNumeric (PASS)

test_removeTerm (PASS)

test_removeTwoTerms (PASS)
