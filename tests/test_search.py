from Pages.Home_page import HomePage
from Pages.Search_page import SearchPage

"""Open browser, navigate to ivi.ru homepage, input name (Царство небесное) in searchbox, 
   the given name must present in search results"""

class TestSearch():
   def test_search_result(self, browser):
    search_pg=HomePage(browser)
    search_pg.make_search()
    search_pg=SearchPage(browser)
    search_pg.search_message_present()
    texts = [el.text for el in search_pg.search_message_present()]
    print(texts)

    assert 'Царство небесное' in texts, "The item is not found"

