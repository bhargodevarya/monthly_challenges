# Save the current challenge and fetch all the challenges for the givem month
def save_challenge(challenge, month):
    challenges_from_file = None
    month_found = False

    with open('./challenges.txt','r') as read_file:
        challenges_from_file = read_file.readlines()
    
    challenges_dict = {}

    with open('./challenges.txt', 'w') as file_rewrite:
        file_rewrite.write('')
    
    if challenges_from_file:
        print('Found challenges')
        for my_challenges in challenges_from_file:
            challenges_data = my_challenges.split(":")
            challenges_dict[challenges_data[0]] = challenges_data[1].split("|")
        
        if month in challenges_dict.keys():
            challenges_dict.get(month).append(challenge)
        else:
            challenges_dict[month] = [challenge]
    else:
        print('No existing challenges')
        challenges_dict[month] = [challenge]
    
    with open('./challenges.txt', 'a') as file_write:
        for month_key in challenges_dict.keys():
            challenge_text : str = ''
            for ch in challenges_dict[month_key]:
                if ch == '\n':
                    continue
                challenge_text += ch 
                challenge_text += '|'
            print(f'{month_key}:{challenge_text}')
            file_write.write(f'{month_key}:{challenge_text}')
            file_write.write('\n')
    
    return challenges_dict[month]



    