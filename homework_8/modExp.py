import csv


def SaveBase(userNameDict, path):
    fieldnameName = []
    for name in userNameDict:
        fieldnameName.append(name)
    print(fieldnameName)
    with open(path, 'w', encoding='UTF-8-sig', newline='') as csvfile:
        writer = csv.DictReader(csvfile, fieldnames=fieldnameName)
        writer.writeheader()
        writer.writerows(fieldnameName)


# def unload_file(file_name, list_of_dict):
#     with open(file_name, 'w', newline='', encoding='UTF-8') as data_base:
#         writer = csv.writer(data_base, delimiter=';',
#                             quotechar=',', quoting=csv.QUOTE_MINIMAL)
#         writer.writerows(list_of_dict)
#     print("Writing complete")


# returnList = []
# with open(pathFile, 'r', encoding='UTF-8') as file:
#     allFile = file.readlines()
#     for el in allFile:
#         if len(returnList) < len(allFile)-1:
#             returnList.append(el[:len(el)-1])
#         else:
#             returnList.append(el)
# return returnList
