
This dataset is described in the paper:
"Shared memories reveal shared structure in neural activity across individuals"
Janice Chen, Yuan Chang Leong, Christopher J. Honey, Chung H. Yong, Kenneth A. Norman, and Uri Hasson. 
Nature Neuroscience 20, no. 1 (January 2017): 115-25. doi:10.1038/nn.4450

Seventeen subjects watched the first 50 minutes of Episode 1 of BBC's Sherlock. The movie was split into two parts of approximately equal length (946 and 1030 TRs). Immediately afterward (a few minutes to set up the next scan, but no intervening task), subjects described aloud what they recalled from the movie. The movie was segmented into 50 scenes, following major shifts in the narrative (e.g., director's cuts) and each subject's recall/description was segmented into the same scenes (for the scenes that they remembered). 

All data were preprocessed and transformed to 3mm MNI space as described in the paper. Data were zscored across time at every voxel. 6mm smoothing was applied.
Files are cropped so that all movie-viewing data are aligned across subjects, and all recall data are aligned to the scene timestamps below. The cropping includes a constant 3-TR (4.5 sec) shift to correct for hemodynamic lag; no additional shifting should be necessary.

Cite the paper when you use these data.

Additional notes:

- Movie scans 1 and 2 are concatenated into a single file for each subject, "sherlock_movie_s#.nii".
Movie Scan 1: 946 TRs
Movie Scan 2: 1030 TRs
Thus, the sherlock_movie_s#.nii files are 1976 TRs total length.

- Subject 5 has a small amount of missing data at the end of the movie scan, ~1 scene; the data have been padded to make them the same length as the other subjects. This can be seen by plotting the timecourses of voxels -- the padded section is perfectly flat. You may choose to exclude these data from your analyses.

Scene number and Onset/Offset of each MOVIE scene, in TRs, same for all subjects:

Movie Scan 1
Scene Onset Offset
     1     1    26
     2    27    35
     3    36    55
     4    56    86
     5    88   109
     6   110   130
     7   132   143
     8   145   157
     9   158   172
    10   174   192
    11   194   203
    12   206   225
    13   227   313
    14   315   361
    15   364   399
    16   400   503
    17   508   525
    18   527   534
    19   536   615
    20   616   633
    21   635   641
    22   643   679
    23   680   697
    24   700   747
    25   749   868
    26   873   891
    27   892   945
   
Movie Scan 2
Scene Onset Offset
1           1          25
2          27          69
3          71         129
4         131         145
5         146         193
6         195         275
7         276         325
8         344         412
9         414         489
10         491         523
11         525         635
12         636         671
13         672         728
14         730         747
15         748         756
16         758         790
17         791         813
18         815         859
19         860         875
20         877         912
21         914         960
22         962        1000
23        1001        1030


Scene number (matching the movie) and Onset/Offset of each RECALL scene, in TRs, different for each subject:

Subject 1:
Scene	Onset	Offset
     2     2     7
     3     8    11
     5    12    17
     8    18    47
    14    48    68
    15    84   113
    16   114   173
    18   195   210
    19   174   194
    22   211   220
    24   221   233
    30   234   257
    32   258   267
    34   268   295
    35   296   311
    36   312   337
    37   338   353
    38   354   382
    39   383   394
    40   395   408
    41   409   423
    43   424   439
    44   440   449
    45   450   478
    48   479   498
    49   499   507
    50   509   520
	
Subject 2:
Scene	Onset	Offset
     2     6    18
     3    19    24
     5    25    44
    13   114   179
    14   273   292
    15    68    99
    16   101   110
    19   180   217
    22   218   249
    24   250   261
    25   293   333
    26   334   354
    29   355   375
    30   399   488
    34   489   517
    35   518   549
    36   550   634
    37   635   653
    38   654   713
    39   714   738
    41   739   751
    44   785   820
    45   821   860
    49   861   883
	
