from instapy import InstaPy
from instapy import smart_run



  session = InstaPy(username=high_ayatollah,
                  password=fertfert,
                  headless_browser=True)



  with smart_run(session):
    session.set_do_follow(enabled=True, percentage=10, times=2)
    session.follow_user_followers(['parsalip', 'snoopdogg', 'wizkhalifa'], amount=400, randomize=False, sleep_delay=60)
