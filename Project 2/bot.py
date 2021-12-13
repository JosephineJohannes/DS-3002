# download module
import discord
import requests
import os
import time

from discord.ext import commands

# This command is important because it is the bot
client = commands.Bot(command_prefix='.')

@client.event
# when the bot is ready and has all the information,
# the bot puts itself in a "ready" state
async def on_ready():
    # These statements are printed to the Python console and not in the Discord Server
    print("Bot is ready")
    print("Input season if you'd like to see the current F1 Season")


@client.command(name='hi', help="This command sends a welcome message")
async def welcome(ctx):
    # Since no input is necessary, this is more for people when they come in to use the Discord server
    response = "Hello! Type .docs to see more information on what I can do!"
    await ctx.send(response)

API_KEY = '8b039e3cf758606d0468a74723862024'


@client.command(name='dogs', help="This command provides a random picture of dogs!")
async def dog_getter(ctx):
    # URL where the dog images are stored
    url = "https://dog.ceo/api/breeds/image/random"
    # Use the GET method to get the necessary information
    response = requests.get(url)
    # Gets the message as a json file
    current = response.json()['message']
    # Returns the picture back to the Discord server
    await ctx.send(current)


@client.command(name='driver_standings', help="This command tells you the current Driver Standings\n\n One input required: year\n\nEx. .driver_standings 2021")
async def driver_getter(ctx, year:str):
    # Access the API through the URL
    url= "http://ergast.com/api/f1/"+str(year)+"/driverStandings.json"
    # Get a response using requests
    response = requests.get(url)
    # Create an empty dictionary
    names = {}
    # This for loop iterates through the json file to get the first name and last name of the drivers
    for i in range(0, 21):
        # Get the first name of the driver
        f_name = response.json()['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings'][i]['Driver']['givenName']
        # Get the last name of the driver
        l_name = response.json()['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings'][i]['Driver']['familyName']
        # Put the first name and last name together
        name = f_name + " " + l_name
        # Input the name and the rank into the dictionary
        names[i+1] = name
    # This for loop returns the rank numbers and the full names of the drivers
    for n in names:
        await ctx.send("Rank " + str(n) + " : " + str(names[n]))


@client.command(name='fastest_laps', help="This command tells you the fastest lap of a specific race from the first 20 laps"
                                          "\n\nTwo inputs required: year and round \n\nEx. .fastest_laps 6 2021 \n\n"
                                          "The round number varies year by year")
async def laps(ctx, year: str, round: str):
    # Initializes an empty list
    times=[]
    # Create a for loop to find the fastest lap
    for i in range(0, 20):
        # Access the API through the URL
        url = "https://ergast.com/api/f1/" + str(year) + "/" + str(round) + "/laps/" + str(i) + ".json"
        # The response gets the URL information
        response = requests.get(url)
        # the response is converted into a json format and then the necessary information is appended to the list
        times.append(response.json()['MRData']['RaceTable']['Races'][0]['Laps'][0]['Timings'][0]['time'])
    # This message is sent back in response to the command to the Discord server
    await ctx.send("The fastest time of the first 20 laps was " + min(times))


@client.command(name='fastest_pitstop', help="This command tells you the fastest pitstop of a specific race(round)"
                                          "\n\n Two inputs required: year and round \n\nEx. .fastest_pistop 6 2021 \n\n"
                                          "The year starts from 2011-2021")
async def pitstop(ctx, year: str, round: str):
    # Create an empty list of times
    times=[]
    # Access the API through the URL
    url = "https://ergast.com/api/f1/" + str(year) + "/" + str(round) + "/pitstops.json"
    # The response is sent from the website using the "GET" function
    response = requests.get(url)
    # Find the number of pitstops on the page as it varies by year and lap
    length = len(response.json()['MRData']['RaceTable']['Races'][0]['PitStops'])
    # Iterate through the different pitstop times
    for i in range(0, length):
        # Adds the pitstop time to the list of pitstop duration
        times.append(response.json()['MRData']['RaceTable']['Races'][0]['PitStops'][i]['duration'])
    # Sends the time back to the Discord server
    await ctx.send("The fastest pit stop for round " + str(round) + " of " + str(year) + " was " + min(times) + " seconds.")


@client.command(name='docs', help="provides a summary of my commands")
async def summary_func(ctx):
    # This message just shows what commands are available
    done= "Hi, I am the F1 bot but I have a special function! I have 7 commands\n\n1. hi (no parameters)\n" \
          "2. driver_standings (1 parameter) \n3. " \
          "fastest_laps(2 parameters) \n4. fastest_pitstop (2 parameters)" \
          "\n5. dogs (no parameter) \n6. docs (no parameters) \n7. help (1 parameter)\n\nTo use any "\
          "of these commands type a . in front of the command (no space) and input any parameters needed with spaces " \
          "in between each parameter\n\nUse the .help + space + command to receive more detailed instructions on how " \
          "to use each command\n\nExample: type .help dogs to learn more about that command!" \
          "\n\nEnjoy!"
    await ctx.send(done)

# This statement allows the bot to run the commands using its token
client.run('OTE5MDI5MTc4OTQ1Mzc2MzE2.YbP2ng.Ezk2XxnL3S9fpMwFZMjkk1gMphY')
