# ConvertKit Exporter

[ConvertKit Exporter](https://convertkit-exporter.fly.dev/) is a Django app that makes it easier to export your subscribers. I saw the need for such a tool in my own work - when I was tasked with creating monthly backups of my clients' subscriber lists, I realized that the native process is quite cumbersome:

1. You click on the tag you'd like to export
2. Select all subscribers
3. Click Export
4. Wait for the email notifying you that your export is done
5. Download the CSV file you found in the email
6. Use the file however you wish
7. Rinse and repeat for every tag you'd like to retrieve

Phew. There has to be a better way, I thought - and shortly after, [ConvertKit Exporter](https://convertkit-exporter.fly.dev/) was born.

Once you have an account and added your ConvertKit API keys (you can find these under Settings -> Advanced), you can access all your tags from the same screen. Click on any button, and you'll get a CSV file of the active subscribers who have that tag. And... that's it 😄

## How to use

First, you'll see a login screen - if you have an account already, you know what to do. Otherwise, use the *Head over here to register* link to get to the registration form.

![login-screen](/doc/login.png)

This is what the registration page looks like. Pretty standard stuff. 

![signup-screen](/doc/signup.png)

Once you're logged in for the first time, you'll be redirected to this screen where you can add your ConvertKit API keys. You can find those in your Settings, under the Advanced tab. When you added the correct keys, hit submit and you'll be redirected to a screen showing all your tags.

![api-screen](/doc/api.png)

Finally, this is what your taglist screen will look like. The first button on the top will let you download the full list of your active subscribers, regardless of their tags (note that the CSV file you'll get this way won't have any tag information either). Below, you'll find a list of all your tags - if you click on them, you'll get a list of active subscribers who have that tag. 

The download process takes some time, so please be patient - especially if you have a large list.

![tag-screen](/doc/taglist.png)

## Thoughts?

I hope you'll enjoy using ConvertKit Exporter. If you have any ideas for new features, if you found a bug, or if you just wanted to say hi, feel free to reach out to me via judit.kisistok@gmail.com ✨