from sklearn.metrics import f1_score


def get_max(list):
    if len(list)==1:
        return list[0]
    else :
        first_num=list[0]
        rest_max_num=get_max(list[1:])
        isTure=first_num>rest_max_num
        if isTure:
            return first_num
        else :
            return rest_max_num

def get_min(list):
    if len(list)==1:
        return list[0]
    else :
        first_num=list[0]
        rest_min_num=get_min(list[1:])
        isTure=first_num<rest_min_num
        if isTure:
            return first_num
        else :
            return rest_min_num
def findMinAndMax(list):
    return (get_max(list),get_min(list))

print(findMinAndMax([1,2,3,4,5,6,7,8]))