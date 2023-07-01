import os


def merge_sim_runs(path):
    i = 1
    for folder in os.listdir(path):
        for sim_folder in os.listdir(path + folder):
            sim_diff = 3 - len(str(i))
            sim_number = str(i)
            for j in range(sim_diff):
                sim_number = '0' + sim_number

            os.rename(path + folder + "/" + sim_folder, path + folder + "/" + 'Sim_' + sim_number)
            i += 1


merge_sim_runs('c:/Users/Tomas/PycharmProjects/emailModelingBe/fullSimStatsLab/')
