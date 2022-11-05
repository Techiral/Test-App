# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Flask modules
from flask   import render_template, request
from jinja2  import TemplateNotFound
from flask import Flask, render_template, request
import openai
from apps import prompt
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user



# App modules
# App modules
views = Blueprint('views', __name__)


# App main route + generic routing
@views.route('/', defaults={'path': 'index.html'})

@views.route('/<path>')
def index(path):

    try:

        # Detect the current page
        segment = get_segment( request )

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template( 'home/' + path, segment=segment )
    
    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

def get_segment( request ): 

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment    

    except:
        return None  

@views.route('/apps/')
@login_required
def apps():
    return render_template("/home/index.html")

@views.route('/title_generator', methods=["GET", "POST"])
@login_required
def yttitlegenerator():
    if request.method == 'POST':
        yt_name = request.form['channelName']
        query='''Generate Engaging Clicky Eye-Catching Short YouTube Video Titles based on the idea "No Code SAAS":

1. How To Build A No Code SaaS (Everything You Need)
2. I Created a SaaS Only Using No Code Tools

Generate Engaging Clicky Eye-Catching Short YouTube Video Titles based on the idea "Grow YouTube Channel":

1. How to Grow New Channel on YouTube -in 3 Steps Only (GUARANTEED) // Grow from 0 Subscribers in 2022
2. How To Grow YouTube Channel From Zero SUBSCRIBERS | ONLY 3 STEPS 🔥

Generate Engaging Clicky Eye-Catching Short YouTube Video Titles based on the idea "squid game challenge":

1. $456,000 Squid Game In Real Life!
2. Squid Game Challenge

Generate Engaging Clicky Eye-Catching Short YouTube Video Titles based on the idea "metaverse":

1. Metaverse World क्या है और इस दुनिया में क्या-क्या हो सकता है? | How Metaverse Works in Hindi?
2. Metaverse Is Dead
3. How Metaverse Works? | Secrets of Metaverse | Explained in Hindi | Dhruv Rathee

Generate Engaging Clicky Eye-Catching Short YouTube Video Titles based on the idea "diy diwali decor 2022":

1. Diwali Decoration Ideas 2022 / 10 Easy and Creative DIY Diwali Decor ideas | Dhara Patel
Generate Engaging Clicky Eye-Catching Short YouTube Video Titles based on the idea {}: <br><br>'''.format(yt_name)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/title_generator.html', **locals())


@views.route('/description_generator', methods=["GET", "POST"])
@login_required
def ytdescgenerator():
    if request.method == 'POST':
        yt_title = request.form['title']
        query='''Generate A Detailed Formatted Professional-Looking Eye-Catching Description in a minimum of 500 words with the intro script and outro script with click-to-action to the other social platforms and other similar videos of Title:- "I Created a SaaS Only Using No Code Tools":

Let me show you which tools to use, and how to set up a SaaS Platform only using No Code tools.

Content:
0:00 Introduction
0:26 Channel welcome
1:33 The setup
3:15 Presenting WiseStamp
4:01 Setting up the website
6:34 Setting up a login system
11:14 Wiring it all together
14:07 What's next?

#saas #business #startup #nocode #tools #automation
------------------------------------------------------------------------------------------------
RELATED VIDEOS

This Is The PERFECT Tech Stack For a SaaS Product
https://www.youtube.com/watch?v=SUjTI...

How To Find BRILLIANT SaaS Ideas
https://www.youtube.com/watch?v=-E7zp...
------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------
CRYPTOVIEW

The CryptoView SaaS is live right here 🤩
(Though, the main functionality is disabled to avoid blowing through my Zap limit)

You can still check out the website and create a user 🚀
https://cryptoview.webflow.io

------------------------------------------------------------------------------------------------
RESOURCES

Webflow:
https://webflow.com/

Memberstack:
https://www.memberstack.com/

Zapier:
https://zapier.com/

------------------------------------------------------------------------------------------------
Follow me here for more content:

✉️ NEWSLETTER ‧ https://increhub.com/newsletter
📱 TIKTOK ‧ https://www.tiktok.com/@techiral
📷 INSTAGRAM ‧ https://www.instagram.com/techiral
🐦 TWITTER ‧ https://twitter.com/techiral
🌐 LINKEDIN ‧ https://www.linkedin.com/in/techiral
Generate A Detailed Formatted Professional-Looking Eye-Catching Description in a minimum of 500 words with the intro script and outro script with click-to-action to the other social platforms and other similar videos of Title:- "{}":'''.format(yt_title)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/yt_description.html', **locals())

