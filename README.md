# scrap-stock-info-at-x.com-bot


You can set x.com pages to let this program to scrap stock info.
Scraping is performed by Python Selenium.
Once scraping process ends, it compares to local file that stacks what you had already scrap.
If it is new information posting it sends information to gemini api.
In this process you will use your own gemini api key so you have to prepare .env file.
By using existing prompts (check the file and you can modify it by your own prompts), gemini sends info back to you in a summary form.
Then you autonomously posts it to website. if you dont want to and just wants to stack in your local, you needs some edit.


Thank you.
