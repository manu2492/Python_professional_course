def remove_duplicates(list):
    list1 = []

    for i in list:
        if i not in list1:
            list1.append(i)
    print(list1)

def run():
    random_list = [1, 1, 2, 2, 3, 3]
    print(remove_duplicates(random_list))



if __name__ == '__main__':
    run()


#SET MODE
def remove_duplicates2():
    random_list2 = [1, 1, 2, 2, 3, 3]
    list2 = list(set(random_list2))
    print(list2)

remove_duplicates2()
