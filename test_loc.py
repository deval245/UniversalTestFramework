from locators.smart_locator import SmartLocator  # ✅ Import the class

# 🔧 Template with dynamic parts
locator_template = "//div[@id='{env}-user-{username}']"

# 🎯 Context to replace the placeholders
context = {"env": "prod", "username": "deval"}

# 🧠 Resolve the dynamic locator using context
final_locator = SmartLocator.resolve(locator_template, context)

# ✅ Final resolved locator
print(final_locator)  # 👉 //div[@id='prod-user-deval']

