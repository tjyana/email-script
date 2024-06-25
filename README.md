# email-script

Learning project to practice:
1. Wrapping a pre-trained model
2. Prompt engineering with a completions-type model to get desired output style
3. Using a Python script to run a OS function




Memo to self:
-------------------------------------
2 ways to schedule the sending of the email:
1. `schedule` module within the script
2. Using Task Scheduler in Windows

1. `schedule` module within the script
- Modify the script as necessary
- Have the script running in command prompt?
Drawbacks:
- Need to have PC open and script running

2. Using Task Scheduler in Windows
- Modify script:
  - Remove `schedule` script as it can mess things up
  - have it run the function
- Set Task in Task Scheduler
- Have PC on or in sleep mode
Drawbacks:
- Task Scheduler is kind of annoying tbh lol


Features to be added:
- Generation of different messages everyday (LLM wrapper)
  - determine what kind of messages lol
