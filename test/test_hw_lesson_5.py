import os.path

from selene import browser, have, be


def test_input_form():
    browser.element("#firstName").type("Name")
    browser.element("#lastName").type("Surname")
    browser.element("#userEmail").type("test@test.ru")
    browser.element("[for='gender-radio-2']").click()
    browser.element("#userNumber").type("9998887766")
    browser.element(".react-datepicker-wrapper").click()
    browser.element(".react-datepicker__month-dropdown-container--select").click().element("[value='7']").click()
    browser.element(".react-datepicker__year-dropdown-container--select").click().element("[value='1994']").click()
    browser.element(".react-datepicker__day--016").click()
    browser.element("#subjectsInput").type("Math").press_enter()
    browser.element("#hobbiesWrapper > div.col-md-9.col-sm-12 > div:nth-child(3) > label").click()
    browser.element("#uploadPicture").send_keys(os.path.abspath("DFRLMLWWl38.jpg"))
    browser.element("#currentAddress").type("Red Square, 1")
    browser.element("#react-select-3-input").should(be.visible).type("NCR").press_enter()
    browser.element("#react-select-4-input").should(be.visible).type("Delhi").press_enter()
    browser.element("#submit").click()

    assert browser.element("#example-modal-sizes-title-lg").should(have.text("Thanks for submitting the form"))
    assert browser.element(".table").all("td:nth-child(2)").should(have.texts('Name Surname',
                                                                              "test@test.ru",
                                                                              "Female",
                                                                              "9998887766",
                                                                              "16 August,1994",
                                                                              "Maths",
                                                                              "Music",
                                                                              "DFRLMLWWl38.jpg",
                                                                              "Red Square, 1",
                                                                              "NCR Delhi"))