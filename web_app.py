import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

st.write("""
# Masters Program Tuition Prediction App (fields related to Data Science)
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    state = st.sidebar.selectbox(
        'Which state?',
        ('New York', 'Nebraska', 'Tennessee', 'California', 'Florida',
       'Wisconsin', 'Maryland', 'Missouri', 'Illinois', 'Kentucky',
       'Washington, D.C.', 'Pennsylvania', 'Texas', 'Massachusetts',
       'North Carolina', 'Vermont', 'New Jersey', 'North Dakota',
       'Delaware', 'Indiana', 'Michigan', 'Minnesota', 'Arizona',
       'Connecticut', 'South Carolina', 'West Virginia', 'Kansas',
       'Colorado', 'Utah', 'Iowa', 'Georgia', 'Rhode Island', 'Oregon',
       'Ohio', 'Mississippi', 'New Mexico', 'Oklahoma', 'Washington',
       'New Hampshire', 'Maine', 'Arkansas', 'Alabama', 'Montana',
       'Nevada', 'Louisiana', 'Virginia', 'Idaho', 'South Dakota'))
    university_tier_ranking = st.sidebar.slider('What tier ranking of university? (1 is best, 5 is worst)', 1, 5, 3)
    duration = st.sidebar.slider('Program duration (months)', 3.0, 36.0, 24.0)
    disciplines = st.sidebar.selectbox(
        'Which area of study?',
        ('Data Science & Big Data', 'Informatics & Information Sciences',
       'Statistics', 'Biotechnology', 'Computer Sciences',
       'General Engineering & Technology',
       'Business Intelligence & Analytics', 'Astronomy & Space Sciences',
       'Public Policy', 'Communication Sciences', 'Public Health',
       'Mathematics', 'Social Work', 'Technology Management',
       'Biomedicine', 'Bio & Biomedical Engineering', 'Design',
       'Economics', 'Political Science', 'Business Administration',
       'Management, Organisation & Leadership', 'Marketing',
       'Health Sciences', 'Business Information Systems', 'Biology',
       'Executive MBA', 'Electrical Engineering', 'Accounting',
       'Geographical Information Systems (GIS)', 'Finance',
       'Applied Mathematics', 'Psychology', 'Agribusiness', 'Geography',
       'Master in Business Administration (MBA)',
       'International Relations', 'Computer Science & IT'))
    tags = st.sidebar.selectbox(
        'Which degree are you pursuing?',
        (' M.Sc. ', ' Master ', ' Postgraduate Certificate ', ' M.B.A. ',
       ' M.A. ', ' M.Eng. '))
    delivered = st.sidebar.selectbox(
        'How would you like the material to be delivered?',
        ('On Campus', 'Online', 'Blended'))
    credits = st.sidebar.slider('Desired program credits', 10.0, 130.0, 30.0)
    gpa = st.sidebar.slider('For the following please select 1 if the university requires it, 0 if not. GPA:', 0,1)
    gre = st.sidebar.slider('GRE:', 0,1)
    ielts= st.sidebar.slider('IELTS:', 0,1)
    toefl = st.sidebar.slider('TOEFL:', 0,1)
    gmat = st.sidebar.slider('GMAT:', 0,1)
    fall = st.sidebar.slider('For the following please select 1 if you want the program to start in that season, 0 if not. Fall:', 0,1)
    spring = st.sidebar.slider('Spring:', 0,1)
    summer= st.sidebar.slider('Summer:', 0,1)
    data = {'state': state,
            'university_tier_ranking': university_tier_ranking,
            'duration': duration,
            'disciplines': disciplines,
            'delivered': delivered,
            'tags': tags,
            'credits': credits,
            'gpa_yn': gpa,
            'gre_yn': gre,
            'ielts_yn': ielts,
            'toefl_yn': toefl,
            'gmat_yn': gmat,
            'fall_start_yn': fall,
            'spring_start_yn': spring,
            'summer_start_yn': summer}
    features = pd.DataFrame(data, index=[0])
    return features

df_user = user_input_features()
st.subheader('User Input parameters')
st.write(df_user)
df = pd.read_csv('https://raw.githubusercontent.com/piercepatrick/Data-Science-Masters-Program-Tuition/master/masters_final_df.csv')
df_model = df[['tuition','university_tier_ranking','tags','duration','state','disciplines','delivered','gpa_yn',
             'gre_yn','toefl_yn','ielts_yn','credits','gmat_yn','fall_start_yn','spring_start_yn','summer_start_yn']]
df_model['label'] = 1
df_user['label'] = 2
concat_df = pd.concat([df_model, df_user])
features_df = pd.get_dummies(concat_df, dummy_na = True)
df_model = features_df[features_df['label'] == 1]
df_user = features_df[features_df['label'] == 2]
df_model = df_model.drop('label', axis=1)
df_user = df_user.drop('label', axis=1)
df_user = df_user.drop('tuition', axis=1)
X = df_model.drop('tuition', axis =1)
y = df_model.tuition.values

rf = RandomForestRegressor(bootstrap=True, ccp_alpha=0.0, criterion='mae',
                           max_depth=None, max_features='auto', max_leaf_nodes=None,
                           max_samples=None, min_impurity_decrease=0.0,
                           min_impurity_split=None, min_samples_leaf=1,
                           min_samples_split=2, min_weight_fraction_leaf=0.0,
                           n_estimators=80, n_jobs=None, oob_score=False,
                           random_state=None, verbose=0, warm_start=False)

rf.fit(X,y)

prediction = rf.predict(df_user)

st.subheader('Prediction')
st.write(prediction)
