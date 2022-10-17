import time


def test_petfriends(driver):
    # Open PetFriends base page:
    driver.get("https://petfriends.skillfactory.ru/")

    time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!

    # click on the new user button
    btn_newuser = driver.find_element("xpath", "//button[@onclick=\"document.location='/new_user';\"]")

    btn_newuser.click()

    btn_exist_acc = driver.find_element("link text", u"У меня уже есть аккаунт")
    btn_exist_acc.click()

    time.sleep(5)

    # add email
    field_email = driver.find_element("id", "email")
    field_email.click()
    field_email.clear()
    field_email.send_keys("lbtumatym1@gmail.com")

    time.sleep(5)

    # add password
    field_pass = driver.find_element("id", "pass")
    field_email.click()
    field_pass.clear()
    field_pass.send_keys("7777777")

    time.sleep(5)

    # click submit button
    btn_submit = driver.find_element("xpath", "//button[@type='submit']")
    btn_submit.click()

    time.sleep(10)  # just for demo purposes, do NOT repeat it on real projects!
    if driver.current_url == 'https://petfriends.skillfactory.ru/all_pets':
        # Make the screenshot of browser window:
        driver.save_screenshot('result_petfriends.png')
    else:
        raise Exception("login error")