Subject 3:
Scene	Onset	Offset
     2     6    20
     3    21    25
     4    26    34
     5    35    54
     8    55    88
     9    89    97
    10    98   107
    11   108   118
    13   180   221
    14   129   152
    16   153   179
    16   222   245
    19   246   273
    22   274   299
    24   300   325
    29   326   345
    30   346   355
    33   356   423
    34   424   461
    35   462   475
    36   476   501
    37   502   506
    38   507   540
    40   541   565
    41   566   575
    42   576   581
    43   586   589
    44   590   608
    45   609   621
    46   622   643
    47   644   676
    48   677   697
    49   698   713
	
Subject 4:
Scene	Onset	Offset
     2     3    12
     3    13    30
     4    31    47
     5    48    66
     8    95   111
     9   112   113
    10   114   119
    11   120   125
    12   126   139
    13   140   158
    14    67    94
    15   168   189
    16   190   217
    19   218   233
    21   240   247
    22   248   271
    23   234   239
    24   272   280
    25   281   284
    27   285   299
    30   300   319
    33   320   339
    34   340   347
    35   348   363
    36   364   371
    37   372   378
    38   379   388
    39   389   395
    40   396   400
    43   401   407
    44   408   414
    45   415   425
    47   426   435
	
Subject 5:
Scene	Onset	Offset
     2     5    22
     4    23    33
     5    34    43
     7    44    55
     9    56    63
    10    64    74
    11    75    84
    12    85    99
    13   100   123
    14   124   135
    15   136   143
    16   144   170
    19   171   183
    22   184   205
    24   206   215
    27   216   238
    29   239   243
    30   244   251
    31   252   279
    34   280   297
    35   298   315
    36   316   327
    37   328   335
    38   336   349
    40   350   364
    42   365   371
    43   372   385
    44   386   400
    45   401   413
    48   414   432
    49   433   444
    50   445   466

Subject 6:
Scene	Onset	Offset
     2    14    28
     3    29    37
     4    38    53
     5    54    64
     7    65    81
     8    82    93
     9    94   109
    10   110   118
    11   119   135
    13   234   273
    14   140   158
    15   159   191
    16   192   233
    18   537   551
    19   276   291
    22   292   305
    24   306   330
    25   331   381
    26   382   425
    27   426   447
    30   448   464
    32   529   536
    33   465   511
    34   512   528
    35   552   603
    36   604   620
    37   621   632
    38   633   645
    39   646   659
    40   660   705
    42   706   712
    43   718   722
    44   723   734
    45   735   759
    46   760   778
    47   810   825
    48   779   809
    49   826   850
    50   851   880
	
Subject 7:
Scene	Onset	Offset
     2    18    25
     3    26    31
     5    32    48
     7   144   160
     8   161   179
     9   180   188
    10   189   207
    11   208   213
    12   221   247
    14    49    79
    15    80    85
    16    86   143
    19   254   293
    22   296   327
    23   333   344
    24   345   358
    27   374   429
    30   359   373
    31   430   463
    33   464   516
    36   598   616
    37   617   620
    38   621   625
    39   626   627
    40   628   634
    45   551   571
    46   635   652
    48   520   550
    49   572   597
    50   653   673
	
Subject 8:
Scene	Onset	Offset
           2          28          37
           3          38          42
           5          44          59
           7          61          75
           8          76          77
           9          79          87
          11          88          97
          12          98         105
          13         106         149
          14         151         164
          14         192         201
          16         166         191
          16         202         240
          19         242         277
          21         280         289
          22         290         340
          23         342         354
          24         355         373
          25         374         426
          26         427         448
          27         450         507
          29         511         530
          30         531         531
          31         534         599
          32         602         622
          34         624         647
          35         648         667
          36         668         695
          37         696         701
          38         703         731
          39         766         789
          40         732         762
          42         798         802
          43         791         797
          44         804         821
          45         823         830
          46         831         848
          47         849         878
          48         880         910
          48         931         949
          49         911         928
          50         950        1009
		  
