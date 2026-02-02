
def mad_lib():
    adjective_1 = input("Enter first Adjective: ").strip().lower()
    noun = input("Enter any Noun(Person/Thing): ").strip().title()
    verb = input("Enter any verb(action word): ").strip().lower()
    place = input("Enter Name of a Place: ").strip().lower()
    adjective_2 = input("Enter second Adjective: ").strip().lower()
    animal = input("Enter Name of a Animal: ").strip().lower()
    clothing = input("Enter Name of a Clothing: ").strip().lower()
    food = input("Enter Name of a Food: ").strip().lower()
    celebrity_name = input("Enter your favorite Celebrity: ").strip().title()
    adverb = input("Enter any Adverb: ").strip().lower()

    story_title_1 = "The Classic Adventure"
    story_result_1 = f"Once upon a time, there was a {adjective_1} {noun} who loved to {verb} in the {place}. One day, they met a {adjective_2} {animal} wearing {clothing} and eating {food}. Together they decided to visit {celebrity_name}'s house."

    story_title_2 = "The Breaking News"
    story_result_2 = f"This just in! A {adjective_1} {noun} has been {adverb} trying to {verb} all over the {place}. Eyewitnesses report seeing a {adjective_2} {animal} in {clothing} offering them some {food}. The {noun} is now requesting a meeting with {celebrity_name} to discuss the situation."

    story_title_3 = "The Recipe Show"
    story_result_3 = f"Welcome to Celebrity Chef {celebrity_name}'s cooking show! Today's {adjective_1} recipe requires one fresh {noun}. First, {verb} {adverb} around your {place}. Then add a {adjective_2} {animal} dressed in {clothing}. Season everything with {food} and your dish is complete!"

    story_title_4 = "The Job Application"
    story_result_4 = f"Dear {celebrity_name}, I am a {adjective_1} {noun} applying for your position. I have {adverb} mastered the ability to {verb} in any {place}. My previous employer, a {adjective_2} {animal} who always wore {clothing}, said I could {verb} better than anyone. References available upon request. P.S. I brought {food}."

    story_title_5 = "The Detective Mystery"
    story_result_5 = f"Detective {noun} arrived {adverb} at the {place} crime scene. The {adjective_1} evidence suggested the culprit was a {adjective_2} {animal} wearing {clothing}. Security footage showed them trying to {verb} while stealing {celebrity_name}'s prized {food}. Case closed!"

    print(f"{'-'*20}\nStories Generated Successfully")

    while True:
        print(f"\n 1. {story_title_1}\n 2. {story_title_2}\n 3. {story_title_3}\n 4. {story_title_4}\n 5. {story_title_5}")

        select_story = input("Enter which story you want to see (1-5): ").strip()

        seperator = f"\n{"-"*100}\n"

        match select_story:
            case "1":
                print(seperator, story_title_1,seperator, story_result_1,seperator)
            case "2":
                print(seperator, story_title_2,seperator, story_result_2,seperator)
            case "3":
                print(seperator, story_title_3,seperator, story_result_3,seperator)
            case "4":
                print(seperator, story_title_4,seperator, story_result_4,seperator)
            case "5":
                print(seperator, story_title_5,seperator, story_result_5,seperator)
            case _:
                print("\n","\n", "Error: Enter valid option")

mad_lib()
