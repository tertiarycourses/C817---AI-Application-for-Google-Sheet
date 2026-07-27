"""
Domain 1 — Getting Started with AI in Google Sheets. Labs 1-4.

THE CONNECTED PROJECT STARTS HERE, IN LAB 1.

Every lab works the SAME dataset: a messy quarter of orders for a small retailer,
"Riverside Supplies". In Lab 1 you take your own copy and get Gemini working on it;
each lab after that adds one AI technique — generating and explaining formulas,
troubleshooting them, and prompting effectively — to the same sheet. Wherever
possible use your OWN non-confidential data; the Riverside Supplies sample sheet
is provided for everyone to follow along.
"""

SCENARIO = (
 "Riverside Supplies is a small home-and-garden retailer. You have just been handed "
 "last quarter's orders as a single Google Sheet — hundreds of rows exported from the "
 "till system, with inconsistent text, mixed date formats and a few blank cells. Your "
 "manager wants the quarter's numbers and a chart by the end of the day. Across this "
 "course you use Gemini AI in Google Sheets to turn that messy export into clean, "
 "analysed, charted data you can trust. Use this scenario only if you cannot use a real "
 "spreadsheet from your own workplace; your own non-confidential data is always preferred."
)

PROJECT_NOTE = (
 "BUILDING BLOCK — what you do in this lab is applied to your copy of the Riverside "
 "Supplies sheet, the single dataset you clean, analyse and chart across all 8 labs."
)