Subject 9:
Scene	Onset	Offset
     2    22    31
     3    34    48
     4    49    70
     8   216   236
    11   238   239
    12   242   249
    14    72   110
    15   115   156
    16   158   190
    19   192   214
    22   250   269
    24   272   285
    27   286   313
    29   316   333
    31   338   363
    32   366   378
    34   379   406
    35   407   439
    36   442   487
    37   488   510
    38   512   575
    39   577   583
    41   584   587
    44   588   594
    45   628   640
    47   642   675
    48   596   627
    50   678   695
	
Subject 10:
Scene	Onset	Offset
     2    11    19
     3    20    23
     4    24    28
     5    29    41
     7    42    54
     8    56    58
     9    74    77
    11    60    70
    12    72    85
    13   133   161
    14    86   131
    15   164   180
    16   184   234
    18   238   249
    19   251   283
    21   285   295
    22   296   329
    24   332   340
    25   342   404
    26   406   418
    27   420   474
    29   484   498
    30   476   483
    31   499   531
    33   534   547
    34   548   572
    35   576   606
    36   608   643
    37   645   659
    38   662   679
    39   680   695
    40   696   727
    41   730   735
    42   736   741
    43   742   756
    44   758   763
    45   764   788
    48   790   819
    49   820   825
    50   828   840
	
Subject 11:
Scene	Onset	Offset
     2    14    24
     3    25    27
     4    28    31
     5    33    47
     8   182   185
     9   160   176
    11   177   181
    12   187   191
    13   210   219
    14    49    65
    15    66    98
    16   100   138
    17   140   146
    19   148   159
    22   192   209
    23   220   239
    24   240   253
    30   255   279
    31   280   297
    32   314   321
    34   298   313
    35   322   355
    36   357   371
    37   372   377
    38   379   396
    39   397   398
    40   399   435
    41   437   439
    42   440   444
    44   445   451
    45   452   461
    48   462   483
    49   485   490
    50   492   521
	
Subject 12:
Scene	Onset	Offset
           2          44          60
           3          62          75
           4          77          89
           5          90         107
           7         109         121
           8         123         152
           9         154         167
          10         170         190
          11         192         203
          12         204         233
          13         236         311
          14         314         341
          15         344         406
          16         408         480
          18         542         551
          19         483         527
          21         530         533
          22         534         541
          22         554         614
          24         616         631
          25         633         664
          26         666         683
          27         685         741
          29         742         773
          30         775         786
          31         788         825
          32         828         836
          34         838         868
          35         870         887
          36         888         937
          37         939         963
          38         965        1006
          38        1012        1040
          39        1008        1011
          41        1042        1050
          42        1051        1056
          44        1058        1073
          45        1075        1111
          48        1112        1166
          50        1168        1223
		  
Subject 13:
Scene	Onset	Offset
           1          67         109
           2         112         123
           3         124         130
           4         132         157
           5         159         203
           6         530         535
           7         208         225
           8         227         232
           8         244         249
           9         234         243
          10         252         262
          11         264         273
          12         276         312
          13         314         409
          14         420         486
          15         412         414
          15         488         527
          16         538         640
          17         830         839
          18         643         651
          19         653         710
          20         712         717
          21         722         737
          22         738         783
          22         814         821
          23         784         801
          24         804         813
          24         823         837
          25         839         940
          25         840         857
          27         942        1035
          29        1036        1072
          30        1074        1111
          31        1113        1167
          32        1170        1194
          33        1196        1283
          34        1284        1333
          35        1336        1360
          36        1366        1396
          37        1397        1413
          38        1419        1513
          38        1562        1571
          39        1518        1541
          40        1542        1561
          41        1572        1581
          42        1761        1765
          43        1583        1589
          44        1598        1607
          45        1608        1657
          46        1766        1780
          48        1659        1717
          49        1718        1729
          50        1730        1760
          50        1782        1789
          50        1818        1823
		  
