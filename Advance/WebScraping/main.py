from bs4 import BeautifulSoup
import requests

html_text = requests.get("https://vidyavaniblogs.blogspot.com/").text
soup = BeautifulSoup(html_text, 'lxml')

posts = soup.find_all("article", class_ = "post-outer-container")

for post in posts:
    title = post.find("h3", class_ = "post-title entry-title")
    post_link = title.find("a").get("href")

    with open("post_details.txt", "a") as f:
        f.write(f"Post Title: {title.text.strip()}\nPost Link: {post_link}\n")