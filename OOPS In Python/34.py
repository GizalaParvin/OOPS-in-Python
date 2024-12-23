class NewsArticle:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nContent: {self.content}\n"
class NewsApplication:
    def __init__(self):
        self.articles = []

    def add_article(self, title, content, author):
        article = NewsArticle(title, content, author)
        self.articles.append(article)
        print("Article added successfully.")

    def view_articles(self):
        if not self.articles:
            print("No articles available.")
        else:
            for idx, article in enumerate(self.articles):
                print(f"Article {idx + 1}:\n{article}")

    def search_articles(self, keyword):
        found_articles = [article for article in self.articles if keyword.lower() in article.title.lower() or keyword.lower() in article.content.lower()]
        if not found_articles:
            print("No articles found.")
        else:
            for article in found_articles:
                print(article)

    def run(self):
        while True:
            print("\nNews Application Menu:")
            print("1. Add Article")
            print("2. View Articles")
            print("3. Search Articles")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                title = input("Enter article title: ")
                content = input("Enter article content: ")
                author = input("Enter article author: ")
                self.add_article(title, content, author)
            elif choice == "2":
                self.view_articles()
            elif choice == "3":
                keyword = input("Enter keyword to search: ")
                self.search_articles(keyword)
            elif choice == "4":
                print("Exiting application.")
                break
            else:
                print("Invalid choice. Please try again.")
if __name__ == "__main__":
    app = NewsApplication()
    app.run()

