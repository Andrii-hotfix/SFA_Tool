import urllib.request
import json
import re
# import PyQt5


def getUserId(user, api_key):
    nikname = user.split('/')[4]
    url = 'http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key='+api_key+'&vanityurl='+nikname
    response = urllib.request.urlopen(url).read().decode('utf-8')
    json_response = json.loads(response)
    return json_response['response']['steamid']


def getUserFriends(id, api_key):
    url = 'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key='+api_key+'&steamid='+id+'&relationship=friend'
    response = urllib.request.urlopen(url).read().decode('utf-8')
    json_response = json.loads(response)
    friends_list = json_response['friendslist']['friends']
    id_list = []
    for friend in friends_list:
        id_list.append('https://steamcommunity.com/profiles/'+friend['steamid'])
    return id_list


def commonFriends(user_list1, user_list2):
    common = []
    for item1 in user_list1:
        for item2 in user_list2:
            if item2 == item1:
                common.append(item2)
                user_list2.remove(item2)
                break
    return common


def bubbleSort(tupleList):
    sort = True
    while(sort):
        sort = False
        for i in range(0, len(tupleList) - 1):
            if tupleList[i][1] < tupleList[i + 1][1]:
                tmp = tupleList[i]
                tupleList[i] = tupleList[i + 1]
                tupleList[i + 1] = tmp
                sort = True
    return tupleList


def bot():
    if re.match(r"https?://steamcommunity.com/id/\w\/?", sfa_tool.lineEdit.text()) \
    or re.match(r"https?://steamcommunity.com/profiles/[0-9]\/?", sfa_tool.lineEdit.text()):
        user = sfa_tool.lineEdit.text()
        result = {}
        private = []
        api_key = '07814D6A28FF029D746FEB6450DBDFC5'

        if re.match(r"https?://steamcommunity.com/id/\w\/?", sfa_tool.lineEdit.text()):
            try:
                user_id = getUserId(user, api_key)
            except urllib.error.HTTPError as err:
                # private account does not provide any information
                if err.code == 401:
                    alert = QtGui.QMessageBox()
                    alert.setText("private account")
                    alert.exec_()
                    sfa_tool.close()
        else:
            # id allready provided
            user_id = user.split('/')[4]

        try:
            user_friends = getUserFriends(user_id, api_key)
        except:
            alert = QtGui.QMessageBox()
            alert.setText("network error occured")
            alert.exec_()
            sfa_tool.close()

        i = 0
        for friend in user_friends:
            try:
                friend_friends = getUserFriends(friend.split('/')[4], api_key)
                common = commonFriends(user_friends, friend_friends)
                result[friend] = common
                sfa_tool.progressBar.setValue((100 * i) / len(user_friends))
                i += 1
            except urllib.error.HTTPError as err:
                # private account does not provide any information
                if err.code == 401:
                    private.append(friend)
                else:
                    alert = QtGui.QMessageBox()
                    alert.setText("network error occured")
                    alert.exec_()
                    sfa_tool.close()

        sfa_tool.progressBar.setValue(100)

        sfa_tool.close()

        result_counted = []

        for item in result.keys():
            tmp = item, len(result[item])
            result_counted.append(tmp)

        sfa_result.tableWidget.setRowCount(len(result_counted))

        result_counted = bubbleSort(result_counted)

        i = 0
        for item in result_counted:
            sfa_result.tableWidget.setItem(i, 0, QtGui.QTableWidgetItem(item[0]))
            sfa_result.tableWidget.setItem(i, 1, QtGui.QTableWidgetItem(str(item[1])))
            i += 1

        for item in private:
            sfa_result.listWidget.addItem(item)

        sfa_result.show()


    else:
        alert = QtGui.QMessageBox()
        alert.setText("Invalid URL!")
        alert.exec_()
