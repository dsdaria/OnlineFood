import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

url_data = 'https://raw.githubusercontent.com/dsdaria/OnlineFood/main/onlinefoods.csv'
df = pd.read_csv(url_data)
df = df.drop([ "Pin code", "Output"] , axis = 1)
df.index = range(1, len(df) + 1)
df['color']  = np.random.rand(len(df), 4).tolist()


def feedback(df):
    st.title('Feedback From Different Occupation Groups')
    st.subheader("Select the Occupation Group: ")
    type_ = st.selectbox(
    'Select',
    ('Student', 'Employee', 'Self Employeed', 'House wife'))

    df_type = df.loc[df['Occupation'] == type_]

    labels = 'Positive', 'Negative'

    pos = df_type['Feedback'].value_counts()['Positive'] / len(df) * 100
    neg = df_type['Feedback'].value_counts()['Negative '] / len(df) * 100
    sizes = [pos, neg]
    explode = (0, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90, colors=["olivedrab", "tomato"])
    ax1.axis('equal')
    st.pyplot(fig1)


def children(df):
    st.title("Conneation Between the Number of Children and Monthly Income")
    st.subheader("Select the number of children: ")

    number_of_children = st.slider('Number of children', 1, 6, 1)

    df_children = df.loc[df['Family'] == number_of_children]

    len_df_c =  len(df_children)

    no_income = df_children['Monthly Income'].value_counts()['No Income'] / len_df_c * 100
    below_10000 = df_children['Monthly Income'].value_counts()['Below Rs.10000'] / len_df_c * 100
    more_50000 = df_children['Monthly Income'].value_counts()['More than 50000'] / len_df_c * 100
    between_g_1 = df_children['Monthly Income'].value_counts()['10001 to 25000'] / len_df_c * 100
    between_g_2 = df_children['Monthly Income'].value_counts()['25001 to 50000'] / len_df_c * 100


    data_children = {"name": ['No Income','Below Rs.10000', 'More than 50000', '10001 to 25000', '25001 to 50000'],
                    "value": [no_income, below_10000, more_50000, between_g_1, between_g_2]}

    data_children = pd.DataFrame(data_children)
    data_children = data_children.set_index("name")
    st.bar_chart(data_children)

def education(df):
    st.title("Age as a Parameter of Educational Qualification Distributions")
    st.subheader("Select an age group: ")

    age_education = st.slider(label='Age',  min_value=18,  max_value=33, step=1)
    df_education = df.loc[df['Age'] == age_education]
    education_counts = df_education.groupby('Educational Qualifications').size()

    plt.figure(figsize=(10, 10))
    plt.pie(education_counts, labels=education_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title('Distribution of Educational Qualifications')
    plt.axis('equal')
    st.pyplot(plt)

def distribution(df):

    st.title("Numerical Distributions: Monthly Income and Family size")
    st.subheader("Select the comparison criterion: ")
    criteria = st.radio("",
              ["Monthly Income", "Family size"],
        index=None,)


    if criteria == 'Monthly Income':
        plt.figure(figsize=(10, 10))
        plt.grid(True)
        plt.scatter(df["Monthly Income"], df['Age'], alpha=0.6, color="sandybrown")
        plt.title('Numerical Distribution and Monthly Income')
        plt.xlabel('Monthly Income')
        plt.ylabel('Age')
        st.pyplot(plt)

    elif criteria == 'Family size':
        plt.figure(figsize=(10, 10))
        plt.grid(True)
        plt.scatter(df["Family"], df['Age'], alpha=0.6, color="sandybrown")
        plt.title('Numerical Distribution and Family size')
        plt.xlabel('Family size')
        plt.ylabel('Age')
        st.pyplot(plt)
    else:
        st.markdown(" ")

def process_main_page():
    show_main_page(df)
    process_side_bar_inputs()

def show_main_page(df):
    st.title('Dataset "Online Food"')
    url = 'https://www.kaggle.com/datasets/sudarshan24byte/online-food-dataset'
    st.markdown('''The app is based on information collected from an online food ordering platform over a period of time.''')
    st.markdown("Check out this link on [Kaggle](%s)" % url)
    st.dataframe(df.iloc[:, 0:-1])
    st.subheader("Unique geographic coordinates of customers")
    st.map(df,
    latitude='latitude',
    longitude='longitude',
    size=5,
    color='color')


def process_side_bar_inputs():
    distirbution_ = st.checkbox('Numerical Distributions')
    feedback_ = st.checkbox('Feedback Analysis')
    children_ = st.checkbox('The Number of Children and Monthly Income')
    education_ = st.checkbox('Age and Educational Qualification Distributions')


    if distirbution_:
        distribution(df)

    if feedback_:
        feedback(df)

    if children_:
        children(df)

    if education_:
        education(df)

if __name__ == "__main__":
    process_main_page()
