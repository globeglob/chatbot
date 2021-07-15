from GPTJ.Basic_api import SimpleCompletion

#prompt = "User says good morning. Machine Replies "

max_length = 20

temperature = 0.6

top_probability = 1.0

#query = SimpleCompletion(prompt, length=max_length, t=temperature, top=top_probability)

#print(query.simple_completion())

def generate(context, prompt):
    conversation = ""
    for i in context:
        conversation += ("\"" + i + "\" ")
    query = SimpleCompletion(conversation + "\"" + prompt + "\"", length=max_length, t=temperature, top=top_probability)
    response = query.simple_completion()
    new_text = response.split('"')
    return new_text[1]
        


    
