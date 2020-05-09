#differnt xpath syntax


xpath = "//input[@value='username']"
# by using or logical operator
xpath = "//input[@value='username' or @id='userid']"
# by using and logical operator
xpath = "//input[@value='username' and @id='userid']"
# by using * in place of tag or attribute name
xpath = "//*[@value='username' or @id='userid']"
xpath = "//input[@* ='username' or @*='userid']"

# using inner text(Visible text)
xpath = "//input[test()='Enter Username']"

# user contains for xpath creation for partial inner text(Visible text)
xpath = "//input[contains(test(),'Username')]"


# xpath = if part of an attribute value is dynamic
xpath = "//input[contains(@value,'user')]"

# xpath = find an element using the parent html elements
xpath = "//table[@role='presentation']/tbody/tr[2]/td[1]/input"

#xpath = find an element using child html elements

xpath = "//input[@type='email']/parent::td/parent::tr/parent::tbody/parent::table"

#xpath = find an element using it's siblings
xpath = "//input[@type='email']/following-sibling::input"
xpath = "//input[@type='email']/preceding-sibling::input"

#xpath = find an element using its siblings/parent/child
xpath = "//input[@type='email']/parent::td/following-sibling::td/input"