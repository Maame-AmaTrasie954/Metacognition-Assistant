import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Metacognition Assistant",
                   layout="wide",
                   page_icon="")

# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

metacognition_model = pickle.load(open('metacognition_model.sav', 'rb'))


# sidebar for navigation
with st.sidebar:
    selected = option_menu('Metacognitive Assistant',
                           ['Type of Learner'],
                           menu_icon='open_book:',
                           icons=['notebook:'],
                           default_index=0)


if selected == 'Type of Learner':

    # page title
    st.title('Metacognitive Assistant')

    #instructions
    st.write("""

For Gender, please enter 0 for male and 1 for female. For Age, enter 0 if you are between 17 and 20 years old, 1 if you are between 21 and 24 years old, and 3 if you are 25 years or older.

For the remaining characteristics, rate each on a scale from 1 to 5, where 1 represents Strongly Disagree, 2 represents Disagree, 3 represents Neutral, 4 represents Agree, and 5 represents Strongly Agree. 
""")

    # getting the input data from the user
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        Gender_input = st.selectbox('Select Gender', options=['M', 'F'])

        # Map "M" to 0 and "F" to 1
        Gender = 0 if Gender_input == 'M' else 1

        st.write(f'Gender mapped to: {Gender}')

    with col2:
        Age_input = st.selectbox('Select Age Range', options=['17-20', '21-24', '25 or older'])

        # Map age ranges to integers
        if Age_input == '17-20':
            Age = 0
        elif Age_input == '21-24':
            Age = 1
        else:  # '25 or older'
            Age = 2

        st.write(f'Age mapped to: {Age}')

    with col3:
        auditoryLearner = st.selectbox(
            'You prefer learning with background music, sounds, or by vocalising thoughts through talking, humming, or singing.',
            options=[1, 2, 3, 4, 5])

    with col4:
        collaborativeLearner = st.selectbox(
            'You prefer learning through explanations, group studies, and collaborative interactions.',
            options=[1, 2, 3, 4, 5])

    with col5:
        visualLearner = st.selectbox(
            'You learn best using visual aids such as diagrams, charts, and drawings, and enjoy visualizing and creating concepts.',
            options=[1, 2, 3, 4, 5])

    with col1:
        focusedLearner = st.selectbox('You are able to stay focused and free from any form of distraction.',
                                      options=[1, 2, 3, 4, 5])

    with col2:
        planner = st.selectbox('You enjoy planning and incorporate both writing and speaking in your study routines.',
                               options=[1, 2, 3, 4, 5])

    with col3:
        linguisticAffinity = st.selectbox(
            'You have a strong affinity for language, enjoy word games, and see yourself as an intellectual, bookworm, or storyteller.',
            options=[1, 2, 3, 4, 5])

    with col4:
        logicalThinker = st.selectbox(
            'You have a strong inclination towards numbers, patterns, logical reasoning, and fact-based arguments.',
            options=[1, 2, 3, 4, 5])

    with col5:
        hands_on_Learner = st.selectbox(
            'You learn best through hands-on activities, physical engagement, and practical lessons.',
            options=[1, 2, 3, 4, 5])

    with col1:
        empathetic = st.selectbox('You are sensitive and empathetic.', options=[1, 2, 3, 4, 5])

    with col2:
        solitaryLearner = st.selectbox(
            'You prefer solitary learning and absorbing information through reading and writing.',
            options=[1, 2, 3, 4, 5])

    with col3:
        socialLearner = st.selectbox('You are extraverted and enjoy learning through social interactions.',
                                     options=[1, 2, 3, 4, 5])

    # code for Prediction
    typeOfLearner = ''

    # creating a button for Prediction

    if st.button('Type of Learner Result'):

        user_input = [Gender, Age, auditoryLearner, collaborativeLearner, visualLearner,
                      focusedLearner, planner, linguisticAffinity,logicalThinker, hands_on_Learner,
                      empathetic, solitaryLearner, socialLearner ]

        user_input = [float(x) for x in user_input]

        Learner_prediction = metacognition_model.predict([user_input])

        if Learner_prediction[0] == 0:
            typeOfLearner = 'You are an Auditory Learner. You learn best through listening and verbal interaction. Similar to verbal and social learners, you absorb information more effectively through discussions and listening to explanations. To improve, listen to audio materials, participate in discussions, and repeat information aloud. Audiobooks, podcasts, and verbal note-taking apps are important resources for you.'
        elif Learner_prediction[0] == 1:
            typeOfLearner = 'You are a Social Learner. You thrive in group settings and learn best through interaction and collaboration with others. Closely related to verbal and auditory learners, you grasp concepts better through discussions and group activities. To improve, engage in group projects, role-playing, and teaching others. Tools like discussion forums, collaboration platforms, and role-play activities are essential for your growth.'
        elif Learner_prediction[0] == 2:
            typeOfLearner = 'You are a Logical Learner. You excel in reasoning, problem-solving, and working with structured data. You’re closely related to visual and physical learners and enjoy puzzles, experiments, and anything involving cause-and-effect reasoning. To enhance your learning, practice problem-solving, analyze data, and engage in experiments. Puzzles, coding kits, and data analysis software are useful tools for you.'
        elif Learner_prediction[0] == 3:
            typeOfLearner = 'You are a Verbal Learner. You excel in learning through words, both written and spoken. Being closely related to auditory and social learners, you enjoy reading, writing, and engaging in debates. To improve, read extensively, practice writing, and engage in verbal exchanges like debates. Books, writing tools, and debate clubs are key resources that support your learning.'
        elif Learner_prediction[0] == 4:
            typeOfLearner = 'You are a Visual Learner. You understand and retain information best when it is presented visually, such as through images, diagrams, charts, and graphs. You’re closely related to logical and kinesthetic learners, as you often prefer to see the bigger picture and make connections through visual representation. To enhance your learning, you can utilize visual aids like mind maps, infographics, and color-coded notes to organize and understand information better. Watching educational videos or drawing diagrams can also help solidify concepts. Incorporating visual tools such as flashcards, visual organizers, and graphic design software into your study routine will support your learning and make complex information more digestible.'
        elif Learner_prediction[0] == 5:
            typeOfLearner = 'You are a Physical/Kinesthetic Learner. You learn best through hands-on activities and physical movement. Engaging your body in the learning process helps you understand and remember information more effectively. You’re closely related to logical and visual learners, as you prefer active learning methods that allow you to manipulate and interact with materials. To improve, you should engage in activities that involve movement or touch, such as building models, conducting experiments, or using tools and equipment. Role-playing scenarios, participating in sports, or even studying while walking around can enhance your retention. Using materials like interactive simulations, physical models, and tools for hands-on projects will further support your learning style, helping you to stay engaged and absorb information more effectively.'
        else:
            typeOfLearner = 'You are a Visual Learner. You understand and retain information best when it is presented visually, such as through images, diagrams, charts, and graphs. You’re closely related to logical and kinesthetic learners, as you often prefer to see the bigger picture and make connections through visual representation. To enhance your learning, you can utilize visual aids like mind maps, infographics, and color-coded notes to organize and understand information better. Watching educational videos or drawing diagrams can also help solidify concepts. Incorporating visual tools such as flashcards, visual organizers, and graphic design software into your study routine will support your learning and make complex information more digestible.'


    st.success(typeOfLearner)

