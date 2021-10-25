# 601-Project2
The Twitter API can be used to programmatically retrieve and analyze data, as well as engage with the conversation on Twitter.
> This API provides access to a variety of different resources including the following:
- Tweets
- Users
- Direct Messages
- Lists
- Trends
- Media
- Places
</br>
In this project, I write three test funcions to try the APIs.

# Retrieve_tweets
In this function, we can search a user by his/hers ID. Then we can get the tweets shared by this person. By the way, Twitter only allows access to a users most recent 3240 tweets with this method. After searching, we will store these tweets in a json file.</br>

I upload the result, named retrieve_tweets.json, of running the python code. In this test, I just searched my own twitter ID - "Tian_Mayu". If you like, you can have a quick look and check it.  

# Hashtags_lookup
This function is used to search some tweets related to specific hashtags. When you set down the hashtags you would like to search, the function will search the tag and send back all related tweets which includes this hashtag. It also responds in a json format. In my practice, I search the "skateboarding dog" tag.
- query [str]: This is a string that will be used for matching the desired Tweets. These query strings can be simple such as “skateboarding dog” or very complex and powerful. They allow you to filter tweets by hashtags, identify retweets, exclude certain words or phrases, or only include tweets of a specific language. 
- tweet_fields [str]: Fields to return in the query, such as attachments, author_id, text, etc. </br>

I also upload the result in a json file.

# Oauth
This function can help you to verify your credentials. It consists of two parts. The first one is to check your user authentication and another one aims to test application authentication. 
It will read OAuth credentials from a text file. The File format as follows:
- consumer_key=YOUR_CONSUMER_KEY
- consumer_secret=YOUR_CONSUMER_SECRET
- access_token_key=YOUR_ACCESS_TOKEN
- access_token_secret=YOUR_ACCESS_TOKEN_SECRET</br>

I also upload my test result within a screenshot PNG image. In this image, after running the code, it responds with "OK", which means your credentials are correct. By the way, you can easily get your own consumer_key, access_token_key, etc on Twitter Developer Platform, if you have a developer account.