@views.route('/script_generator', methods=["GET", "POST"])
@login_required
def ytscriptgenerator():
    if request.method == 'POST':
        yt_title = request.form['title']
        query='Generate A Detailed Formatted Professional-Looking Eye-Catching Video Script in a minimum of 500 words with the intro script and outro script with click-to-action to the other social platforms and other similar videos of Title:- "{}": <br><br>'.format(yt_title)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/video_script.html', **locals())

@views.route('/tweet_generator', methods=["GET", "POST"])
@login_required
def yttweetgenerator():
    if request.method == 'POST':
        yt_title = request.form['title']
        query='Generate Short Clicky Professional-Looking Eye-Catching Tweet Ideas on Title:- "{}": <br><br>'.format(yt_title)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/tweet_ideas.html', **locals())

@views.route('/post_generator', methods=["GET", "POST"])
@login_required
def postgenerator():
    if request.method == 'POST':
        yt_title = request.form['title']
        query='Generate Short Clicky Professional-Looking Eye-Catching Facebook Post Ideas on Title:- "{}": <br><br>'.format(yt_title)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/post.html', **locals())

@views.route('/caption_generator', methods=["GET", "POST"])
@login_required
def instagenerator():
    if request.method == 'POST':
        yt_title = request.form['title']
        query='Generate Short Clicky Professional-Looking Eye-Catching Instagram Caption Ideas on Title:- "{}": <br><br>'.format(yt_title)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/caption.html', **locals())

@views.route('/hashtag_generator', methods=["GET", "POST"])
@login_required
def hashgenerator():
    if request.method == 'POST':
        yt_title = request.form['title']
        query='Generate Short Clicky Professional-Looking Viral Eye-Catching Instagram HashTags on Title:- "{}": <br><br>'.format(yt_title)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/hash.html', **locals())

@views.route('/blog_generator', methods=["GET", "POST"])
@login_required
def headgenerator():
    if request.method == 'POST':
        yt_title = request.form['title']
        query='Brainstorm short Eye-Catching Clickable Professional-Looking Blog Headlines For the Topic: "{}": <br><br>'.format(yt_title)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/blogHeadline.html', **locals())

@views.route('/blog_post_generator', methods=["GET", "POST"])
@login_required
def blog_script_generator():
    if request.method == 'POST':
        yt_title = request.form['title']
        query='''Generate A Blog Post About "Tea Cups":-

If you're a tea lover, then you need to check out our list of the best tea cups. We've compiled a list of the best tea cups on the market, so you can find the perfect one for your needs.

We've included a variety of tea cups on our list, so you're sure to find one that's perfect for you. Whether you're looking for a teacup that's stylish, functional or both, we've got you covered.

Here are our top picks for the best tea cups:

- The Best Tea Cup: Royal Doulton 1815 Tea Cup
- The Best Budget Tea Cup: Japanese Style Cast Iron Tea Cup
- The Best Design Tea Cup: Kinto Slow Coffee Style Mug
- The Best Travel Tea Cup: Teavana Perfect Tea Mug

To learn more about each of these tea cups, and to find out which one is right for you, head over to our website at https://www.teacups.com/.
        Generate A Blog Post About "{}": <br><br>'''.format(yt_title)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/blogScript.html', **locals())

