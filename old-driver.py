# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import re
# import random

# class JKLMBot:

#     wordlist = []


#     def __init__(self, room_code):
#         self.room_code = room_code
#         self.driver = None
#         try:
#             with open("wordlist.txt", "r") as file:
#                 self.wordlist = file.read().splitlines()
#         except FileNotFoundError:
#             print("No wordlist found")

#     def setup_driver(self):
#         service = Service(executable_path="chromedriver.exe")
#         options = webdriver.ChromeOptions()
#         options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})
#         self.driver = webdriver.Chrome(service=service, options=options)
#         link = f"https://jklm.fun/{self.room_code}"
#         self.driver.get(link)
#         print("Driver setup complete and navigated to the room.")

#     def enter_room(self):
#         try:
#             WebDriverWait(self.driver, 20).until(
#                 EC.presence_of_element_located((By.CLASS_NAME, "styled.nickname"))
#             )
#             nickname_input = self.driver.find_element(By.CLASS_NAME, "styled.nickname")
#             nickname_input.clear()
#             nickname_input.send_keys("HelpBot by AgusCode", Keys.ENTER)
#             print("Entered the room with nickname.")
#             time.sleep(3)
#         except Exception as e:
#             print(f"ERROR entering room: {e}")

#     def present(self):
#         try:
#             message = " ⛑️ Hey! I'm ready to help everyone in this room, command: !helpbot:(syllable) ⛑️ .\n Example: !helpbot:mis"
#             WebDriverWait(self.driver, 20).until(
#                 EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[data-placeholder-text='typeHereToChat']"))
#             )
#             textarea = self.driver.find_element(By.CSS_SELECTOR, "textarea[data-placeholder-text='typeHereToChat']")
#             textarea.send_keys(message, Keys.ENTER)
#             print("Sent presentation message.")
#             time.sleep(5)
#         except Exception as e:
#             print(f"ERROR presenting: {e}")

#     def inject_mutation_observer(self):
#         script = """
#             var targetNode = document.querySelector('.log.darkScrollbar');
#             var config = { childList: true, subtree: true };

#             var callback = function(mutationsList, observer) {
#                 for(var mutation of mutationsList) {
#                     if (mutation.type === 'childList') {
#                         var newNodes = mutation.addedNodes;
#                         for (var i = 0; i < newNodes.length; i++) {
#                             var newNode = newNodes[i];
#                             // Check if the newNode has a class 'text'
#                             var textNode = newNode.querySelector('.text');
#                             if (textNode) {
#                                 console.log('NEW_MESSAGE: ' + textNode.innerText);
#                             }
#                         }
#                     }
#                 }
#             };

#             var observer = new MutationObserver(callback);
#             observer.observe(targetNode, config);
#             console.log("MutationObserver injected successfully.");
#         """
#         self.driver.execute_script(script)
#         print("Injected MutationObserver script.")

#     def capture_messages(self):
#         while True:
#             logs = self.driver.get_log('browser')
#             for log in logs:
#                 if 'NEW_MESSAGE:' in log['message']:
#                     message = log['message'].split('NEW_MESSAGE:', 1)[1].strip()
#                     message = message[:-1]
#                     print("New message captured:", message)
#                     self.process_message(message)
#             time.sleep(1)  # Small pause to avoid an overly fast loop

#     def process_message(self, message):
#         if message == '!helpbot':
#             self.send_message("Helpbot guide - Type '!helpbot:[syllable]' so i can help you find words!")

#         # Define a regex pattern to match '!helpbot:xx' or '!helpbot:xxx' where xx or xxx can be any letters
#         pattern = r'^!helpbot:([a-zA-Z]{2,3})$'
        
#         # Check if the message matches the pattern
#         match = re.match(pattern, message.lower())
#         if match:
#             letters = match.group(1).lower()  # Extract the letters xx or xxx
#             print("Ayudando...")
#             self.help_user(letters)

 
#     def help_user(self, letters):
#         random.shuffle(self.wordlist)
#         possible_words = []
#         for word in self.wordlist:
#             if letters in word.lower():
#                 possible_words.append(word.capitalize())
#             if len(possible_words) >= 6:
#                 break

#         if possible_words:
#             # Format wordlist
#             word_list_message = "\n".join(possible_words)
#             self.send_message(f"Don't worry! Here are some words that might help:\n{word_list_message}")
#         else:
#             self.send_message("Sorry, I couldn't find any words matching that criteria.")




#     def send_message(self, message):
#         try:
#             WebDriverWait(self.driver, 20).until(
#                 EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[data-placeholder-text='typeHereToChat']"))
#             )
#             textarea = self.driver.find_element(By.CSS_SELECTOR, "textarea[data-placeholder-text='typeHereToChat']")
#             textarea.send_keys(message, Keys.ENTER)
#             print(f"Bot response sent: {message}")
#         except Exception as e:
#             print(f"ERROR sending message: {e}")

#     def run(self):
#         self.setup_driver()
#         self.enter_room()
#         self.present()
#         self.inject_mutation_observer()
#         self.capture_messages()``