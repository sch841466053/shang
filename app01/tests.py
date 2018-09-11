from django.test import TestCase
from app01.models import Event,Guest
from django.contrib.auth.models import User
# Create your tests here.


class ModelTest(TestCase):

    def setUp(self):
        self.event = Event.objects.create(id=10,name="洪哥发布会", status=False, limit=1000,
                                          address="深圳", start_time="2018-9-19 08:00:00")
        self.guest = Guest.objects.create(id=9, event_id=10, realname="洪哥", phone=13714658754,
                                          email="5465@qq.com",sign=False)

    def tearDown(self):
        pass

    def test_event_models(self):
        # result = Event.objects.get(name='洪哥发布会')
        result = self.event
        self.assertEqual(result.address, "深圳")
        self.assertFalse(result.status)

    def test_guest_models(self):
        # result = Guest.objects.get(phone="13714658754")
        result = self.guest
        self.assertEqual(result.realname, "洪哥")
        self.assertFalse(result.sign)


class IndexPaTest(TestCase):
    """
    测试index登录页面
    """
    def test_index(self):
        response = self.client.get("/index/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")


class LoginAction(TestCase):
    """
    测试登录动作
    """
    def setUp(self):
        self.user = User.objects.create_user("admin", "admin@mail.com", "admin123")

    def test_login(self):
        user = self.user
        self.assertEqual(user.username, "admin")
        # self.assertEqual(user.password, "admin123")

    def test_login1(self):
        data = {"username": "admin","password": "admin123" }
        response = self.client.post("/login_action/", data=data)
        self.assertEqual(response.status_code, 302)
        # self.assertIn("登录名或者密码错误", response.content.decode("utf-8") )


class EventMange(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("admin", "admin@mail.com", "admin123")
        self.event = Event.objects.create(id=10,name="洪哥1发布会", status=False, limit=1000,
                                          address="深圳1", start_time="2018-9-19 08:00:00")
        self.login_user = {"username": "admin", "password": "admin123"}

    def test_event(self):
        response = self.client.post("/login_action/", data=self.login_user)
        # response = self.client.get("/event_manage/")
        response = self.client.post("/event_manage/")
        self.assertEqual(response.status_code,200)
        self.assertIn("洪哥1发布会", response.content.decode("utf-8"))
        self.assertIn("深圳1", response.content.decode("utf-8"))

    def test_event1(self):
        response = self.client.post("/login_action/", data=self.login_user)
        # response = self.client.get("/event_manage/?name=洪哥1发布会")
        response = self.client.get("/event_manage/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("洪哥1发布会", response.content.decode("utf-8"))
        self.assertIn("深圳1", response.content.decode("utf-8"))
