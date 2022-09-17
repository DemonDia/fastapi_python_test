import requests
# =====================Other helper functions=====================
# check if test case pass
def validateOutcome(actualResult, expectedResult):
    if actualResult == expectedResult:
        print("Test case passed")
    else:
        print("Test case failed")
# delete all data
def deleteAll(url):
    results = requests.delete(url+"deleteall")
    return results.json()

# seed data
def seedData(url):
    results = requests.post(url+"seedall")
    return results.json()

# reset to defaults
def resetDataToDefaults(url):
    deleteResults = deleteAll(url)
    seedResults = seedData(url)
    return deleteResults["success"] == seedResults["success"]

# =====================CRUD functions=====================
# Gets single row based on its ID
def getSingleRow(url,rowId):
    obtainedRow = requests.get(url+"{rowId}".format(rowId=rowId))
    return obtainedRow.json()

# Gets all rows
def getAllRows(url):
    rows = requests.get(url)
    return rows.json()

# Add row
def addRow(url,jsonObject):
    addedRow = requests.post(url, json=jsonObject)
    return addedRow.json()
# Update rows
def updateRow(url, rowId,jsonObject):
    updatedRow = requests.put(url+"{rowId}".format(rowId=rowId),json = jsonObject)
    return updatedRow.json()
# Delete rows
def deleteRow(url, rowId):
    deletedRow = requests.delete(url+"{rowId}".format(rowId=rowId))
    return deletedRow.json()