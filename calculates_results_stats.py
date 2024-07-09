def calculates_results_stats(results_dic):
    
    results_stats_dic = dict()
    #Z
    num_of_images = len(results_dic)
    #A
    num_dog_match = 0
    for key, values in results_dic.items():
        if values[3] == 1 and values[4] == 1:
            num_dog_match += 1
    num_notdog_match = 0
    for key, values in results_dic.items():
        if values[3] ==0 and values[4] == 0:
            num_notdog_match += 1
    num_dog_images = 0
    num_notdog_images = 0
    for key, labels in results_dic.items():
        if labels[3] == 1:
            num_dog_images += 1
        else:
            num_notdog_images += 1
           
    num_breed_match = 0
    for key, labels in results_dic.items():
        if labels[3] == 1 and labels[2] == 1:
            num_breed_match += 1
          
    num_label_match = 0
    for key, labels in results_dic.items():
        if labels[2] == 1:
            num_label_match += 1
            
    pct_dog_image = num_dog_match / num_dog_images * 100
    
    #C/D
    if num_notdog_images > 0:
        pct_notdog_image = num_notdog_match / num_notdog_images * 100
    else:
        print("0")
    #E/B
    pct_dog_breed = num_breed_match / num_dog_images * 100
    
    #Y/Z
    pct_label_match = num_label_match / num_of_images * 100
    #Add key-value to the results_stats_dic dictionary
    key = ('n_correct_dogs', 'pct_correct_dogs', 'n_correct_breed', 'pct_correct_breed')
    value = (num_dog_match, pct_dog_image, num_breed_match, pct_dog_breed)
    results_stats_dic['n_correct_dogs'] = num_dog_match
    results_stats_dic['pct_correct_dogs'] = pct_dog_image
    results_stats_dic['n_correct_breed'] = num_breed_match
    results_stats_dic['pct_correct_breed'] = pct_dog_breed
    results_stats_dic['n_images'] = len(results_dic)
    results_stats_dic['n_dogs_img'] = num_dog_images
    results_stats_dic['n_notdogs_img'] = num_notdog_images
    results_stats_dic['pct_correct_notdogs'] = pct_notdog_image
    
    # Replace None with the results_stats_dic dictionary that you created with 
    # this function 
    print(results_stats_dic)
    return results_stats_dic

