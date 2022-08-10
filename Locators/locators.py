class GenericLocators:
    header_sign_in = "//a[contains(text(), 'Sign In')]"


class RegisterLocators:
    next_sign_up = "//div[@class='style_motionDiv__3KQNW']/button/p[contains(text(), 'Sign Up')]"
    email_input = "//form[@class='style_form__1z6RX']//input[@name='email']"
    password_input = "//form[@class='style_form__1z6RX']//input[@name='password']"
    register_sign_up = "//form[@class='style_form__1z6RX']/button[@id='login-btn-submit']"
    confirm_reg_pop_up = "//div[@class='chakra-alert__desc css-zycdy9' and contains(text(), 'Sign Up success')]"


class LoginLocators:
    email_input = "//form[@class='style_form__14a_b']//input[@name='email']"
    password_input = "//form[@class='style_form__14a_b']//input[@name='password']"
    login_button = "//p[@class='chakra-text css-16iqw5x' and contains(text(), 'Log in')]"


class ForgotPasswordLocators:
    forgot_password = "//button[@class='chakra-button css-lcsn02' and contains(text(), 'Forgot Password?')]"
    email_input = "//input[@name='email']"
    recover_password_button = "//p[@class='chakra-text css-t3bb45' and contains(text(), 'Recover Password')]"
    confirm_recover_pass_pop_up = "//div[@class='chakra-alert__desc css-zycdy9' and contains(text(), 'Check your email')] "

