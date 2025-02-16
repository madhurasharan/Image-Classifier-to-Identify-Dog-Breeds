def calculates_results_stats(results_dic):
  
    results_stats_dic = dict()

    results_stats_dic['n_dogs_img'] = 0
    results_stats_dic['n_match'] = 0
    results_stats_dic['n_correct_dogs'] = 0
    results_stats_dic['n_correct_notdogs'] = 0
    results_stats_dic['n_correct_breed'] = 0       
    
    for key in results_dic:
         
        # Labels Match Exactly
        if results_dic[key][2] == 1:
            results_stats_dic['n_match'] += 1


        pass
        

        if results_dic[key][3] == 1:
            results_stats_dic['n_dogs_img'] += 1
            

            if results_dic[key][4] == 1:
                results_stats_dic['n_correct_dogs'] += 1

        else:
 
            pass

    results_stats_dic['n_images'] = len(results_dic)


    results_stats_dic['n_notdogs_img'] = (results_stats_dic['n_images'] - 
                                      results_stats_dic['n_dogs_img']) 

    results_stats_dic['pct_match'] = 0.0

    results_stats_dic['pct_correct_dogs'] = 0.0

    results_stats_dic['pct_correct_breed'] = 0.0

    if results_stats_dic['n_notdogs_img'] > 0:
        results_stats_dic['pct_correct_notdogs'] = (results_stats_dic['n_correct_notdogs'] /
                                                results_stats_dic['n_notdogs_img'])*100.0
    else:
        results_stats_dic['pct_correct_notdogs'] = 0.0


    return None

