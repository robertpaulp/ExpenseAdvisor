import os
import openai
from dotenv import load_dotenv

def ask_chat_gpt(question):
    try:
        # Ensure the OPENAI_API_KEY environment variable is set
        load_dotenv()

        with open('.env', 'w') as f:
            f.write(f'OPENAI_API_KEY={"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"}\n')

        api_key = os.environ.get("OPENAI_API_KEY")

        if not api_key:
            raise ValueError("OpenAI API key not set in environment variables.")

        # Initialize the OpenAI client
        client = openai.OpenAI(api_key=api_key)

        # Create a chat completion
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": question + "Give me just the short answer without any explanation (it is is a number, just the number), (if there are some jobs, just list them))",
                }
            ],
            model="gpt-4",  # Change this if you're using a different model
        )

        # Parse the response
        response = chat_completion.choices[0].message.content
        return response

    except Exception as e:
        return f"An error occurred: {e}"

def main():
    question = input("Ask a question: ")
    # answer = ask_chat_gpt("Choose just one relevant to a Banker Please? : IT, Real Estate, Apparel, Media & Telecom, Construction, Business, Churches, Temples & Mosque, Entertainment & Hobbies, Community, Food & Beverage, Health & Medical, Home & Garden, Transportation & Shipping, Marketing & Sales, Travel & Tourism, Finance, Education, Agriculture & Farms, Manufacturing & Wholesale, Automotive, Petroleum Refining & Related Activities, Services, Beauty, Electrical & Electronic Stores, Sports, Legal, Retail, Industrial Production, Pets, Fashion Accessories Stores, Others, Textile Production, Boat Services, Funeral Services, Driving School, Wedding & Event Planning Services, Solar Energy Company, Gift & Boutique Shops, Utility Companies, Care Services, Food Production, Food Production & Distribution, Wood & Paper Manufacturing, Oil, Gas & Fuel Companies, General Stores & Hardware Stores,")
    print(answer)

if __name__ == "__main__":
    main()
