import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response):
        #savig the css/html code to a variable (those with tag article)
        books = response.css('article')

        #taking out from css/html code information about each book
        for book in books:
            #saving results to key value pairs
            yield{
                'name' : book.css('h3 a::text').get(),
                'price' : book.css('.product_price .price_color::text').get(),
                'url' :  book.css('h3 a').attrib['href']
            }

        #finding and saving the next page url tail
        next_page = response.css('li.next a ::attr(href)').get()

        #if url to next page exists, do something
        if next_page is not None:
            #the links to the next pages either had catalogue word or not, so we took it into consideration
            if 'catalogue/' in next_page:
                next_page_url = 'http://books.toscrape.com/' + next_page
            else:
                next_page_url = 'http://books.toscrape.com/catalogue/' + next_page
            #yielding the response from next page url and self callign the parsce method of this class
            yield response.follow(next_page_url, callback= self.parse)