experimental_data=[(203.96935366605618, 3.6236800011478305), (245.69114764482345, 2.5689954976962932), (239.63438120412232, 2.5713366188827265), (189.36591228846885, 3.1540244055624758), (111.43204914150688, 8.1696752407461783), (207.32680522705272, 3.026045517845918), (264.8393324954053, 2.4416420424392249), (144.85766191924512, 5.1482403318133469), (124.84448741258993, 6.5462805948653529), (109.11582701887153, 9.5459326923835963), (109.14575513306579, 8.701586669774322), (153.76859067461749, 4.9682826810133864), (246.59886090908026, 2.7941491059160417), (145.08430033257423, 5.3798783290838301), (181.48630172255744, 3.3786473079440942), (296.00840136351894, 2.7076518974888186), (143.51791746953251, 5.2283390658181625), (291.33779532362166, 1.9130435659045719), (130.65687336694253, 6.479997876184644), (267.9807806900896, 2.8677012219049618), (232.66081388011543, 3.2860854111655939), (298.65839492102384, 2.366780626113413), (280.43866195918883, 2.0389654773857879), (273.45156179153878, 2.2732288646263061), (266.23615785290224, 2.5199497092331762), (139.69880734182109, 5.3218862610124091), (248.32274960154558, 2.9751709238837432), (119.33547334977861, 7.6779774629955426), (115.84875500204355, 8.2377243679585082), (112.12311197712026, 8.9201008361384204), (266.93119983401641, 2.9565481485864806), (187.05077060298555, 4.0088838201523149), (103.85112749577554, 10.032991787687269), (198.90333963103947, 3.6822393220531722), (195.49304748667089, 3.2713352779807159), (292.63056978401187, 2.2042519892918793), (217.02147505796466, 2.8111877951917199), (201.33078125784647, 3.1775229263026636), (216.37990435154126, 2.9256344629180924), (281.50670292987559, 1.9933463522298778), (211.56148022544059, 3.0773921955233199), (133.11995792016782, 6.5682826888103056), (191.68563190316667, 3.4379386715422964), (285.17511666000246, 2.4537442491121171), (254.94338341999406, 2.1552075747097761), (227.63603305109274, 2.4546627992454644), (230.17654229002088, 3.2077960310435225), (177.76631733590341, 4.2148539864942531), (174.49707572077983, 4.403014573195728), (100.5210960776798, 11.046854338400221), (141.1260218959988, 5.1055128973332531), (200.28225702824335, 3.1968177710127277), (267.68867211105407, 2.8018708963966579), (128.8809959552226, 6.796888943234479), (209.65910535851197, 3.3430911403901469), (285.14483063498903, 2.5726698754266852), (171.92317896938238, 4.1256045510260195), (158.07639389549189, 5.0795224010122979), (113.19666217333469, 7.9426707556544232), (193.48966030242107, 3.1722804406157343), (255.07329354144537, 2.3344124005137377), (195.28068107295562, 3.4573465897461508), (183.09725218584222, 3.2249328487824225), (135.95121929524774, 5.4153477686167175), (267.47601424004125, 2.3212487554600036), (215.8969424087125, 2.7946129548309626), (113.93297318297932, 8.1609464202344668), (203.31353375613435, 3.4971561246431224), (158.68449233558033, 4.538225058225497), (183.45844792035984, 3.4459350872523986), (156.16290402828591, 4.2852214699536253), (280.6398476314381, 1.9176106807059239), (140.94426342931845, 5.1533855583412427), (175.62052653070822, 4.0434904236526572), (186.07999195301434, 3.4414274801117868), (234.13238756182704, 3.1589330490903196), (237.9183918239728, 3.021185463566284), (113.3629902933059, 7.8521790858837237), (138.16666669007344, 5.6283905540747856), (129.83386512795178, 5.9957233266021204), (217.21859499857163, 2.8353008897700707), (252.70524179629422, 2.7277927526130439), (216.75453259096082, 3.5249659388859351), (159.14482568642438, 4.772017375345083), (219.51226392175252, 2.7242634665703145), (244.03849796909088, 2.6010537089914068), (170.73657567094938, 4.4017327441768153), (139.04336390741207, 5.9218621403594858), (233.99576678643649, 2.4296255018678501), (155.7527106158966, 4.7151482622656502), (133.19681725820718, 5.6937119116585535), (242.76647988792055, 2.6353213576862471), (189.1788922720159, 3.3385707870618901), (247.03945453501777, 2.972159429935691), (234.02696189516342, 2.9823121771307903), (129.90075057086969, 6.0769569333148192), (276.36743553532108, 2.5350931205675171), (237.48595334396069, 3.1120208936124176), (169.31498940778619, 4.1020927705134218), (194.84992167847139, 3.5816350401484569)]
T,K=zip(*experimental_data)
T=list(T)
K=list(K)
print (temp)
print(rate)
R=8.314
ans=0
def f(dG):
    er=0
    for i in range(1,100,1):
        er=er+(rate[i]-(np.exp(-deltag/(R*temp[i]))))**2
        return er
dGmin=minimize(func,b)
print(dGmin)
print(dGmin.x)

