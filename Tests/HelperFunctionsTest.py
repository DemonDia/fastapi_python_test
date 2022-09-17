import requests
# =====================Other helper functions=====================
# check if test case pass
def validateOutcome(actualResult, expectedResult):
    if actualResult == expectedResult:
        print("===============Test case passed===============")
    else:
        print("===============Test case failed===============")
# delete all data
def deleteAll(url):
    requests.delete(url)

# =====================CRUD functions=====================
# Gets single row based on its ID
def getSingleRow(url,rowId):
    obtainedRow = requests.get(url+"{rowId}".format(entityId=rowId))
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
def updateRow(url, rowId,userJson):
    updatedUser = requests.put(url+"{userId}".format(rowId=rowId),params = userJson)
    return updatedUser.json()
# Delete rows
def deleteRow(url, rowId):
    deletedRow = requests.delete(url+"{rowId}".format(rowId=rowId))
    return deletedRow.json()