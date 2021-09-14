from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import home, userPage, accountSettings, registerPage, loginPage, logoutUser, products, customer, createOrder, updateOrder, deleteOrder


class TestUrls(SimpleTestCase):
    
    def test_home_url(self):
        # name of url
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home)

    def test_home_url(self):
        # name of url
        url = reverse('userpage')
        print(resolve(url))
        self.assertEquals(resolve(url).func, userPage)

    def test_home_url(self):
        # name of url
        url = reverse('accountsettings')
        print(resolve(url))
        self.assertEquals(resolve(url).func, accountSettings)