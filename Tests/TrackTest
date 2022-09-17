from HelperFunctionsTest import *
BASE = "http://127.0.0.1:8000/tracks/"

# ======================Test cases======================
# 1) Delete all data
def deleteAllDataTest():
    print("1) Delete all data")
    result = deleteAll(BASE)
    validateOutcome(result,True)
    print()

# 2) Seed data
def seedDataTest():
    print("2) Seed data")
    result = seedData(BASE)
    validateOutcome(result,True)
    print()

# 3) Reset data to defaults
def resetDataToDefaultTest():
    print("3) Reset data to defaults")
    result = resetDataToDefaults(BASE)
    validateOutcome(result,True)
    print()

# 4) Get all data
def getAllDataTest():
    print("4) Get all data")
    result = getAllRows(BASE)
    validateOutcome(result,True)
    print()

# 5) Get data by ID
def getDataByIdTest():
    print("5) Get data by ID")
    print("5)a)ID exists")
    idExists = getSingleRow(BASE,200)
    validateOutcome(idExists,True)

    print("5)b)ID does not exist")
    idDoesNotExist = getSingleRow(BASE,99999)
    validateOutcome(idDoesNotExist,False)
    print()

# 6) Add data
def addDataTest():
    print("6) Add data")
    print("6)a) Successful adding")
    jsonToAddPass = {
        "title":"Test Title",
        "artist":"Test Artist",
        "duration":180.0,
        "last_play":"2017-04-01T08:31:33"
    }
    addDataPassResult = addRow(BASE,jsonToAddPass)
    validateOutcome(addDataPassResult,True)

    print("6)b)Unsuccessful adding due to missing fields")
    jsonToAddFail = {
        "title":"Test Title",
        "artist":"Test Artist",
        "duration":180.0,
    }
    addDataFailResult = addRow(BASE,jsonToAddFail)
    validateOutcome(addDataFailResult,False)
    print()

# 7) Update data
def updateDataTest():
    print("7) Update data")
    print("7)a) Update successful")
    updateData = {
        "title":"Test Titl X",
        "artist":"Test Artist X",
        "duration":180.0,
        "last_play":"2017-04-01T08:31:33"
    }
    updatePass = updateRow(BASE,87,updateData)
    validateOutcome(updatePass,True)

    print("7)b) Update unsuccessful due to ID not found")
    updateFail = updateRow(BASE,122125,updateData)
    validateOutcome(updateFail,False)
    print()
    
# 8) Delete data
def deleteDataTest():
    print("8) Delete data")
    print("8)a) Delete successful")
    deletePass = deleteRow(BASE,87)
    validateOutcome(deletePass,True)

    print("8)b) Delete unsuccessful due to ID not found")
    deleteFail = deleteRow(BASE,8888887)
    validateOutcome(deleteFail,False)
    print()

if __name__ == "__main__":
    deleteAllDataTest()
    seedDataTest()
    resetDataToDefaultTest()
    getAllDataTest()
    getDataByIdTest()
    # addDataTest()
    updateDataTest()
    deleteDataTest()