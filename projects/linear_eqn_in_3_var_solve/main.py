from openai import OpenAI
import matplotlib.pyplot as plt
client = OpenAI(api_key='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')

class GenGraphs:
    def lineGraph3Lines(x=[[1,2], [5,4]], y=[[1,2], [10,4]]):
        for graphNo in range(len(x)):
            plt.plot(x[graphNo], y[graphNo])
        plt.show()

def askAI(message, temperature):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a genius mathematician, and you also know how to code. You know all the formulas in the world, and also are capable to visualise data of the problems given. You are tasked to solve the questions given by the user. Write professional solutions given by the users."},
            {
                "role": "user",
                "content": message
            }
        ],
        temperature=temperature
    )
    return completion.choices[0].message.content

if __name__ == "__main__":
    while True:
        user_input = input("ask@ai\n$ ")
        if user_input == 'bye':
            print("Bye!")
            break
        else:
            GenGraphs.lineGraph3Lines()
            # ai_resp = askAI(user_input, 1)
            # print(ai_resp)