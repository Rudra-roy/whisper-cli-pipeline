import openai

# Replace with your OpenAI API key
openai.api_key = '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'

def generate_text(prompt, model="gpt-4o-mini"):
    response = openai.completions.create(
        model=model,
        prompt=prompt,
        max_tokens=150
    )

    return response.choices[0].message['content']

if __name__ == "__main__":
    data= """
Find the embedded locations and addresses in the bellow text, and retuen only the founded text. No, extra word or anything. Do not write extra line of text from yourself. Its a strict order only the locations and addresses. If you found nothing then return nothing found.

So yeah, um, I was thinking about how all of this ties together, you know, like when I was last in New York, uh, staying at the Hilton Midtown, I realized how interconnected things are. I was just walking down 6th Avenue, and there’s always something happening, like this time I ended up visiting 230 5th Avenue, you know, that rooftop bar with the incredible views of Empire State Building. I mean, just wow, right?And it wasn’t just New York, you know? Like last month, I had to go down to 1234 Peachtree Street NE, in Atlanta, for a conference. And the meeting, let me tell you, it was so intense. We were discussing data models for hours, right there at The Georgian Terrace. Then later that evening, we all went for dinner at 1500 Southland Circle NW. That area in West Midtown has really grown recently, and I don’t know if you’ve been, but it’s a pretty great spot.Moving on, oh, I also, um, traveled to San Francisco—1 Market Street is where we had this startup showcase. That area around Embarcadero Plaza is just gorgeous. Anyway, Baker Beach, yeah, I managed to squeeze that in between meetings. It’s at 1504 Pershing Drive, and the view of Golden Gate Bridge from there, oh man, so spectacular.Actually, speaking of travel, um, when I was in Los Angeles last year, I stayed in Hollywood. I booked a room at 7000 Hollywood Boulevard. Yeah, that’s, uh, the Roosevelt Hotel, and oh, right down the road at 6801 Hollywood Boulevard, the Hollywood Walk of Fame is always buzzing with people. Just a short drive from there, I visited Venice Beach, which was amazing. You know, the boardwalk and Ocean Front Walk, such an iconic LA vibe. I think the address for the parking lot I used was 100 Venice Boulevard.Then, when I was in London, I had this fascinating conversation with someone at the British Library, which, by the way, is located at 96 Euston Road. It's a beautiful area, especially with King’s Cross Station just around the corner. Anyway, during that same trip, I made a quick stop by 221B Baker Street, you know, the whole Sherlock Holmes thing. It’s funny, how tourists gather around that spot for photos.Oh, oh, and let me tell you about Tokyo. When I was there, uh, I stayed at the Park Hyatt, which is like, um, 3-7-1-2 Nishishinjuku. That view over Shinjuku is just mind-blowing. Then, I took a stroll down to Harajuku, and ended up at Meiji Shrine, which was, um, around 1-1 Yoyogi-Kamizono-cho. That whole Shibuya district—oh, the lights, the energy, it’s unreal.But hey, don’t get me wrong, not all my trips are work-related. For example, I spent a weekend at 400 Royal Street in New Orleans. That’s where Jackson Square is, and it’s just magical. I even got to try beignets at Cafe Du Monde, which is right there on 800 Decatur Street.And yeah, um, when I went to Chicago, the meetings were at 875 North Michigan Avenue. That’s where the John Hancock Center is, and you can see Lake Michigan from the observation deck. Just down the road is 360 Chicago, right at 875 North Michigan. The vibe around Magnificent Mile is amazing, with places like Water Tower Place and Michigan Avenue Bridge.I can’t forget Paris. Uh, Eiffel Tower, as everyone knows, is at Champ de Mars, 5 Avenue Anatole France. But my favorite part? Actually, I loved the quiet mornings in Montmartre. I stayed at this charming little place near Rue de l'Abreuvoir, not far from Place du Tertre. The food, the streets, everything there, just a dream.It reminds me of my trip to Sydney, where I stayed at 201 Sussex Street, which is, uh, near Darling Harbour. The views from the harbor are pretty stunning, and it’s just a quick walk to the Sydney Opera House at Bennelong Point. I also checked out the famous Bondi Beach, the address for the beach parking is around Queen Elizabeth Drive, I think.Coming back to, um, the U.S., I made a trip to Miami last year. Had a few meetings in Brickell, uh, the main office was at 600 Brickell Avenue.










"""
    d = "hello"
    output = generate_text(d)
    print("Model's Response:")
    print(output)
