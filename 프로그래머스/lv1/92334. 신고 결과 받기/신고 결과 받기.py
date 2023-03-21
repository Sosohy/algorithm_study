def solution(id_list, report, k):
    dicReport = dict.fromkeys(id_list, 0);
    dicID = dict.fromkeys(id_list, 0);
    report = set(report)
    
    for i in report:
        reportIDs = i.split(" ");
        dicReport[reportIDs[1]] += 1;

    for i in report:
        uID, reID = i.split(" ");
        if (dicReport[reID] >= k):
            dicID[uID] += 1;

    answer = list(dicID.values());
    return answer