@views.route('/story_generator', methods=["GET", "POST"])
@login_required
def story_generator():
    if request.method == 'POST':
        yt_title = request.form['title']
        query='Brainstorm a Detailed Story with minimum 500 words with characters: "{}": <br><br>'.format(yt_title)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/story.html', **locals())

@views.route('/lyrics_generator', methods=["GET", "POST"])
@login_required
def lyrics_generator():
    if request.method == 'POST':
        yt_title = request.form['title']
        query='Brainstorm Rhyming Medolius Song Lyrics with minimum 500 words containing keywords or characters or emotion: "{}": <br><br>'.format(yt_title)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/song.html', **locals())

@views.route('/startup_idea_generator', methods=["GET", "POST"])
@login_required
def start_idea_generator():
    if request.method == 'POST':
        yt_title = request.form['title']
        query='Generate Startup Ideas For: "{}":- <br><br>'.format(yt_title)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/startup_idea.html', **locals())

@views.route('/slogan_generator', methods=["GET", "POST"])
@login_required
def slogan_generator():
    if request.method == 'POST':
        yt_title = request.form['title']
        query='Generate Slogans for a business: "{}": <br><br>'.format(yt_title)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/slogan.html', **locals())

@views.route('/next_product_idea_generator', methods=["GET", "POST"])
@login_required
def nexIdea_generator():
    if request.method == 'POST':
        yt_title = request.form['title']
        query='What should be the Next Product according to the last product "{}" of our company: <br><br>'.format(yt_title)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/nexIdea.html', **locals())

@views.route('/product_description_generator', methods=["GET", "POST"])
@login_required
def prodesc():
    if request.method == 'POST':
        yt_title = request.form['title']
        yt_desc = request.form['desc']
        yt_home = request.form['home']
        yt_serve = request.form['serve']
        yt_cost = request.form['cost']
        query='''Generate Detailed Product Description For "Techiral" which is "A Startup That Helps Building New SAAS Startups". The homepage link is "techiral.github.io". Services Provided Are "Build ReadMe Markdown For Your Projects", "Generate Product Descriptions For Products", "Generate YouTube Video Descriptions", "Get Tweet Ideas", "Generate Cold Emails For Products", "Get Business Pitch Ideas", "Get Video Ideas" This has "Both Freemium and Premium Versions. Premium Price Starts From $30 as basic plan.":-

# Techiral

## What is Techiral?

Techiral is a startup that helps build new SAAS startups. We provide services like building ReadMe Markdown for your projects, generating product descriptions for products, generating YouTube video descriptions, getting tweet ideas, generating cold emails for products, getting business pitch ideas, and getting video ideas. We have both freemium and premium versions. The premium price starts from $30 as the basic plan.

## How can Techiral help me?

If you are a startup founder, you can use Techiral to get help with your product marketing. We can help you with things like creating a product description, generating YouTube video descriptions, getting tweet ideas, and more. We also offer a premium plan that gives you access to more features and services.

## What are the features of Techiral?

Some of the features of Techiral include:

- Build ReadMe Markdown for your projects
- Generate product descriptions for products
- Generate YouTube video descriptions
- Get tweet ideas
- Generate cold emails for products
- Get business pitch ideas
- Get video ideas

## How much does Techiral cost?

Techiral has both a free and a premium version. The premium version starts at $30 per month.

## How to reach Techiral?

You can stick to the updates on techiral.github.io.
Generate Detailed Product Description For "{}" which is "{}". The homepage link is "{}". Services Provided Are "{}". This has "{}":- <br><br>'''.format(yt_title, yt_desc, yt_home, yt_serve, yt_cost)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/prodesc.html', **locals())

