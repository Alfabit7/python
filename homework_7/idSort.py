def sortUserId(data_base):
    otherDataUserList = []
    dictUser = {}
    dictUsers = {}
    userList = []
    sortedList = []
    for i in range(len(data_base)):
        for j in range(1, len(data_base[i])):
            fio = data_base[i][0]
            otherDataUserList.append(data_base[i][j])
        dictUser = {fio: otherDataUserList}
        dictUsers.update(dictUser)
        otherDataUserList = []
    dictUsers = dict(sorted(dictUsers.items()))

    for name, data in dictUsers.items():
        userList.append(name)
        for el in data:
            userList.append(el)
        sortedList.append(userList)
        userList = []
    return sortedList
