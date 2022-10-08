def text_sum(cash):
    
    zlote_list=[i for i in str(cash)]
    grosze_list=[]
    if '.' in zlote_list:
        grosze_list=zlote_list[zlote_list.index('.')+1:]
        zlote_list=zlote_list[:zlote_list.index('.')]
    jedn={'1':'jeden','2':'dwa','3':'trzy','4':'cztery','5':'pięć','6':'sześć','7':'siedem','8':'osiem','9':'dziewięć'}
    nas={'1':'jedenaście','2':'dwanaście','3':'trzynaście','4':'cztarenaście','5':'piętnaście','6':'szesnaście','7':'siedemnaście','8':'osiemnaście','9':'dzewiętnaście','0':'dziesięć'}
    dzie={'2':'dwadzieścia','3':'trzydzieści','4':'czterdzieści','5':'pięćdziesiąt','6':'sześćdziesiąt','7':'siedemdziesiąt','8':'osiemdziesiąt','9':'dziewięćdziesiąt'}
    set={'1':'sto','2':'dwieście','3':'trzysta','4':'czterysta','5':'pięćset','6':'sześćset','7':'siedemset','8':'osiemset','9':'dziewięćset'}
    tys={'1':'tysiąc','2':'dwa tysiące','3':'trzy tysiące','4':'cztery tysiące','5':'pięć tysięcy','6':'sześć tysięcy','7':'siedem tysięcy','8':'osiem tysięcy','9':'dziewięć tysięcy'}

    if len (zlote_list)>1 and zlote_list[-2]=='1':
        if zlote_list[-1] in nas:
            zlote_list[-1]=nas[zlote_list[-1]]
            zlote_list[-2]='x'
    else:
        if zlote_list[-1] in jedn:
            zlote_list[-1]=jedn[zlote_list[-1]]
        if len(zlote_list)>1 and zlote_list[-2] in dzie:
            zlote_list[-2]=dzie[zlote_list[-2]]
    if len(zlote_list)>2:
        if zlote_list[-3] in set:
            zlote_list[-3]=set[zlote_list[-3]]
    #==================tysiące====================================================
    if len (zlote_list)>4 and zlote_list[-5]=='1':
        if zlote_list[-4] in nas:
            zlote_list[-4]=nas[zlote_list[-4]]+' tysięcy'
            zlote_list[-5]='x'
    else:

        if len (zlote_list)>4 and zlote_list[-5] in dzie:
            zlote_list[-5]=dzie[zlote_list[-5]]

    if len(zlote_list)>3:
        if zlote_list[-4] in tys:
            zlote_list[-4]=tys[zlote_list[-4]]
    #==================dziesiątzlote_listi tysięcy========================================
    if len(zlote_list)>4:
        if zlote_list[-5] in dzie:
            zlote_list[-5]=dzie[zlote_list[-5]]
        if zlote_list[-4]=='tysiąc':
            zlote_list[-4]='jeden tysięcy'
        if zlote_list[-4]=='0':
            zlote_list[-4]='tysięcy'

    #==============setzlote_listi tysięcy=================================================
    if len(zlote_list)>5:
        if zlote_list[-6] in set:
            zlote_list[-6]=set[zlote_list[-6]]
            #zlote_list[-4]='tysięcy'






    zlote_final_str=[]
    if len(zlote_list) > 0:
        for i in range(len(zlote_list)):
            if len(zlote_list)>0 and zlote_list[i]!='x' and zlote_list[i]!='0':
                zlote_final_str.append(zlote_list[i])
    zlote_word=''
    if zlote_list[len(zlote_list)-1]=='dwa' or zlote_list[len(zlote_list)-1]=='trzy' or zlote_list[len(zlote_list)-1]=='cztery':
        zlote_word=' złote'
    elif len(zlote_list)==1 and zlote_list[0]=='jeden':
        zlote_word= ' złoty'

    else:
        zlote_word=' złotych'
#==========================grosze=================================================================
    m = ''
    grosze_final_str = []
    if len(grosze_list)>0:
        if len(grosze_list)==1:
            grosze_list.append('0')
        if len(grosze_list) > 1 and grosze_list[-2] == '1':
            if grosze_list[-1] in nas:
                grosze_list[-1] = nas[grosze_list[-1]]
                grosze_list[-2] = 'x'
        else:
            if grosze_list[-1] in jedn:
                grosze_list[-1] = jedn[grosze_list[-1]]
            if len(grosze_list) > 1 and grosze_list[-2] in dzie:
                grosze_list[-2] = dzie[grosze_list[-2]]


        for i in range(len(grosze_list)):
            if grosze_list[i] != 'x' and grosze_list[i] != '0':
                grosze_final_str.append(grosze_list[i])

        if grosze_list[len(grosze_list) - 1] == 'dwa' or grosze_list[len(grosze_list) - 1] == 'trzy' or grosze_list[len(grosze_list)-1]=='cztery':
            grosze_word = ' grosze'
        elif grosze_list[len(grosze_list) - 1] == 'jeden' and grosze_list[len(grosze_list) - 2]=='0' :
            grosze_word='grosz'
        else:
            grosze_word = ' groszy'
        grosze_final_str=' '.join(grosze_final_str)



    zlote_final_str=' '.join(zlote_final_str)

    if grosze_final_str and zlote_list!=['0']:
        return zlote_final_str + zlote_word +' '+grosze_final_str+ ' '+grosze_word
    elif grosze_final_str and zlote_list==['0'] and grosze_final_str!='N o n e':
        return grosze_final_str+' '+grosze_word
    elif zlote_final_str=='':
        return '-'
    elif zlote_final_str!='N o n e':
        return zlote_final_str + zlote_word
    else:
        return '-'

