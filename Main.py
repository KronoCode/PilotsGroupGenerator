from GroupsCreation import GroupsCreation
from KartManagement import KartManagement
from openpyxl import Workbook
import sys


def main(nbr_pilots, special_pilots, nbr_of_groups, nbr_of_races):
    # Create a workbook and sheet
    wk = Workbook()
    groups_per_race = [[[] for _ in range(nbr_of_groups)] for _ in range(nbr_of_races)]
    groups_creation = GroupsCreation(nbr_pilots, special_pilots, nbr_of_groups, nbr_of_races, wk)
    groups = groups_creation.create_groups()
    for race in range(nbr_of_races):
        wk = groups_creation.export_to_excel(race)
    kart_management = KartManagement(wk, nbr_of_races, nbr_pilots, nbr_of_groups, groups)
    kart_management.deterministic_kart_schedule()
    for race in range(nbr_of_races):
        kart_management.test(race)
    kart_management.export_to_excel()
    print(groups)

    wk.save('Group_Pilots.xlsx')
