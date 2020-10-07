# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define sylvie = Character("Sylvie")

define eileen = Character("Eileen")

define system = Character("")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg club

    #scene office_background

    show screen calendar(date_inf)

    scene bg club

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show sylvie blue normal:
        xalign 0.0
        yalign 1.0


    # Start by playing some music.
    play music "illurock.opus"

    # Define slow disolve
    define slowDissolve = Dissolve(1.0)

    # These display lines of dialogue.

    sylvie "First day at the new job! I’m so excited to get started."

    show eileen happy:
        xalign 0.75
        yalign 1.0
    with Dissolve(0.5)

    eileen "I’m glad we were able to get hired at the same company Sylvie. I can't wait for our next project"

    sylvie "Did you hear Eileen? The company is looking for a new young developer to launch the new project."

    show eileen concerned
    eileen "Oh no! Here you go again"

    show sylvie blue giggle
    sylvie "That’s right here I go again, I’m taking on “The Big One”"

    sylvie "It's time to get cracking! Let's go ahead and see which developers are being assigned to the big one that way we can go ahead and put our team together and get started working."

    scene office_background
    show sylvie blue smile
    with slowDissolve

    show sylvie blue normal:
        xalign 0.75
        yalign 1.0
    with Dissolve(0.5)

    show eileen vhappy:
        xalign 0.0
        yalign 1.0
    with Dissolve(0.7)

    eileen "So how are we going to do this?"

    show sylvie blue giggle
    sylvie "Using scrum and agile methodology."

    eileen "What's that?"

    show eileen happy
    show sylvie blue normal
    sylvie "In short, scrum refers to a framework that makes for effective collaborations among teams that are working on complex products.
    Although it is most often used by software development teams, scrum is beneficial to any team that is working toward a common goal."

    sylvie "In particular, scrum is a collection of meetings, roles, and tools
    that work together to help teams to better structure and manage their workload."


    scene team_meeting_room
    show sylvie blue smile
    with slowDissolve

    sylvie "So for our project, I'll be the Scrum master. The scrum master is the facilitator of the scrum development process.
    In addition to holding daily meetings with the scrum team,"

    sylvie "The scrum master makes certain that scrum rules are being enforced and
    applied as intended."


    scene team_meeting_room
    show eileen happy
    with slowDissolve

    sylvie "Eileen you'll be the Product owner, representing
    stakeholders, which are typically customers."

    sylvie "To ensure the scrum team is
    always delivering value to stakeholders and the business, the product owner
    determines product expectations, records changes to the product and administers
    a scrum backlog, a detailed and constantly updated to-do list for the scrum project."

    scene team_meeting_room
    show software_team:
    with slowDissolve

    sylvie "The rest of the developers will be the scrum team. A scrum team
    is a self-organized group of three to nine individuals who have the business,
    design, analytical, and development skills to carry out the actual work, solve
    problems, and produce deliverable products."

    scene office_background
    show sylvie blue normal:
        xalign 0.75
        yalign 1.0

    show eileen happy:
        xalign 0.0
        yalign 1.0
    with slowDissolve

    eileen "So what will you be doing on a week to week basis?"

    #Start tutorial for weekly calendar events

    jump tutorial

label tutorial:

    scene office_background

    system "Throughout the game, you will advance week by week."

    system "Each week, you will generate a number and it will be added to your character attributes
    that you can see on the top right hand corner."

    # Add focus after

    system "The player attributes that you will have in this game are: Level (Exp Points), Technical Skills, Productivity, Stress, and Money."

    system "Throughout the game, there will be checkpoints that will determine if you have the necessary amount of attribute points to advance."

    system "You will have to make sure you are actively gaining and balancing the points in all categories throughout the game."

    system "Your Level acts as your completion progress to your team's software engineering project.
    As you advance through the game and complete the project, you will gain experience points (Exp Points) and level up."

    system "Your Technical Skill is your knowledge of programming languages and computer science principles needed for software engineering.
    As you advance through the game, you will gain Technical Skill points by researching and correctly answering game questions."

    system "Your Productivity Points are how well you are progressing and managing the project as a scrum leader.
    As you advance through the game, you will gain Productivity Points by performing code reviews and supporting your team."

    system "As every person knows, stress accumulates over the time that you work.
    As you advance through the game, you will generate stress. You will have to manage developing your project and skills while managing your stress as well."

    system "Lastly, every 2 weeks, it is payday! You will recieve money for your work that you will be able to use to pay your bills and purchase items."

    system "Here's a tip: The best software engineers are not the ones that are the smartest or busiest.
    Be sure to try to get the perfect balance between all of your skills!"

    # Add relationships after

    jump test_calendar

label test_calendar:

    system "Week has advanced"

    $ calendar.next() #Function that moves onto next week

    jump tutorial
