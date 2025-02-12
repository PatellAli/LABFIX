from supabase_config import supabase

#Sign in user
def SignInUser(email, password):
    return  supabase.auth.sign_in_with_password(
        {"email":email, "password":password}
    )

#SignOutUser
def SignOutUser():
    supabase.auth.sign_out()