@views.route('/cold_e-mail_generator', methods=["GET", "POST"])
@login_required
def coldmail_generator():
    if request.method == 'POST':
        yt_title = request.form['title']
        yt_desc = request.form['desc']
        yt_home = request.form['home']
        query='''Generate A Cold Email For "BorgeTube" which is "An Online Tool that helps to rank YouTube Content and Videos With The Help Of AI" published on "https://techiral.io/borgetube/":-

Hi there!

If you're looking for a way to rank your YouTube content and videos, then you need to check out BorgeTube. We offer a wide range of services to help you succeed. We have the resources and expertise you need to get your videos to the top of  YouTube search results.

Here are some of the things we can do for you:

- We can help you optimize your videos for the YouTube search algorithm.
- We can help you create engaging and keyword-rich titles and descriptions.
- We can help you promote your videos through social media and other channels.

If you're interested in learning more about what we can do for you, then please visit our website at https://techiral.io/borgetube/. We offer a free trial so you can see for yourself how we can help you rank your YouTube videos.

Thank you for your time,

The BorgeTube Team

Generate A Cold Email For "{}" which is "{}" published on "{}":- <br><br>'''.format(yt_title, yt_desc, yt_home)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/cold_email.html', **locals())

@views.route('/welcome_e-mail_generator', methods=["GET", "POST"])
@login_required
def welmail_generator():
    if request.method == 'POST':
        yt_title = request.form['title']
        yt_desc = request.form['desc']
        yt_home = request.form['home']
        yt_serve = request.form['serve']
        yt_page = request.form['page']
        query='''Generate A Welcome Email To "Aakash" from "Techiral" for the product "IncreHub" with services "An Online Tool that helps to rank YouTube Content and Videos With The Help Of AI" on the homepage "www.increhub.io":-

Hi Aakash,

Welcome to Increhub – we’re excited to have you on board and we’d love to say thank you on behalf of our whole company for choosing us. We believe our Increhub will help you to optimize your videos for the YouTube search algorithm.
To ensure you gain the very best out of our Increhub, we’ve put together some of the most helpful guides:
This video www.increhub.io walks you through setting up your IncreHub for the first time. Our FAQ www.increhub.io/faq/ is a great place to find the answers to common questions you might have as a new customer. The knowledge base www.increhub.io has the answers to all of your tech-related questions. Our blog www.blog.increhub.io has some great tips and best practices on how you can use and benefit from Increhub.
Have any questions or need more information? Just shoot us an email! We’re always here to help.

Take care,
Increhub


Generate A Welcome Email To "{}" from "{}" for the product "{}" with services "{}" on the homepage "{}":- <br><br>'''.format(yt_title, yt_desc, yt_home, yt_serve, yt_page)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/wel_mail.html', **locals())

@views.route('/cancellation_e-mail_generator', methods=["GET", "POST"])
@login_required
def cancelmail_generator():
    if request.method == 'POST':
        yt_title = request.form['title']
        yt_desc = request.form['desc']
        yt_home = request.form['home']
        yt_serve = request.form['serve']
        query='''Generate A Cancellation Email To "{}" from "{}" for the product "{}" with the survey link "{}":- <br><br>'''.format(yt_title, yt_desc, yt_home, yt_serve)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/cancelMail.html', **locals())

@views.route('/verification_e-mail_generator', methods=["GET", "POST"])
@login_required
def verimail_generator():
    if request.method == 'POST':
        yt_title = request.form['title']
        yt_desc = request.form['desc']
        yt_home = request.form['home']
        query='''Generate A Verification Email To "{}" from "{}" for the product "{}" with the unique OTP:- <br><br>'''.format(yt_title, yt_desc, yt_home)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/veriMail.html', **locals())

