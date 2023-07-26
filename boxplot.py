import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



#nromal boxplot

rf=pd.DataFrame([0.6610704796028136, 0.6336416219310012, 0.6530073098004708, 0.6355436205556919, 0.6561907894876406, 0.6360116133064602, 0.6506643070334116, 0.643203693451923, 0.6438873407929572, 0.6555056003514369, 0.6460651408442184,0.68])
nn=pd.DataFrame([0.501941010323575, 0.5798529860008141, 0.36639456547571947, 0.6908891119651694, 0.40691763730372704, 0.43356418340252806, 0.5666886977330897, 0.5118540079519854, 0.5449933616711626, 0.6114973701050309, 0.42561529006585413, 0.6400373165463188])
gb=pd.DataFrame([0.5431092639870988, 0.5067550578753418, 0.5745621839499561, 0.5638048444803284, 0.5577657726316588, 0.54096695005311, 0.5456609189577102, 0.565411947039747, 0.49876885289759487, 0.5464135989457533, 0.5782390604755123, 0.5812247696823123])
cnn=pd.DataFrame([0.27382368389524386,  0.6123621425474535, 0.5956942908541674, 0.5908615329957071, 0.5092341322952305, 0.2669533186981732, 0.6074894689126191, 0.6133770995093805, 0.6226114564461124, 0.24542454704688152, 0.099211782099943, 0.6124465445945212])
knn=pd.DataFrame([0.5340911850250072, 0.4412671373307255, 0.4772188746094865, 0.5225246194036038, 0.5081382424789826, 0.23660768391594966, 0.3681514823040711, 0.5191810363274831, 0.616915384981121, 0.3788624328038725, 0.5922732737075355, 0.49675286932405094])
xgb=pd.DataFrame([0.5839899870394852, 0.5568348451837797, 0.3594062596660228, 0.5567628030673069, 0.39160804060808024, 0.2075715475601531, 0.4367204020913954, 0.46981789378739053, 0.5122133126216317, 0.43715420465115945, 0.4424478196034137, 0.3788045763294031])
lgb=pd.DataFrame([0.5204467145876885, 0.5560056852009747, 0.5357058429485695, 0.5192120659979603, 0.4151613419943713, 0.18334266309824093, 0.5134919590717876, 0.5311225883251025, 0.5673565029526042, 0.46873147914119956, 0.5079205611630848, 0.6299079589494782])
vote=pd.DataFrame([0.5115933983119288, 0.607058208819898, 0.47504197504348994, 0.49256865806844785, 0.5179768100434937, 0.6879121047107933, 0.5524426159167063, 0.35147489599835524, 0.45804709810558397, 0.3467446873131164, 0.3552911712120134, 0.4879667969553634])
knn=pd.DataFrame([0.5069407447672837, 0.2130621092079041, 0.5567657560673808, 0.4589461442990797, 0.3334783581283819, 0.37025797247756953, 0.39235187030844254, 0.5487014742570276, 0.4854651441276783, 0.547420616432074, 0.45345577505807544, 0.37667070822549664])
cat_boost=pd.DataFrame([0.5366411932551483, 0.4806309378549934, 0.42237581089574094, 0.38610668887476984, 0.5528879083023305, 0.5487604167587395, 0.35558709900900176, 0.6222085820777882, 0.4578563511386132, 0.4786824722323896, 0.6374757912222478, 0.2429311930525665])
total=pd.concat([rf,nn,gb,cnn,xgb,lgb,vote,knn,cat_boost],axis=1)
total.columns=['rf','nn','gb','cnn','xgb','lgb','vote','knn','cat_boost']

print(total)
plt.boxplot(total,labels=total.columns)
plt.title('wheat dataset for Trait02')
plt.show()





#compare boxplot

one_nn=pd.DataFrame([0.501941010323575, 0.5798529860008141, 0.36639456547571947, 0.6908891119651694, 0.40691763730372704, 0.43356418340252806, 0.5666886977330897, 0.5118540079519854, 0.5449933616711626, 0.6114973701050309, 0.42561529006585413, 0.6400373165463188])
one_nn_not=pd.DataFrame([0.47892728663575335, 0.5853382719937363, 0.5324708187541283, 0.46314300798833447, 0.45691179675226923, 0.4750655237748883, 0.5592040378920959, 0.650452300990326, 0.4444474478478819, 0.4712681163613289, 0.5653872648039167, 0.28623747700845836])

one_nn2=pd.DataFrame([0.5860594681322036,0.6397579347422794,0.5357317087890068,0.580846784454448,0.549819752485119,0.6238165483561586,0.5754742308675268,0.5758225025787143,0.58162975613153,0.6051625920786494, 0.6140883536392122, 0.582171314485582])
one_nn_not2=pd.DataFrame([0.5646646297693628, 0.49281609552102473, 0.5330454131891275, 0.5574061866584491, 0.5578233695294648,0.5954881066329952, 0.5932176257039505, 0.48533958602115174, 0.44641708003484276, 0.5276671129752761, 0.47068818358733, 0.49454569952707667])

