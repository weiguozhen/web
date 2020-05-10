*** Settings ***
Library  pylib.web
*** Test Cases ***
tc0001
    register
    ${data}  login
    should be true  $data == '会员姓名：2'
