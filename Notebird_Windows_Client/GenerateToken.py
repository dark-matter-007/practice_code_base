# THIS CLASS IS INTENDED NOT TO BE TOUCHED, AND IT IS RESPONSIBLE FOR GENERATING USER SIGN IN TOKENS

# data = {"email": "ashwin.aksharma.p@gmail.com", "password": "shsh yflx zouo xxlw"}
# pickle.dump(data, open("./token.bin", "wb"))

class GenerateToken:
    @staticmethod
    def generate_token(email: str, password: str):
        import pickle
        dataa = {"email": email, "password": password}
        pickle.dump(dataa, open("./token.bin", "wb"))