cat_one=pd.DataFrame([0.5972203521970915,0.5803026318329206,0.5901644716257275,0.5201155212923365,0.5131679345996107,0.5271201156477785,0.5275665211023239,0.47718294344592965,0.5233873229005999,0.5903685886577816,0.534854240839461,0.5986924806953065])
cat_one_not=pd.DataFrame([0.5582944266566151, 0.6480000649391953, 0.5536183989748236, 0.5381806294434821, 0.5416106678738515, 0.5444928367777432, 0.5375918049011673, 0.6055783551860912, 0.5346264509155557, 0.5549982893003093, 0.5860914761846668, 0.5773734581446137])

knn_not=pd.DataFrame([0.5623555128865763, 0.6343365717246922, 0.5050946997766201, 0.5686335185016969, 0.5124656701440105, 0.5708699894809791, 0.53029186134365, 0.507865595670425, 0.54978567751119, 0.6166098677451308, 0.5463356973047244, 0.5677428583925861])
knn_one=pd.DataFrame([0.6019400254015612 ,0.5236013581251865, 0.5049402658654573,0.5455471731645406,0.5387738459895516, 0.6365764335157061, 0.585999697772185, 0.5716794297881254, 0.5759694309751434, 0.6101654632790354, 0.6298354622773312, 0.6104639675160967])


y1=pd.concat([one_nn,one_nn2,cat_one,knn_one],axis=1)
y2=pd.concat([one_nn_not,one_nn_not2,cat_one_not,knn_not],axis=1)
#x=pd.DataFrame()
#hue=pd.DataFrame(['yes','no','yes','no','yes','no','yes','no'])

x1 = np.arange(1,15,4)
x2 = x1+1
box1 = plt.boxplot(y1,positions=x1,patch_artist=True,showmeans=True,
            boxprops={"facecolor": "C0",
                      "edgecolor": "grey",
                      "linewidth": 0.5},
            medianprops={"color": "k", "linewidth": 0.5},
            meanprops={'marker':'+',
                       'markerfacecolor':'k',
                       'markeredgecolor':'k',
                       'markersize':5})
box2 = plt.boxplot(y2,positions=x2,patch_artist=True,showmeans=True,
            boxprops={"facecolor": "C1",
                      "edgecolor": "grey",
                      "linewidth": 0.5},
            medianprops={"color": "k", "linewidth": 0.5},
            meanprops={'marker':'+',
                       'markerfacecolor':'k',
                       'markeredgecolor':'k',
                       'markersize':5})

city = ['trait02_nn','bruchclaster_nn','bruchclaster_catboost','bruchclaster_knn']
plt.xticks([1.5,5.5,9,13.5],city,fontsize=9.5)
# plt.ylim(10,45)
plt.ylabel('person correlation ',fontsize=11)
plt.grid(axis='y',ls='--',alpha=0.8)

plt.legend(handles=[box1['boxes'][0],box2['boxes'][0]],labels=['yes','no'])

#plt.tight_layout()
plt.title('one_hot encoding or not ')
# plt.savefig('boxplot2.png',dpi=600)
plt.show()


#boxplot with linchart

x_num=[16,32,80,120]
x = [i for i in x_num for _ in range(10)]
print(x)
y=[0.5116432132597554, 0.5736828048826517, 0.5801718801457383, 0.5321480819388315, 0.6234522466027288, 0.591235336421676,
0.5816501253505392, 0.60082839816846, 0.5597908952266634, 0.5659858451629978,
   0.5286236860278205, 0.5463124769403721, 0.4885318238369455, 0.5327574673272132, 0.5624845568175074,
   0.6581342031434455,
   0.257050199569373, 0.5763088989326144, 0.5143228966959229, 0.5602668354748629,
   0.5679296157075772, 0.49804262260418825, 0.7625042057672697, 0.6253010635623443, 0.6137935990684469,
   0.6493910541587881, 0.6865952037184663, 0.7219246712149344, 0.6303157097422921, 0.6373430222290306,
   0.5417782251414167, 0.2593691830466444, 0.5935867013610553, 0.3780651168508841, 0.6201239632830772,
   0.39051783959562675, 0.6167088703228926, 0.6307453531588748, 0.6754309777139763, 0.2766735829131614 ]
df = pd.DataFrame({'x': x, 'y': y})

fig, ax = plt.subplots()

# Boxplot
df.boxplot(column='y', by='x', ax=ax, grid=False)

# Median line and points
medians = df.groupby('x')['y'].median()
ax.plot(range(1,5), medians, color='red', linestyle='--', label='Median')
ax.scatter(range(1,5), medians, color='red', marker='o')

ax.set_xlabel('neuron number')
ax.set_ylabel('Pearson correlation coefficient')
ax.set_title('Prediction accuracy trend by neuron number')

plt.legend()
plt.show()





