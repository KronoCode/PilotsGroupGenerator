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
        self.karts_per_pilot = []
        self.groups = groups
        self.karts_pilots_mapping = []

    # def manage_karts_per_group(self):
    #     karts_used_by_group = []
    #     for race in range(self.nbr_of_races):
    #         for group in self.groups[race]:
    #             for pilot in group:
    #                 #iterate through the number of karts equal to the number of pilots per groups.
    #                 #common_karts = set(len(group)) & set(karts_used_by_group) & set(self.karts_per_pilot[pilot-1])
    #                 available_karts = [i for i in range(len(group)-1) if i not in karts_used_by_group
    #                                    and i not in self.karts_per_pilot[pilot-1]]

    #                 if len(available_karts) == 0:
    #                     # self.swap_karts(available_karts, group, pilot)
    #                     quit("error : available_karts length is 0")

    #                 kart = random.choice(available_karts) + 1
    #                 karts_used_by_group.append(kart)
    #                 self.karts_per_pilot[pilot-1].append(kart)
    #             karts_used_by_group.clear()
    #     print(self.karts_per_pilot)

    def deterministic_kart_schedule(self, seed=42):
        random.seed(seed)

        K = len(self.groups[0][0])
        pilots = list(range(1, self.nbr_of_pilots + 1))
        pilot_used_karts = {p: set() for p in pilots}

        self.karts_per_pilot = []

        for race_groups in self.groups:
            race_assignment = []
            for group in race_groups:
                group_map = {}
                available_karts = list(range(1, K + 1))
                random.shuffle(available_karts)

                for pilot in group:
                    for kart in available_karts:
                        if kart not in pilot_used_karts[pilot]:
                            group_map[pilot] = kart
                            pilot_used_karts[pilot].add(kart)
                            available_karts.remove(kart)
                            break
                    else:
                        raise ValueError(f"No available kart for pilot {pilot}")

                race_assignment.append(group_map)
            self.karts_per_pilot.append(race_assignment)


    def test(self, race):
        race = race+1
        ws = self.workbook.create_sheet(f"Test Race {race}")

        # Now fill by column instead of by row
        for col_idx, column in enumerate(self.groups[race-1], start=1):
            for row_idx, value in enumerate(column, start=1):
                ws.cell(row=row_idx, column=col_idx, value=f"{value} : {self.karts_per_pilot[race-1][col_idx-1][value]}")
        return self.workbook
        pass

    def export_to_excel(self):
        ws = self.workbook.create_sheet(title=f"Kart distribution")

        # Write headers (group numbers)
        ws.cell(row=1, column=1, value=f"Pilot ID")

        #Fill pilot IDs
        for idx in range(self.nbr_of_pilots):
            ws.cell(row=2+idx, column=1, value=f"{idx+1}")

        for race, pilot_kart_for_race in enumerate(self.karts_per_pilot):
            ws.cell(row=1, column=2+race, value=f"Kart for race {race+1}")
            for group_nbr in range(self.nbr_of_groups):
                for pilot in range(self.nbr_of_pilots):
                    pilot += 1 #to remove shift due to range function
                    if pilot in pilot_kart_for_race[group_nbr]:
                        value = pilot_kart_for_race[group_nbr][pilot]
                        ws.cell(row=1+pilot, column=2+race, value=value)



            # i = len(self.groups[race]) * race
            # ws.cell(row=1, column=race+1, value=f"Kart for Race {race+1}")

            # # Now fill by column instead of by row
            # for col_idx, column in enumerate(pilot_kart_for_race, start=1+i):
            #     for row_idx, value in enumerate(column, start=1):
            #         ws.cell(row=row_idx+1, column=col_idx+1, value=f"{column[value]} : {value}")

        # # Write headers (group numbers)
        # for g_idx in range(len(race_groups)):
        #     ws.cell(row=1, column=g_idx+2, value=f"Group {g_idx+1}")

        # # # Find max pilots per group (for row count)
        # # max_pilots = max(len(group_map) for group_map in race_groups)

        # # Fill in kart numbers
        # for g_idx, group_map in enumerate(race_groups):
        #     pilots_in_group = list(group_map.keys())
        #     karts_in_group = list(group_map.values())
        #     for row_idx, (pilot, kart) in enumerate(zip(pilots_in_group, karts_in_group), start=2):
        #         ws.cell(row=row_idx, column=1, value=pilot)      # Pilot ID in first column
        #         ws.cell(row=row_idx, column=g_idx+2, value=kart) # Kart number in group column

        # # Add header for pilot IDs column
        # ws.cell(row=1, column=1, value="Pilot ID")
        return self.workbook










