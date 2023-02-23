
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.shopping as SP
import time

# user login
foUserId = GSV.forUserID
foUserPwd = GSV.forUserPwD

Swag = AC.openBrowser()
AC.login(foUserId, foUserPwd)
time.sleep(2)
SP.product(Swag)
AC.closeBrowser()
print("Status:Passed -> Completed Successfully")





