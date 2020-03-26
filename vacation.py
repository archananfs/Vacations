import datetime
import holidays
import numpy as np

class Vacation:

    def get_holiday_list (self, country, year):
        holiday_date_list = []
        for key, value in holidays.CountryHoliday(country, years = year).items():
            if key.weekday() is not 5 and key.weekday() is not 6:
                holiday_date_list.append([key, 0])
        # print(holiday_date_list)
        return holiday_date_list

    def get_number_of_workingdays(self, holiday_date_list):
        for n in range(0, (len(holiday_date_list) - 1)):
            holiday_date_list[n][1] = (np.busday_count((holiday_date_list[n][0] + datetime.timedelta(days=1)), holiday_date_list[n + 1][0]))
        return holiday_date_list

    def get_iteration_list(self, holiday_date_list, Number_of_holidays):
        iteration_list = []
        for i in range(0, (len(holiday_date_list))):
            total = 0
            iterations = 1
            for j in range(i, (len(holiday_date_list))):
                total = total + holiday_date_list[j][1]
                if total < Number_of_holidays:
                    iterations = iterations + 1
                else:
                    break
            iteration_list.append([holiday_date_list[i][0], iterations])

        return iteration_list


    def get_max_holiday_list(self, iteration_list):
        max_value = max([x[-1] for x in iteration_list])
        Max_list = [sublist for sublist in iteration_list if sublist[-1] >= max_value]
        return Max_list

    def select_option(self, Max_list, Number_of_holidays):
        delta = []
        d = {}
        result = []
        for j in range(0, len(Max_list)):
            delta.append(Max_list[j][0].weekday())

        for i in range(0, len(delta)):
            print("Option :", i + 1)
            option_result = []
            for j in range(i, delta[i] + 1):
                start_date = Max_list[i][0] - datetime.timedelta(days=j)
                End_date = np.busday_offset(start_date, Number_of_holidays + Max_list[i][1])
                start_date64 = np.datetime64(start_date)
                if start_date.weekday() == 0:
                    d["Start Date"] = str(start_date - datetime.timedelta(days=2))
                    d["End Date"] = str(End_date)
                    d["Total days"] = str((End_date - start_date64) + 2)

                else:
                    d["Start Date"] = str(start_date)
                    d["End Date"] = str(End_date)
                    d["Total days"] = str(End_date - start_date64)
                option_result.append(d)
            result.append(option_result)
        
        return result

    def get_vacation_options(self, number_of_vacations, country, year):
        date_list = self.get_holiday_list(country, year)
        date_list_updated = self.get_number_of_workingdays(date_list)
        iteration_list = self.get_iteration_list(date_list_updated, number_of_vacations)
        max_list = self.get_max_holiday_list(iteration_list)
        result = self.select_option(max_list, number_of_vacations)
        return result
