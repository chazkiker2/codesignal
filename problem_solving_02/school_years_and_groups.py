from string import ascii_lowercase


def years_and_groups_01(years, groups):
    groupings_by_year_str = ""
    for year in range(years):
        for group in range(groups):
            groupings_by_year_str += f"{year + 1}{ascii_lowercase[group]}, "
    return groupings_by_year_str[:-2]


def years_and_groups_02(years, groups):
    groupings_by_year = ""
    for year in range(years):
        for group_num in range(groups):
            groupings_by_year += f"{year + 1}{ascii_lowercase[group_num]}, "

    return groupings_by_year[:-2]


def years_and_groups_03(years, groups):
    lst = [f"{year + 1}{ascii_lowercase[group_num]}"
           for group_num in range(groups)
           for year in range(years)]
    
    return ", ".join(lst)


if __name__ == '__main__':
    res1 = years_and_groups_01(3, 3)
    res2 = years_and_groups_02(3, 3)
    res3 = years_and_groups_03(3, 3)
    print(res1)
    print(res2)
    print(res3)
