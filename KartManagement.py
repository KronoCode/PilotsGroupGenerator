import random


class KartManagement:
    """Needed arguments for class functional :
                    workbook : TODO: TO BE REMOVED BUT NEEDED FOR CREATING EXCEL SHEET FOR NOW
    """

    def __init__(self, workbook, nbr_of_races, nbr_of_pilots, nbr_of_groups, groups):
        self.workbook = workbook
        self.nbr_of_races = nbr_of_races
        self.nbr_of_pilots = nbr_of_pilots
        self.nbr_of_groups = nbr_of_groups
        self.pilots = list(range(1, self.nbr_of_pilots + 1))
        self.karts_per_pilot = [[] for _ in range(self.nbr_of_pilots)]
        self.groups = groups
        self.karts_pilots_mapping = []

    def manage_karts_per_group(self):
        karts_used_by_group = []
        for race in range(self.nbr_of_races):
            for group in self.groups[race]:
                for pilot in group:
                    #iterate through the number of karts equal to the number of pilots per groups.
                    #common_karts = set(len(group)) & set(karts_used_by_group) & set(self.karts_per_pilot[pilot-1])
                    available_karts = [i for i in range(len(group)-1) if i not in karts_used_by_group
                                       and i not in self.karts_per_pilot[pilot-1]]

                    if len(available_karts) == 0:
                        # self.swap_karts(available_karts, group, pilot)
                        quit("error : available_karts length is 0")

                    kart = random.choice(available_karts) + 1
                    karts_used_by_group.append(kart)
                    self.karts_per_pilot[pilot-1].append(kart)
                karts_used_by_group.clear()
        print(self.karts_per_pilot)

#    def pilot_kart_mapping(self):
#        pilots_and_karts = []
#        for group in self.groups[0]:
#            for pilot in group:
#                pilots_and_karts.append(pilot)
#                for self.karts_per_pilot[pilot-1]

    def export_to_excel(self):
        ws = self.workbook.create_sheet(f"Kart per pilot")

        # Now fill by column instead of by row
        for pilot_karts in self.karts_per_pilot:
            ws.append(pilot_karts)
        return self.workbook

    # def swap_karts(self, pilot, group, karts_available):
    #     for to_be_swapped_pilot in group:
    #         for kart in karts_available:
    #             new_kart = self.karts_per_pilot[to_be_swapped_pilot - 1][-1]
    #             if kart not in self.karts_per_pilot[to_be_swapped_pilot-1] and new_kart not in karts_available:
    #                 new_kart = self.karts_per_pilot[to_be_swapped_pilot-1][-1]
    #                 if new_kart in
    #                 self.karts_per_pilot[to_be_swapped_pilot-1][-1] = kart
    #                 self.karts_per_pilot[pilot - 1][-1] = new_kart










