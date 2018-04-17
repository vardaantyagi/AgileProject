import unittest
from methods import US15, US21_Wife, US21_Husband, US22, US30, US42

class TestCases(unittest.TestCase):

#Tests for US15 (Fewer than 15 siblings): There should be fewer than 15 siblings in a family
    def test_US15_lessthan15(self):
        array = [1,2,3]
        husb = "Ahusband"
        wife = "Awife"
        self.assertTrue(US15(array, husb, wife))

    def test_US15_exactly15(self):
        array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        husb = "Ahusband"
        wife = "Awife"
        self.assertFalse(US15(array, husb, wife))

    def test_US15_morethan15(self):
        array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        husb = "Ahusband"
        wife = "Awife"
        self.assertFalse(US15(array, husb, wife))

#Tests for US21 Correct gender for role: Husband in family should be male and wife in family should be female
    def test_US21_Wife_wifeIsCorrectGender(self):
        genderWife = "F"
        wife = "Awife"
        self.assertTrue(US21_Wife(genderWife, wife))

    def test_US21_Wife_wifeIsWrongGender(self):
        genderWife = "M"
        wife = "Awife"
        self.assertFalse(US21_Wife(genderWife, wife))

    def test_US21_Husband_husbandIsCorrectGender(self):
        genderHusb = "M"
        husb = "Ahusband"
        self.assertTrue(US21_Husband(genderHusb, husb))

    def test_US21_husbanIsWrongGender(self):
        genderHusb = "F"
        husb = "Ahusband"
        self.assertFalse(US21_Husband(genderHusb, husb))

#Tests for US22 Unique IDs:	All individual IDs should be unique and all family IDs should be unique
    def test_US22_noDuplicateIDs(self):
        IDs = ["F1", "F2", "F3"]
        self.assertTrue(US22(IDs))

    def test_US22_duplicateIDs(self):
        IDs = ["I1", "I2", "I1"]
        self.assertFalse(US22(IDs))

#Tests for US30
    def test_US30_aliveMarried(self):
        dday = "Alive"
        spouseIn = "F2"
        personID = "I1"
        self.assertTrue(US30(dday, spouseIn, personID))

    def test_US30_deadMarried(self):
        dday = "11/11/17"
        spouseIn = "F2"
        personID = "I2"
        self.assertFalse(US30(dday, spouseIn, personID))

    def test_US30_aliveNotMarried(self):
        dday = "Alive"
        spouseIn = "None"
        personID = "I3"
        self.assertFalse(US30(dday, spouseIn, personID))

    def test_US30_deadNotMarried(self):
        dday = "11/11/17"
        spouseIn = "None"
        personID = "I4"
        self.assertFalse(US30(dday, spouseIn, personID))

    def test_US42_aValidDate(self):
        date = "4 APR 2005"
        self.assertTrue(US42(date))

    def test_US42_anInvalidDate(self):
        date = "200 APR 2005"
        self.assertFalse(US42(date))

if __name__ == '__main__':
    unittest.main()
def test_US27():
	today = datetime.datetime.today().date()
	birthday = datetime.datetime(1900,5,10).date()
	assert int(days_difference(birthday,today,'years')) == 117
def test_US13():
	children=['@I2', '@I4']
	childbirth = {'@I2': datetime.date(1979, 4, 25), '@I4': datetime.date(1979, 5, 27)}
	temp = childbirth.copy()
	count = 0
	assert US13(childbirth, temp, children, count) == 1
def test_US3301():
	age = 19
	name = "US34ID"
	assert US33(age, name) == True
def test_US3302():
	age = 16
	name = "US34ID2"
	assert US33(age, name) == False
def test_US3401():
	birthH = datetime.datetime(1970,1,17).date()
	birthW = datetime.datetime(2010,5,10).date()
	today = datetime.datetime.today().date()
	husb = "HUSBID"
	wife = "WIFEID"
	assert US34(birthH, birthW, today, husb, wife) == False
def test_US3402():
	birthH = datetime.datetime(1972,8,21).date()
	birthW = datetime.datetime(1975,3,16).date()
	today = datetime.datetime.today().date()
	husb = "HUSBID2"
	wife = "WIFEID2"
	assert US34(birthH, birthW, today, husb, wife) == False
def test_US3901():
	married = datetime.datetime(2011,11,30).date()
	tempNum = 6
	today = datetime.datetime.today().date()
	husb = "HUSBID"
	wife = "WIFEID"
	assert US39(married, today, tempNum, husb, wife) == True

def test_US3902():
	married = datetime.datetime(2011,5,10).date()
	tempNum = 6
	today = datetime.datetime.today().date()
	husb = "HUSBID"
	wife = "WIFEID"
	assert US39(married, today, tempNum, husb, wife) == False
	
def test_US1801():
	key = "ID1"
	key2 = "ID2"
	value = "@FAM1@"
	value2 = "@FAM1@"
	assert US18(value, value2, key, key2) == 1

def test_US1802():
	key = "ID1"
	key2 = "ID2"
	value = "@FAM1@"
	value2 = "@FAM2@"
	assert US18(value, value2, key, key2) == 0
