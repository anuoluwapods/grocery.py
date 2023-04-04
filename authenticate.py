import streamlit.auth as auth

# Create a GoogleOAuth authenticator instance
google_authenticator = auth.GoogleOAuth(
    client_id="1014493001260-c9d10163p9dtf1dohs0u99bieok07t10.apps.googleusercontent.com",
    client_secret="GGOCSPX-vxgQ-b-SSOXB4e2tT_DoNrwaGfbK",
    redirect_uri="http://localhost:8501/oauth_callback",
    scopes=["email", "profile"],
)

# Authenticate the user using Google
user = auth.authenticate(google_authenticator)

# Verify the user's email address
email = auth.get_verified_email(google_authenticator)

if email:
    st.write(f"Welcome, {email}!")
else:
    st.write("Authentication failed.")
