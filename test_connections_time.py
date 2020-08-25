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

# get time from the module
now = Time().get_time()

# get time from first three connections listed
first_con = ip.time1.get_time_format()
second_con = ip.time2.get_time_format()
third_con = ip.time2.get_time_format()

# validate that three first connections listed are passed current time
assert first_con >= now and second_con >= now and third_con >= now

print(f'current time           {now}')
print(f'first connection time: {first_con}')
print(f'second connection time:{second_con}')
print(f'third connection time: {third_con}')
print('all the connections are passed current time')
print('test passed')
browser.quit()

# test will not pass if there is a delay on a connection and therefore is passed current time