@views.route('/github_readme_generator', methods=["GET", "POST"])
@login_required
def readme_generator():
    if request.method == 'POST':
        yt_title = request.form['title']
        yt_desc = request.form['desc']
        yt_home = request.form['home']
        yt_url = request.form['url']
        yt_mail = request.form['mail']
        query='''
Generate Detailed GitHub Readme Markdown For A "web app" "Milk" "which is a business generator, and management tool. With this tool, you can build apps for yourself, build websites, and others". It is available on "https:/techiral.github.io/milk" E-mail for support "techiraltofuture@gmail.com":-

# Milk

Milk is a business generator, and management tool. With this tool, you can build apps for yourself, build websites, and others.

## Features

-   Build apps for yourself
-   Build websites
-   Manage your business
-   Get support from the community

## Usage

- Clone Repo From https:/techiral.github.io/milk.
```
git clone https://github.com/techiral/milk.git
```

## Documentation

You can find the documentation for Milk on the website"https:/techiral.github.io/milk/docs.".

## Help

Email: techiraltofuture@gmail.com

Generate Detailed GitHub Readme Markdown For A "{}" "{}" "{}". It is available on "{}" E-mail for support "{}":- <br><br>'''.format(yt_title, yt_desc, yt_home, yt_url, yt_mail)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/readme.html', **locals())

@views.route('/python_code_generator', methods=["GET", "POST"])
@login_required
def code_generator():
    if request.method == 'POST':
        yt_title = request.form['title']
        query='''Convert query "Text To Speech with pyttsx3" into python code:-

# Import the required module for text
# to speech conversion
import pyttsx3

# init function to get an engine instance for the speech synthesis
engine = pyttsx3.init()

# say method on the engine that passes input text to be spoken
engine.say('Hello sir, how may I help you, sir.')

# run and wait method, it processes the voice commands.
engine.runAndWait()

Convert query "how to get the stock data of Tesla in python" into python code:-

import urllib.request, json
resp = urllib.request.urlopen('https://query2.finance.yahoo.com/v10/finance/quoteSummary/tsla?modules=price')
data = json.loads(resp.read())
price = data['quoteSummary']['result'][0]['price']['regularMarketPrice']['raw']
print(price)

Convert query "Build Instagram Bot" into python code:-

from instabot import Bot
bot = Bot()
bot.login(username="", password="")

######  upload a picture #######
bot.upload_photo("yoda.jpg", caption="biscuit eating baby")

######  follow someone #######
bot.follow("elonrmuskk")

######  send a message #######
bot.send_message("Hello from Techiral", ['user1','user2'])

######  get follower info #######
my_followers = bot.get_user_followers("techiralsays")
for follower in my_followers:
    print(follower)

bot.unfollow_everyone()
    Convert query "{}" into python code:- <br><br>'''.format(yt_title)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/pythoncode.html', **locals())

@views.route('/ai_coach', methods=["GET", "POST"])
@login_required
def coach():
    if request.method == 'POST':
        yt_title = request.form['title']
        query='''Solve the programming query: {}:- <br><br>'''.format(yt_title)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/coach.html', **locals())

@views.route('/hero-villian_story_generator', methods=["GET", "POST"])
@login_required
def herovillian_story_generator():
    if request.method == 'POST':
        yt_title = request.form['title']
        yt_desc = request.form['desc']
        query="Generate A Detailed And Interesting Hero-Villian story for kids to amaze them in which the hero's name is: {} and the villain's name is: {}:- <br><br>".format(yt_title, yt_desc)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/hero-story.html', **locals())

@views.route('/horror_story_generator', methods=["GET", "POST"])
@login_required
def horror_story_generator():
    if request.method == 'POST':
        query="Generate A Detailed Terrifying And Thrilling Horror story to terrify them:- <br><br>"
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/horror-story.html', **locals())

@views.route('/fairy-tales_generator', methods=["GET", "POST"])
@login_required
def fairytales_generator():
    if request.method == 'POST':
        query="Generate Detailed Interesting Cute Fantasy Magical Fairy Tales to amaze kids:- <br><br>"
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/fairy.html', **locals())

@views.route('/love_letter_generator', methods=["GET", "POST"])
@login_required
def love_generator():
    if request.method == 'POST':
        yt_title = request.form['title']
        yt_desc = request.form['desc']
        query='''Generate a detailed romantic love letter to your "{}" "{}" with your love assent:- <br><br>'''.format(yt_title, yt_desc)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/love.html', **locals())

@views.route('/privacy/')
def privacy():
    return render_template('/home/privacy.html', **locals())

