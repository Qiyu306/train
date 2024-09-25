# import packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# show the title
st.title('Titanic App by Zhangjie Lai')


# read csv and show the dataframe
df = pd.read_csv('train.csv')

# create a figure with three subplots, size should be (15, 5)
# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
# a sample diagram is shown below

st.write(df[['city', 'country', 'population']])
fig,ax= plt.subplots(1,3,figsize=(15,5))
df[df['Pclass']==1].Fare.plot.box(ax=ax[0])
ax[0].set_xlabel('Pclass=1')
ax[0].set_ylabel('Fare')

df[df['Pclass']==2].Fare.plot.box(ax=ax[1])
plt.xlabel('Fare')
ax[1].set_xlabel('Pclass=2')

df[df['Pclass']==3].Fare.plot.box(ax=ax[2])
plt.xlabel('Fare')
ax[2].set_xlabel('Pclass=3')


st.pyplot(fig)