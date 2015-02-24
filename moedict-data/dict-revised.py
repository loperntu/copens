from json import load

#list=[{heteronyms:[{definitions:{def:value}},{definitions:{def:value}},...], non_radical_stroke_count:[{definition:{def:value}}]},...]
list=load(open('dict-revised.json'))
for dict in list:
    #dict.keys()=['heteronyms','non_radical_stroke_count','title','stroke_count','radical']
    heteronyms_list=dict['heteronyms']
    title=dict['title']
#    print title.encode('utf8'),
    for d in heteronyms_list:
        definition_list=d['definitions']
        for definition in definition_list:
            print title.encode('utf8'),definition['def'].encode('utf8')
