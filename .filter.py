from transformers import pipeline

# Load the NER pipeline with a pre-trained model
ner_pipeline = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english", grouped_entities=True)

# Define the input text
text="""
I see you from EMS 2 on 1.
I see you.
Repeat your message.
Yeah, this is EMS 2.
I took over staging.
What you have is a rescue, three EMS2. I took over staging.
What you have is a Rescue 3 and a vacuum truck in staging.
We also have engine 29 and truck 94 responding as well.
They should meet up with you in staging.
Roger, engine 29 and, did you say truck 94 or engine 94?
Just let me know when they get off scene.
Roger.
Go.
Rescue 35, it's 12th at FR11 to a 6.
345 south New Hampshire.
So, from Rescue 8, take 4, available on our first hand, if there's a call we can take it.
Natural Rescue 829, we're recampled.
829, yes, update is set 5
830
cancel 835, please respond to Iran
Engine 100
overdose, 6350, Mount Lola.
Rescue 8-0-6, press...
Rescue 8-35, you're cancelled. Mix till available.
"""

# Use the model to extract named entities
entities = ner_pipeline(text)

# Extract only location entities
locations = [entity['word'] for entity in entities if entity['entity_group'] == 'LOC']

print("Locations found:", locations)

