import speedtest
import pandas as pd
from os.path import exists

def run_test():
       servers = []
       # If you want to test against a specific server
       # servers = [1234]

       threads = None
       # If you want to use a single threaded test
       # threads = 1

       s = speedtest.Speedtest()
       s.get_servers(servers)
       s.get_best_server()
       s.download(threads=threads)
       s.upload(threads=threads)
       s.results.share()

       results_dict = s.results.dict()
       del results_dict['server'], results_dict['client'], results_dict['share']


       results_dict['download'] = round(results_dict['download']/1000000,0)
       results_dict['upload'] = round(results_dict['upload']/1000000,0)

       return results_dict


def make_csv(result_dic):
       if exists('speedtest_results.csv'):
              df = pd.DataFrame.from_dict([result_dic])
              df.to_csv (r'speedtest_results.csv', mode='a', index = False, header=False)

       else:
              df = pd.DataFrame.from_dict([result_dic])
              df.to_csv (r'speedtest_results.csv', index = False, header=True)