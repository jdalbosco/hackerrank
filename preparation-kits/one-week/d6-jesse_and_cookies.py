import collections


class CookieTray:
    def __init__(self, cookies):
        self.cookies = collections.deque()
        self.new_cookies = collections.deque()
        for cookie in sorted(cookies):
            self.cookies.append(cookie)
    
    def __is_tray_empty(self):
        return not self.cookies and not self.new_cookies
        
    def get_least_sweet(self):
        if self.__is_tray_empty():
            return None
        if not self.new_cookies:
            return self.cookies.popleft()
        if not self.cookies:
            return self.new_cookies.popleft()
        else:
            return self.cookies.popleft() if self.cookies[0] < self.new_cookies[0] else self.new_cookies.popleft()
        
    def get_two_least_sweet(self):
        least_sweet = self.get_least_sweet()
        second_least_sweet = self.get_least_sweet()
        return least_sweet, second_least_sweet


def make_new_cookie(cookie1, cookie2):
    return cookie1 + (2 * cookie2)
    
    
def cookies(min_sweetness, cookies):
    jesses_cookies = CookieTray(cookies)
    iterations = 0
    
    least_sweet, second_least_sweet = jesses_cookies.get_two_least_sweet()
    while second_least_sweet is not None and least_sweet < min_sweetness:
        jesses_cookies.new_cookies.append(make_new_cookie(least_sweet, second_least_sweet))
        iterations += 1
        least_sweet, second_least_sweet = jesses_cookies.get_two_least_sweet()
        
    if least_sweet < min_sweetness:
        return -1
    
    return iterations