Subject 14:
Scene	Onset	Offset
           2          54          70
           3          71          77
           4          79          89
           5          92         121
           7         168         194
           8         196         207
          10         208         232
          11         235         259
          12         260         289
          13         291         353
          14         124         165
          15         364         409
          16         354         362
          16         410         509
          19         512         559
          21         560         567
          22         569         618
          24         620         649
          25         650         678
          26         680         697
          30         699         717
          31         719         754
          33         758         777
          34         778         803
          35         804         828
          36         829         866
          37         867         885
          38         887         901
          38         981        1017
          39         903         937
          40         938         979
          42        1019        1030
          43        1032        1041
          44        1044        1057
          45        1062        1077
          46        1206        1227
          47        1081        1093
          48        1095        1145
          49        1146        1205
          50        1228        1275
		  
Subject 15:
Scene	Onset	Offset
     8    22    45
    11    48    55
    13    58   133
    15   164   202
    16   136   163
    16   204   253
    17   257   261
    19   263   289
    22   293   323
    24   325   339
    27   342   415
    30   421   442
    31   445   470
    32   474   484
    33   487   511
    34   512   521
    35   524   541
    36   544   563
    37   565   575
    38   578   618
    38   664   675
    39   620   640
    40   644   663
    44   677   695
    45   698   749
    46   752   771
    48   774   797
    49   798   810
    50   813   827
	
Subject 16:
Scene	Onset	Offset
     2    20    25
     3    32    34
     5    26    31
     5    36    54
     7    56    64
     8    65    66
     9    68    69
    11    97   113
    13    71    95
    14   118   133
    15   135   169
    16   170   235
    16   446   457
    18   274   280
    19   236   255
    21   256   262
    22   263   273
    22   281   323
    23   324   329
    24   330   356
    25   364   413
    27   358   363
    27   414   427
    27   574   589
    30   429   445
    30   459   471
    31   473   520
    34   522   553
    35   554   571
    36   591   621
    37   623   635
    38   636   652
    39   654   674
    40   676   699
    41   702   710
    42   712   717
    43   718   737
    44   739   745
    45   746   769
    46   792   808
    48   770   790
    49   810   833
    50   835   866
	
Subject 17:
Scene	Onset	Offset
           2          41          51
           3          52          67
           4          69          81
           5          83         109
           7         112         136
           8         138         146
           8         384         387
           9         147         163
          10         165         185
          11         186         197
          11         388         390
          12         199         201
          12         211         221
          12         391         393
          13         202         210
          13         223         251
          14         254         289
          15         292         333
          16         334         383
          19         395         424
          22         426         461
          25         464         567
          27         568         628
          29         629         637
          30         648         703
          31         704         737
          32         739         754
          33         756         813
          34         816         833
          35         834         887
          35        1290        1296
          36         889         968
          37         970         989
          38         990        1050
          38        1212        1234
          39        1052        1077
          40        1078        1135
          41        1137        1173
          43        1174        1183
          44        1184        1211
          44        1235        1251
          45        1254        1288
          46        1298        1315
          47        1350        1377
          48        1317        1348
          49        1378        1409
          50        1412        1440
		  
		  
To check your results, here are the mean diagonal values for each subject's movie vs. recall (within-subject) correlation matrix of average scene patterns in the "pmc_nn.nii" ROI:
(same values as in the Nat Neurosci paper figure 2C)
(ROI taken from a resting-state connectivity atlas, Shirer et al. (2012) Cereb Cortex)
Subject  R-value
1	0.0764
2	0.1857
3	0.1558
4	0.0924
5	0.1104
6	0.2262
7	0.1007
8	0.1811
9	0.0861
10	0.1331
11	0.1429
12	0.2254
13	0.1737
14	0.1087
15	0.1386
16	0.0800
17	0.2540

There may be slight variation in these computed R-values (around 0.01), depending on calculation details such as the order of averaging steps and z-scoring (e.g., averaging across subjects at the TR-level before within-scene).



