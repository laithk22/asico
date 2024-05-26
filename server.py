from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/signup", methods=["POST"])
def save_input():
  
  data = request.get_json()  # Get user data from request body

  if data:
    email = data.get("email", "")
    password = data.get("password", "")
    username = data.get("userName", "")
    fullname = data.get("fullName", "")

    # Use the username or full name to personalize the response
    print(f"success mr {fullname}, or should i say {username}")
    return data
  else:
    return "Error in sending data"
  
@app.route("/login", methods=["POST"])
def process_input():
  data = request.get_json()  
  if data:
    email = data.get("email", "")
    password = data.get("password", "")
    print(f"success with email {email}, and password as {password}")
    return data
  
  else:
    return "Error in sending data"
  
@app.route("/chat", methods=["POST"])
def send_LLMresponse():
    
  data = request.get_json()  
  if data:
    usermessage = data.get("usermessage", "")
    response = f"success with your message: {usermessage}, I received it" #replace with LLM response
    print(f"user sent {usermessage}, and response was {response}")
    return response
  else:
    return "Error in sending data"

    
if __name__ == "__main__":
  app.run(debug=True, port=8000)  # Run the Flask app in debug mode


  