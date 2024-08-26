import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df=pd.read_csv('medical_examination.csv')

# 2
df['overweight']=[ 1 if x>25 else 0 for x in df['weight']/((df['height']/100)**2)]

# 3
df['cholesterol']=[ 0 if x==1 else 1 for x in df['cholesterol']]
df['gluc']=[ 0 if x==1 else 1 for x in df['gluc']]

# 4
def draw_cat_plot():
    # 5
    df_cat=pd.melt(df,id_vars='cardio',value_vars=['cholesterol','gluc','smoke','alco','active','overweight'])


    # 6
    df_cat=df_cat.groupby(['cardio','variable','value']).value_counts().to_frame()
    df_cat=df_cat.reset_index()
    df_cat=df_cat.rename(columns={0:'total'})
    

    # 7



    # 8
    fig=sns.catplot(data=df_cat, x='variable',y='total', kind='bar', hue='value', col='cardio').figure


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat=df.loc[(df['ap_lo'] <= df['ap_hi']) & 
               (df['height'] >= df['height'].quantile(0.025)) & 
               (df['height']<=df['height'].quantile(0.975)) &
               (df['weight'] >= df['weight'].quantile(0.025)) & 
               (df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr()

    # 13
    mask=np.triu(corr)



    # 14
    fig, ax = plt.subplots(figsize=(12,6))

    # 15
    sns.heatmap(corr, annot=True, mask=mask, fmt='.1f')



    # 16
    fig.savefig('heatmap.png')
    return fig