DOMAIN1 = [
 dict(
 num=1, topic=1,
 title="Set Up and Access Gemini AI in Google Sheets",
 objective="Open the sample sheet, make your own copy, open the Gemini side panel, and run a first AI prompt on the data.",
 desc="This lab gets AI working in your spreadsheet. You make your own copy of the Riverside Supplies "
 "orders sheet, open the Gemini side panel, and ask a first read-only question so you can see the "
 "ask-check loop before you rely on it. " + PROJECT_NOTE,
 build="Your own copy of the Riverside Supplies sheet in Drive, with Gemini open and a first answer verified.",
 services="Google Sheets, Google Drive, Gemini side panel (Ask Gemini)",
 steps=[
 ("Open the sample 'Riverside Supplies — Q1 Orders' sheet from the link the trainer shares.", ""),
 ("Make it yours: File > Make a copy, and save it to your Drive as 'Riverside Supplies — Q1 Orders (<YOUR NAME>)'.", ""),
 ("Look at the Orders tab: note the columns Order ID, Order Date, Customer, Region, Product, Category, Quantity, Unit Price, Total — and that some cells are messy. You will fix those later.", ""),
 ("Open the Gemini side panel — click 'Ask Gemini' (the sparkle, top-right). If you cannot see it, tell the trainer; access is confirmed at the start of the day.", ""),
 ("Ask a first, read-only question to confirm Gemini can see your data.",
  "How many rows of orders are in the Orders tab, and what does each column mean?"),
 ("Check the answer: compare the row count Gemini gives against the row count shown at the bottom-left of the sheet.", ""),
 ("Ask one follow-up so you see Gemini use the data.",
  "Which 3 products appear most often in the Orders tab?"),
 ("Confirm nothing changed — asking Gemini a question is read-only. You have now seen the ask-check loop safely.", ""),
 ],
 test="You have your own copy of the sheet in Drive, the Gemini panel open, and a first answer whose row count matches the count shown at the bottom of the sheet.",
 ),
 dict(
 num=2, topic=1,
 title="Generate and Explain Formulas with AI",
 objective="Use AI to generate a spreadsheet formula from a plain-language description, and to explain an existing formula.",
 desc="Now you let AI write formulas for you. You fill the blank Total column and add a grand total by "
 "asking Gemini for the formula, verify each against a value you can confirm, then paste an unfamiliar "
 "formula and have AI explain it step by step. " + PROJECT_NOTE,
 build="A working, AI-generated Total column and grand total, each verified, plus a plain-English explanation of a formula.",
 services="Gemini side panel, formula generation, formula explanation, SUM, IF",
 steps=[
 ("Click cell I2 (Total). Ask Gemini for a formula that multiplies Quantity by Unit Price.",
  "Write a Google Sheets formula for cell I2 that multiplies Quantity in G2 by Unit Price in H2."),
 ("Paste the formula into I2 and fill it down the column (double-click the small square at the cell's bottom-right).",
  "=G2*H2"),
 ("Verify: pick any row and check by hand that Quantity x Unit Price equals the Total shown.", ""),
 ("Ask AI for one formula that totals the whole Total column into cell K1.",
  "Write a formula for cell K1 that gives the grand total of the Total column I2:I200."),
 ("Paste it into K1 and read the result.",
  "=SUM(I2:I200)"),
 ("Cross-check: select I2:I200 and read the Sum shown in the status bar at the bottom-right — it should match K1.", ""),
 ("Learn from a formula: paste this into the Gemini panel and ask it to explain, step by step.",
  "Explain what this formula does, step by step: =IF(G2>=10,\"Bulk\",\"Standard\")"),
 ("Read the explanation and write one sentence in your notes on what =IF does.", ""),
 ],
 test="The Total column is filled with a verified formula, K1 equals the status-bar Sum of I2:I200, and you can explain in one sentence what the =IF formula does.",
 ),
 dict(
 num=3, topic=1,
 title="Combine and Troubleshoot Formulas with AI",
 objective="Use AI to build a multi-step formula, then diagnose and fix a broken one against a value you can confirm.",
 desc="Real formulas need combining and fixing. You ask AI for a conditional total (sales for one region), "
 "hit the messy-data edge case that makes it wrong, and use Gemini to diagnose and correct it — verifying "
 "every version against a filtered check. " + PROJECT_NOTE,
 build="A verified region-total formula (SUMIF) and an AI-assisted fix for a deliberately broken formula.",
 services="Gemini side panel, SUMIF, COUNTIF, troubleshooting, refinement",
 steps=[
 ("In cell K3, ask AI for a formula that adds up Total for every order where Region is 'North'.",
  "Write a formula for K3 that sums column I where column D equals \"North\", for rows 2 to 200."),
 ("Paste it into K3 and note the figure.",
  "=SUMIF(D2:D200,\"North\",I2:I200)"),
 ("Verify: filter the sheet to Region = North and read the status-bar Sum of the visible Total cells — it should match K3.", ""),
 ("Spot the problem: the Region column is messy ('north', 'North ', 'NORTH'), so SUMIF may miss rows and under-count. Tell AI and ask for a fix.",
  "My Region column has inconsistent capitalisation and extra spaces, so SUMIF misses rows. Give me a formula that totals Total for North regardless of case or spaces."),
 ("Paste the improved formula Gemini gives and compare the new North total with the old one.",
  "=SUMIF(D2:D200,\"*north*\",I2:I200)"),
 ("Ask AI to explain, in one or two sentences, why the first formula missed rows.", ""),
 ("Break something on purpose: change K3 to reference the wrong column, then paste the wrong result to Gemini and ask what is wrong.",
  "This formula gives the wrong total: =SUMIF(C2:C200,\"North\",I2:I200). What is wrong and how do I fix it?"),
 ("Apply Gemini's fix and confirm the corrected total matches your filtered check from step 3.", ""),
 ],
 test="K3 gives a North total that matches your filtered status-bar Sum, and you have used AI to diagnose and correct a deliberately broken formula.",
 ),
 dict(
 num=4, topic=1,
 title="Write Effective Prompts for Spreadsheet Tasks",
 objective="Compare a vague prompt with a specific one and capture a reusable four-part prompt pattern for spreadsheet work.",
 desc="A result is only as good as the prompt. You run a vague prompt, then a specific one that names the "
 "range, goal, output and conditions, see the difference, and distil what worked into a reusable pattern "
 "you will use for the rest of the course. " + PROJECT_NOTE,
 build="A written four-part prompt pattern and one strong, tested prompt saved for reuse.",
 services="Prompt design, range/goal/output/conditions, refinement",
 steps=[
 ("Run a deliberately vague prompt in the Gemini panel and note how generic the answer is.",
  "Tell me about my sales."),
 ("Now run a specific prompt for the same intent and compare the result.",
  "From the Orders tab range A1:I200, list the top 5 products by total sales value. Show product name and total, sorted highest first, as a table."),
 ("Write down the four parts that made the second prompt work: the Range, the Goal, the Output format, and the Conditions.", ""),
 ("Capture your reusable pattern in a notes cell or a document so every future prompt follows it.",
  "RANGE: <which cells/tab> | GOAL: <what to produce> | OUTPUT: <table/formula/number & where> | CONDITIONS: <filters, sort, limits>"),
 ("Add conditions that keep results trustworthy: state the range explicitly and ask AI to show the formula it used so you can check it.", ""),
 ("Rewrite one question of your own about the data using the pattern, and run it.", ""),
 ("Refine once: change the Output or Conditions part (for example 'top 10', or 'North region only') and re-run to see the result change. Keep the better version.", ""),
 ("Save your best prompt where you can find it again — you will reuse this pattern in every remaining lab.", ""),
 ],
 test="You can show two answers for the same intent (vague vs specific), a written four-part prompt pattern, and one refined prompt that produced the output you specified in the format you asked for.",
 ),
]
