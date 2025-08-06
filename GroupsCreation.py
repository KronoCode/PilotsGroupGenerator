import random
from openpyxl import Workbook


class GroupsCreation:
    """Needed arguments for class functional :
                total_pilots_nbr : total number of pilots,
                sp_pilots_nbr : total number of special pilots,
                nbr_of_groups : number of groups of pilots for each race
                nbr_of_races : numbers of races
                workbook : TODO: TO BE REMOVED BUT NEEDED FOR CREATING EXCEL SHEET FOR NOW
    """
    def __init__(self, total_pilots_nbr, sp_pilots_nbr, nbr_of_groups, nbr_of_races, workbook):

        self.total_pilots_nbr = total_pilots_nbr
        self.sp_pilots_nbr = sp_pilots_nbr
        self.nbr_of_groups = nbr_of_groups
        self.nbr_of_races = nbr_of_races
        self.workbook = workbook

        try:
            self.sp_per_group = int(sp_pilots_nbr/nbr_of_groups)
            self.total_normal_pilots_list = list(range(self.sp_pilots_nbr + 1, self.total_pilots_nbr+1))
            self.total_special_pilots_list = list(range(1, self.sp_pilots_nbr + 1))
            self.groups = [[[] for _ in range(self.nbr_of_groups)] for _ in range(self.nbr_of_races)]

        except Exception as e:
            exit(f"error in initializing Groups : {e}")

    """"PUBLIC METHODS"""
    def create_groups(self):
        # special_pilots = list(range(1, self.sp_pilots_nbr+1))
        previous_race_last_group = []

        for race_nbr in range(self.nbr_of_races):

            self.total_normal_pilots_list = list(range(self.sp_pilots_nbr + 1, self.total_pilots_nbr + 1))
            self.total_special_pilots_list = list(range(1, self.sp_pilots_nbr + 1))

            race_nbr += 1
            self.special_pilots_per_group(race_nbr, previous_race_last_group)
            self.pilots_per_group(race_nbr, previous_race_last_group)
            # self.export_to_excel(race_nbr)
            # previous_race_last_group = self.clear_groups()

            # Clear previous last group of last race to store the new one
            previous_race_last_group.clear()
            previous_race_last_group = [pilot for pilot in self.groups[race_nbr - 1][self.nbr_of_groups - 1]]
        return self.groups

    """"PRIVATE METHODS"""
    def pilots_per_group(self, race, last_group_previous_race):
        while len(self.total_normal_pilots_list) > 0:
            for group in range(self.nbr_of_groups):
                filtered_pilot_list = [pilot for pilot in self.total_normal_pilots_list
                                       if pilot not in last_group_previous_race]
                if group == 0 and race > 1:
                    if len(filtered_pilot_list) == 0:
                        quit("error : filtered_pilot_list")
                    pilot = random.choice(filtered_pilot_list)

                else:
                    common = set(last_group_previous_race) & set(self.total_normal_pilots_list)
                    if common:
                        pilot = random.choice(list(common))
                    else:
                        pilot = random.choice(self.total_normal_pilots_list)

                self.groups[race-1][group].append(pilot)
                self.total_normal_pilots_list.remove(pilot)

                if len(self.total_normal_pilots_list) == 0:
                    break

    def special_pilots_per_group(self, race, last_group_previous_race):
        chunk_size = self.nbr_of_groups
        while len(self.total_special_pilots_list) > 0:
            for group in range(self.nbr_of_groups):
                sp_pilots_per_group = []
                special_pilots_in_subgroups = []
                if group == 0 and race > 1:
                    filtered_sp_pilot_list = [sp_pilot for sp_pilot in self.total_special_pilots_list
                                              if sp_pilot not in last_group_previous_race]
                    filtered_sp_pilot_list.sort()
                    special_pilots_in_subgroups = self.create_sp_subgroups(filtered_sp_pilot_list, chunk_size)

                    for subgroup in special_pilots_in_subgroups:
                        sp_pilots_per_group.append(random.choice(subgroup))
                else:
                    special_pilots_in_subgroups = self.create_sp_subgroups(self.total_special_pilots_list, chunk_size)

                    for subgroup in special_pilots_in_subgroups:
                        sp_pilots_per_group.append(random.choice(subgroup))
                self.groups[race-1][group].extend(sp_pilots_per_group)
                self.total_special_pilots_list = [sp_pilots for sp_pilots in self.total_special_pilots_list if
                                                  sp_pilots not in sp_pilots_per_group]

                if len(self.total_special_pilots_list) == 0:
                    break

    def export_to_excel(self, race):
        race = race+1
        if race == 1:
            ws = self.workbook.active
            ws.title = f"Race {race}"
        else:
            ws = self.workbook.create_sheet(f"Race {race}")

        # Now fill by column instead of by row
        for col_idx, column in enumerate(self.groups[race-1], start=1):
            for row_idx, value in enumerate(column, start=1):
                ws.cell(row=row_idx, column=col_idx, value=value)
        return self.workbook

    def clear_groups(self):
        group1 = [pilot for pilot in self.groups[self.nbr_of_races - 1]]
        for group in self.groups:
            group.clear()
        return group1

    def create_sp_subgroups(self, pilots, chunk):
        subgroups = {}
        for pilot in pilots:
            # Determine the group key based on value
            key = (pilot - 1) // chunk
            subgroups.setdefault(key, []).append(pilot)
        return list(subgroups.values())
