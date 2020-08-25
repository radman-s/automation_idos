from pages.drivers import Drivers
from pages.idos_page import IdosPage
from pages.current_time import Time

browser = Drivers('--start-maximized').chrome()
ip = IdosPage(driver=browser)

# test start
ip.go()
ip.only_direct.click()
# connection from
ip.from_search.input_text('praha')
ip.from_search.arrow_down()
ip.from_search.enter()
# connection to
ip.to_search.input_text('pardubice')
ip.to_search.arrow_down()
ip.to_search.enter()
ip.search_button.click()

# get times from first three connections
web_t1 = ip.time1.text()[:5].replace(':', '.')
web_t2 = ip.time2.text()[:5].replace(':', '.')
web_t3 = ip.time3.text()[:5].replace(':', '.')


# get time from the module
now = Time().get_time()

# assert that all the connections are same or later then current time
# and check if there is delay on any connection
if float(now) <= float(web_t1) and float(now) <= float(web_t2) and float(now) <= float(web_t3):
    print(f'curent time is:           {now}')
    print(f'first connection trains:  {web_t1}')
    print(f'second connection trains: {web_t2}')
    print(f'third connection trains:  {web_t3}')
    print('all the connections listed are after the current time')
    print('test passed')
else:
    late = ip.delay.text()
    print(late)

browser.quit()

