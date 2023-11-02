import os.path

from selene import browser, have


def test_input_form():
    browser.element("#firstName").type("Name")
    browser.element("#lastName").type("Surname")
    browser.element("[for='gender-radio-2']").click()
    browser.element("#userNumber").type("9998887766")
    browser.element(".react-datepicker-wrapper").click()
    browser.element(".react-datepicker__month-dropdown-container--select").click().element("[value='7']").click()
    browser.element(".react-datepicker__year-dropdown-container--select").click().element("[value='1994']").click()
    browser.element(".react-datepicker__day--016").click()
    browser.element("#hobbiesWrapper > div.col-md-9.col-sm-12 > div:nth-child(3) > label").click()
    browser.element("#uploadPicture").send_keys(os.path.abspath("DFRLMLWWl38.jpg"))
    browser.element("#submit").click()

    assert browser.element("#example-modal-sizes-title-lg").should(have.text("Thanks for submitting the form"))
    assert browser.element(".table").all("td:nth-child(2)").should(have.texts('Name Surname', "", "Female",
                                                                              "9998887766","16 August,1994","","Music",
                                                                              "DFRLMLWWl38.jpg","",""))