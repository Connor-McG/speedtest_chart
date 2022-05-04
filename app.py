import speedtest_get as speed_g

results_dict = speed_g.run_test()
speed_g.make_csv(results_dict)