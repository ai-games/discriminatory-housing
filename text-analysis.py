import json
import os
import re
import string

def readData():
    data = []
    
    for root, dirs, filenames in os.walk('./Listings'):
        for filename in filenames:
            if 'listing' in filename:
                with open('./Listings/' + filename) as f:
                    jsonData = json.load(f)

                    for line in jsonData:
                        data.append(line)

    return data

def wordFrequencyList(posts):
    frequency = {}

    for post in posts:
        match_pattern = re.findall(r'\b[a-z]{3,15}\b', post['description'])
         
        for word in match_pattern:
            count = frequency.get(word,0)
            frequency[word] = count + 1
             
    return frequency.keys()

def possibleDiscriminatoryPosts(posts):
    with open('./possible_discriminatory_words.txt') as f:
        words = f.read().splitlines()

        regexExp = ''
        for word in words:
            regexExp += '\\b'+ word + '\\b|'

        regexExp = regexExp[:len(regexExp) - 1]

        disPosts = []
        for post in posts:
            search = re.findall(r"\bonly\b|\bstudents\b|\bfamily\b|\bprofessional\b|\bpet\b|\bstudent\b|\bprofessionals\b|\bgraduate\b|\bpaint\b|\byoung\b|\bundergrads\b|\bincome\b|\bhopeless\b|\bmusic\b|\bmoldings\b|\bgrade\b|\bchildren\b|\bfemale\b|\blead\b|\blie\b|\bdrugs\b|\bovernight\b|\billegal\b|\binstruments\b|\bmassage\b|\bmeow\b|\bnoise\b|\bpromotions\b|\bpromotion\b|\bkids\b|\bprof\b|\btwenties\b|\bundergrad\b|\bhandsome\b|\bundergraduates\b|\bliquor\b|\bmen\b|\bguys\b|\bgirl\b|\badult\b|\bfob\b|\bhealthiest\b|\bsexy\b|\bbeer\b|\binternship\b|\boutrageous\b|\bartist\b|\beducated\b|\boccupation\b|\bundergraduate\b|\bhuman\b|\bpharma\b|\bdevelopers\b|\bfulltime\b|\btwenty\b|\bamateurs\b|\bcorporate\b|\bdance\b|\bdoctors\b|\bembarrassment\b|\bentrepreneur\b|\bgay\b|\bgirls\b|\bhers\b|\bmom\b|\bnortheastern\b|\bpostdocs\b|\bresidency\b|\bteacher\b|\bentertainer\b|\bfemales\b|\bgraduating\b|\bsenior\b|\bvegetarian\b|\baerobics\b|\bcreepy\b|\bdancing\b|\bdoctor\b|\bebony\b|\bfrat\b|\bgirlfriend\b|\bgraduates\b|\bguns\b|\bimmigrants\b|\bmusician\b|\bsingles\b|\btopsstudents\b|\bundergradsno\b|\bbusinessmen\b|\bdocumented\b|\bengineers\b|\bextrovert\b|\bextroverted\b|\bextroverts\b|\bfederalist\b|\bgraduated\b|\bguitar\b|\bguitars\b|\binternships\b|\blgbtq\b|\bmusical\b|\bmusicians\b|\bpostdoc\b|\bstudentseeing\b|\btransgender\b", post['description'])
            if len(search) > 0:
                disPosts.append(post)

        return disPosts                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           

def jsonToFile(posts):
    fout = open('./possible-discriminatory-posts.json', 'w')
    fout.write('[')
    count = 0
    maxLen = len(posts)
    for i in posts:
        fout.write(json.dumps(i))
        count += 1
        if (count < maxLen):
            fout.write(',\n')
    fout.write(']')

    fout.close()

posts = []
posts = readData()

frequency_list = wordFrequencyList(posts)
discriminatoryPosts = possibleDiscriminatoryPosts(posts)
jsonToFile(discriminatoryPosts)


