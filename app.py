# streamlit
import streamlit as st
st.set_page_config(page_title= " growth mindset project")
st.title("Unlock Your Potential with AI-Driven Growth Mindset")

st.header("🚀 Welcome to Your Growth Journey! 🌱")
st.write("A growth mindset with AI means embracing artificial intelligence as a tool for continuous learning, innovation, and problem-solving. Instead of fearing automation or limitations, individuals with a growth mindset see AI as an opportunity to expand their skills, enhance productivity, and adapt to new challenges.")
st.header("💡 Today's Growth Mindset Quote")
st.write('"The only limit to our realization of tomorrow is our doubts of today." — Franklin D. Roosevelt 🚀')

st.header("⚔️ What's your challange today")
user_input = st.text_input("Describe a challange you're facing:")

# condition
if user_input:
    st.success(f"💪 You are facing:{user_input}.Push beyond limits and chase your dreams! 🚀")
else:
  st.warning("Tell us about your challange to get started")

#   reflexing
st.header("🧠 Reflect on your journey")
reflection = st.text_area("Write your out come here")
if reflection:
    st.success(f"🌟 Great insight your reflection: {reflection}")
else:
    st.info("Reflecting on experience help your grow! Share your difficulties")
    # achivement    
    st.header("🏆Celebrate your accomplishments")
    achivement = st.text_input("Share your accomplishment  here:")
    if achivement:
        st.success(f"🎉 Congratulations on your achivement: {achivement}")
    else:
        st.info("Big or Small , every acheivments count: Share one now 😊")

    # footer
    st.write("- - -")
    st.write("✨keep believing in your self growth is a journey ,not a destination ✨")
st.write("**@All rights are reserved created by sumaira shakeel**")




